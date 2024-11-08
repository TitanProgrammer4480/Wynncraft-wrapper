import requests as r

class Player:
    def __init__(self, name, uuid=""):
      self.name = name
      self.uuid = uuid
      self.url = "https://api.wynncraft.com/v3/player"
      self.data = {}
      self.characters = {}

    def main_stats(self):
        self.data = r.get(self.url + "/" + self.name + "/" + self.uuid)
        return self.data

    def full_stats(self):
        self.data = r.get(self.url + "/" + self.name + "/" + self.uuid + "?fullResult")
        return self.data

    def characters(self):
        self.characters = r.get(self.url + "/" + self.name + "/" + self.uuid + "/characters")
        return self.characters

    def character(self, char_uuid):
        return r.get(self.url + "/" + self.name + "/" + self.uuid + "/characters/" + char_uuid)

    def character_abilities(self, char_uuid):
        return r.get(self.url + "/" + self.name + "/" + self.uuid + "/characters/" + char_uuid + "/abilities")