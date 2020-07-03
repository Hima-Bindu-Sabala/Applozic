import unittest
import smtplib
from datetime import time
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def Send_mail(msg):
    sender_email = "prodclient11@gmail.com"
    password = "Pa$$word123"
    revc_email = "prodclient11@gmail.com"
    message = "Hi automated email"+str(msg)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, revc_email, message)
    print(msg)

class Applozic_FAQ(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='.\chromedriver')
        self.driver.implicitly_wait(30)
        self.base_url = "https://test.kommunicate.io/"
        self.driver.get("https://test.kommunicate.io/")
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_Count_FAQ(self):
        try:
            driver = self.driver
            driver.implicitly_wait(5)
            driver.switch_to.frame(0)
            ele = driver.find_element_by_xpath("/html/body/div[5]/a/div[2]")
            actions = ActionChains(driver)
            actions.move_to_element(ele).perform()
            ele.click()
            driver.implicitly_wait(5)
            driver.find_element_by_xpath("//button[@id='km-faq']").click()
            co = driver.find_elements_by_xpath("//a[@class='km-faqdisplay']")
            count=len(co)
            if (count < 20):
                Send_mail(count)
            else:
                print(count)
        except Exception as err:
            Send_mail(err)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
