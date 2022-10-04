from cgitb import text
from bs4 import BeautifulSoup
import requests

baseUrl = "https://www.google.com/search?q=site%3Aedu"
# baseUrl = "https://duckduckgo.com/?q=site%3Aedu"
inputUrl = str(input("Please enter what you want to search: ")).lower()
input_with_plus = "%s%s" % ("+", inputUrl.replace(" ","+"))
url_plus_input = "%s%s" % (baseUrl, input_with_plus)
print(inputUrl)
print(input_with_plus)
print(url_plus_input)

url = url_plus_input
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())

eduLinks = doc.find_all(text=inputUrl)
print(eduLinks)
