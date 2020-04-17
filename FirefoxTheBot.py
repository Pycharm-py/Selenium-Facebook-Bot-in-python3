from selenium import webdriver
import time
class FbBot():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\Path\to\your\geckodriver.exe')
        self.driver.get('https://facebook.com')
        time.sleep(2)
    def login(self):
        self.driver.find_element_by_css_selector("#email").send_keys("YOUR LOGIN")
        self.driver.find_element_by_css_selector("#pass").send_keys("YOUR PASSWORD")
        self.driver.find_element_by_css_selector("#u_0_b").click()
        time.sleep(15)
        # find on a list of friends
        try:
            self.driver.find_element_by_css_selector("li._42fz:nth-child(2) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
        except Exception:
            time.sleep(2)
            self.driver.find_element_by_css_selector("li._42fz:nth-child(2) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
        try:
            # finding chat and sending a message to second person from your friends list
            message = self.driver.find_element_by_xpath("//div[contains(@class,'_5rpu') and @role='combobox']")
            message.send_keys("hi" + u'\ue007')
        except Exception:
            time.sleep(2)
            message = self.driver.find_element_by_xpath("//div[contains(@class,'_5rpu') and @role='combobox']")
            message.send_keys("hi" + u'\ue007')
            time.sleep(5)

        self.driver.close()

bot = FbBot()
bot.login()
