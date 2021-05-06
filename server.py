from TrObject import *

devices = TrObject.loadFromTrassir()
TrObject.saveToFile(devices[0])
