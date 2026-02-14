import time
from playwright.sync_api import Page, BrowserContext, Browser
class TestGoogle:
    def test_google(self, browser: Browser):
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        page.set_default_timeout(5000)
        page.goto("https://www.google.com/")
        page.locator("[name=q]").fill("Cat")
        time.sleep(2)
        # page.pause()
        # page.get_by_role("button", name='Google Search').nth(0).click()
        page.get_by_role("button", name='Google Search').first.click()
        time.sleep(5)
        context.close()

    def test_google1(self, session_page):
        session_page.goto("https://www.google.com/")
        session_page.locator("[name=q]").fill("Cat")
        time.sleep(2)
        # page.pause()
        # page.get_by_role("button", name='Google Search').nth(0).click()
        session_page.get_by_role("button", name='Google Search').first.click()
        time.sleep(5)

    def test_google2(self, session_page: Page):
        session_page.go_back()
        time.sleep(5)

    def test_guru99_submit(self, session_page):
        """Navigate to demo.guru99.com, enter an email, submit and extract credentials."""
        session_page.goto("https://demo.guru99.com/")
        session_page.locator("input[name='emailid']").fill("test@example.com")
        session_page.locator("input[type='submit']").click()

        # wait for the result table row that contains the generated credentials
        session_page.locator("td:has-text('User ID') + td").wait_for(timeout=5000)

        user = session_page.locator("td:has-text('User ID') + td").text_content().strip()
        password = session_page.locator("td:has-text('Password') + td").text_content().strip()

        print(f"Extracted user: {user}")
        print(f"Extracted password: {password}")

        assert user, "User ID not extracted"
        assert password, "Password not extracted"

    def test_table_extraction(self, session_page : Page):
        """Navigate to a page with a table and extract data."""
        session_page.goto("https://www.w3schools.com/html/html_tables.asp")
        # Wait for the table to be visible
        session_page.locator("#customers").wait_for(timeout=5000)

        # Extract all rows of the table
        rows = session_page.locator("#customers tr").all()
        data = []
        for row in rows:
            cells = row.locator("th, td").all_text_contents()
            data.append(cells)

        print("Extracted table data:")
        for row in data:
            print(row)

        assert len(data) > 1, "No table data extracted"

        print("P: " + session_page.get_by_role("table").locator("tr").nth(1).locator("td").nth(1).inner_text())