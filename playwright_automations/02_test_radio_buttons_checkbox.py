from playwright.sync_api import Page, expect

def test_radiobuttons(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    radio_button = page.get_by_label("Standard")
    expect(radio_button).not_to_be_checked
    radio_button.check()
    expect(radio_button).to_be_checked()


def test_checkboxes(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    checkboxes = ["Sunday", "Monday", "Tuesday", "Wednesday"]
    checkboxes = [page.get_by_label(item) for item in checkboxes]
    for item in checkboxes:
        expect(item).not_to_be_checked()
        item.check()
        expect(item).to_be_checked()
    

    