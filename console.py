#!/usr/bin/python3
""" Console 0.0.1 """


import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ cmd class """

    prompt = "(hbnb) "

    cls = {"BaseModel", "User"}

    def do_quit(self, arg):
        """ Quit command to exist the program """
        return True

    def do_EOF(self):
        """ EOF command to exist the program"""
        return True

    def emptyline(self):
        """ skip empty line"""
        pass

    def do_create(self, arg):
        """ create a new instance of the class BaseModel """
        if arg == None:
            print ("** class doesn't exist **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print (new_instance.id)
            except NameError:
                print ("** class name missing **")


    def do_show(self, arg):
        """ show the string representaion of an instance based on ID """
        args = arg.split()
        if not args:
            print ("** class name missing **")
        else:
            cls_name = args[0]
            if len(args) == 0:
                print("** class name missing **")
            elif cls_name not in HBNBCommand.cls:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key_obj = "{}.{}".format(cls_name, args[1])
		all_objs = storage.all()
                if key_obj in all_objs:
                    print(all_objs[key_obj])
                else:
                    print("** no instance found **")





if __name__ == '__main__':
    HBNBCommand().cmdloop()
