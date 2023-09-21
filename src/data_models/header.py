from dataclasses import dataclass
from pathlib import Path


@dataclass
class Header:
    name: str
    image: Path
    github: str
    linkedin: str
