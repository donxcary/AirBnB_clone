#!/usr/bin/python3
"""Unittest For The Console"""
import unittest
import console
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """"Testing HBNB Command CLass"""
    def setUp(self):
        """SetUp"""
        self.command_interpreter = HBNBCommand()

    def tearDown(self):
        """Tear Down"""
        pass

    def test_create_command(self):
        """Testing Create Command"""
        line = "MyClass"
        result = class_create(line)
        self.assertEqual(result, MyClass)

    def test_missing_class_name(self):
        """Testing Missing Line"""
        line = ""
        expected_msg = "** class name missing **"
        result = class_create(line)
        self.assertEqual(result, expected_msg)

    def test_non_existing_class(self):
        """Testing Non-Existing Line"""
        line = "NonExistentClass"
        expected_msg = "** class doesn't exist **"
        result = class_create(line)
        self.assertEqual(result, expected_msg)

    def test_empty_line(self):
        """Testing Empty Line"""
        line = ""
        result = line_to_words(line)
        self.assertEqual(result, [])

    def test_single_word_line(self):
        """Testing Single Word Line"""
        line = "Hello"
        expected_words = ["Hello"]
        result = line_to_words(line)
        self.assertEqual(result, expected_words)

    def test_multiple_words_line(self):
        """Testing Multiple Word Line"""
        line = "This is a test"
        expected_words = ["This", "is", "a", "test"]
        result = line_to_words(line)
        self.assertEqual(result, expected_words)

    def test_line_with_whitespace(self):
        """Testing White Space"""
        line = "    Many spaces      here    "
        expected_words = ["Many", "spaces", "here"]
        result = line_to_words(line)
        self.assertEqual(result, expected_words)


class StorageMock:
    """Class StorageMock"""
    @staticmethod
    def all():
        return {"MyClass.1": "Instance1", "MyClass.2": "Instance2"}


def class_create_mock(line):
    """Class CreateMock"""
    if line == "MyClass":
        return "MyClass"
    else:
        return "** class doesn't exist **"


class TestPrintAll(unittest.TestCase):
    """Testing PrintAll Class"""
    def test_empty_length(self):
        """Testing Empty Length"""
        result = print_all(0, [])
        expected_result = ["Instance1", "Instance2"]
        self.assertEqual(result, expected_result)

    def test_non_empty_length(self):
        """Testing NotEmptyLength"""
        result = print_all(1, ["MyClass"])
        expected_result = ["Instance1", "Instance2"]
        self.assertEqual(result, expected_result)

    def test_non_existent_class(self):
        """TestingNonExistingClass"""
        result = print_all(1, ["NonExistentClass"])
        expected_result = "** class doesn't exist **"
        self.assertEqual(result, expected_result)

    @patch('builtins.print')
    def test_do_create(self, mock_print):
        """TestingDoCreate"""
        with patch('console.class_create', return_value=Mock())
        as mock_class_create:
            self.cmd.do_create("MyClass")
            mock_print.assert_called_once_with('Generated instance id')

        with patch('console.class_create', return_value="** class
            doesn't exist **") as mock_class_create:
            self.cmd.do_create("NonExistentClass")
            mock_print.assert_called_once_with('** class doesn\'t exist **')

    @patch('builtins.print')
    def test_do_show(self, mock_print):
        """Testing DO Show"""
        with patch('console.class_create', return_value=Mock())
        as mock_class_create:
            self.cmd.do_show("MyClass 1")
            mock_print.assert_called_once_with('Instance details')

        self.cmd.do_show("")
        mock_print.assert_called_once_with('** class name missing **')
        with patch('console.class_create', return_value=Mock())
        as mock_class_create:
            self.cmd.do_show("MyClass")
            mock_print.assert_called_once_with('** instance id missing **')

    @patch('builtins.print')
    def test_do_destroy(self, mock_print):
        """Testing DO Destroy"""
        with patch('console.class_create', return_value=Mock())
        as mock_class_create:
            self.cmd.do_destroy("MyClass 1")
            mock_print.assert_called_once_with('Instance deleted')

        self.cmd.do_destroy("")
        mock_print.assert_called_once_with('** class name missing **')

        with patch('console.class_create', return_value=Mock())
        as mock_class_create:
            self.cmd.do_destroy("MyClass")
            mock_print.assert_called_once_with('** instance id missing **')

    @patch('builtins.print')
    def test_do_all(self, mock_print):
        """Testing Do All"""
        with patch('console.print_all', return_value=["Instance1",
            "Instance2"]) as mock_print_all:
            self.cmd.do_all("")
            mock_print.assert_called_once_with(["Instance1", "Instance2"])

        with patch('console.print_all', return_value=["Instance1",
            "Instance2"]) as mock_print_all:
            self.cmd.do_all("MyClass")
            mock_print.assert_called_once_with(["Instance1", "Instance2"])

    @patch('builtins.print')
    def test_do_update(self, mock_print):
        """Testing Do Update"""
        with patch('console.class_create', return_value=Mock())
        as mock_class_create:
            with patch('console.storage.all', return_value={'MyClass.1':
                Mock()}) as mock_storage_all:
                with patch('builtins.eval', return_value='new_value')
                as mock_eval:
                    self.cmd.do_update("MyClass 1 attribute_name new_value")
                    mock_print.assert_called_once_with('Attribute updated')

        self.cmd.do_update("")
        mock_print.assert_called_once_with('** class name missing **')

        with patch('console.class_create', return_value=Mock())
        as mock_class_create:
            self.cmd.do_update("MyClass")
            mock_print.assert_called_once_with('** instance id 
                missing **')

        with patch('console.class_create', return_value=Mock())
        as mock_class_create:
            self.cmd.do_update("MyClass 1")
            mock_print.assert_called_once_with('** attribute name
                    missing **')

        with patch('console.class_create', return_value=Mock())
        as mock_class_create:
            self.cmd.do_update("MyClass 1 attribute_name")
            mock_print.assert_called_once_with('** value missing **')

    def test_quit_command(self):
        """Testing Quit Command"""
        with patch("sys.exit") as mock_exit:
            self.command_interpreter.onecmd("quit")
            mock_exit.assert_called_once_with()

    def test_eof_command(self):
        """Testing EOF Command"""
        with patch("sys.exit") as mock_exit:
            self.command_interpreter.onecmd("EOF")
            mock_exit.assert_called_once_with()

    def test_emptyline_command(self):
        """Testing Emptyline Command"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.command_interpreter.onecmd("\n")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")


if __name__ == '__main__':
    unittest.main()
