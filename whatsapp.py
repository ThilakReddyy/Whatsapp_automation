from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import json
f = open('csvjson.json')
data = json.load(f)

import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:/Users/tilak/OneDrive/Desktop/temp/COLLEGE/chromedriver.exe')
url="https://web.whatsapp.com/"
driver.get(url)
time.sleep(20)
for i in data:
    try:
        url=""
        msg="Hello, "+i["Name"]+"%0A"+"Based on your preference in registration that we sent earlier regarding the coding club we are sharing the whatsapp group link, Join the whatsapp group :"
        msg2="%0A"+"It is advised not to share the link."
        # print(i["Name"],i["Whatsapp Number"],i["Rate yourself as a coder"])
        if(i["Rate yourself as a coder"]=="NOOB ( no knowledge in programming)"):
            link="https://chat.whatsapp.com/LvjZaPenFyIFo607ePjlqd"
            send=msg+link+msg2
            url="https://web.whatsapp.com/send?phone=+91"+"8341008861"+"&text="+send
        if(i["Rate yourself as a coder"]=="Beginner (know  basics of  atleast one programming language and able to  code  if/else statements, loops, functions , recursion)"):
            link="https://chat.whatsapp.com/IqOkoSsVzDyFPCdAceY51R"
            send=msg+link+msg2
            url="https://web.whatsapp.com/send?phone=+91"+"8341008861"+"&text="+send
        if(i["Rate yourself as a coder"]=="Intermediate ( able to implement data structures(arrays, stacks,queues,hashing,binary trees, graphs),sorting and searching algorithms, divide and conquer,greedy )"):
            link="https://chat.whatsapp.com/LR5dSxnIOfLFZfNj94aFlm"
            send=msg+link+msg2
            url="https://web.whatsapp.com/send?phone=+91"+"8341008861"+"&text="+send
        if(i["Rate yourself as a coder"]=="Expert ( Hold very good rating on competitive programming platforms like codechef, codeforces, topcoder etc"):
            url="https://web.whatsapp.com/send?phone=+91"+"8341008861"+"&text="+msg+msg2
        
        driver.get(url)
        elem = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_4sWnG")) #This is a dummy element
            )
        time.sleep(2)
        driver.find_element_by_class_name("_4sWnG").send_keys(Keys.ENTER)
        time.sleep(2)
    except:
        print(i)
        time.sleep(2)
        
