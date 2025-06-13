from selenium.webdriver.common.by import By

class Registration_page():
    txtbox_password_id="password"
    txtbox_firstname_id="first_name"
    txtbox_lastname_id="last_name"
    txtbox_address_id="address1"
    txtbox_state_id="state"
    txtbox_city_id="city"
    txtbox_zipcode_id="zipcode"
    txtbox_mobile_id="mobile_number"
    createact_xpath="//button[contains(text(),'Create Account')]"
    txtmsg_confirmation_xpath="/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/p[1]"
    continue_xpath="//a[normalize-space()='Continue']"

    def __init__(self,driver):
        self.driver=driver

    def set_password(self,password):
        self.driver.find_element(By.ID,self.txtbox_password_id).send_keys(password)

    def set_firstname(self,firstname):
        self.driver.find_element(By.ID,self.txtbox_firstname_id).send_keys(firstname)

    def set_lastname(self,lastname):
        self.driver.find_element(By.ID,self.txtbox_lastname_id).send_keys(lastname)

    def set_address(self,address):
        self.driver.find_element(By.ID,self.txtbox_address_id).send_keys(address)

    def set_state(self,state):
        self.driver.find_element(By.ID,self.txtbox_state_id).send_keys(state)

    def set_city(self,city):
        self.driver.find_element(By.ID,self.txtbox_city_id).send_keys(city)

    def set_zipcode(self,zipcode):
        self.driver.find_element(By.ID,self.txtbox_zipcode_id).send_keys(zipcode)

    def set_mobile(self,mobile):
        self.driver.find_element(By.ID,self.txtbox_mobile_id).send_keys(mobile)

    def set_createaccount(self):
        self.driver.find_element(By.XPATH,self.createact_xpath).click()

    def get_confirm_msg(self):
        try:
            return self.driver.find_element(By.XPATH,self.txtmsg_confirmation_xpath).text
        except:
            print("no conf msg")

    def cont(self):
        self.driver.find_element(By.XPATH,self.continue_xpath).click()
