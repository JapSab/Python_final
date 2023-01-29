## This is an app which will help you find your favorite movie "სეანს" in Tbilisi

to use this app you have to have this libraries:
``` Python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import undetected_chromedriver as UC
from pprint import pprint as pp
import json
from unidecode import unidecode
```
---
## How to use this app:
1. run the program
2. enter your favorite theater name
3. follow instructions
4. enter the movie name
5. woalla!
---
## Functions
* Search by theater name on tkt.ge/movies
* Search movie details by movie name
* Get all schedule details in json file


