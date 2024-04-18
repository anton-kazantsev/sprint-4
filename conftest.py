import pytest
from main import BooksCollector

@pytest.fixture
def added_book():
    book = BooksCollector()
    return book