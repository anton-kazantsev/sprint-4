import pytest
from main import BooksCollector


def test_add_new_book_negative_result(self):
    book = BooksCollector()
    book.add_new_book('Гарри Поттер')
    book.add_new_book('Гарри Поттер')
    assert len(self.books_genre) == 0

@pytest.mark.parametrize('name', ['Гарри Поттер', 'Песнь льда и пламени'])
def test_add_new_book_append_two_books_positive_result(self, name):
    book = BooksCollector()
    book.add_new_book(name)
    book.add_new_book(name)
    assert len(self.books_genre) == 2

def test_set_book_genre_added_genre_positive_result(self):
    book = BooksCollector()
    book.add_new_book('Гарри Поттер')
    book.set_book_genre('Гарри Поттер', 'Фантастика')
    assert self.books_genre['Гарри Поттер'] == 'Фантастика'

def test_get_book_genre_positive_result(self):
    book = BooksCollector()
    book.add_new_book('Гарри Поттер')
    book.set_book_genre('Гарри Поттер', 'Фантастика')
    assert self.books_genre.get('Гарри Поттер')

@pytest.mark.parametrize('name,genre', [['Гарри Поттер', 'Фантастика'], ['Песнь льда и пламени', 'Фантастика'], ['Венгерска вода', 'Детективы']])
def test_get_books_with_specific_genre_fantastic_positive_result(self, name, genre):
    book = BooksCollector()
    book.add_new_book(name)
    book.set_book_genre(name, genre)
    assert len(book.get_books_with_specific_genre('Фантастика')) == 2

@pytest.mark.parametrize('name,genre', [['Гарри Поттер', 'Фантастика'], ['Кладбище домашних животных', 'Ужасы'], ['Ревизор', 'Комедии'], ['Дежавю', 'Детективы']])
def test_get_books_for_children_positive_result(self, name, genre):
    book = BooksCollector()
    book.add_new_book(name)
    book.set_book_genre(name, genre)
    assert len(book.get_books_for_children()) == 2

def test_add_book_in_favorites_append_book_in_favorites_positive_result(self):
    book = BooksCollector()
    book.add_new_book('Гарри Поттер')
    book.add_book_in_favorites('Гарри Поттер')
    assert len(self.favorites) == 1

@pytest.mark.parametrize('name', ['Гарри Поттер', 'Песнь льда и пламени'])
def test_add_book_in_favorites_append_two_books_in_favorites_positive_result(self, name):
    book = BooksCollector()
    book.add_new_book(name)
    book.add_book_in_favorites(name)
    assert len(self.favorites) == 2

def test_delete_book_from_favorites_delete_book_in_favorites_positive_result(self):
    book = BooksCollector()
    book.add_new_book('Гарри Поттер')
    book.add_book_in_favorites('Гарри Поттер')
    book.delete_book_from_favorites('Гарри Поттер')
    assert len(self.favorites) == 0

