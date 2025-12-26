# from django.test import LiveServerTestCase # biblioteca para teste do selenium
from utils.browser import make_chrome_browser
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
from selenium.webdriver.common.by import By

class RecipeBaseFunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = make_chrome_browser()
        return super().setUp()
    
    def tearDown(self):
        self.browser.quit()
        return super().tearDown()    

    def sleep(self, seconds=5):
        time.sleep(seconds)

class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):
    def sleep(self, seconds=5):
        time.sleep(seconds)

    def test_the_test(self):
        self.browser.get(self.live_server_url)
        self.sleep()
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('No recipes found here 🥲', body.text)
        