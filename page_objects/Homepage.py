from selenium.webdriver.common.by import By

class Home_page:
    click_signup_xpath="//a[normalize-space()='Signup / Login']"
    txtbox_name_name="name"
    txtbox_email_xpath="//input[@data-qa='signup-email']"
    press_signup_xpath="//button[normalize-space()='Signup']"

    def __init__(self,driver):
        self.driver=driver

    def click_sign_up(self):
        self.driver.find_element(By.XPATH,self.click_signup_xpath).click()

    def signup_name(self,signname):
        self.driver.find_element(By.NAME,self.txtbox_name_name).send_keys(signname)

    def signup_email(self,signemail):
        self.driver.find_element(By.XPATH,self.txtbox_email_xpath).send_keys(signemail)

    def press_signup(self):
        self.driver.find_element(By.XPATH,self.press_signup_xpath).click()


