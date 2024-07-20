import asyncio
from pyppeteer import launch

async def submit_form(url, form_data):
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto(url)

    for field, value in form_data.items():
        await page.type(field, value)

    await page.click('button[type=submit]')
    await page.waitForNavigation()

    await browser.close()

async def main():
    url = 'https://www.saucedemo.com/'
    form_data = {
        '#name': 'Automated User',
        '#email': 'test@test.com',
        '#message': 'Hello, this is an automated submission!'
    }
    await submit_form(url, form_data)

asyncio.get_event_loop().run_until_complete(main())
