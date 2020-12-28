import logging
from pathlib import Path
from http.client import CREATED, BAD_REQUEST, OK, NO_CONTENT

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny

from . import upload_manager, serializers, models, services


logger = logging.getLogger(__name__)


@api_view(['PUT'])
def upload_prepare(request):
    try:
        filename = request.data['filename']
    except KeyError:
        return Response(
            {'detail': 'Filename not provided'}, status=BAD_REQUEST
        )
    if not Path(filename).suffix:
        return Response({'detail': 'Filename invalid'}, status=BAD_REQUEST)
    upload, video = upload_manager.prepare(
        user=request.user, filename=filename
    )
    return Response(
        {
            'upload_id': upload.id,
            'presigned_upload_url': upload.presigned_upload_url,
            'video_id': video.id,
        },
        status=CREATED,
    )


@api_view(['PUT'])
def upload_complete(request, upload_id):
    try:
        models.Upload.objects.get(id=upload_id, user_id=request.user.id)
    except ObjectDoesNotExist:
        logger.warning(
            'User %s attempted to complete upload %s',
            request.user.id,
            upload_id,
        )
        raise PermissionDenied(detail='You do not have permission to do that')
    upload_manager.complete.delay(upload_id)
    return Response({}, status=OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def video(request, video_id):
    video = models.Video.objects.get(id=video_id)
    data = serializers.VideoSerializer(video).data
    return Response(data, status=OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def video_playlist(request, video_id):
    playlist_str = services.generate_master_playlist(video_id=video_id)
    if not playlist_str:
        return HttpResponse('', status=NO_CONTENT)
    content_type = 'Content-Type: application/vnd.apple.mpegurl'
    return HttpResponse(playlist_str, status=OK, content_type=content_type)
