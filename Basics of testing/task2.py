import unittest
import json
import os
from unittest.mock import patch

class TestPhonebookApplication(unittest.TestCase):

    def setUp(self):
        self.test_phonebook_filename = "test_phonebook.json"
        self.test_phonebook_data = [
            {
                "first_name": "John",
                "last_name": "Doe",
                "telephone": "123-456-7890",
                "city": "Anytown",
                "state": "CA",
            },
            {
                "first_name": "Jane",
                "last_name": "Smith",
                "telephone": "987-654-3210",
                "city": "Sometown",
                "state": "NY",
            },
        ]
        with open(self.test_phonebook_filename, 'w') as file:
            json.dump(self.test_phonebook_data, file)

    def tearDown(self):
        if os.path.exists(self.test_phonebook_filename):
            os.remove(self.test_phonebook_filename)

    def test_load_phonebook_existing_file(self):
        loaded_data = load_phonebook(self.test_phonebook_filename)
        self.assertEqual(loaded_data, self.test_phonebook_data)

    def test_load_phonebook_nonexistent_file(self):
        non_existent_filename = "non_existent.json"
        loaded_data = load_phonebook(non_existent_filename)
        self.assertEqual(loaded_data, [])

    def test_save_phonebook(self):
        test_data = [
            {
                "first_name": "Alice",
                "last_name": "Johnson",
                "telephone": "555-123-4567",
                "city": "Wonderland",
                "state": "WL",
            }
        ]
        save_phonebook(self.test_phonebook_filename, test_data)

        with open(self.test_phonebook_filename, 'r') as file:
            saved_data = json.load(file)

        self.assertEqual(saved_data, test_data)

    @patch('builtins.input', side_effect=['John'])
    def test_search_entries_by_first_name(self, mock_input):
        results = search_entries(self.test_phonebook_data, "first_name", "John")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["first_name"], "John")

    @patch('builtins.input', side_effect=['987-654-3210'])
    def test_search_entries_by_telephone(self, mock_input):
        results = search_entries(self.test_phonebook_data, "telephone", "987-654-3210")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["telephone"], "987-654-3210")

if __name__ == '__main__':
    unittest.main()
