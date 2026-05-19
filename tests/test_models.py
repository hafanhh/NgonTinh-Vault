import pytest
from pydantic import ValidationError
from ngontinh_vault.core.models import Story, ReadingStatus


@pytest.fixture
def basic_story():
    return Story(id="test", title="Trọng Sinh", author="Abc")


def test_basic_creation(basic_story):
    assert basic_story.title == "Trọng Sinh"
    assert basic_story.status == ReadingStatus.PLAN_TO_READ
    assert basic_story.progress_percent == 0.0


def test_progress_calculation():
    s = Story(id="x", title="y", author="Abc", total_chapters=200, current_chapter=47)
    assert s.progress_percent == pytest.approx(23.5)
    assert s.is_finished is False


def test_invalid_rating_raises():
    with pytest.raises(ValidationError):
        Story(id="x", title="y", author="Abc", rating="hello")

def test_missing_required_fields_raises():
    with pytest.raises(ValidationError):
        Story()


def test_enum_auto_convert():
    s = Story(id="x", title="y", author="Abc", status="reading")
    assert s.status == ReadingStatus.READING


def test_serialize_to_dict():
    s = Story(id="abc", title="Hello", author="Abc", tags=["niên hạ", "HE"])
    data = s.model_dump()
    assert data["id"] == "abc"
    assert data["tags"] == ["niên hạ", "HE"]
