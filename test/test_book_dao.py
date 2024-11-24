import os
import unittest

from conftest import TestBookDAO


class TestBookDAOMethods(unittest.TestCase):
    def setUp(self):
        TestBookDAO.create_repo()

    def tearDown(self):
        os.remove(TestBookDAO.js_file)

    def test_create_book(self):
        res = TestBookDAO.create_book(
            title='Bylka',
            author='Sverlo H.S.',
            year='2022'
        )

        assert_res = {
            "id": 2,
            "title": "Bylka",
            "author": "Sverlo H.S.",
            "year": "2022",
            "status": "В наличии"
        }

        self.assertEqual(res, assert_res)

    def test_change_status(self):
        res = TestBookDAO.change_book_status(1, 'ВыДаНа')

        assert_res = {
            "id": 1,
            "title": "second",
            "author": "fresco",
            "year": "2222",
            "status": "выдана"
        }

        self.assertEqual(res, assert_res)

    def test_delete_book(self):
        res = TestBookDAO.delete_book(1)

        assert_res = {
            "id": 1,
            "title": "second",
            "author": "fresco",
            "year": "2222",
            "status": "В наличии"
        }

        self.assertEqual(res, assert_res)

    def test_get_all_books(self):
        res = TestBookDAO.get_all()

        assert_res = TestBookDAO.repo_structure

        self.assertEqual(res, assert_res)

    def test_filter_books(self):
        res = TestBookDAO.get_book_by_filter(year='2222')

        assert_res = TestBookDAO.repo_structure['books']

        res_1 = TestBookDAO.get_book_by_filter(title='First')

        assert_res_1 = {
            "id": 0,
            "title": "first",
            "author": "test",
            "year": "2222",
            "status": "В наличии"
        }

        self.assertEqual(res, assert_res)
        self.assertEqual(res_1, assert_res_1)


if __name__ == '__main__':
    unittest.main()
