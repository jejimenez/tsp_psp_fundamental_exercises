"""
.. module:: lines_of_code_counter
   :platform: Unix, Windows
   :synopsis: Count the lines of a python program given by params. Exclude 
   the comment and empty lines. Count the lines in every unit of program:
   class, function, subclass, etc. And print the result

.. moduleauthor:: Jaime Jimenez

"""
import os
import fnmatch
from enum import Enum

class LinesOfCodeCounter:
    """This is the main class to count the lines of code. First set the 
    path attribute to start the inspection.
    """
    class Unit():
        """Used as every unit in the program (class, function, subclass)"""
        pass

    class Type():
        """ Type of Units """
        _module = "module"
        _class = "class"
        _function = "def"

    def __init__(self):
        self.path = None
        self.units = []
        self.total = 0

    def get_modules_of_path(self, path=None):
        """Function to set the first level of units (top_level) that are
        modules or py files
        """
        if self.path is None:
            self.path = path
        if self.path is None:
            raise ValueError("Please set a value in path first!. Or give it as\
                param")
        for root, dirs, files in os.walk(self.path, topdown=False):
            for name in fnmatch.filter(files, "*.py"):
                u = self.Unit()
                u.name = name
                u.path = os.path.join(root, name)
                u.type = self.Type._module
                self.units.append(u)
                #print(u.__dict__)
            #for name in dirs:
        #print(self.units[0].__dict__)
        return self.units

    def inspect_module(self, unit):
        """Count the number of lines of module and  units inside the 
           module
        """
        #:10:20 - 11:00
        if not os.path.exists(unit.path):
            raise ValueError("There is a problem loading the file "+unit.path)
        with open(unit.path) as f:
            content = f.read().splitlines()
            unit.units = []
            #print(unit.__dict__)
            unit_final, n_real_lines = self.count_lines_in_array(content, unit)
            unit_final.last_line = n_real_lines
            unit.init_line = 1
            self.total = self.total + unit.lines
            #print(unit_final)
            return unit_final

    def inspect_modules(self, units):
        aux_units = []
        #print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>3")
        for un in units:
            aux_units.append(self.inspect_module(un))
        return aux_units, self.total


    def count_lines_in_array(self, content, unit, content_row=0):
        """get the conent array with the lines of code to inspect """
        #ext_lines = n_lines
        #for ln in range() content[content_row:]:
        n_level = None
        n_lines = 0
        comment_oppened = False
        while True:
            if content_row >= len(content):
                break
            l = content[content_row]
            content_row += 1
            if l.strip() != '':
                #Exclude the empty lines
                aux_level = 0
                for char in l:
                    #Control the indentation of code to know if get out from
                    #unit
                    if char == ' ' or char == '\t':
                        aux_level += 1
                    else:
                        break
                if n_level is None:
                    #Store first level. If lines has level less than the first
                    #then is getting out of the current scope
                    n_level = aux_level
                words = l.split()
                if (not words[0].startswith('#') and not words[0].startswith('"""') 
                and not comment_oppened):
                    #Exclude the comments: when line is not starting with # or """
                    if aux_level >= n_level:
                        if words[0].startswith(str(self.Type._class)) or words[0].startswith(str(self.Type._function)):
                            nested_unit = self.Unit()
                            nested_unit.name = l.strip()
                            nested_unit.init_line = content_row
                            nested_unit.units = []
                            nested_unit, content_row_nested = self.count_lines_in_array(content,
                            nested_unit, content_row)
                            nested_unit.last_line = content_row_nested
                            unit.units.append(nested_unit)
                            n_lines += nested_unit.lines
                            content_row = content_row_nested
                        else:
                            n_lines += 1
                    else:
                        unit.lines = n_lines+1
                        unit.end_line = content_row
                        return unit, content_row-1
                # if this line is a comment embraced by """ just continue
                elif l.strip().startswith('"""') and l.strip().endswith('"""') and len(l.strip()) > 3:
                    continue
                # if this is a start or end of lie
                elif l.strip().startswith('"""') or l.strip().endswith('"""'):
                    comment_oppened = not comment_oppened
                    #print("comment open or close "+str(comment_oppened)+" - "+str(content_row)+" - "+str(l[:30]))
            else:
                #print(str(content_row))
                continue

        unit.lines = n_lines
        #print(unit.__dict__)
        return unit, content_row
