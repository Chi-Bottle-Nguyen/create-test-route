# create-test-route
Automatically creates a route for driver on the Sharing Excess Food Rescue app

**Dependancies**

1, Chromedriver

_INSTALLATION_
- Download Chromedriver at: https://chromedriver.storage.googleapis.com/index.html?path=87.0.4280.20/
- Extract the ```chromedriver.exe``` 
- Put the path for ```chromedriver.exe``` in your PATH variable (assusming you're using Windows). You might want to restart your laptop.
- If you've done that, and the script doesn't work, put ```chromedriver``` in your Python\Python38-32\Scripts (or in the Scripts folder of whatever Python version you're using)

2, Selenium module

_INSTALLATION_

```pip install selenium```

**How to run**

After cloning the repo, open ```createRoute.py``` and edit your email, password, driver name, etc there. Then you can run the script by one of the following ways:

1, In command prompt, navigate to the script's directory and simply run ```py createRoute.py```

2, If you're fancy, modify the ```createRoute.bat``` file in the repo as follow:
            
            @py.exe C:\PATH-TO-THIS-DIRECTORY\create-test-route\createRoute.py %*
   
   Note: if you have white space in your path, put your path in quotation marks.
   
   - Put the path to myRoute directory (eg: C:\Users\Chi\create-test-route) in your PATH variable (assuming you're using Windows again). You might want to restart your laptop.
   
Once you've done that, to run the script, ```press Windows key + R, and type createRoute and press Enter```.
