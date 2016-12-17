"""
.. module:: RelativeSize
   :platform: Unix, Windows
   :synopsis: Calculate the relative sizes XS, S, M , L, XL from
   the array passed in arr variable.
   The array must be in the form [[20,3],[55,6],[43,2],[10,4],...] or
   [[10],[5],[40],[12],[14],...]

.. moduleauthor:: Jaime Jimenez

"""
import math

class RelativeSize:

    def __init__(self, arr = None):
        self.XS = self.S = self.M = self.L = self.XL = None
        self.avg = self.var = self.sd = self.vals = None
        if arr is not None:
            self.set_vals(arr)
            self.calc_relative_sizes()

    def calc_relative_sizes(self):
        """
        Calculate the required values and finaly the relative sizes.

        """
        len_arr = len(self.vals)
        self.avg = self.sum_ln(self.vals)/len_arr
        self.var = self.sum_variance(self.vals, self.avg) / (len_arr-1)
        self.ds = math.sqrt(self.var)
        self.XS = math.exp(self.avg-(2*self.ds))
        self.S = math.exp(self.avg-(1*self.ds))
        self.M = math.exp(self.avg-(0*self.ds))
        self.L = math.exp(self.avg+(1*self.ds))
        self.XL = math.exp(self.avg+(2*self.ds))

    def antilog(self, x):
        return 10**x

    def sum_variance(self, arr, avg):
        """
        Calculate the variance of the array elements
        Args:
           arr: Array with the vals to calculate the variance
        Returns:
           Number: The value of the variance.

        """
        sum_var = 0
        for a in arr:
            sum_var = sum_var + ((math.log(a)-avg)**2)
        return sum_var

    def sum_ln(self, arr):
        """
        Calculate the sum of the logarithm natural of every array element
        Args:
           arr: Array with the vals to calculate the sum of logarithm natural
        Returns:
           Number: The value of the sum of the logarithm natural.

        """
        sum_ln = 0
        for a in arr:
            sum_ln = sum_ln + math.log(a)
        return sum_ln

    def set_vals(self, arr):
        """
        Get the values from the multimimentional array arr, and set in 
        the simple array values.
        Args:
           arr: Multidimentional array with the value`s of the Headers.

        """
        vals = []
        for i in arr:
            if len(i) == 1:
                vals.append(i[0])
            elif len(i) == 2:
                vals.append(i[0]/i[1])
            else:
                raise ValueError("El array recibido para calcular el tamaño\
                    relativo no es correcto")
        self.vals = vals
