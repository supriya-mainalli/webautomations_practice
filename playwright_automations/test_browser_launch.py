from playwright.sync_api import Page, expect
import time

def test_pages(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    title = page.title()
    url = page.url
    expect(page).to_have_title(title)
    expect(page).to_have_url(url)
    page.close()


# by img alt
def test_img_alt(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_timeout(5000)
    logo = page.get_by_alt_text("company-branding")
    expect(logo).to_be_visible()
    page.close()


# by role and labels
def test_by_label_role(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    expect(page.get_by_text("Forgot your")).to_have_text("Forgot your password? ")
    page.get_by_role("button", name="Login").click()