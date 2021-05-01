# Import required modules
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyttsx3

# voice setup
speak = pyttsx3.init()
def Voice_message():
    voices = speak.getProperty("voices")
    speak.setProperty('voice',voices[1].id)
    
# driver setup
PATH = 'C:\Program Files (x86)\geckodriver.exe'
driver = webdriver.Firefox(executable_path=PATH)
driver.get("https://www.google.co.in/maps")
print(driver.title)
sleep(3)


if __name__ == "__main__":

    Voice_message()

    driver.quit()
    speak.runAndWait()
    print("Code Completed 🔥")
