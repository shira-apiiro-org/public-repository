import requests

pwd = "AIzaSyDzmABOfcTbibcP_VnZPhFn0q3Ro3sXlSQ"

res = requests.get('http://google.com', {'password': pwd})
