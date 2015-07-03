from configparser import ConfigParser

config = ConfigParser()
config.read("config.cfg")
recordar = config.getboolean("Recordatorios", "Recordar")
actualizar_cada = config.getint("Recordatorios", "Actualizar cada")
