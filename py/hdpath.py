# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 16:03:46 2016

@author: Kazuki
"""
import os

def load():
    if os.name != 'nt':
        if os.getcwd() == '/Users/Kazuki/Python':
            'Mac'
            path_org = "/Users/Kazuki/home-depot/ORG//"
            path_sub = "/Users/Kazuki/home-depot/SUB//"
        else:
            path_org = "/Users/Kazuki/Documents/home-depot/ORG//"
            path_sub = "/Users/Kazuki/Documents/home-depot/SUB//"
    else:
        'Win'
#        path_org = "D:\COMPE\KAGGLE\home-depot\ORG\\"
#        path_sub = "D:\COMPE\KAGGLE\home-depot\SUB\\"
        path_org = "G:\share\homedepo\ORG\\"
        path_sub = "G:\share\homedepo\SUB\\"
    return path_org,path_sub