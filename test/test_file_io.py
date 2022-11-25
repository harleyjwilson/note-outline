import unittest
import os
from src.note_outline.file_io import read_file, write_file


class test_file_io(unittest.TestCase):
    def setUp(self):
        file = open("blank-read.md", "w")
        file.writelines([''])
        file = open("small-read.md", "w")
        file.writelines(
            ['# Small Text\n', '\n', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n'])

    def tearDown(self):
        os.remove('blank-read.md')
        os.remove('small-read.md')
        os.remove('blank-write.md')
        os.remove('small-write.md')

    def test_read_lines(self):
        self.assertEqual(read_file("blank-read.md"), [])

        self.assertEqual(read_file("small-read.md"), [
                         '# Small Text\n', '\n', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n'])

        with self.assertRaises(FileNotFoundError):
            read_file('does_not_exist.md')

    def test_write_lines(self):
        write_file("blank-write.md", [])
        file = open("blank-write.md", "r")
        self.assertEqual(file.readlines(), [])

        write_file("small-write.md", [
            '# Small Text\n', '\n', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n'])
        file = open("small-write.md", "r")
        self.assertEqual(file.readlines(), [
                         '# Small Text\n', '\n', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n'])

        with self.assertRaises(FileNotFoundError):
            read_file('does_not_exist.md')


if __name__ == '__main__':
    unittest.main()
