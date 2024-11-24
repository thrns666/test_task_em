Functional description:
Console app for manage book libriary

- get all books --> get_all_books -> returns list[dict] of all books (id, title, author, year, status)
- create books --> create_book -> Dream, Ahova A. V., 1999 (title, author, year) -> return dict: Dream, Ahova A. V., 1999
- search books --> search_book -> year=1999 -> return dict: Dream, Ahova A. V., 1999
 If app found many books, it will return a book-list.
-change book status --> change_status -> 0, выдана (id, status[выдана, в наличии])
- delete books --> delete_book -> 0 (id) -> return dict with deleted book

Data stored in JSON file, file create automatically, when you run main.py for first time.
For unittests tests, the JSON file is automatically created and deleted.

Execute:
run main.py
