import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import geckodriver_autoinstaller
from selenium import webdriver
youtbeLinks = [
    'https://www.youtube.com/@Mrwhosetheboss',
    'https://www.youtube.com/@A2DChannel',
    'https://www.youtube.com/@mkbhd'
]  # urls of the youtube channels, replace with your preffered Youtube channels

geckodriver_autoinstaller.install()

# path to firefox profile..replace with your profile path
firefoxProfileFolder = '/home/userName/.mozilla/firefox/ba2uc9zw.default-release' #This is an example

profile = webdriver.FirefoxProfile(firefoxProfileFolder)

profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()
desired = DesiredCapabilities.FIREFOX

driver = webdriver.Firefox(firefox_profile=profile,
                           desired_capabilities=desired)


driver.get("http://youtube.com")
time.sleep(5)
for link in youtbeLinks:
    driver.get(link)
    try:
        time.sleep(2)
        ele = driver.find_element(
            By.CSS_SELECTOR, '#subscribe-button-shape button')
        ele.click()
    except:
        print("Channel already subscribed or Google account is not signed in")
    time.sleep(7)
driver.quit()
