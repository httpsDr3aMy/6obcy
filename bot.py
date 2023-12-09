from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 


ACCEPT_RULES_BUTTON= '//*[@id="sd-current"]/div/div[2]/button[2]'
CONNECT_TO_USER = '//*[@id="intro-start"]'
CAPTCHA_POPUP = '//*[@id="sd-current"]/div'
WAITING_TIME_CAPTCHA = 1000
TEXTAREA_XPATH = '//*[@id="box-interface-input"]'
WAITING_TIME_INPUT = 10
FIRST_MESSAGE_STRANGER = '//*[@id="log-dynamic"]/p[2]'


#Driver settings
driver = webdriver.Chrome()
driver.get("https://6obcy.org/")


#Main page section
acceptButton = driver.find_element(By.XPATH, ACCEPT_RULES_BUTTON)
acceptButton.click()
connectUser = driver.find_element(By.XPATH, CONNECT_TO_USER)
connectUser.click()


#Captcha waiting
wait = WebDriverWait(driver, WAITING_TIME_CAPTCHA)
element = wait.until(EC.invisibility_of_element_located((By.XPATH, CAPTCHA_POPUP)))


#Texting with stranger "KM"
try:
    textarea = WebDriverWait(driver, WAITING_TIME_INPUT).until(
        EC.element_to_be_clickable((By.XPATH, TEXTAREA_XPATH))
    )
    textarea.send_keys("KM", Keys.ENTER)
finally:
    driver.quit()

#Checking messages from stranger
firstMessageStrangerParagraph = driver.find_element(By.XPATH, FIRST_MESSAGE_STRANGER)
firstMessageStranger = firstMessageStrangerParagraph.text
print(firstMessageStranger)
