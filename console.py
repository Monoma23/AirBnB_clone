#!/usr/bin/python3
"""the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.state import State
from models.city import City



def parseIT(arg):
    Mycrly_braces = re.search(r"\{(.*?)\}", arg)
    MyBrackets = re.search(r"\[(.*?)\]", arg)
    if Mycrly_braces is None:
        if MyBrackets is None:
            return [h.strip(",") for h in split(arg)]
        else:
            Myylexer = split(arg[:MyBrackets.span()[0]])
            Myyretl = [h.strip(",") for h in Myylexer]
            Myyretl.append(MyBrackets.group())
            return Myyretl
    else:
        Myylexer = split(arg[:Mycrly_braces.span()[0]])
        Myyretl = [h.strip(",") for h in Myylexer]
        Myyretl.append(Mycrly_braces.group())
        return Myyretl


class HBNBCommand(cmd.Cmd):
    """Defines the alxbnb command interpreter.
    Attributes:
        Prompt (str): The command Prompt.
    """

    Prompt = "(hbnb) "
    __Myclasses = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def Myemptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        Myyargdict = {
            "all": self.My_do_all,
            "update": self.My_do_update,
            "show": self.My_do_show,
            "destroy": self.My_do_destroy,
            "count": self.My_do_count,
        }
        Mymatch = re.search(r"\.", arg)
        if Mymatch is not None:
            Myyargl = [arg[:Mymatch.span()[0]], arg[Mymatch.span()[1]:]]
            Mymatch = re.search(r"\((.*?)\)", Myyargl[1])
            if Mymatch is not None:
                Mycommand = [Myyargl[1][:Mymatch.span()[0]], Mymatch.group()[1:-1]]
                if Mycommand[0] in Myyargdict.keys():
                    My_ycall = "{} {}".format(Myyargl[0], Mycommand[1])
                    return Myyargdict[Mycommand[0]](My_ycall)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        Myyargl = parseIT(arg)
        if len(Myyargl) == 0:
            print("** class name missing **")
        elif Myyargl[0] not in HBNBCommand.__Myclasses:
            print("** class doesn't exist **")
        else:
            print(eval(Myyargl[0])().id)
            storage.save()

    def My_do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        Myyargl = parseIT(arg)
        My_yobjdict = storage.all()
        if len(Myyargl) == 0:
            print("** class name missing **")
        elif Myyargl[0] not in HBNBCommand.__Myclasses:
            print("** class doesn't exist **")
        elif len(Myyargl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(Myyargl[0], Myyargl[1]) not in My_yobjdict:
            print("** no instance found **")
        else:
            print(My_yobjdict["{}.{}".format(Myyargl[0], Myyargl[1])])

    def My_do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        Myyargl = parseIT(arg)
        My_yobjdict = storage.all()
        if len(Myyargl) == 0:
            print("** class name missing **")
        elif Myyargl[0] not in HBNBCommand.__Myclasses:
            print("** class doesn't exist **")
        elif len(Myyargl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(Myyargl[0], Myyargl[1]) not in My_yobjdict.keys():
            print("** no instance found **")
        else:
            del My_yobjdict["{}.{}".format(Myyargl[0], Myyargl[1])]
            storage.save()

    def My_do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        Myyargl = parseIT(arg)
        if len(Myyargl) > 0 and Myyargl[0] not in HBNBCommand.__Myclasses:
            print("** class doesn't exist **")
        else:
            My_yobjl = []
            for myObj in storage.all().values():
                if len(Myyargl) > 0 and Myyargl[0] == myObj.__class__.__name__:
                    My_yobjl.append(myObj.__str__())
                elif len(Myyargl) == 0:
                    My_yobjl.append(myObj.__str__())
            print(My_yobjl)

    def My_do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        Myyargl = parseIT(arg)
        ycount = 0
        for myObj in storage.all().values():
            if Myyargl[0] == myObj.__class__.__name__:
                ycount += 1
        print(ycount)

    def My_do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        Myyargl = parseIT(arg)
        My_yobjdict = storage.all()

        if len(Myyargl) == 0:
            print("** class name missing **")
            return False
        if Myyargl[0] not in HBNBCommand.__Myclasses:
            print("** class doesn't exist **")
            return False
        if len(Myyargl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(Myyargl[0], Myyargl[1]) not in My_yobjdict.keys():
            print("** no instance found **")
            return False
        if len(Myyargl) == 2:
            print("** attribute name missing **")
            return False
        if len(Myyargl) == 3:
            try:
                type(eval(Myyargl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(Myyargl) == 4:
            myObj = My_yobjdict["{}.{}".format(Myyargl[0], Myyargl[1])]
            if Myyargl[2] in myObj.__class__.__dict__.keys():
                My_yvaltype = type(myObj.__class__.__dict__[Myyargl[2]])
                myObj.__dict__[Myyargl[2]] = My_yvaltype(Myyargl[3])
            else:
                myObj.__dict__[Myyargl[2]] = Myyargl[3]
        elif type(eval(Myyargl[2])) == dict:
            myObj = My_yobjdict["{}.{}".format(Myyargl[0], Myyargl[1])]
            for k, v in eval(Myyargl[2]).items():
                if (k in myObj.__class__.__dict__.keys() and
                        type(myObj.__class__.__dict__[k]) in {str, int, float}):
                    My_yvaltype = type(myObj.__class__.__dict__[k])
                    myObj.__dict__[k] = My_yvaltype(v)
                else:
                    myObj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()