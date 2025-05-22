from celery import shared_task

@shared_task
def fetch_gold_price():
    # Your scraping or API fetching logic here
    print("Gold price fetched and saved!")