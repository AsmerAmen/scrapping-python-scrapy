# Objective
- Scraping Amazon.com for non-commercial purposes. I found it challenging so I did it.

# Used Tech:
1. Python3.6.
    * Working on Both Ubuntu18.4 and Windows 10.
2. Scrapy.
    * Tried using  ["scrapy.Spider"](https://docs.scrapy.org/en/latest/topics/spiders.html) and ["scrapy.spiders.CrawlSpider"](https://docs.scrapy.org/en/latest/topics/spiders.html#crawlspider). I found the later better when I was scraping all the subcategories of smart home, instead of doing it one by one.
    * More detailed to found in the next section.
3. SQLite3 'the current used database'. 
    * MySQL and MongoDB can work as well.

# Work Flow
## Done
1. Scraping product pages one by one.
    * Check the 'AmazonSpiderProduct' class in Amazon script.
2. Scraping 'Lighting' subcategory products, page by page.
    * Check the 'AmazonSpiderSubcategory' and 'AmazonSpiderProduct' classes in Amazon script.
    * Running the 2 crawler sequentially in the same order. Making sure that the first one created the database and the second update it, not delete it.
3. Scraping the whole department/category of smart home saving the products values into SQLite database. 
4. The values are:
    1. URL.
    2. Name.
    3. Provider/selling company.
    4. Price.
    5. Image link.
    6. If it supported by Amazon Alexa or not.
    7. It's category, which is the subcategory of smart home, like 'lighting', 'door lock', etc.
## Doing
1. Fixing the price scraping selector. As almost have of the product price are missed.
## To-Do
1. Scrap the image link and amazon certified. as after the last update to scrap the whole category of smart home I had to leave them.