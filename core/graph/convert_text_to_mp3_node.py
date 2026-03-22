from core.file_operations.file_writer import read_file
from core.graph import NewsPodcastState
from text_to_mp3_conversion.convert import newsletter_to_audio


def convert_text_to_mp3(state: NewsPodcastState):
    print(f'\n🔊 Converting files to mp3')

    files_to_convert = state["file_to_convert"]
    converted_files_list = []
    for file in files_to_convert:
        file_content = read_file(file)
        converted_file = newsletter_to_audio(file_content)

        print(f" - saved to {converted_file}")
        converted_files_list.append(converted_file)
