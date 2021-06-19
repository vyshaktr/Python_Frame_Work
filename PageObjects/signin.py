from selenium.webdriver.common.by import By


class signin:
    def __init__(self,driver):
        self.driver=driver
        assert "Amazon Sign In" == driver.title

    user=(By.XPATH,"//input[@id='ap_email']")
    cont=(By.XPATH,"//span[@id='continue']")
    error=(By.XPATH,"//div[@id='auth-error-message-box']")
    passwrd=(By.XPATH,"//input[@id='ap_password']")
    signinsub=(By.ID,"signInSubmit")
    messagebox=(By.ID,"auth-warning-message-box")
    forgotpwd=(By.LINK_TEXT,"Forgot Password")

    def username(self):
        return self.driver.find_element(*signin.user)

    def contbutton(self):
        return self.driver.find_element(*signin.cont)

    def errorbox(self):
        return self.driver.find_element(*signin.error)

    def password(self):
        return self.driver.find_element(*signin.passwrd)

    def signinbtn(self):
        return self.driver.find_element(*signin.signinsub)

    def msgbox(self):
        return self.driver.find_element(*signin.messagebox)

    def forgotpwdlink(self):
        return self.driver.find_element(*signin.forgotpwd)

