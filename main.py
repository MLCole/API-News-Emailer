import requests

api_key = 'a708646291ad416a8b2f72a5bd03cc02'
url = "https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=a708646291ad416a8b2f72a5bd03cc02"

# Make Request
request = requests.get(url)
# Get data and turn it into a dictionary to allow for indexing
content = request.json()

# Access the article data
for article in content["articles"]:
    print(article["title"])
    print(article["author"])
    print(article["description"])
    print(" ")