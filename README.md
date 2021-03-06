<p align="center">
<img src="https://i.imgur.com/H1rXKKv.png" width="300"/>
</p>

<hr>

# veems

**An open-source platform for online video.**

The code powering https://veems.tv.
A next generation video sharing platform, with freedom of speech values.

![https://github.com/VeemsHQ/veems/workflows/Tests/badge.svg](https://github.com/VeemsHQ/veems/workflows/Tests/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/5924e6affd4354f0af97/maintainability)](https://codeclimate.com/github/VeemsHQ/veems/maintainability)

## Stay in touch

- [Telegram](https://veems.tv/telegram)
- [Discord](https://discord.gg/RjCZMtZ)
- [Twitter](https://twitter.com/veemshq)
- [Reddit](https://www.reddit.com/r/VeemsHQ/)
- [Twitch.tv](https://www.twitch.tv/richardarpanet)

## Contributing

We're actively looking for help with both frontend and backend development.

[Join us on Discord](https://discord.gg/RjCZMtZ) if you're interested in being involved.

[![https://i.imgur.com/Ujf8Ti8.png](https://i.imgur.com/Ujf8Ti8.png)](https://discord.gg/RjCZMtZ)

## Screenshots

A preview of what we're building.

Further design materials can be found [here](https://github.com/VeemsHQ/design).

![https://i.imgur.com/pkrQgzE.png](https://i.imgur.com/pkrQgzE.png)

![https://i.imgur.com/ZMJYNvl.png](https://i.imgur.com/ZMJYNvl.png)

![https://i.imgur.com/VGC6FQj.png](https://i.imgur.com/VGC6FQj.png)

## Feature Roadmap

In order of priority.

### Alpha Release

- Uploading, transcoding of content, playlist video packaging (backend ✅, frontend ✅).
- Playback of video content (backend ✅, frontend ✅).
- User & API authentication (backend ✅, frontend ✅).
- Creation of "Channels" (backend ✅, frontend ✅).
- Homepage video listings ✅.
- Search function ✅.
- Channel Manager (basics).
    - Video Management (backend ✅, frontend ⏳).
    - Channel customisation (backend ✅, frontend ⏳).
- Like/dislike videos (backend ✅, frontend ✅).
- Related videos suggestions, Video playback page.
- Sync channel(s) content from YT to Veems automatically.
    - Channel Dashboard, sync configuration.
    - Background sync process.
    - Related user notifications.
- Video view metrics.
- Follow (Subscribe to) a Channel.
- User notifications.
    - Email notifications.
- Moderation
    - Ability to report content.
    - Moderation queue in Admin with actions.
    - Content error pages if unavailable due to moderation.
    - IP logging.
    - DMCA submission form.

### Beta Release

- Video comments.
- Video responses.
- Video categories pages.
    - Sport
    - Comedy
    - etc
- Trending videos.
    - Trending algorithm.
    - Trending section on Homepage.
- User notifications.
    - UI notifications.
- Live streaming.
- User controlled content hiding. (e.g. Don't show me any cat videos).
- User Badges (earned by performing actions on the platform).
- Monetization.
    - Revenue share from Premium user accounts.
    - Banner ads.
    - Pre-roll video player ads.
    - Video view validation.
- Embeddable video player.

This section is work-in-progress, more to be added shortly.

## Installation

First install OS dependencies, ffmpeg and ffprobe. You will also need Docker.

Linux:

```bash
sudo apt update
sudo apt install ffmpeg
ffmpeg -version
```

Mac:

```bash
brew install ffmpeg
```

From within a Python 3.6+ virtualenv (we recommend using [pyenv](https://github.com/pyenv/pyenv) to manage your virtualenvs).

```bash
make install
```

Set of the required environment variables for the application, see `.env.template` for examples. A few of the secrets relating to the hosting provider (ACCESS_KEY_ID, SECRET_ACCESS_KEY) you may need to request values for.

## Running the tests

Start up the supporting docker containers (RabbitMQ, Postgres, Localstack).
Then run the tests.

```bash
make start-deps
make test
```

## Usage

### Running the webserver

```bash
make start-deps
python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py runserver
```

Via docker:

```bash
make run
```

Then visit http://localhost:8000/

### Importing seed data

```bash
make reset
```


### Running the background [Celery](https://docs.celeryproject.org/en/stable/index.html) workers

```bash
./celeryworker-entrypoint.sh
./celerybeat-entrypoint.sh
```

## Architectural Concepts

- **Channel** -- a Channel containing many Videos.
    - **Upload** -- a raw video file upload into the system
        - **Video** -- a video, which you can view via the website
            - **Video Rendition** -- a version of the Video file at a specific resolution, bitrate, etc. e.g. 1080p
                - **Video Rendition Segment** -- a small chunk of the Video Rendition video file to be served to the video player
                - **Video Rendition Thumbnail** -- a thumbnail at a certain timestamp within the Video Rendition video file
