import webbrowser
from googlesearch import search

# Setting Chrome as Browser
chrome_path = r"C:\\Program Files\\Google\\Chrome\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

webbrowser.open_new("https://www.youtube.com")

search("Google")