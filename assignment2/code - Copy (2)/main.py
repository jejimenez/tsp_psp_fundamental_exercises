"""
.. module:: main
   :platform: Unix, Windows
   :synopsis: Call the lines_of_code_counter program.
   Count the lines in every unit of program:
   class, function, subclass, etc.

.. moduleauthor:: Jaime Jimenez


"""
import os
from lines_of_code_counter import LinesOfCodeCounter



def units_to_string(units, total, tabs=''):
    resp = ""
    for un in units:
        if hasattr(un, 'path'):
            resp = resp + "\n"
        resp = resp + tabs + un.name + " | "+str(un.lines)+" \n"
        resp = resp + units_to_string(un.units, None, tabs+'|-->')
    if total is not None:
        resp = resp + "\n\nTOTAL: "+str(total)
    return resp

path = input("Cual es el path que se va a evaluar?\
	Para evaluar las carpetas que stán ubicadas dentro de el actual \
	, solo deje el espacio vacío.\n\n\n")
if path == "":
	path = "."

_eval = LinesOfCodeCounter()

units = _eval.get_modules_of_path(path)
units, total = _eval.inspect_modules(units)

resps = units_to_string(units, total)


f1 = open('.result.txt', 'w+')
f1.write(resps)
#f1.write(str(units[0].__dict__))
f1.close

print(resps)
