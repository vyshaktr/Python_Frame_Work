import time
from Testdata.Datafile import Testdata

import pytest

# @pytest.mark.usefixtures("setup")
from PageObjects.landingPage import landing
from PageObjects.signin import signin
from utilities.Actionclass import Actions
from utilities.BaseClass import Baseclass


class TestCases(Baseclass):
    @pytest.mark.smoke
    # Test case to validate Landing page (Test case ID : 1 )
    # Authored by vyshak on 19/06/2021
    def test_signin_launch(self):
        log=self.getLogger()
        log.info("Step 1 :Launching amazon website")
        log.info("Step 1.a :Test code")
        land=landing(self.driver)
        log.info("Step 2 :Verification of  tooltip")
        if(land.tooltipv().is_displayed()):
            assert "New customer? Start here." == land.tooltipv().text
            log.info("Step 3 :Tool tip Present")
        else:
            log.info("Tooltip not present")
        #locator=land.Hellotab()
        act = Actions(self.driver)
        act.mouseover(land.Hellotab())
        land.signinbutton().click()
        time.sleep(2)
        log.info("step 4 :Verifying  amazon title")
        assert "Amazon Sign In" == self.driver.title
        log.info("Step 5 :Expected titile is found")

    @pytest.mark.smoke
    # Test case to validate Invalid sign in  (Test case ID : 2 )
    # Authored by vyshak on 19/06/2021
    def test_invalidsignin(self):
        log = self.getLogger()
        log.info("Testing invalid username entered for sign in")
        land=landing(self.driver)
        act = Actions(self.driver)
        act.mouseover(land.Hellotab())
        log.info("Step 1 : Launching the website and Clicking on sign in button")
        land.signinbutton().click()
        time.sleep(2)
        userdetails = signin(self.driver)
        log.info("Step 2 :Entering invalid username")
        userdetails.username().send_keys(Testdata.Username1)
        userdetails.contbutton().click()
        assert True == userdetails.errorbox().is_displayed()
        log.info("Step 3 : Verifying the error message")

    @pytest.mark.smoke
    # Test case to validate wrong password (Test case ID : 3 )
    # Authored by vyshak on 19/06/2021
    def test_wrongpassword(self):
        land=landing(self.driver)
        act = Actions(self.driver)
        act.mouseover(land.Hellotab())
        land.signinbutton().click()
        time.sleep(2)
        userdetails = signin(self.driver)
        userdetails.username().send_keys(Testdata.Username2)
        userdetails.contbutton().click()
        userdetails.password().send_keys(Testdata.Username2_password)
        userdetails.signinbtn().click()
        assert  True == userdetails.msgbox().is_displayed()
        assert True == userdetails.forgotpwdlink().is_displayed()
        userdetails.forgotpwdlink().click()
        assert "Amazon Password Assistance" == self.driver.title

    @pytest.mark.regression
    # Test case to validate Login (Test case ID : 4 )
    # Authored by vyshak on 19/06/2021
    def test_validlogin(self):
        land = landing(self.driver)
        act = Actions(self.driver)
        act.mouseover(land.Hellotab())
        land.signinbutton().click()
        time.sleep(2)
        userdetails = signin(self.driver)
        userdetails.username().send_keys(Testdata.Username3)
        userdetails.contbutton().click()
        userdetails.password().send_keys(Testdata.Username3_password)
        userdetails.signinbtn().click()
        act.moveandclick(land.Hellotab())
        assert "Your Account"==self.driver.title

    @pytest.mark.smoke
    #Test case to validate Dropdwons present(test case ID : 5)
    #Authored by vyshak on 19/06/2021
    def test_dropdowns(self):
        land = landing(self.driver)
        self.dropdownselct(land.dropdown(),"Deals")










