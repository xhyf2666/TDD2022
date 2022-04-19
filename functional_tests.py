from selenium import webdriver      #  (1)
import unittest

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
        self.fail('Finish the test!')


if __name__=='__main__':
    unittest.main(warnings='ignore')
