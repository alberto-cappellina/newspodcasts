import os
from mutagen.mp3 import MP3


def get_mp3_info(path: str) -> tuple[int, int]:
    """Return (duration_seconds, file_size_bytes) for the given MP3 file."""
    audio = MP3(path)
    duration = int(audio.info.length)
    size = os.path.getsize(path)
    return duration, size
