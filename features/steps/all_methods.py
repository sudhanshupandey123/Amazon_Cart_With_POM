def search_product(page, locator, product_name):
    page.locator(locator).fill(product_name)
    page.keyboard.press('Enter')


def filtering_product(page, locator, rating_value):
    rating_dict = {4: 1, 3: 2, 2: 3, 1: 4}
    for rating in rating_dict:
        if rating == int(rating_value):
            page.locator(locator + f'{[rating_dict[rating]]}').click()


def adding_to_cart(page, locator, number_of_product):
    filtered_product_list = "//span[@class='a-size-medium a-color-base a-text-normal']"
    searched_value = "(//div[@class='sg-col-inner']//div//span)[3]"
    all_product_box = page.locator(filtered_product_list)
    searched_product = page.locator(searched_value).text_content()
    added_to_cart = 1

    for index in range(0, all_product_box.count()):
        page.wait_for_load_state()
        if added_to_cart > int(number_of_product):
            break

        product_name = all_product_box.nth(index).text_content()
        '''verifying if searched product name is present in product name then only add to cart'''

        user_search = searched_product.split()[0].replace('"', '')
        if user_search in product_name:
            with page.expect_popup() as popup_info:
                all_product_box.nth(index).click()
            page1 = popup_info.value
            page1.locator(locator).click()
            page1.close()
            page.bring_to_front()
            added_to_cart += 1
