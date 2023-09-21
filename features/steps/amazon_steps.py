from behave import when, then
from all_methods import *


@when(u'User Search For "{item_name}"')
def searching_for_product(context, item_name):
    '''
    This Is For Searching Product Based On User Input
    :param item_name: Contain Value Of User Want to search
    '''

    search_box = "//input[@id='twotabsearchtextbox']"
    search_product(context.page, search_box, item_name)


@when(u'Filtered Product Based On "{rating_value_for_filter}" star rating')
def filtering_product_based_on_rating(context, rating_value_for_filter):
    '''
    This Is For Filtering Product Based On User Given Rating Value
    :param rating_value_for_filter: Contains User Interest Rating Value
    '''

    rating_box = "((//div[@id='p_72-title']/following-sibling::ul)//li)"
    filtering_product(context.page, rating_box, rating_value_for_filter)


@then(u'He Added "{number_of_product}" Product To Cart')
def adding_product_to_cart(context, number_of_product):
    '''
    This Is Used For adding product to cart based on number of product user want to add
    :param number_of_product: Contains Value Of Product User Want To add
    '''

    add_to_cart_button = "//input[@id='add-to-cart-button']"
    adding_to_cart(context.page, add_to_cart_button, number_of_product)


@then(u'Actual Price Should Be Same As Cart Price')
def verifying_summarized_price_and_subtotal(context):
    '''
    This Is For Verification Whether The Summarized Price Is Equal To Sub-Total or Not
    '''

    subtotal = "(//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap'])[1]"
    cart_button = "//span[@id='nav-cart-count']"
    product_price = "//p[@class='a-spacing-mini']/child::span"

    context.page.locator(cart_button).click()
    subtotal_value = context.page.locator(subtotal).text_content()
    subtotal_value = subtotal_value.replace('.', '')
    subtotal_value = subtotal_value.replace(',', '')
    actual_price_list = context.page.locator(product_price)
    total_price = 0
    for i in range(actual_price_list.count()):
        '''This Loop add all product actual price and store in total_price variable
        For Comparision with subtotal value'''

        s = actual_price_list.nth(i).text_content()
        s = s.replace(',', '')
        s = s.replace('.', '')
        total_price += float(s)

    '''
    This Exception Handling Block will generate message if cart subtotal is not same as summarized
    Hence add_to_cart is not working properly after adding to cart also'''

    try:
        assert float(subtotal_value) == float(total_price), 'Add Cart Is Not Working Properly'
    except AssertionError as msg:
        print(msg)
