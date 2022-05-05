from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

#open linkedin.com
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://linkedin.com/")

time.sleep(1)

#find UN/PW fields on the page
username = driver.find_element(By.XPATH, "//input[@name='session_key']")
password = driver.find_element(By.XPATH, "//input[@name='session_password']")

#********************LOGIN INFORMATION****************
#Input login credentials
username.send_keys('')
password.send_keys('')

#time.sleep(1)
#click the submit button to login
submit = driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(4)

#for random greeting generator
import random

#the number of pages to cycle through
n_pages = 3

#looping through page numbers, by adding the the range as a str at the end of the URL for page=n 
for n in range(1,n_pages):
    
    #Input URL for: ["people, connection_type(1)"]
    driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&page=" + str(n))

    #COMMENT ME OUT, this is the test
    #driver.get("https://www.linkedin.com/search/results/people/?keywords=d%C3%A9ric%20durocher&network=%5B%22F%22%5D&origin=FACETED_SEARCH&position=0&searchId=0e7beca5-1f2e-407e-ab39-1b8b66c5a933&sid=64n")

    #extra wait time if needed
    time.sleep(2)

    #run through the page finding buttons named message
    all_buttons = driver.find_elements(By.TAG_NAME, "button")
    message_buttons = [btn for btn in all_buttons if btn.text == "Message"]

    #looping through the list
    for i in range(0, len(message_buttons)):

        #click on message button
        driver.execute_script("arguments[0].click()", message_buttons[i])
        
        time.sleep(2)

        #click on the "enter message field"
        main_div = driver.find_element(By.XPATH, "//div[starts-with(@class, 'msg-form__msg-content-container')]")
        driver.execute_script("arguments[0].click()", main_div)

        time.sleep(2)

        #type message in message field with value of ""
        paragraphs = driver.find_elements(By.TAG_NAME, "p")

        time.sleep(2)
        
        #find names of people in the list
        names = driver.find_elements(By.XPATH, "//*[@id='main']/div/div/div[1]/ul/li/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]")
           
        #greetings array
        greetings = ["Hello", "Hey", "Hi"]    

        time.sleep(2)
            
        #generate greeting phrase
        greetings_idx = random.randint(0, len(greetings)-1)
        message = greetings[greetings_idx] + " " + names[i].text.split(" ")[0] + ", nice to meet you"
        
        #type message
        paragraphs[-5].send_keys(message)
        time.sleep(4)

        #send message
        submit = driver.find_element(By.XPATH, "//button[@type='submit']")
        driver.execute_script("arguments[0].click()", submit)

        time.sleep(2)

        #close message box
        close_button = driver.find_element(By.XPATH, "//button[starts-with(@data-control-name, 'overlay.close_conversation_window')]")
        driver.execute_script("arguments[0].click()", close_button)
