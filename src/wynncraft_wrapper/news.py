import requests as r

class News:
  def __init__(self):
    self.url = "https://api.wynncraft.com/v3/latest-news"
    self.news = {}

  def get_news(self):
    self.news = r.get(self.url)
    return self.news