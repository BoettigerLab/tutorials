import sys,os,glob
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Search for python-functions-library.
"""
Assumes the working folder and the python-functions folder share the same parent directory 
e.g. ...Code\my-notebook\this-Ipython-script.ipyn  
and   ...Code\python-functions\python-functions-library\...
"""
current_folder = os.path.dirname(os.path.abspath(__file__))
code_folder = os.path.dirname(code_folder)
python_functions_lib = code_folder+os.sep+'python-functions'+os.sep+'python-functions-library'
sys.path.append(python_functions_lib)
print 'Added to path: '+python_functions_lib

# import some libraries from the python-functions-library
import GeneralTools as gt # my general tools
import StormAnalysisAdditions as saa # library for STORM analysis
import imreg_dft as ird # for image registration, from web, optimized by BB




