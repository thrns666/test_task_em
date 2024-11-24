import pathlib
from typing import NoReturn

from book_dao import BookDAO
from lyrics import help_command


def main_script() -> NoReturn:
    """
    Main console router

    return: NoReturn
    """
    while True:
        inpt_value = input(
            'Enter the one of command: get_all_books, create_book, delete_book, search_book, change_status: '
        ).lower()

        if inpt_value == 'create_book':
            try:
                data_string = input(
                    'Write below title, author and year for book: \n Example: Vinograd, Below A.A., 1974: '
                )

                title, author, year, *other = data_string.split(',')
                res = BookDAO.create_book(
                    title=title.strip(),
                    author=author.strip(),
                    year=year.strip()
                )
                print(res)
            except Exception as e:
                print(e)

        elif inpt_value == 'get_all_books':
            try:
                res = BookDAO.get_all()
                if res:
                    books = res.get('books')
                    for book in books:
                        print(book)
            except Exception as e:
                print(e)

        elif inpt_value == 'delete_book':
            try:
                book_id = input('Enter book id below:')

                if not book_id.isdigit():
                    raise ValueError('book id must be only integer digit')

                res = BookDAO.delete_book(int(book_id))
                print(f'{res} has been deleted')
            except Exception as e:
                print(e)

        elif inpt_value == 'change_status':
            try:
                a = input('Enter id and status(В наличии, выдана) for book:')
                book_id, status, *other = a.split(',')
                res = BookDAO.change_book_status(int(book_id), status.strip())

                print(res)
            except Exception as e:
                print(e)

        elif inpt_value == 'search_book':
            try:
                a = input('Enter the attr for search \n example: title=Vinograd: ')
                search_filter, value, *other = a.split('=')

                if search_filter == 'id':
                    data_a = {
                        search_filter: int(value)
                    }
                else:
                    data_a = {
                        search_filter: value
                    }

                res = BookDAO.get_book_by_filter(**data_a)
                if isinstance(res, list):
                    for book in res:
                        print(book)
                else:
                    print(res)
            except Exception as e:
                print(e)

        elif inpt_value == 'help':
            print(help_command)
        else:
            print(f'{inpt_value} is unknown command, use "help" for solve you problem')


if __name__ == '__main__':
    json_repo = pathlib.Path(BookDAO.js_file).is_file()
    if not json_repo:
        BookDAO.create_repo()

    main_script()
