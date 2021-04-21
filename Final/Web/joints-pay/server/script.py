from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

account = {
    "email": "bambangbajigur1@gmail.com",
    "password": "passwordsementara"
}

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(chrome_options=chrome_options)

def wait_until(ec, by, value):
    return WebDriverWait(driver, 10).until(ec((by, value)))

url = "http://jointspay-nginx/"
driver.get(url)

loginDiscordXPath = "/html[1]/body[1]/div[1]/div[1]/a[1]/p[1]"
loginDiscordButton = wait_until(
    EC.element_to_be_clickable,
    By.XPATH,
    loginDiscordXPath
)
loginDiscordButton.click()

discordEmailFormXPath = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/input[1]"
discordPasswordFormXPath = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/input[1]"
discordLoginButtonXPath = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[3]/button[2]/div[1]"

discordEmailForm = wait_until(
    EC.presence_of_element_located,
    By.XPATH,
    discordEmailFormXPath
)
discordPasswordForm = wait_until(
    EC.presence_of_element_located,
    By.XPATH,
    discordPasswordFormXPath
)
discordLoginButton = wait_until(
    EC.element_to_be_clickable,
    By.XPATH,
    discordLoginButtonXPath
)

discordEmailForm.send_keys(account['email'])
discordPasswordForm.send_keys(account['password'])
discordLoginButton.click()

discordAuthorizeButtonXPath = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/button[2]"
discordAuthorizeButton = wait_until(
    EC.element_to_be_clickable,
    By.XPATH,
    discordAuthorizeButtonXPath
)
discordAuthorizeButton.click()

while True:
    time.sleep(15)
    driver.get(url)