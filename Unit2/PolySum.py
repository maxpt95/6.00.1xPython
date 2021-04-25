# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:09:11 2021

@author: maxperezt
"""

import math

def polysum(n, s):
    """
    n (int): number of sides in the polygon.
    s (float): length of the sides.
    
    Return:  
    polysum (float): sum of the area and square of the perimeter of the regular polygon. 
    """
    area = (0.25*n*s**2)/math.tan(math.pi/n);
    perimeter = s*n;
    
    polysum = area + perimeter**2;
    return round(polysum,4);

polys