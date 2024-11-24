import json

from book_dao import BookDAO


class TestBookDAO(BookDAO):
    js_file = 'test_repo.json'

    repo_structure = {
        "books": [
            {
                "id": 0,
                "title": "first",
                "author": "test",
                "year": "2222",
                "status": "В наличии"
            },
            {
                "id": 1,
                "title": "second",
                "author": "fresco",
                "year": "2222",
                "status": "В наличии"
            },
        ]
    }

    @classmethod
    def create_repo(cls):
        try:
            with open(cls.js_file, 'w') as fp:
                json.dump(cls.repo_structure, fp=fp)

        except Exception as e:
            return e
