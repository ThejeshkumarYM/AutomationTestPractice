import pytest
from page_objects.Homepage import Home_page
from page_objects.AccountRegistrationPage import Registration_page
from utilities import randomstring
import os
from utilities.readproperties import read_config_ini
from utilities.customlogger import logcol


class Test_001_AccountRegistrarion:
    baseurl=read_config_ini.get_application_url()
    logger=logcol.loggen()
    logger.info("log initialised")

    def test_actreg(self,setup):
        self.logger.info("*** test_001_AccountRegistration started ***")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.hp=Home_page(self.driver)
        self.hp.click_sign_up()
        self.hp.signup_name("thejesh")
        self.email=randomstring.generate_random_string()+'@gmail.com'
        self.hp.signup_email(self.email)
        self.hp.press_signup()
        self.driver.implicitly_wait(10)

        self.actreg=Registration_page(self.driver)
        self.driver.implicitly_wait(10)
        self.password=randomstring.generate_random_string()
        self.actreg.set_password(self.password)
        self.driver.implicitly_wait(10)
        self.firstname=randomstring.generate_random_string()
        self.actreg.set_firstname(self.firstname)
        self.lastname=randomstring.generate_random_string()
        self.actreg.set_lastname(self.lastname)
        self.actreg.set_address("bangalore")
        self.actreg.set_state("karnataka")
        self.actreg.set_city("bangalore")
        self.actreg.set_zipcode("777777")
        self.mobile=randomstring.generate_random_string()
        self.actreg.set_mobile(self.mobile)
        self.actreg.set_createaccount()
        self.conf_msg=self.actreg.get_confirm_msg()
        if self.conf_msg=='Congratulations! Your new account has been successfully created!':
            self.actreg.cont()
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_act_registratin.png")
            self.driver.close()
            assert False

        self.logger.info("*** test_001_AccountRegistration completed ***")





