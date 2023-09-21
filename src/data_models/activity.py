from dataclasses import dataclass, field
from datetime import date


@dataclass
class Activity:
    title: str
    location: str
    city: str
    start_date: date
    end_date: date
    skills: field(default_factory=list)
    description: str
