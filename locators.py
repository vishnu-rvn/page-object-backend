# from src.base import BasePageLocator
# from selenium.webdriver.common.by import By
#
#
# class HomePage(BasePageLocator):
#     MY_ACCOUNT_LINK = By. XPATH, "//a[contains(text(), 'My Account')]"
#     LOGIN_LINK = By. XPATH, "//a[contains(text(), 'Login']"
#     SIGN_UP_LINK = By. XPATH, "//a[contains(text(), 'Sign Up')]"
#     HOTELS_LINK = By. XPATH, ".a[title='Hotels']"
#
#
# class LoginPage(BasePageLocator):
#     EMAIL_FIELD = By.NAME, "username"
#     PASSWORD_FIELD = By.NAME, "password"
#     LOGIN_BUTTON = By.XPATH, "//button[text()='Login']"
#     SIGN_UP_LINK = By.XPATH, "//a[contains(text(), 'Sign Up')]"
#     FORGET_PASSWORD_LINK = By.XPATH, "//a[text()='Forget Password']"
import json

with open('t.txt', 'r') as file:
    contents = file.read()

h = []
for each_line in contents.split('\n'):
    name, type_selector = each_line.split(' = ')
    type_, selector = type_selector.split(', "')
    h.append({
        'name': name,
        'selector': selector.strip('"'),
        'selector_type': type_.strip('By.').lower()
    })

with open('data.json', 'w') as file:
    json.dump(h, file, indent=4)