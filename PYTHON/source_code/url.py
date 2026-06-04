import random
import string
url_database = {}
def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for i in range(6))
    return short_code

def shorten_url(long_url):
    short_code = generate_short_url()
    url_database[short_code] = long_url
    return f"http://short.ly/{short_code}"

def retrieve_url(short_url):
    short_code = short_url.split("/")[-1]
    return url_database.get(short_code, "URL not found")

original_url = "https://www.google.com"
short_url = shorten_url(original_url)
print("Short URL:", short_url)

print("Original URL:", retrieve_url(short_url))