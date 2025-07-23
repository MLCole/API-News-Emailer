import requests
from send_mail import send_mail

api_key = 'a708646291ad416a8b2f72a5bd03cc02'
url = "https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=a708646291ad416a8b2f72a5bd03cc02"

# Make Request
request = requests.get(url)
# Get data and turn it into a dictionary to allow for indexing
content = request.json()

# create message to send
message = ""

# Access the article data
for article in content["articles"]:
    message += str(article["title"]) + "\n"
    message += str(article["author"]) + "\n"
    message += str(article["description"]) + "\n\n"

send_mail(message)
