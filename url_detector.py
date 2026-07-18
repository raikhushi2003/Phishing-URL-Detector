import re

url = input("Enter URL: ")

if len(url) > 75:
    print("Long URL Detected")

if "@" in url:
    print("@ Symbol Found")

if re.search(r"\d+\.\d+\.\d+\.\d+", url):
    print("IP Address Detected")

keywords = ["login", "verify", "update", "secure", "bank"]

for word in keywords:
    if word in url.lower():
        print("Suspicious Keyword:", word)

print("Scan Completed")
