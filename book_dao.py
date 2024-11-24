import json
import os
from typing import Dict, List, NoReturn

from model import Book


class BookDAO:
    _base_dir = os.path.dirname(os.path.abspath(__file__))
    _file_path = os.path.join(_base_dir, 'repo.json')

    __model = Book
    js_file = _file_path

    @classmethod
    def create_repo(cls) -> NoReturn | Exception:
        """
        Create JSON file to store data

        return: NoReturn | Exception
        """
        try:
            with open(cls.js_file, 'w') as fp:
                repo_arch = {
                    "books": [
                    ]
                }

                json.dump(repo_arch, fp=fp)

        except Exception as e:
            return e

    @classmethod
    def get_book_by_filter(cls, **filters) -> List | Dict | Exception:
        """
        Find object(s) by kwargs(**filters)

        :param filters: kwargs
        :return: List | Dict | Exception
        """
        try:
            with open(cls.js_file, 'r') as json_data:
                session = json.load(json_data)

            books = session['books']
            res = []

            for book in books:
                for k, v in filters.items():
                    value = book.get(k)
                    if isinstance(value, int) and isinstance(v, int):
                        if value == v:
                            res.append(book)
                    else:
                        if value.lower() == v.lower():
                            res.append(book)
            if res:
                if len(res) == 1:
                    return res[0]

                return res
            else:
                raise ValueError('Book not found')
        except Exception as e:
            return e

    @classmethod
    def get_all(cls) -> Dict | Exception:
        """
        Returns dict with all 'Books'

        :return: Dict | Exception
        """
        try:
            with open(cls.js_file, 'r') as fp:
                session = json.load(fp)
                return session
        except Exception as e:
            return e

    @classmethod
    def create_book(cls, title: str, author: str, year: str) -> Dict | Exception:
        """
        Create book instance in JSON file

        :param title: str
        :param author: str
        :param year: str
        :return: Dict | Exception
        """
        try:
            with open(cls.js_file, 'r') as fp:
                session = json.load(fp)
                session['books'].sort(key=lambda a: a['id'])

            if len(session['books']) > 0:
                pr_id = session['books'][-1].get('id') + 1
            else:
                pr_id = 0

            book = Book(
                book_id=pr_id,
                title=title,
                author=author,
                year=year,
                status='В наличии'
            )
            session['books'].append(book.as_dict())

            with open(cls.js_file, 'w') as fp:
                json.dump(session, fp=fp)

            return book.as_dict()
        except Exception as e:
            return e

    @classmethod
    def delete_book(cls, book_id: int) -> Dict | Exception:
        """
        Delete 'Book' from JSON file by id

        :param book_id: int
        :return: Dict | Exception
        """
        try:
            book = cls.get_book_by_filter(id=book_id)

            if isinstance(book, Exception):
                raise ValueError(f'Book with id: {book_id} not found')

            if isinstance(book, dict) and book['id'] == book_id:
                with open(cls.js_file, 'r') as fp:
                    session = json.load(fp)

                for i in range(len(session['books'])):
                    obj = session['books'][i]
                    if obj.get('id') == book_id:
                        del_obj = session['books'].pop(i)

                        with open(cls.js_file, 'w') as fp:
                            json.dump(session, fp=fp)

                        return del_obj
            else:
                raise TypeError

        except Exception as e:
            return e

    @classmethod
    def change_book_status(cls, book_id: int, status: str) -> Dict | Exception:
        """
        Change 'Book' status by id

        :param book_id: int
        :param status: str, (В наличии, выдана)
        :return: Dict | Exception
        """
        try:
            status = status.lower()
            if status not in ['в наличии', 'выдана']:
                raise ValueError('Status can only be changed to "В наличии" or "выдана"')

            book: Dict = cls.get_book_by_filter(id=book_id)
            if not isinstance(book, dict):
                raise TypeError

            if book['id'] == book_id:
                with open(cls.js_file, 'r') as fp:
                    session = json.load(fp)

                for i in range(len(session['books'])):
                    obj = session['books'][i]
                    if obj.get('id') == book_id:
                        find_obj = session['books'][i]
                        find_obj['status'] = status

                        with open(cls.js_file, 'w') as fp:
                            json.dump(session, fp=fp)

                        return find_obj
            else:
                raise ValueError('Book not found')
        except Exception as e:
            return e
