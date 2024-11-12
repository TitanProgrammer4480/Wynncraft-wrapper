import requests as r

class Guild:
    def __init__(self, name, u_name, uuid=""):
      self.name = name
      self.names = {}
      self.u_name = u_name
      self.uuid = uuid
      self.url = "https://api.wynncraft.com/v3/guild"
      self.list = {}
      self.terr = {}
      self.pref = {}

    def guild_list(self):
        self.list = r.get(self.url + "/guild/list/guild")
        return self.list

    def guild_territory(self):
        self.terr = r.get(self.url + "/guild/list/territory")
        return self.terr

    def guild_pref(self):
        self.pref = r.get(self.url + "/guild/prefix/" + self.name + "?identifier=" + self.u_name + "/" + self.uuid)
        return self.pref

    def guild_name(self):
        self.names = r.get(self.url + "/guild/" + self.name + "?identifier=" + self.u_name + "/" + self.uuid)
        return self.names