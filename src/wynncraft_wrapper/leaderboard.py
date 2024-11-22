import requests as r

class Leaderboard:
  def _init__(self):
    self.url = "https://api.wynncraft.com/v3/leaderboard"

  def types(self):
    types = r.get(self.url + "/types")
    return types

  def leaderboard(self, type, numres = 100):
    lb = r.get(self.url + type + "?resultLimit=" + numres)
    return lb