## What is the PyQt?
   As per official documents "PyQt is a library that lets you use the Qt GUI framework from Python language. Qt is written in C++ language. You can build applications much more quickly using with Python and you have to make no compromise with the speed of C++."

   PyQt5 refers to the most recent version 5 of Qt. You may still find the occasional mention of (Py)Qt4 on the web, but it is old and no longer supported.

  An interesting new competitor to PyQt is Qt for Python. Its API is virtually identical. Unlike PyQt, it is licensed under the LGPL and can thus be used for free in commercial projects. It's backed by the Qt company, and thus likely the future. We use PyQt here because it is more mature. Since the APIs are so similar, you can easily switch your apps to Qt for Python later.

##  How to install PyQt5?
If you don't want any dependency with any other projects then creating a virtual environment will be right idea.

1) To create a virtual environment in the current directory, execute the following command:

  python3 -m venv venv

2) This will creates the venv/ folder. To activate the virtual environment on Windows, run:

  call venv/scripts/activate.bat

3) On Mac and Linux, use:

  source venv/bin/activate
4) It will look like this in Windows
   D:\DemoProject\PyQT_DesktopApp>python3 -m venv venv
   D:\DemoProject\PyQT_DesktopApp>call venv/scripts/activate.bat
   (venv) D:\DemoProject\PyQT_DesktopApp>

5) To now install PyQt, use the following command:
    pip install PyQt5==5.9.2
    
