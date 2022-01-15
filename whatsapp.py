from selenium.webdriver.common.by import By
import time
import json


f = open('phonenumbers.json') #the json file which contains the phone numbers
data = json.load(f)

driver=webdriver.Chrome("chromedriver.exe") #loading the chrome driver
url="https://web.whatsapp.com/"
driver.get(url) #loading the url
wait = WebDriverWait(driver, 30)# waiting for the user to scan the code under 30 seconds
url="https://web.whatsapp.com/send?phone=+91" #basic url to send whatsapp message
for i in data:
    try:
        msg="Hello Diwali ra"+i["Name"]
        toload=url+i["Phone"]+"&text="+msg
        driver.get(toload)
        elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "_4sWnG")) )
        time.sleep(2)
        driver.find_element_by_class_name("_4sWnG").send_keys(Keys.ENTER)
    except:
        print(i)
    time.sleep(1)
