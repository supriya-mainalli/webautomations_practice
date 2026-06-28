from playwright.sync_api import Page, expect

def test_static_dropdowns(page:Page):
    page.goto("https://www.bstackdemo.com/")
    page.locator("select").select_option("lowestprice")

    page.wait_for_timeout(5000)
    mobile_names = page.locator("div[class='shelf-item'] p").all_text_contents()
    prices = page.locator("div [class='shelf-item__price'] div[class='val'] b").all_text_contents()
    my_dict = dict(zip(mobile_names, prices))
    print(my_dict)
    prices = [price for price in prices]
    print(prices)

def test_single_select_Dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # select by label
    page.locator("#country").select_option("Canada")
    #select by value
    page.locator("#country").select_option(value="canada")
    #select by index
    page.locator("#country").select_option(index=5)

    # print all the texts from the dropdwons
    country = page.locator("#country>option")
    
    country_text = [x for x in country.all_text_contents()]
    print(country_text)

    #to check count
    expect(country).to_have_count(10)

def test_multi_dropdowns(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # select by label
    page.locator("#colors").select_option(label=["Red","Blue"])
    # select by value
    page.locator('#colors').select_option(value=["green","yellow"])
    # select by index
    page.locator('#colors').select_option(index=[5,1])

    #print all the text
    colors = page.locator('#colors>option')
    colors_text = [x for x in colors.all_text_contents()]
    print(colors_text)