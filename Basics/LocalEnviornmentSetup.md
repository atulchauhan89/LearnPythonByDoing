# If you want to have a local enviornment for a project

# Step1
  1) Open terminal in the root folder
  2) Run this command--> python -m venv venv
  3) In case of  homebrew installed Python run:python3 -m venv venv
  4) Once step 2 or 3 is done then execute -> venv\Scripts\activate.bat
  5) Now you are in the virtual enviornment. Now you can install your project dependancy by doing pip install.
  6) You can verify your installed files at venv folder in the root folder
  
 # Step2 How to install dependancy in the virtual env with from the requirement.txt
   Normal Setup-> pip install -r requirements.txt
    Homebrew Seteup-> pip3 install -r requirements.txt
