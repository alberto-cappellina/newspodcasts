import boto3

from core.environment.environment import get_aws_access_key_id, get_aws_secret_access_key
from core.file_operations.file_writer import get_temp_file_path

POLLY_CHAR_LIMIT = 3000


def _chunk_text(text: str, max_chars: int = POLLY_CHAR_LIMIT) -> list[str]:
    """Split *text* into chunks of at most *max_chars* characters.

    Splitting always occurs on whitespace boundaries so no word is ever broken
    mid-word. Intended for use with AWS Polly, which enforces a 3 000-character
    limit per SynthesizeSpeech call.

    Args:
        text: The plain-text string to split.
        max_chars: Maximum number of characters allowed per chunk (default: 3 000).

    Returns:
        A list of non-empty strings, each at most *max_chars* characters long.
        Returns an empty list when *text* is empty or contains only whitespace.
    """
    chunks, current = [], ""
    for word in text.split(" "):
        # Prepend a space only when joining to an existing chunk
        addition = (" " + word) if current else word
        if len(current) + len(addition) <= max_chars:
            # Word fits in the current chunk — keep accumulating
            current += addition
        else:
            # Current chunk is full — flush it and start a new one
            if current:
                chunks.append(current)
            current = word
    # Flush the last chunk if non-empty
    if current:
        chunks.append(current)
    return chunks


def newsletter_to_audio(text_to_convert: str) -> str:
    aws_access_key_id = get_aws_access_key_id()
    aws_secret_access_key = get_aws_secret_access_key()

    if not aws_access_key_id.get_secret_value():
        raise ValueError("AWS_ACCESS_KEY_ID is not set. Please configure it in your .env file.")
    if not aws_secret_access_key.get_secret_value():
        raise ValueError("AWS_SECRET_ACCESS_KEY is not set. Please configure it in your .env file.")

    client = boto3.client(
        'polly',
        region_name='eu-west-1',
        aws_access_key_id=aws_access_key_id.get_secret_value(),
        aws_secret_access_key=aws_secret_access_key.get_secret_value(),
    )

    audio_bytes = b""
    for chunk in _chunk_text(text_to_convert):
        response = client.synthesize_speech(
            Text=chunk,
            OutputFormat='mp3',
            VoiceId='Carla'
        )
        audio_bytes += response['AudioStream'].read()

    file_path = get_temp_file_path(with_extension=".mp3")
    with open(file_path, 'wb') as f:
        f.write(audio_bytes)

    return file_path
