from .environment import Config

Config.loadConfig()

configBOT = Config.Bot()
configDB = Config.Database()
