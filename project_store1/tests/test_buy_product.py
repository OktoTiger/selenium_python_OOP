from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pytest
import sys
sys.path.append("..\\project_store1")
from pages.new_order_page import New_order_page
from pages.description_tv_page import Description_tv_page
from pages.catalog_page import Catalog_page
from pages.category_tv import Category_tv
from pages.personal_page import Personal_page
from pages.login_page import Login_page 


def test_buy_product():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(chrome_options=options)
    
    login = Login_page(browser)
    login.authorization()
    
    go_to_products = Personal_page(browser)
    go_to_products.to_products()
    
    choose_category_tv = Catalog_page(browser)
    choose_category_tv.category_tv()
    
    choose_tv = Category_tv(browser)
    choose_tv.choose_price()
    
    go_to_cart = Description_tv_page(browser)
    go_to_cart.description_tv()
    
    new_order = New_order_page(browser)
    new_order.order_information()

