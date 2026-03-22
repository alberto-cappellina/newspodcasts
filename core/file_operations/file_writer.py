import tempfile
import uuid


def write_string_temp_file(mail_content: str):
    tmp_path = f"{tempfile.gettempdir()}/{uuid.uuid4()}.txt"
    with open(tmp_path, "w") as temporary_file:
        temporary_file.write(mail_content)

    return tmp_path


def read_file(path: str) -> str:
    with open(path, "r") as f:
        return f.read()

