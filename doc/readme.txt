Install latest Python 
- Make sure it's available to everyone
- Preferably install the 64 bit version
- in my case it's installed in this location: C:\Program Files\Python38


Create virtual environment 
- In your project folder run the following command to create one
- python -m venv
- You should see a .venv subfolder created under your project folder. 
- All pip packages will be installed locally in this folder
- Say yes when VS Code ask if you want to switch to this virtual 
  environment
 
Install pipenv
- pipenv allows you to manage pip packages like npm 
- run the following command with Admin priviledge
- pip install pipenv
- where it is installed:   
- C:\Program Files (x86)\Python38-32\Lib\site-packages\pipenv
- from now on use pipenv instead of pip to install packages

Install jupyter
- run the following command in your project folder 
  to install jupyter 
- pipenv install jupyter
- the package should be installed inside .venv\lib\site-packages
- check Pipfile under your project file, and you will see this entry
  [packages]
  jupyter = "*"

Install Microsoft Python extension to your VS Code 
https://marketplace.visualstudio.com/items?itemName=ms-python.python
   




