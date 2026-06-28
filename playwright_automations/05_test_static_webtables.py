from playwright.sync_api import Page, expect

def test_static_webtables(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    
    # locating the tables  
    table = page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()
    header = table.locator("tr th").all_inner_texts()
    print(f"the header is {header}")

    # print specific 2nd row contents
    second_row = table.locator("tr").nth(1).locator("td")
    second_row_text = second_row.all_inner_texts()
    print(second_row_text)

    # assert second contents  
    expect(second_row).to_have_text(['Learn Selenium', 'Amit', 'Selenium', '300'])

    rows = table.locator("tr")
    all_row_data = rows.all()
    

    # for author Animesh, pick the bookname
    for data in all_row_data[1:]:
        author=data.locator("td").nth(1).inner_text()
        if author=="Animesh":
            print(data.locator("td").nth(0).inner_text())
            break

    # calculate the book price

    sum_ = 0
    for data in all_row_data[1:]:
        price=int(data.locator("td").nth(3).inner_text())
        sum_ += price
        print(price)


