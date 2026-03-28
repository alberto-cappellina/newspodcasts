from dataclasses import dataclass, field


@dataclass
class Job:
    file_path: str
    mp3_files: list[str] = field(default_factory=list)
