import os
import time
from selenium import webdriver
from datetime import date


psiphonpath = r'C:\Users\user\Downloads\psiphon3.exe'           # path to psiphon3.exe
Webdriverpath = r'C:\Users\user\Downloads\chromedriver.exe'     # path to selenium webdriver (i am using chrome webdriver)

emailID = r""   # enter emailID or username
password = r""  # enter password

while 1:
    print("opening Psiphon3")
    os.startfile(psiphonpath)
    time.sleep(20)              # giving time for psiphon to initialize
    print("Psiphon3 must be open and ready")

    driver = webdriver.Chrome(Webdriverpath)
    driver.get("https://open.spotify.com/")
    time.sleep(3)
    LoginButt = driver.find_element_by_class_name("PzcmS_Z8j0D6n3ZEmv20.Hy_P64B8lNKgp3N7Qz4Z")  # if an error occurs ,update this as the class name may have changed
    LoginButt.click()

    time.sleep(5)
    emailbox = driver.find_element_by_id("login-username")
    emailbox.send_keys(emailID)
    print("email filled")

    passbox = driver.find_element_by_id("login-password")
    passbox.send_keys(password)
    print("password filled")

    LoginButt = driver.find_element_by_id("login-button")
    time.sleep(4)
    LoginButt.click()

    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    print(f"login done {d2}")

    time.sleep(20)      # this allows login to not be interrupted due to sudden closing of psiphon
    print("closing psiphon ")
    os.system("TASKKILL /IM psiphon3.exe")
    # os.system("TASKKILL /IM Google Chrome.exe") not closing chrome as i might be doing other stuff on it
    time.sleep(604800)  # you can change re-logging time to a time that suits you, i have set it to 7 days

