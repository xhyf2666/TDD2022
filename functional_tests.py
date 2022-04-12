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
        self.assertIn('To-do',self.browser.title),"Browser title was :"+self.browser.title
        sele.fail('Finish the test!')

        #she is invited to enter a tp-do item straight away
        #is tying fly-fishing lures)

        #when she hits enter,the page updates,and now the page lists
        # '1':Buy peacock feathers' as an item in a to-do list

        #There is still a text box inviting her to add another item.
        #She enter "Use peacock feathers to make a fly" (Edith is very methodical)

        #The page updates again,and now shows both items on her list

        #Edith wonders whether the site will remember her list.Then shee sees
        #that the site has generated a unique URL for her -- there is some
        #explanatory text to that effect.

        #She visits that URL - her to-do is still there.

        #Satisfied,she goes back to sleep.

if __name__=='__main__':
    unittest.main(warnings='ignore')
