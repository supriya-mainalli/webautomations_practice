from playwright.sync_api import Page,expect

def test_hidden_dropdowns(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_timeout(5000)
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(3000)

    #navigate to PIM
    page.get_by_text("PIM").click()

    page.locator("form i").nth(2).click()

    #capture all elements from the dropdowns
    dropdwon_list = page.locator(".oxd-select-option span")
    page.wait_for_timeout(3000)
    print(dropdwon_list.all_inner_texts())
    # print(dropdwon_list)
    # count_ = len(dropdwon_list)

    # print(f'the count is {count_} and the data type is {type(count_)}')

    webs_ele = page.locator(".oxd-select-option span").all()

    
    expect(dropdwon_list).to_have_count(29)

    for item in webs_ele:
        if item.inner_text() == "Software Architect":
            item.click()
            break

    page.wait_for_timeout(3000)
    
