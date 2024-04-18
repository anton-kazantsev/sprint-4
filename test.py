import pytest
from main import BooksCollector

class TestBooksCollector:


    def test_add_new_book_long_name(self, book):
        book.add_new_book('Клуб любителей книг и пирогов из картофельных очистков')
        assert len(book.books_genre()) == 0

    @pytest.mark.parametrize('name', ['Гарри Поттер', 'Клуб любителей книг и пирогов из картофел'])
    def test_add_new_book_append_two_books_of_different_lengths(self, name, book):
        book.add_new_book(name)
        assert len(book.books_genre()) == 1

    def test_set_book_genre_added_genre_positive_result(self, book):
        book.add_new_book('Гарри Поттер')
        book.set_book_genre('Гарри Поттер', 'Фантастика')
        assert book.books_genre('Гарри Поттер') == 'Фантастика'

    def test_get_book_genre_positive_result(self, book):
        book.add_new_book('Гарри Поттер')
        book.set_book_genre('Гарри Поттер', 'Фантастика')
        assert book.books_genre.get('Гарри Поттер')

    def test_get_books_with_specific_genre_fantastic_positive_result(self, book):
        book.add_new_book('Гарри Поттер')
        book.set_book_genre('Гарри Поттер', 'Фантастика')
        book.add_new_book('Песнь льда и пламени')
        book.set_book_genre('Песнь льда и пламени', 'Фантастика')
        book.add_new_book('Песнь льда и пламени')
        book.set_book_genre('Венгерска вода', 'Детективы')
        assert len(book.get_books_with_specific_genre('Фантастика')) == 2

    def test_get_books_for_children_positive_result(self, book):
        book.add_new_book('Гарри Поттер')
        book.set_book_genre('Гарри Поттер', 'Фантастика')
        book.add_new_book('Кладбище домашних животных')
        book.set_book_genre('Кладбище домашних животных', 'Ужасы')
        book.add_new_book('Ревизор')
        book.set_book_genre('Ревизор', 'Комедии')
        book.add_new_book('Дежавю')
        book.set_book_genre('Дежавю', 'Детективы')
        assert len(book.get_books_for_children()) == 2

    def test_add_book_in_favorites_append_book_in_favorites_positive_result(self, book):
        book.add_new_book('Гарри Поттер')
        book.add_book_in_favorites('Гарри Поттер')
        assert len(book.favorites()) == 1

    @pytest.mark.parametrize('name', ['Гарри Поттер', 'Песнь льда и пламени'])
    def test_add_book_in_favorites_append_two_books_in_favorites_positive_result(self, name, book):
        book.add_new_book(name)
        book.add_book_in_favorites(name)
        assert len(book.favorites()) == 2

    def test_delete_book_from_favorites_delete_book_in_favorites_positive_result(self, book):
        book.add_new_book('Гарри Поттер')
        book.add_book_in_favorites('Гарри Поттер')
        book.delete_book_from_favorites('Гарри Поттер')
        assert len(book.favorites()) == 0