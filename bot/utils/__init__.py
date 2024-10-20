from .environment import Config

Config.loadConfig()

configBOT: Config.Bot = Config.Bot()
configDB: Config.Database = Config.Database()
