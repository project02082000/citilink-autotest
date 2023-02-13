import time
import re
import allure

from pages.main_page import MainPage
from pages.laptops_page import LaptopsPage
from pages.chosen_laptop_page import ChosenLaptopPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.shop_choice_page import ShopChoicePage

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import assertpy


@allure.description("Test buy product")
def test_buy_product(set_up):
    url = "https://www.citilink.ru"

    service = Service("C:\\Users\\MSI GF75\\PycharmProjects\\resource\\chromedriver.exe")
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

    chosen_laptop_page = ChosenLaptopPage(driver)
    chosen_laptop_page.add_and_go_to_cart()

    cart_page = CartPage(driver)
    cart_page.go_to_checkout()

    assertpy.assert_that(cart_page.laptop_name_2).described_as("Assertion of laptop's name in CartPage and "
                                                               "ChosenLaptopPage is incorrect").is_equal_to(
        chosen_laptop_page.laptop_name_1)

    assertpy.assert_that(cart_page.laptop_price_2).described_as("Assertion of laptop's price in CartPage and "
                                                                "ChosenLaptopPage is incorrect").is_equal_to(
        chosen_laptop_page.laptop_price_1)

    checkout_page = CheckoutPage(driver)
    checkout_page.input_personal_info()

    laptop_name_1 = re.sub(r" [\d]+\.[\d]+ГГц", "", chosen_laptop_page.laptop_name_1)
    laptop_name_1 = re.sub(r" \[.*\]", "", laptop_name_1)
    laptop_name_1 = laptop_name_1.split(",")
    laptop_name_3 = checkout_page.laptop_name_3.split(",")

    assertpy.assert_that(laptop_name_3).described_as("Assertion of laptop's name in CheckoutPage and ChosenLaptopPage "
                                                     "is incorrect").is_subset_of(laptop_name_1)

    assertpy.assert_that(checkout_page.laptop_price_3).described_as("Assertion of laptop's price in CheckoutPage and "
                                                                    "ChosenLaptopPage is incorrect").is_equal_to(
        chosen_laptop_page.laptop_price_1)

    assertpy.assert_that(checkout_page.sum_price).described_as("Assertion of laptop's final price in CheckoutPage and "
                                                               "ChosenLaptopPage is incorrect").is_equal_to(
        chosen_laptop_page.laptop_price_1)

    shop_choice_page = ShopChoicePage(driver)
    shop_choice_page.choose_shop()
