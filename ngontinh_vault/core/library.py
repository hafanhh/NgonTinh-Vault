''' Library: Contain class managing a collection of stories '''

from typing import Optional
from ngontinh_vault.core.models import Story, ReadingStatus

class Library:
    ''' Manages a collection of stories with lookup-by-id and filtering. '''

    def __init__(self) -> None:
        ''' Initialize an empty library '''
        self._stories: dict[str, Story] = {}

    def add(self, story: Story) -> None:
        ''' Add a story to the library.
        Raises:
            ValueError: if a story with the same id already exists 
        '''
        if story.id in self._stories:
            raise ValueError(f"Story '{story.id}' already exists.")
        self._stories[story.id] = story
    
    def get(self, story_id: str) -> Optional[Story]:  # -> Story | None:
        ''' Return story by ID, or None if not found. '''
        return self._stories.get(story_id)
    
    def filter_by_status(self, status: ReadingStatus) -> list[Story]:
        ''' Return all stories matching the given status. '''
        return [story for story in self._stories.values() if story.status == status]
    
    def filter_by_tag(self, tag: str) -> list[Story]:
        '''Return all stories matching the given tags'''
        return [story for story in self._stories.values() if tag in story.tags]
    
    def __len__(self) -> int:
        ''' Return number of stories in library '''
        return len(self._stories)
    
    def __iter__(self):
        ''' Iterate over all stories '''
        return iter(self._stories.values())
    
    def __contains__(self, story_id: str) -> bool:
        ''' Check if a story ID exists in library '''
        return story_id in self._stories
    