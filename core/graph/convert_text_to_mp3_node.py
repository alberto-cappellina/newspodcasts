from core.common.processing_file import ProcessingFile
from core.file_operations.file_writer import read_file
from core.graph import NewsPodcastState
from text_to_mp3_conversion.convert import newsletter_to_audio


def convert_text_to_mp3(state: NewsPodcastState) -> dict:
    print(f'\n🔊 Converting files to mp3')

    files_to_convert = state["file_to_convert"]
    converted_files_list = []
    for file in files_to_convert:
        file_content = read_file(file.path)
        converted_file = newsletter_to_audio(file_content)

        print(f" - saved to {converted_file}")

        ready_file = ProcessingFile(
            path=converted_file,
            podcast=file.podcast,
            email=file.email
        )

        converted_files_list.append(ready_file)

    return {**state, "file_to_publish": converted_files_list}
