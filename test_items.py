import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_client_should_see_add_to_basket_button(browser):
    browser.get(link)	
    time.sleep(30)
    button = browser.find_element_by_class_name("btn-add-to-basket")
    assert button!=None, "No such element"
