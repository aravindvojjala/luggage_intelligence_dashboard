from playwright.sync_api import sync_playwright
import pandas as pd
import time

def scrape():
    data = []
    brands = ["Safari luggage", "Skybags luggage", "VIP luggage", "American Tourister luggage"]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # page = browser.new_page()
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
        )

        for brand in brands:
            page.goto(f"https://www.amazon.in/s?k={brand.replace(' ', '+')}")
            time.sleep(3)

            products = page.query_selector_all(".s-result-item")

            for product in products[:5]:
                try:
                    title = product.query_selector("h2 span").inner_text()
                    price = product.query_selector(".a-price-whole").inner_text()

                    link = product.query_selector("a").get_attribute("href")
                    page.goto("https://www.amazon.in" + link)
                    time.sleep(3)

                    reviews = page.query_selector_all(".review-text-content span")

                    for r in reviews[:10]:
                        data.append({
                            "brand": brand,
                            "product": title,
                            "price": price,
                            "review": r.inner_text()
                        })

                    page.go_back()
                    time.sleep(2)

                except:
                    continue

        browser.close()

    df = pd.DataFrame(data)
    df.to_csv("data/raw_data.csv", index=False)

if __name__ == "__main__":
    scrape()