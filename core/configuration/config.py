from dataclasses import dataclass, field


@dataclass
class Config:
    url1: str = ""
    items: list[ItemConfig] = field(default_factory=list)


@dataclass
class FilterConfig:
    sender: list[str] = field(default_factory=list)
    title: str = ""


@dataclass
class ItemConfig:
    name: str = ""
    label: str = ""
    filter: FilterConfig = field(default_factory=FilterConfig)
