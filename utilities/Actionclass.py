from selenium.webdriver import ActionChains


class Actions:

    def __init__(self,driver):
        self.driver=driver



    def mouseover(self,locator):
        self.locator = locator
        self.action = ActionChains(self.driver)
        return self.action.move_to_element((self.locator)).perform()

    def moveandclick(self,locator):
        self.locator = locator
        self.action = ActionChains(self.driver)
        return self.action.move_to_element((self.locator)).click().perform()

