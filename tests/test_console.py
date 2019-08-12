#!/usr/bin/python3
"""Unit tests for comsole"""
import unittest
from models.base_model import BaseModel
"""
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
"""
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from datetime import datetime
import json
import io
from contextlib import redirect_stdout

class testsForConsole(unittest.TestCase):
    """Tests for comsole"""

    @classmethod
    def setUpClass(cls):
        """Prints that unit testing for console
        will commence!
        """
        print("\n...Testing for console...")

    def setUp(self):
        """setUp method creates console instance
        """
        self.hbnb = HBNBCommand()

    def tearDown(self):
        """tearDown method quits console instance if it's open"""
        try:
            self.hbnb.do_quit()
        except TypeError:
            pass

    def test_doc_string(self):
        """Tests doc string of console"""
        doc = ('console').__doc__
        self.assertIsNotNone(doc)

    def test_prompt(self):
        """Tests if the command prompt is correct"""
        self.assertEqual(self.hbnb.prompt, "(hbnb) ")

    def test_prompt_stdout(self):
        """Tests prompt prints to stdout correctly"""
        self.hbnb.do_quit()
        f = io.StringIO()
        with redirect_stdout(f):
            hbnb = HBNBCommand()
            self.assertEqual(f, "(hbnb) ")

    def test_do_quit_return_true(self):
        """Tests if quit returns correct value"""
        self.assertEqual(self.hbnb.do_quit(), True)

    def test_quit_too_many_args(self):
        """Tests quit with too many args"""
        self.assertEqual(self.hbnb.do_quit("arg"), True)

    def test_do_EOF_return_true(self):
        """Tests EOF returning true"""
        self.assertEqual(self.hbnb.do_EOF(), True)

    def test_do_create(self):
        """Tests creation of a new object"""
        x = self.hbnb.do_create("BaseModel")
        self.assertEqual(type(x), type(BaseModel()))

    def test_do_create_no_args(self):
        """Tests create with no class name"""
        strio = io.StringIO()
        with redirect_stdout(strio):
            self.hbnb.do_create()
            self.assertEqual(strio, "** class name missing **)")

    def test_do_create_too_many_args(self):
        """Tests create with too many arguments"""
        strio = io.StringIO()
        with redirect_stdout(strio):
            self.hbnb.do_create("BaseModel", "arg")
            self.assertEqual(strio, "** too many args **")

    def test_create_arg_in_wrong_place(self):
        """Tests args in the wrong place"""
        pass

    def test_create_too_many_wrong_args(self):
        """Tests create with too many args all incorrect"""
        pass

    def test_load_file(self):
        """Tests that a created file is loaded when a new console
        is started"""
        pass

    def test_show_no_args(self):
        """Tests show with no args"""
        strio = io.StringIO()
        with redirected_stdout(strio):
            self.hbnb.do_show()
            self.assertEqual(strio, "** instance id missing **")

    def test_show_one(self):
        """Tests show with one correct arg"""
        strio = io.StringIO()
        self.hbnb.do_show(BaseModel)
        with redirected_stdout(strio):
            self.assertEqual(strio, "")

    def test_show_one_bad(self):
        """Tests show with one bad arg"""
        pass

    def test_show_two_ok(self):
        """Tests standard usage of show"""
        pass

    def test_show_args_wrong_place(self):
        """Tests show with args in the wrong place"""
        pass

    def test_show_bad_id(self):
        """Tests show with a bad id"""
        pass

    def test_show_bad_model_good_id(self):
        """Tests show with only the first argument incorrect"""
        pass

    def test_show_too_many_args(self):
        """Tests show with too many args"""
        pass

    def test_show_bad_model_too_many(self):
        """Tests show with too many arguments and a bad model"""
        pass

    def test_show_bad_id_too_many(self):
        """Tests show with too many args and a bad id"""
        pass

    def test_show_bad_both_too_many(self):
        """Tests show with too many args all bad"""
        pass

    def test_all_no_args(self):
        """Tests all with no args"""
        pass

    def test_all_BaseModel(self):
        """Tests all with the BaseModel class"""
        pass

    def test_all_User(self):
        """Tests all with the User class"""
        pass

    def test_all_FileStorage(self):
        """Tests all with the FileStorage class"""
        pass

    def test_all_bad(self):
        """Tests all with a bad argument"""
        pass

    def test_all_too_many_ok(self):
        """Tests all with too many arguments"""
        pass

    def test_all_args_wrong_place(self):
        """Tests all with args in the wrong place"""
        pass

    def test_all_too_many_bad(self):
        """Tests all with bad args and too many"""
        pass

    def test_destroy_BaseModel(self):
        """Tests destruction of created BaseModel"""
        pass

    def test_destroy_User(self):
        """Tests destruction of a User"""
        pass

    def test_destroy_FileStorage(self):
        """Tests destruction of a FileStorage instance"""
        pass

    def test_destroy_too_few_args(self):
        """Tests destroy with too few args"""
        pass

    def test_destroy_bad_model(self):
        """Tests destroy with a bad model"""
        pass

    def test_destroy_bad_id(self):
        """Tests destroy with a bad id"""
        pass

    def test_destroy_too_many_args(self):
        """Tests destroy with too many args"""
        pass

    def test_destroy_args_wrong_place(self):
        """Tests destroy with misplaced args"""
        pass

    def test_update_no_args(self):
        """Tests update with no args"""
        pass

    def test_update_1_only_model(self):
        """Tests update with only a model"""
        pass

    def test_update_1_bad_model(self):
        """Tests update with only a bad model"""
        pass

    def test_update_2_ok_args(self):
        """Tests update with only 2 correct args"""
        pass

    def test_update_2_bad_model(self):
        """Tests update with 2 args, bad model"""
        pass

    def test_update_2_bad_id(self):
        """Tests update with 2 args, bad id"""
        pass

    def test_update_2_both_bad(self):
        """Tests update with 2 bad args"""
        pass

    def test_update_3_bad_model(self):
        """Tests update with 3 args, bad model"""
        pass

    def test_update_3_bad_id(self):
        """Tests update with 3 args, bad id"""
        pass

    def test_update_3_bad_attr(self):
        """Tests update with 3 args, bad attribute"""
        pass

    def test_update_3_bad_model_id(self):
        """Tests update with 3 args, bad model and id"""
        pass

    def test_update_3_bad_id_attr(self):
        """Tests update with 3 args, bad id and attribute"""
        pass

    def test_update_3_bad_model_attr(self):
        """Tests update with 3 args, bad model and attribute"""
        pass

    def test_update_3_all_bad(self):
        """Tests update with 3 args, all bad"""
        pass

    def test_update_4_ok(self):
        """Tests update with standard usage"""
        pass

    def test_update_4_bad_model(self):
        """Tests update with 4 args, bad model"""
        pass

    def test_update_4_bad_model_id(self):
        """Tests update with 4 args, bad model and id"""
        pass

    def test_update_4_bad_model_id_attr(self):
        """Tests update with 4 args, bad model, id, attribute"""
        pass

    def test_update_4_all_bad(self):
        """Tests update with 4 args, all bad"""
        pass

    def test_update_4_bad_id(self):
        """Tests update with 4 args, bad id only"""
        pass

    def test_update_4_bad_id_attr(self):
        """Tests update with 4 args, bad id and attribute"""
        pass

    def test_update_4_bad_id_attr_value(self):
        """Tests update with 4 args, bad id, attribute, value"""
        pass

    def test_update_4_bad_id_value(self):
        """Tests update with 4 args, bad id and value"""
        pass

    def test_update_4_bad_attr(self):
        """Tests update with 4 args, bad attribute only"""
        pass

    def test_update_4_bad_attr_value(self):
        """Tests update with 4 args, bad attribute and value"""
        pass

    def test_update_4_bad_value(self):
        """Tests update with 4 args, bad value"""
        pass

    def test_update_4_all_bad(self):
        """Tests update with 4 bad args"""

    def test_update_4_args_wrong_place(self):
        """Tests update with 4 args in the wrong place"""
        pass

    def test_update_too_many_args_ok(self):
        """Tests update with too many args"""
        pass

    def test_update_too_many_bad(self):
        """Tests update with too many args, all bad"""
        pass

if __name__ == '__main__':
    unittest.main
