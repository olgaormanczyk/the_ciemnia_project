import unittest
import main
import os


class MyTestCase(unittest.TestCase):
    def test_print_hi(self):
        self.assertEqual("Hi, michal", main.print_hi("michal"))

    def test_save_config(self):
        file_name = 'test_config'
        data = ('wyderka', 'marchewka', 1, 2, 3)
        main.save_config(data, file_name)

        self.assertEqual(data, main.load_config(file_name))

        self.delete_file(file_name)

    def test_save_config_on_existing_file(self):
        file_name = 'existing_test_file'

        main.save_config('wyderka', file_name)
        main.save_config('marchew', file_name)
        self.assertEqual('wyderka', main.load_config(file_name))

        self.delete_file(file_name)

    def delete_file(self, file_name):
        if os.path.exists(file_name):
            os.remove(file_name)


if __name__ == '__main__':
    unittest.main()
