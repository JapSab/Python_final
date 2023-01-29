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

class MovieApp:
    
    def __init__(self):
        self.PATH = '/home/jafara/Documents/chromedriver.exe'
        self.driver = UC.Chrome(use_subprocess=True)
        self.wait = WebDriverWait(self.driver, 10) 


    def search_theater(self):
        self.driver.get('https://tkt.ge/movies')
        self.wait = WebDriverWait(self.driver, 10)
        e = self.driver.find_element(By.XPATH, "//*[text()='ვეთანხმები']")
        e.click()
        while True:
            try:
                self.driver.get('https://tkt.ge/movies')
                
        
                self.theaterName = input('Enter the theater name: ')

                theaters = self.driver.find_element(By.XPATH, f"//*[text()='{self.theaterName}']")
                theaters.click()

                time.sleep(2)

                element_list = self.driver.find_elements(By.CSS_SELECTOR,'div[data-testid="event-item"]')
            
                pp([i.text for i in element_list ])
                print('press N to continue to next step...')
                a = input('Press any key to search again.')
                if a.lower() == 'n':
                    break
            except Exception as e:
                print(e)

        input('Searching finished! Press any key to continue...')

    def search_movie(self):
        self.search_theater()
        self.movieName = input('Enter the movie name: ')
        element_list = self.driver.find_elements(By.CSS_SELECTOR,'div[data-testid="event-item"]')
        
        for i in element_list:
            try:
                if i.text== self.movieName:
                    i.click()
            except:
                pass
        input('Searching finished! Press any key to continue...')

        
    def search_date(self):
        self.search_movie()
        days = ['ორშ', 'სამ', 'ოთხ', 'ხუთ', 'პარ', 'შაბ', 'კვი']
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//*[text()='აღწერა']")))
        info = {}

        for i in days:
            try:
                count = 1
                
                self.driver.find_element(By.XPATH, f"//*[text()='{i}']").click()
                time.sleep(2)
                rows = []
                while True:
                    try:
                        element = self.driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[7]/div/div[4]/div[{count}]')   
                        count +=1
                        spans = [unidecode(j.text) for j in element.find_elements(By.CSS_SELECTOR, 'span') ]
                        spans.append(unidecode(element.find_element(By.CSS_SELECTOR, 'div').text))
                        rows.append(spans)
                    except:
                        break
                info[unidecode(i)] = rows
                
                    
            except:
                pass
    

        with open(self.movieName + '.json', 'w') as f:
            f.write(json.dumps(info, indent=2))

        input('Finished!')    
            

    
app = MovieApp()
app.search_date()