from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append("..\\project_store1\\")
from base.base_class import Base 

class Description_tv_page (Base):
    
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
    
    locator_name_tv = "//h1[@class='collection-top-banner-caption-text']"
    locator_cart = "//button[@id='button-to-card']"
    locator_button_go_to_cart = "//a[@class='button go_to_cart']"

    # Getters

    def get_name_tv(self):
        return WebDriverWait(self.browser,30).until(EC.presence_of_element_located((By.XPATH, self.locator_name_tv)))  

    def get_cart(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_cart)))  

    def get_go_to_cart(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_button_go_to_cart)))  

    # Actions
    """Нажатие на кнопку в корзину"""    
    def click_cart(self):
        self.get_cart().click()
        print ("Click cart") 
        
    """Переход в корзину"""     
    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print ("Click go to cart")     
    
    # Methods
    
    def description_tv(self):
        self.get_current_url()
        self.assert_word(self.get_name_tv(),'Телевизор Candy Uno 55')
        self.click_cart()
        self.click_go_to_cart()












# 