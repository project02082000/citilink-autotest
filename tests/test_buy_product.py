import time
import re
import os

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.service import Service
from allure import description, step, severity, severity_level
from assertpy import assert_that

from pages.main_page import MainPage
from pages.laptops_page import LaptopsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.shop_choice_page import ShopChoicePage


@description("Product purchase")
@severity(severity_level.CRITICAL)
def test_buy_product(set_up):
    url = "https://www.citilink.ru"
    dir_name = os.path.dirname(__file__)
    service = Service(os.path.join(dir_name, "chromedriver.exe"))
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(options=options, service=service)
    driver.get(url)
    driver.maximize_window()

    main_page = MainPage(driver)
    main_page.choose_laptops()

    laptops_page = LaptopsPage(driver)
    laptops_page.accept_cookies()
    laptops_page.add_laptop_filters()
    laptops_page.sort_by_reviews()
    time.sleep(0.5)
    laptops_page.choose_laptop()

    product_page = ProductPage(driver)
    product_page.save_laptop_name()
    product_page.save_laptop_price()
    print("laptop_name_product_page:", product_page.get_product_name_value())
    print("laptop_price_product_page:", product_page.get_product_price_value(), "\n")
    product_page.add_and_go_to_cart()

    cart_page = CartPage(driver)
    cart_page.save_laptop_name()
    cart_page.save_laptop_price()
    print("laptop_name_cart:", cart_page.get_product_name_value())
    print("laptop_price_cart:", cart_page.get_product_price_value(), "\n")

    with step("Check that info on Cart Page matches info on Product Page"):
        assert_that(cart_page.laptop_name_cart) \
            .described_as("Laptop's name on Cart Page doesn't match name on Product Page") \
            .is_equal_to(product_page.laptop_name_product_page)
        assert_that(cart_page.laptop_price_cart) \
            .described_as("Laptop's price on Cart Page doesn't match price on Product Page") \
            .is_equal_to(product_page.laptop_price_product_page)

    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(driver)
    try:
        checkout_page.save_laptop_name()
        checkout_page.save_laptop_price()
    except exceptions.TimeoutException:
        checkout_page.save_laptop_name_2()
        checkout_page.save_laptop_price_2()
    print("laptop_name_checkout:", checkout_page.get_product_name_value())
    print("laptop_price_checkout:", checkout_page.get_product_price_value(), "\n")

    laptop_name_product_page = re.sub(r" [\d]+\.[\d]+ГГц", "", product_page.laptop_name_product_page)
    laptop_name_product_page = re.sub(r" \[.*\]", "", laptop_name_product_page)
    laptop_name_product_page = laptop_name_product_page.split(",")
    laptop_name_checkout = checkout_page.laptop_name_checkout.split(",")

    with step("Check that info on Checkout Page matches info on Product Page"):
        assert_that(laptop_name_checkout) \
            .described_as("Laptop's name on Checkout Page doesn't match name on Product Page") \
            .is_subset_of(laptop_name_product_page)
        assert_that(checkout_page.laptop_price_checkout) \
            .described_as("Laptop's price on Checkout Page doesn't match price on Product Page") \
            .is_equal_to(product_page.laptop_price_product_page)

    checkout_page.input_personal_info()
    time.sleep(3)

    shop_choice_page = ShopChoicePage(driver)
    shop_choice_page.choose_shop()

    try:
        checkout_page.save_sum_price()
    except exceptions.TimeoutException:
        checkout_page.save_sum_price_2()
    print("sum_price", checkout_page.get_sum_price_value(), "\n")

    with step("Check that final price on Checkout Page matches price on Product Page"):
        assert_that(checkout_page.sum_price) \
            .described_as("Laptop's final price on Checkout Page doesn't match price on Product Page") \
            .is_equal_to(product_page.laptop_price_product_page)

    driver.close()
