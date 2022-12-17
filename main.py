import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

os.environ['path'] += r"C:/selenium drivers"
driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")
driver.implicitly_wait(5)

print("scan QR code and then enter")
input()

def logout():
    menu = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/header/div[2]/div/span/div[4]/div/span')
    menu.click()
    time.sleep(1)
    logout_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/header/div[2]/div/span/div[4]/span/div/ul/li[5]/div')
    logout_button.click()
    button = driver.find_element(By.XPATH, '/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div')
    button.click()
    print("Successfully logout Yay (◠‿◕)")
    time.sleep(2)

def type_message():
    messageBox = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    message1 = input("Enter the message: ")
    messageBox.send_keys(message1, Keys.ENTER)
    time.sleep(1)

def search_contact():
    searchBox = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]')
    if searchBox.text != '' :
        searchBox.clear()
    print("Enter the name of contact")
    name = input()
    searchBox.send_keys(name)
    time.sleep(1)
    try:
        no_contact = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/span')
        if no_contact :
            print(no_contact.text)
    except:
        searchBox.send_keys(Keys.ENTER)
        time.sleep(1)
        chat_name = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[1]/div/span')
        print("The chat which was opened was: ", end='')
        print(chat_name.text)
        proceed = input("Do you want to proceed enter yes otherwise no: ")
        if(proceed == "yes"):
            type_message()

run = "yes"

while run != "no":
    choice = input("Enter yes for searching a contact else enter no ")
    if choice == "yes" : search_contact()
    else :
        choice = input("Do you want to logout ? Enter yes otherwise no ")
        if choice == "yes" :
            logout()
            run = "no"

driver.quit()

