"""
.. module:: ProbeMethod
   :platform: Unix, Windows
   :synopsis: Calculate linear regression parameters (ßø y ß¡) and correlation
   parameters (r y r²)..
   Count the lines in every unit of program:
   class, function, subclass, etc.

.. moduleauthor:: Jaime Jimenez


"""
import math

class ProbeMethodVals:

    def __init__(self, linked_list = None):
        self.sum_XY = None
        self.sum_X = None
        self.sum_Y = None
        self.avg_X = None
        self.avg_Y = None
        self.sum_X_saquared = None
        self.sum_Y_saquared = None
        self.n = None
        if linked_list is not None:
            self.calculate_vals(linked_list)

    def calculate_vals(self, linked_list = None):
        """Return all the values of the object calculated. 
        Args: 
           linked_list: LinkedList with the values to calculate the all the vals.
        Returns: 
           self.  ProbeMethod object with all the values already calculated 

        >>> print calculate_vals(self, linked_list = None) self

        """
        if linked_list is None:
            raise ValueError("Please populate the linked_list")
        i = self.sum_XY =  self.sum_X =  self.sum_Y = \
        self.sum_X_saquared = self.sum_Y_saquared = 0
        for nd in linked_list:
            x, y = nd.value[0], nd.value[1]
            self.sum_XY += (x*y)
            self.sum_X += x
            self.sum_Y += y
            self.sum_X_saquared += (x**2)
            self.sum_Y_saquared += (y**2)
            i += 1
        self.avg_X = self.sum_X / i
        self.avg_Y = self.sum_Y / i
        self.avg_XY = self.sum_XY / i
        self.n = i
        return self

class LinearRegression:

    def __init__(self, probe_vals = None, linked_list = None, E = None):
        self.beta_0 = None
        self.beta_1 = None
        self.linked_list = None
        self.E = E
        self.__init_probe_vals(probe_vals, linked_list)

    def __init_probe_vals(self, probe_vals, linked_list):
        """Initialize the values of ProbeMethod based on probe_vals or linked_list. 
        Args: 
           probe_vals: probe_vals object with all the vals.
           linked_list: LinkedList with the values to calculate the all the vals.

        >>> print __init_probe_vals(self, probe_vals, linked_list) 

        """
        if probe_vals is not None:
            self.probe_vals = probe_vals
        elif linked_list is not None:
            self.linked_list = linked_list
            self.probe_vals = ProbeMethodVals(linked_list)
        else:
            self.probe_vals = ProbeMethodVals()

    def get_beta_1(self):
        """Return the value of beta_1 .
        Returns: 
           self.beta_1  value of beta_1 calculated 

        >>> print get_beta_1(self) self.beta_1

        """
        vals = self.probe_vals
        if self.beta_1 is not None:
            return self.beta_1
        if vals is None:
            vals = self.probe_vals.calculate_vals(self.linked_list)
        self.beta_1 = (vals.sum_XY - (vals.n * vals.avg_X * vals.avg_Y)) / \
            (vals.sum_X_saquared - (vals.n * (vals.avg_X**2)))
        return self.beta_1

    def get_beta_0(self):
        """Return the value of beta_0 .
        Returns: 
           self.beta_1  value of beta_0 calculated 

        >>> print get_beta_0(self) self.beta_0

        """
        vals = self.probe_vals
        if self.beta_0 is not None:
            return self.beta_0
        if self.beta_1 is None:
            self.get_beta_1()
        self.beta_0 = vals.avg_Y - (self.beta_1 * vals.avg_X)
        return self.beta_0

    def get_P(self, E = None):
        """Return the value of beta_0 .
        Args: 
           E: estimated proxy size value.
        Returns: 
           self.P  value of prediction calculated 

        >>> print get_P(self, E = None) self.P

        """
        if E is not None:
            self.E = E
        if self.E is None:
            raise ValueError("You must assign a value to E to calc the Prediction")
        self.P = self.beta_0 + (self.beta_1 * self.E)
        return self.P




class CorrelationFactor:

    def __init__(self, probe_vals = None, linked_list = None):
        self.r = None
        self.r_squared = None
        self.__init_probe_vals(probe_vals, linked_list)

    def __init_probe_vals(self, probe_vals, linked_list):
        """Initialize the values of ProbeMethod based on probe_vals or linked_list. 
        Args: 
           probe_vals: probe_vals object with all the vals.
           linked_list: LinkedList with the values to calculate the all the vals.

        >>> print __init_probe_vals(self, probe_vals, linked_list) 

        """
        if probe_vals is not None:
            self.probe_vals = probe_vals
        elif linked_list is not None:
            self.linked_list = linked_list
            self.probe_vals = ProbeMethodVals(linked_list)
        else:
            self.probe_vals = ProbeMethodVals()

    def get_r(self):
        """Return the value of r .
        Returns: 
           self.r  value of r calculated 

        >>> print get_r(self) self.r

        """
        vals = self.probe_vals
        if self.r is not None:
            return self.r
        if vals is None:
            vals = self.probe_vals.calculate_vals(self.linked_list)
        self.r = ((vals.n * vals.sum_XY) - (vals.sum_X * vals.sum_Y)) / \
            math.sqrt(((vals.n * vals.sum_X_saquared) - vals.sum_X**2 ) * 
            ((vals.n * vals.sum_Y_saquared) - vals.sum_Y**2 ) )
        return self.r

    def get_r_squared(self):
        """Return the value of r_squared .
        Returns: 
           self.r_squared  value of r_squared calculated 

        >>> print get_r_squared(self) self.r_squared

        """
        if self.r_squared is not None:
            return self.r_squared

        self.r_squared = self.r**2
        return self.r_squared













