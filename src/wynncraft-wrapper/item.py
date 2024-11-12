import requests as r

class Item:
  def __init__(self):
    self.url = "https://api.wynncraft.com/v3/item/"
    self.item = ""
    self.infos = {}
    self.metadata = {}

  def search(self, item):
    self.infos = r.get(self.url + "search/" + self.item)
    return self.infos

  def metadata(self):
    self.metadata = r.get(self.url + "metadata")
    return self.metadata