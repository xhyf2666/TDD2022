from selenium import webdriver      #  (1)
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()       #  (2)
        
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        
        #Edith has heard about a cool new online to-do app.She goes
        #to check out its homepage
        self.browser.get('http://localhost:8000')#  (3)


        #sheh notices the page title and header menthion to-do lists
        self.assertIn('To-Do',self.browser.title),"Browser title was :"+self.browser.title
        header_text=self.browser.find_element(By.TAG_NAME,'h1').text
        self.assertIn('To-Do',header_text)

        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers',[row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly',[row.text for row in rows])

        self.fail('Finish the test!')

if __name__=='__main__':
    unittest.main(warnings='ignore')
