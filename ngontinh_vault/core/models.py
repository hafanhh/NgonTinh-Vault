'''Pydantic models for stories and reading status'''

from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

class ReadingStatus(str, Enum):
    '''
    Possible reading states for a story.
    '''
    PLAN_TO_READ = "plan_to_read"
    READING = "reading"
    COMPLETED = "completed"
    DROPPED = "dropped"
    ON_HOLD = "on_hold"


class Story(BaseModel):
    '''A single ngon tinh storu in the library'''

    # Required fields
    id : str
    title: str
    author: str

    # Optional fields
    tags: list[str] = []
    total_chapters: Optional[int] = None
    current_chapter: int = 0
    status: ReadingStatus = ReadingStatus.PLAN_TO_READ
    rating: Optional[float] = None
    notes: str = ""
    chapter_summaries: dict[int, str] = {}

    # Timestamps
    added_at: datetime = Field(default_factory = datetime.now)
    last_read_at: Optional[datetime] = None

    @property
    def progress_percent(self) -> float:
        '''Reading progress as a percentage (0-100)'''
        if not self.total_chapters:
            return 0.0
        return (self.current_chapter/self.total_chapters) * 100
    
    @property
    def is_finished(self) -> bool:
        '''True if the story is marked as complete'''
        return self.status == ReadingStatus.COMPLETED
    
class Config:
    json_dencoders = {datetime: lambda v: v.isoformat()}
