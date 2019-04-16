import locators


class LoginPage(locators.LoginPage):
    def login(self, username, password):
        self.element(self.EMAIL_FIELD).send_keys(username)
        self.element(self.PASSWORD_FIELD).send_keys(password)
        self.element(self.LOGIN_BUTTON).click()