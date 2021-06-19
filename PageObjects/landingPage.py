from selenium.webdriver.common.by import By


class landing:
    def __init__(self,driver):
        self.driver=driver
        assert "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"==driver.title

    tooltip=(By.XPATH,"//div[@id='nav-signin-tooltip']/div")
    hello=(By.XPATH,"//*[@class='layoutToolbarPadding']//*[text()='Account & Lists']")
    sign=(By.XPATH,"//span[text()='Sign in']")
    dropdwn=(By.XPATH,"//select[@id='searchDropdownBox']")

    def tooltipv(self):
        return self.driver.find_element(*landing.tooltip)

    def Hellotab(self):
        return self.driver.find_element(*landing.hello)
    def signinbutton(self):
        return self.driver.find_element(*landing.sign)
    def dropdown(self):
        return self.driver.find_element(*landing.dropdwn)







