import selenium
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_visible_btn_add_to_basket(browser):
    browser.get(link)
    # Здесь раскоментировать для review time.sleep(30)
    # Данный метод с len использован, чтобы работал assert без exceptions.NoSuchElementException
    find_button = len(browser.find_elements_by_css_selector('.btn-add-to-basket'))
    assert find_button > 0, 'Button add to basket not found!'
