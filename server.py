from TrObject import *

devices = TrObject.loadFromServer()
for i in devices[1][0].offlineDevice():
    print(i._name)
