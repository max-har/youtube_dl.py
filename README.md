# youtube2flac

## How to

1. run `python3 youtube2flac.py`
2. paste URL
3. check output in present working directory

## How it works

uses your local youtube-dl and the command `youtube-dl -x --audio-format "flac" --audio-quality 0 <URL>`

`-x, --extract-audio`: Convert video files to audio-only files (requires ffmpeg or avconv and ffprobe or avprobe)

`--audio-format FORMAT`: Specify audio format: "best", "aac", "flac", "mp3", "m4a", "opus", "vorbis", or "wav"; "best" by default; No effect without -x

`--audio-quality QUALITY`: Specify ffmpeg/avconv audio quality, insert a value between 0 (better) and 9 (worse) for VBR or a specific bitrate like 128K (default 5)
