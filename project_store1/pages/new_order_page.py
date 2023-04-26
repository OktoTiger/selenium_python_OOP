from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import sys
sys.path.append("..\\project_store1\\")
from base.base_class import Base 

class New_order_page(Base):
    
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
    
    locator_comment = "//textarea[@id='order_comment']"
    locator_street = "//input[@id='shipping_address_street']"
    locator_house = "//input[@id='shipping_address_house']"
    locator_flat = "//input[@id='shipping_address_flat']"
    locator_housing = "//input[@id='shipping_address_field_10232924']"
    locator_floor = "//input[@id='order_field_13874844']"
    locator_for_stairs = "//*[@id='riseFloor']/div[3]/div[3]/label[1]"


    # Getters
    """Получение локаторов для заполнения финальной формы"""
    def get_comment(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_comment)))  

    def get_street(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_street)))  

    def get_house(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_house))) 
    
    def get_flat(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_flat)))  
    
    def get_housing(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_housing)))  
    
    def get_floor(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_floor)))      
    
    def get_for_stairs(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_for_stairs)))    
   
    # Actions
    
    def input_comment(self, text):
        self.get_comment().send_keys(text)
        print ("Input comment")    

    def input_street(self, street):
        self.get_street().send_keys(street)
        print ("Input street")  
        
    def input_house(self, street):
        self.get_house().send_keys(street)
        print ("Input house")  

    def input_flat(self, flat):
        self.get_flat().send_keys(flat)
        print ("Input flat")  

    def input_housing(self, housing):
        self.get_housing().send_keys(housing)
        print ("Input housing")
        
    def clear_floor(self):
        self.get_floor().send_keys(Keys.BACKSPACE)
        print ("Clear floor")   
        
    def input_floor(self,floor):
        self.get_floor().send_keys(floor)
        print ("Input floor")            

    def click_for_stairs(self):
        self.get_for_stairs().click()
        print ("Choose stairs")  
            
    # Methods
    
    def order_information(self):
        self.get_current_url()
        self.input_comment("Добрый день! Прошу доставить в период с 10 до 15 часов")
        self.input_street("Мориса-Тореза")
        self.input_house("17")
        self.input_flat("8")
        self.input_housing("1")
        self.clear_floor()
        self.input_floor("3")
        self.click_for_stairs()

        














