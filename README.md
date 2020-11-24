# create-test-route
Automatically creates a route for driver on the Sharing Excess Food Rescue app

**Dependancies**

1, Chromedriver

_INSTALLATION_
- Download Chromedriver at: https://chromedriver.storage.googleapis.com/index.html?path=87.0.4280.20/
- Extract the ```chromedriver.exe``` 
- Put the path for ```chromedriver.exe``` in your PATH variable (assusming you're using Windows)
- If you've done that, and the script doesn't work, put ```chromedriver``` in your Python\Python38-32\Scripts (or in the Scripts folder of whatever Python version you're using)

2, Selenium module

_INSTALLATION_

```pip install selenium```

**How to run**

1, In command prompt, navigate to the script's directory and simply run ```py createRoute.py```

2, (Optional) If you're fancy, modify the ```createRoute.bat``` file in the repo as follow:
            
            @py.exe C:\PATH-TO-THIS-DIRECTORY\myRoute\createRoute.py %*
   
   Note: if you have white space in your path, put your path in quotation marks.
   
   - Put the path to myRoute directory (eg: C:\Users\Chi\myRoute) in your PATH variable (assuming you're using Windows again)
   
Once you've done that, to run the script, ```press Windows key + R, and type createRoute and press Enter```.