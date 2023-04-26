from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append("C..\\project_store1\\")
from base.base_class import Base 

class Personal_page (Base):
    
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Locarors
    locator_to_products = "//ul[@class='links fl']/li[1]"
    
    # Getters
    """Метод получения локатора для перехода на главную страницу"""
    def get_to_products(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_to_products)))  
    
    # Actions
    
    def click_to_products_button(self):
        self.get_to_products().click()
        print ("Click button to products")
        
    def to_products(self):
        self.get_current_url()
        self.get_screenshot()
        self.click_to_products_button()









