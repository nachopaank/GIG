from time import sleep

from behave import *
from selenium import webdriver


driver = webdriver.Chrome()
@when("I navigate to site {url}")
def step_impl(context,url):
    driver.get(url)
    driver.maximize_window()


@step("I log in as {user} with password {password}")
def step_impl(context,user,password):
    driver.find_element("id","user-name").send_keys(user)
    driver.find_element("id","password").send_keys(password)
    driver.find_element("id","login-button").click()
    assert (driver.find_element("id","shopping_cart_container").is_displayed())


@step('I click on "Add to cart" button in the backpack item and see the item added')
def step_impl(context):
    driver.find_element("id","add-to-cart-sauce-labs-backpack").click()
    assert (driver.find_element("xpath","//span[@class='shopping_cart_badge']").text == str(1))


@step('I click on the shopping cart icon and click on the "Checkout" button')
def step_impl(context):
    driver.find_element("id","shopping_cart_container").click()
    driver.find_element("id", "checkout").click()
    assert(driver.find_element("id", "first-name").is_displayed())


@step("I set {name}, {lastname}, {zip} for First Name, Last Name and Zip and click on Continue and then Finish")
def step_impl(context,name,lastname,zip):
    driver.find_element("id","first-name").send_keys(name)
    driver.find_element("id","last-name").send_keys(lastname)
    driver.find_element("id","postal-code").send_keys(zip)
    driver.find_element("id","continue").click()
    driver.find_element("id", "finish").click()


@then("I see my order dispached")
def step_impl(context):
    text = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
    assert (driver.find_element("xpath","//div[@class='complete-text']").text == text)
    driver.close()