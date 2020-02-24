from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_book_into_box(self):
        self.should_be_adding_to_basket_button()
        self.add_book_to_basket()
        self.solve_quiz_and_get_code() #for stepic task check
        self.should_be_confirm_messages()
        self.should_be_book_name_in_confirm_message()
        self.should_be_confirmation_message_for_book()
        self.should_be_benefit_offer()
        self.should_be_product_amount_message()
        self.should_be_product_amount_mini_basket()
        self.should_be_confirmation_message_with_amount()

    def should_be_adding_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "\"Add to basket\" button is Not exist"

    def add_book_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def should_be_confirm_messages(self, timeout=10):
        self.browser.implicitly_wait(timeout)
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_PRODUCT), "One of confirm messages are Not displayed"
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_BENEFIT), "One of confirm messages are Not displayed"
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_PAYMENT), "Payment confirm messages is Not displayed"

    def should_be_book_name_in_confirm_message(self, timeout=10):
        self.browser.implicitly_wait(timeout)
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        book_name = book_name.text
        book_name_confirm = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_CONFIRM)
        book_name_confirm = book_name_confirm.text
        assert book_name == book_name_confirm, \
            f"Wrong product name, got '{book_name_confirm}' instead of '{book_name}'"

    def should_be_confirmation_message_for_book(self):
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        book_name = book_name.text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT)
        message = message.text
        assert message == f"{book_name} has been added to your basket.", \
            f"Wrong confirm book payment message, got {message}"

    def should_be_benefit_offer(self):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_BENEFIT)
        message = message.text
        assert message == "Your basket now qualifies for the Deferred benefit offer offer.", \
            f"Wrong benefit message, got {message} instead of " \
            f"\"Your basket now qualifies for the Deferred benefit offer offer.\""

    def should_be_product_amount_message(self):
        amount = self.browser.find_element(*ProductPageLocators.PRODUCT_PAYMENT)
        amount = amount.text
        amount_confirm = self.browser.find_element(*ProductPageLocators.PRODUCT_PAYMENT_CONFIRM)
        amount_confirm = amount_confirm.text
        assert amount_confirm == amount, \
            f"Wrong product amount in message, got '{amount_confirm}' instead of '{amount}'"

    def should_be_product_amount_mini_basket(self):
        amount_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PAYMENT_BASKET_MINI)
        amount_basket = amount_basket.text
        amount = self.browser.find_element(*ProductPageLocators.PRODUCT_PAYMENT)
        amount = amount.text
        assert amount in amount_basket, \
            f"Wrong product amount in basket, expected {amount} instead of {amount_basket}"

    def should_be_confirmation_message_with_amount(self):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_PAYMENT)
        message = message.text
        amount = self.browser.find_element(*ProductPageLocators.PRODUCT_PAYMENT)
        amount = amount.text
        assert f"Your basket total is now {amount}" in message, \
            f"Wrong confirm amount message, got '{message}'"

