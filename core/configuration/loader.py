from pathlib import Path
import yaml
from dotenv import dotenv_values

from .config import Config, FilterConfig, ItemConfig




def load_config(path: str) -> Config:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Configuration file not found: {path}")
    if not p.is_file():
        raise ValueError(f"Path is not a file: {path}")
    try:
        data = yaml.safe_load(p.read_text())
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML in configuration file: {e}") from e
    if not isinstance(data, dict):
        raise ValueError(f"Configuration file must contain a YAML mapping, got: {type(data).__name__}")
    cfg = data.get("configuration", {})
    items = [
        ItemConfig(
            name=item["name"],
            label=item["label"],
            filter=FilterConfig(
                sender=[f] if isinstance(f := item.get("filter", {}).get("sender", []), str) else f,
                title=item.get("filter", {}).get("title", ""),
            ),
        )
        for item in data.get("items", [])
    ]
    return Config(url1=cfg.get("url1", ""), items=items)
