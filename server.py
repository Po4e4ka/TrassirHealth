from TrObject import *

devices = TrObject.loadFromServer()
TrObject.saveToFile(devices[0])
