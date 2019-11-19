#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 21:53:10 2019

@author: root
"""
import numpy as nitards
u=nitards.arange(1,101,1).reshape(10,10)
x=u*u
print("thiis is the matrix",u)
div3=x[x%3==0]
print("this are the ones divisible by 3",div3)