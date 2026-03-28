import tempfile
import uuid


def get_temp_file_path(with_extension: str) -> str:
    tmp_path = f"{tempfile.gettempdir()}/{uuid.uuid4()}{with_extension}"
    return tmp_path


def write_string_temp_file(mail_content: str) -> str:
    path = get_temp_file_path(".txt")
    return write_string_temp_file_at_path(path, mail_content)


def write_string_temp_file_at_path(
        path: str,
        mail_content: str) -> str:
    with open(path, "w") as temporary_file:
        temporary_file.write(mail_content)

    return path


def read_file(path: str) -> str:
    with open(path, "r") as f:
        return f.read()
