import asyncio
from pyppeteer import launch

async def scrape_news_titles(url):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(url)

    titles = await page.evaluate('''() => {
        return Array.from(document.querySelectorAll('h1.article-title')).map(title => title.innerText);
    }''')

    await browser.close()
    return titles

async def main():
    url = 'https://example-news-website.com'
    titles = await scrape_news_titles(url)
    for i, title in enumerate(titles, 1):
        print(f'{i}. {title}')

asyncio.get_event_loop().run_until_complete(main())
