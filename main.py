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

# search places
def search():
    searhc_box_text = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div/div[3]/div/input[1]")
    searhc_box_text.send_keys("mumbai")


def search_click():
    sleep(3)
    search_click = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    search_click.click()


def direction():
    sleep(10)
    direction = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/button")
    direction.click()


def starting_point():
    sleep(5)
    start = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
    start.clear()
    start.send_keys("Mumbai")
    
  

def end_point():
    sleep(5)
    end = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/input")
    end.clear()
    end.send_keys("New delhi")


def search_again():
    sleep(4)
    search = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/button[1]")
    search.click()
    sleep(10)


# total dist and time

def dist_time():
    sleep(5)
    total_kilometers = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[2]/div/div[1]/div[1]/div[2]/div")
    print(f"Total Distance ==> {total_kilometers.text}🔥")

    reaching_time = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[1]/div/div[2]/div[1]/div")
    print(f"Reaching Time ==> {reaching_time.text}🔥")

    speak.say(f"Total Distance is {total_kilometers.text} \n and reaching time will be {reaching_time.text}")
    

if __name__ == "__main__":

    Voice_message()
    search()
    search_click()
    direction()
    starting_point()
    end_point()
    search_again()
    dist_time()


    driver.quit()
    speak.runAndWait()
    print("Code Completed 🔥")
