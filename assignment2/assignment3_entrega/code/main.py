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

def units_to_string_detailed(units, total, init_line=''):
    resp = ""
    for un in units:
        if hasattr(un, 'path'):
            resp = resp + "\n"
        resp = resp + init_line + un.name + " | "+str(un.lines)+ " | "+str(len(un.units))+" \n"
        resp = resp + units_to_string_detailed(un.units, None, init_line+'|-->')
    if total is not None:
        resp = "UNIT NAME | LINES | ITEMS"+resp
        #resp = resp + "\n\nTOTAL: "+str(total)
    return resp

def units_to_string_summarized(units, total, init_line=' * '):
    resp = ""
    resp = resp+"MODULE | LINES | ITEMS \n"
    for un in units:
        resp = resp + init_line + un.name + " | "+str(un.lines)+ " | "+str(len(un.units))+" \n"
    resp = resp + "\n\nTOTAL: "+str(total)
    return resp

path = input("\n\nCual es el path que se va a evaluar?\
	Para evaluar las carpetas que stán ubicadas dentro de el actual \
	, solo deje el espacio vacío.\n\n\n")
if path == "":
	path = "."

_eval = LinesOfCodeCounter()

units = _eval.get_modules_of_path(path)
units, total = _eval.inspect_modules(units)

resps = units_to_string_detailed(units, total)

sumr = units_to_string_summarized(units, total)

f1 = open('.result.txt', 'w+')
f1.write(resps)
#f1.write(str(units[0].__dict__))
f1.close

print(resps)
print("\n==============RESUME==============\n")
print(sumr)
