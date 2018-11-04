"""
Let's start with Hello World program as a beginner.
Python source files use the ".py" extension we called them as "modules". 
"""

"""
import is used to import any module. We will import sys module, which is a standard module.
Modules are pre-written code in Python. As everybody who is coding in python need the same
kind of functionality in there programs,So many Python comes with the idea of Module. 
The module is basically code or programs created by other developers to help the community.
"""

import sys

# Create a main() function for stucturing our code.
def main():
    print("Hello, World!")
# "print()" is a built-in Python function that used for getting text output to the console.

# Standard boilerplate to call the main() function to begin the program.    
if __name__ == '__main__':
    main()
