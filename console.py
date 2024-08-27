#!/usr/bin/python3
"""
Contains a class for command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def class_create(line):
    """
    Function to try creating a class if it exists
    """
    if len(line) == 0:
        msg = "** class name missing **"
        return msg
    else:
        try:
            class_name = eval(line)
            return class_name
        except NameError:
            msg = "** class doesn't exist **"
            return msg


def line_to_words(line):
    """
    Function to create words in a line
    """
    line_list = []
    word = ""
    count = 0
    for letter in line:
        word = word + letter
        if letter.isspace() is True:
            line_list.append(word)
            word = ""
        count = count + 1
        if count == len(line):
            line_list.append(word)
    stripped_words = []
    for word in line_list:
        word = word.strip()
        stripped_words.append(word)
    return stripped_words


def check_id(word1, word2):
    """
    Function to check if instance exists with id given
    """
    obj = storage.all()
    for key, value in obj.items():
        class_name, ids = key.split(".")
        if class_name == word1 and ids == word2:
            return value
    message = "** no instance found **"
    return message


def print_all(length, line):
    """
    Function for string representation of classes
    """
    if length == 0:
        obj = storage.all()
        instances = []
        for key, value in obj.items():
            instances.append(str(value))
        return instances
    else:
        creating = class_create(line[0])
        if type(creating) is str:
            return creating
        else:
            instances = []
            obj = storage.all()
            for key, value in obj.items():
                class_name, ids = key.split(".")
                if class_name == creating.__name__:
                    instances.append(str(value))
            return instances


class HBNBCommand(cmd.Cmd):
    """
    Class containing entry point
    of command interpreter
    """
    prompt = '(hbnb) '

    def do_create(self, line):
        """
        Create command to creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        creating = class_create(line)
        if type(creating) is str:
            print(creating)
        else:
            my_model = creating()
            my_model.save()
            print(my_model.id)

    def do_show(self, line):
        """
        Show command to prints the string representation of
        an instance based on the class name and id
        """
        words_list = line_to_words(line)
        if len(line) == 0:
            print("** class name missing **")
            return
        creating = class_create(words_list[0])
        if type(creating) is str:
            print(creating)
        else:
            if len(words_list) == 1:
                print("** instance id missing **")
            elif len(words_list) > 1:
                instance = check_id(words_list[0], words_list[1])
                print(instance)

    def do_destroy(self, line):
        """
        Destroy command to delete an instance based on
        the class name and id (save the change into the
        JSON file)
        """
        words_list = line_to_words(line)
        if len(line) == 0:
            print("** class name missing **")
            return
        creating = class_create(words_list[0])
        if type(creating) is str:
            print(creating)
        else:
            if len(words_list) == 1:
                print("** instance id missing **")
            elif len(words_list) > 1:
                instance = check_id(words_list[0], words_list[1])
                if type(instance) is str:
                    print(instance)
                else:
                    obj = storage.all()
                    for key, value in obj.items():
                        if instance == value:
                            del obj[key]
                            storage.save()
                            break

    def do_all(self, line):
        """
        All command to print all string representation of
        all instances based or not on the class name
        """
        words_list = line_to_words(line)
        all_inst = print_all(len(words_list), words_list)
        print(all_inst)

    def do_update(self, line):
        """
        Update command to update an instance based on the
        class name and id by adding or updating attribute
        (save the change into the JSON file)
        """
        words_list = line_to_words(line)
        if len(line) == 0:
            print("** class name missing **")
            return
        creating = class_create(words_list[0])
        if type(creating) is str:
            print(creating)
        else:
            if len(words_list) == 1:
                print("** instance id missing **")
            elif len(words_list) > 1:
                instance = check_id(words_list[0], words_list[1])
                if type(instance) is str:
                    print(instance)
                    return
                if len(words_list) == 2:
                    print("** attribute name missing **")
                    return
                elif len(words_list) == 3:
                    print("** value missing **")
                    return
                else:
                    if words_list[3][0] != '"':
                        words_list[3] = eval(words_list[3])
                    elif words_list[3][0] == '"' and words_list[3][-1] == '"':
                        words_list[3] = eval(words_list[3])
                    if len(words_list) > 4:
                        if words_list[3][0] == '"':
                            if words_list[len(words_list) - 1][-1] == '"':
                                m = words_list[3][1:]
                                new_word = []
                                for words in words_list[4:len(words_list) - 1]:
                                    new_word.append(words)
                                o = words_list[len(words_list) - 1][0:-1]
                                if len(new_word) > 0:
                                    n = ""
                                    for word in new_word:
                                        n = n + word + " "
                                else:
                                    n = " "
                                words_list[3] = m + " " + n + o
                    obj = storage.all()
                    for key, value in obj.items():
                        if instance == value:
                            setattr(instance, words_list[2], words_list[3])
                            value.save()
                            break

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, line):
        """EOF command to exit the program"""
        exit()

    def emptyline(line):
        """
        Empty line + ENTER shouldn�~@~Yt execute anything
        """
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
