import pytest
from ngontinh_vault.core.models import Story, ReadingStatus
from ngontinh_vault.core.library import Library


@pytest.fixture
def lib_with_stories():
    lib = Library()
    lib.add(Story(id="trong-sinh", title="Trọng Sinh", author="Author A", status=ReadingStatus.READING))
    lib.add(Story(id="hon-nhan", title="Hôn Nhân", author="Author B", tags=["niên hạ", "HE"]))
    return lib


def test_empty_library():
    lib = Library()
    assert len(lib) == 0
    assert lib.get("xxx") is None


def test_add_and_get(lib_with_stories):
    assert len(lib_with_stories) == 2
    assert lib_with_stories.get("trong-sinh").title == "Trọng Sinh"


def test_add_duplicate_raises(lib_with_stories):
    with pytest.raises(ValueError):
        lib_with_stories.add(Story(id="trong-sinh", title="duplicate", author="X"))


def test_filter_by_status(lib_with_stories):
    reading = lib_with_stories.filter_by_status(ReadingStatus.READING)
    assert [s.title for s in reading] == ["Trọng Sinh"]


def test_filter_by_tag(lib_with_stories):
    he = lib_with_stories.filter_by_tag("HE")
    assert [s.title for s in he] == ["Hôn Nhân"]


def test_contains(lib_with_stories):
    assert "trong-sinh" in lib_with_stories
    assert "xxx" not in lib_with_stories


def test_iter(lib_with_stories):
    titles = [s.title for s in lib_with_stories]
    assert "Trọng Sinh" in titles
    assert "Hôn Nhân" in titles