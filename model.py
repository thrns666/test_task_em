from typing import Dict


class Book:
    def __init__(self, book_id, title, author, year, status):
        self.book_id: int = book_id
        self.title: str = title
        self.author: str = author
        self.year: str = year
        self.status: str = status

    def as_dict(self) -> Dict:
        """
        Return jsonable obj of cls instance

        :return: Dict
        """
        book_dict = {
            "id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

        return book_dict

    def __repr__(self):
        return str(self.as_dict())
