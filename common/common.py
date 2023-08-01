from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from typing import List
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


if __name__=='__main__':
    import Web_element
    import config
else:
    from common import Web_element
    from common import config    


def setup_commmon():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10) 
    driver.get("https://www.chatbot.com/chatbot-demo/")
    wait_a_little()
    return driver

def open_chatbubble(driver:webdriver):
    iframe = driver.find_element(By.CSS_SELECTOR, "iframe[src*='https://cdn.chatbot.com/widget/v2/chat.html?id=61f28451fdd7c5000728b4f9&v=32']")
    driver.switch_to.frame(iframe)

    chatbubble = driver.find_element(By.CSS_SELECTOR , Web_element.chatbubble_css)
    wait_a_while()
    chatbubble.click() 
    wait_a_little()


def wait_a_little():
    time.sleep(config.wait_a_little)

def wait_a_while():
    time.sleep(config.wait_a_while)

def wait_a_lot():
    time.sleep(config.wait_a_lot)

def wait_long():
    time.sleep(config.wait_long)