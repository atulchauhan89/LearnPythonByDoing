"""
Let's start with Hello World program as a bignner.
Python source files use the ".py" extension we called them as "modules". 
"""

"""
import is used to import any module. We will import sys module,which is a standerd module.
Modules are pre written code in Python.As everybody who is coding in python need same kind of functionality in there programs,
So many Python comes with idea of Module. 
Module are basically code or programs created by other developer to help the community.
"""

import sys

# Create a main() function for stucturing our code.
def main():
    print("Hello, World!")
# "print()" is a built-in Python function that used for getting text output to the console.

# Standard boilerplate to call the main() function to begin the program.    
if __name__ == '__main__':
    main()
