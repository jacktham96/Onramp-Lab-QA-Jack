if __name__ == "__main__" :
    from sys import path
    from os.path import dirname as dir
    path.append(dir(path[0]))

from common import common
from common import Web_element
from common import file_utility

import os
import logging
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC





class Test_Chatbot(unittest.TestCase):
   
    def setUp(self):
        print('Setup Class Init...')
        self.driver = common.setup_commmon()
        common.open_chatbubble(self.driver)
        common.wait_a_little()
        
 
    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()
        
        
    def test_go_pricing_page_through_chatbot_keyboard(self):
        input_text = self.driver.find_element(By.CSS_SELECTOR, Web_element.chatbot_input_text)
        input_text.send_keys("I have questions")
        common.wait_a_lot()
        input_text.send_keys(Keys.RETURN)
        wait = WebDriverWait(self.driver, 20) 
        response_text = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, Web_element.chatbot_last_response_text)))

        chatbot_response = response_text.text
        print("Chatbot response:", chatbot_response)

        input_text = self.driver.find_element(By.CSS_SELECTOR, Web_element.chatbot_input_text)
        input_text.send_keys("pricing")
        input_text.send_keys(Keys.RETURN)
        common.wait_a_lot()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".message:last-child .button")))


        compare_plan = self.driver.find_element(By.CSS_SELECTOR, Web_element.chatbot_compare_plan_btn)


        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).click(compare_plan).key_up(Keys.CONTROL).perform()
        self.driver.switch_to.window(self.driver.window_handles[-1])

        common.wait_a_lot()
        print('done')

        current_url = self.driver.current_url
        expected_url = "https://www.chatbot.com/pricing/"
        if current_url == expected_url:
            logging.info("Assertion passed: Current URL is %s", expected_url)
        else:
            logging.error("Assertion failed: Current URL is %s, expected %s", current_url, expected_url)
            raise AssertionError("Current URL does not match expected URL.")
        

    def test_go_pricing_page_by_click_pricing_btn(self) :
        input_text = self.driver.find_element(By.CSS_SELECTOR, Web_element.chatbot_input_text)
        input_text.send_keys("I have questions")
        common.wait_a_lot()
        input_text.send_keys(Keys.RETURN)
        wait = WebDriverWait(self.driver, 20) 
        response_text = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, Web_element.chatbot_last_response_text)))
        
        chatbot_response = response_text.text
        print("Chatbot response:", chatbot_response)
        common.wait_a_lot()

        pricing_btn = self.driver.find_element(By.CSS_SELECTOR, ".quick-replies-buttons .single-button:nth-child(2)")
        pricing_btn.click()
        common.wait_a_lot()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".message:last-child .button")))

        compare_plan = self.driver.find_element(By.CSS_SELECTOR, Web_element.chatbot_compare_plan_btn)


        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).click(compare_plan).key_up(Keys.CONTROL).perform()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        common.wait_a_lot()

        current_url = self.driver.current_url
        expected_url = "https://www.chatbot.com/pricing/"
        if current_url == expected_url:
            logging.info("Assertion passed: Current URL is %s", expected_url)
        else:
            logging.error("Assertion failed: Current URL is %s, expected %s", current_url, expected_url)
            raise AssertionError("Current URL does not match expected URL.")



    def test_invalid_input(self) :
        input_text = self.driver.find_element(By.CSS_SELECTOR, Web_element.chatbot_input_text)
        input_text.send_keys("@#$%^&*")
        common.wait_a_lot()
        input_text.send_keys(Keys.RETURN)

        wait = WebDriverWait(self.driver, 20) 
        response_text = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, Web_element.chatbot_last_response_text)))
        chatbot_response = response_text.text
        print("Chatbot response:", chatbot_response)

        self.assertEqual(chatbot_response, "😵‍💫 Oops! Sorry, I didn't understand your question. Please rephrase it or click the button below to go back to the menu.")

    
    def test_multi_language(self):

        try :
            input_text = self.driver.find_element(By.CSS_SELECTOR, Web_element.chatbot_input_text)
            input_text.send_keys("價錢")
            common.wait_a_lot()
            input_text.send_keys(Keys.RETURN)

            pricing_btn = self.driver.find_element(By.CSS_SELECTOR, ".quick-replies-buttons .single-button:nth-child(2)")
            pricing_btn.click()
            common.wait_a_lot()

            wait = WebDriverWait(self.driver, 20) 
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".message:last-child .button")))

            compare_plan = self.driver.find_element(By.CSS_SELECTOR, Web_element.chatbot_compare_plan_btn)


            actions = ActionChains(self.driver)
            actions.key_down(Keys.CONTROL).click(compare_plan).key_up(Keys.CONTROL).perform()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            common.wait_a_lot()

            current_url = self.driver.current_url
            expected_url = "https://www.chatbot.com/pricing/"
            
            self.assertEqual(current_url, expected_url)
        
        
        except Exception as e:            
            raise AssertionError("An error occurred during the test: %s" % str(e))


    def test_similar_word(self):
        words_to_test = ["Costing", "Rate", "Charge", "Fee"]

        for word in words_to_test :

            try :
                input_text = self.driver.find_element(By.CSS_SELECTOR, Web_element.chatbot_input_text)
                input_text.send_keys(word)
                common.wait_a_lot()
                input_text.send_keys(Keys.RETURN)

                wait = WebDriverWait(self.driver, 20) 
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".message:last-child .button")))

                compare_plan = self.driver.find_element(By.CSS_SELECTOR, Web_element.chatbot_compare_plan_btn)
                self.assertTrue(compare_plan.is_enabled(), f"Button not clickable for word '{word}'")


            except Exception as e:
                print(f"Error for '{word}': {str(e)}")
                self.all_words_passed = False  

        # Fail the test if any word resulted in a failure
        self.assertTrue(self.all_words_passed, "One of the word failed")




if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestCheckOut)
    # unittest.TextTestRunner(verbosity=2).run(suite)
        #定義 輸出log檔 名稱
    file_dir=os.path.dirname(__file__)
    test_base_name=os.path.basename(__file__)
    
    # 開檔 跑測試
    with open(file_utility.generate_log_name_debug(file_dir,test_base_name), 'w', encoding='utf-8') as log_file:
        suite = unittest.TestLoader().loadTestsFromTestCase(Test_Chatbot)
        runner=unittest.TextTestRunner(stream=log_file,verbosity=3)
        testResult=runner.run(suite)
