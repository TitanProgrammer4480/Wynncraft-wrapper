import requests as r

class Player:
    def __init__(self, name, uuid=""):
      self.name = name
      self.uuid = uuid
      self.url = "https://api.wynncraft.com/v3/player"
      self.data = {}

    def main_stats(self):
        self.data = r.get(self.url + "/" + self.name + "/" + self.uuid)
        return self.data

    def full_stats(self):
        self.data = r.get(self.url + "/" + self.name + "/" + self.uuid + "?fullResult")
        return self.data