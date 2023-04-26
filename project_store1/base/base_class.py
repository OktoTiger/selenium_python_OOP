import datetime

class Base():
    def __init__(self,browser):
        self.browser = browser
        
    """Method asset word""" 
    
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Проверка названия телевизора успешна")
        
        """Method get current url"""
    
    def get_current_url(self):
        get_url = self.browser.current_url
        print("Correct url: " + get_url)
        
    """Method screenshot"""
    
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.browser.save_screenshot("C:\\Users\\User\\Desktop\\Study_Lessons\\project_store\\screen\\" + name_screenshot)
        

    