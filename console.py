#!/usr/bin/python3
""" this is Cmd interpreter.
"""
import cmd

from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command iterpreter public class supporting inheritance from base class cmd
    """
    prompt = '(hbnb) '
    __clsss = ["BaseModel", "User", "State", "City", "Amenity", "Place",
             "Review"]

    def my_exit(self, ligne):
        """quit cmd ^ exit program
        """
        return True

    def end_file(self, ligne):
        """ctrl+d => exit the program
        """
        print()
        return True

    def vide_ligne(self):
        """appeler when empty ligne then Enter
        """
        pass

    def create_baseMDL(self, ligne):
        """ use: create a BaseModel
        Build new instance of BaseModel, save it 
        and display id
        """
        args = ligne.split(" ")
        if args[0] == "":
            print("** class name missing **")
        elif not args[0] in __class__.__clsss:
            print("** class doesn't exist **")
        else:
            if args[0] == "BaseModel":
                my_instance = BaseModel()
            elif args[0] == "User":
                my_instance = User()
            elif args[0] == "State":
                my_instance = State()
            elif args[0] == "City":
                my_instance = City()
            elif args[0] == "Amenity":
                my_instance = Amenity()
            elif args[0] == "Place":
                my_instance = Place()
            elif args[0] == "Review":
                my_instance = Review()
            print(my_instance.id)

    def reveal_str(self, ligne):
        """Print str representation of instance based on classname & id
        """
        args = ligne.split(" ")
        if args[0] in __class__.__clsss:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                all_objs = storage.all()
                for obj_id in all_objs.keys():
                    if key == obj_id:
                        print(all_objs[obj_id])
                        break
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        elif args[0] == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def Destroy_it(self, ligne):
        """Delete instance based on classname and id then save changes
        intoo JSON file
        """
        args = ligne.split(" ")
        if args[0] in __class__.__clsss:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                objs_dictionr = storage.all()
                if objs_dictionr.pop(key, None) is None:
                    print("** no instance found **")
                else:
                    storage.save()
            else:
                print("** instance id missing **")
        elif args[0] == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def display_all(self, ligne):
        """Prints string representations of all instances whatever the class name
        """
        args = ligne.split(" ")
        if args[0] == "" or args[0] in __class__.__clsss:
            strgg_obj = []
            all_objs = storage.all()
            for obj_key in all_objs.keys():
                if args == [''] or obj_key.split(".")[0] == args[0]:
                    strgg_obj.append(str(all_objs[obj_key]))
            print(strgg_obj)
        else:
            print("** class doesn't exist **")

    def update_inst(self, ligne):
        """Updates instance based on class name and id
        """
        args = ligne.split(" ")
        if args[0] == "":
            print("** class name missing **")
        elif not args[0] in __class__.__clsss:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = storage.all()
            if key in all_objs.keys():
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(storage.all()[key], args[2], args[3])
                    storage.all()[key].save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()