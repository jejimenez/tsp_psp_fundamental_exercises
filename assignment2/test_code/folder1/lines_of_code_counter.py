"""
.. module:: lines_of_code_counter
   :platform: Unix, Windows
   :synopsis: Count the lines of a python program given by params. Exclude 
   the comment and empty lines. Count the lines in every unit of program:
   class, function, subclass, etc.

.. moduleauthor:: Jaime Jimenez


"""
import os
import fnmatch

class LinesOfCodeCounter:
    """This is the main class to count the lines of code. First set the 
    path attribute to start the inspection.
    """
    class Unit:
        """Used as every unit in the program (class, function, subclass)"""
        pass

    class Types(Enum):
    	""" Types of Units """
        _module = "module"
        _class = "class"
        _function = "function"

    def __init__(self):
        path = None
        units = []

    def get_modules_of_path(self, path=None):
        if self.path is None:
            self.path = path
        if self.path is None:
        	raise ValueError("Please set a value in path first!. Or give it as\
                param")
        #
        def set_modules(self):
            for root, dirs, files in os.walk(top, topdown=False):
                for name in fnmatch.filter(files, "*.py"):
            	    u = Unit()
            	    u.path = os.path.join(root, name)
            	    u.type = Types._module
                    units.append(u)
                #os.remove(os.path.join(root, name))
                for name in dirs:
                #os.rmdir(os.path.join(root, name))


