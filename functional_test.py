from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # instead of time 
from selenium.webdriver.support import expected_conditions as EC # 
import unittest
from time import sleep

class NewVisitorTest(unittest.TestCase):
    
    @classmethod
    def setUp(cls):
        options = Options()
        options.headless = False # use true if you want the browser not to be displayed.
        cls.browser = webdriver.Firefox(options=options)
    
    @classmethod    
    def tearDown(cls):
        cls.browser.quit()
        
    def test_can_start_a_list_and_retreive_later(self):
        # Samantha has heard about a cool new online to-do app. She goes to checkout the home page
        self.browser.get('http://localhost:8000')
        
        # she notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertTrue('Your to-do list', header_text)
        
        # she is invited to enter a to-do list item straight away
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        
        # she types "Buy Groceries" into a text box
        inputbox.send_keys('Buy Groceries')
        inputbox.send_keys(Keys.ENTER)
        sleep(1)
        
        # When she hits enter, the page updates, and now the page lists "1. Buy Groceries" as an item in a to-do list.
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, 'id_list_table')))
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn('1: Buy Groceries', [row.text for row in rows])
        
        # There is still a text box inviting her to add another item. She enters "Make a meal plan" (she is very methodical)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Make a meal plan')
        inputbox.send_keys(Keys.ENTER)
        
        # The page updates again, and now shows both items on her list
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn('1: Buy Groceries', [row.text for row in rows])
        self.assertIn('2: Make a meal plan', [row.text for row in rows])
        
        # She wonders whether the site will remember her list. The she sees that the site has generated an unique URL for her -- there is some explanatory text to that effect. 
        



        # She visits that URL - her to-do list is still there. 
        self.fail('Finish the test')
        # Satisfied, she goes back to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    
    