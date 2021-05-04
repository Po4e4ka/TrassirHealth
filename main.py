# Скрипт будет передавать информацию о состаянии серверов
'''
<parameters>
	<company>ICS</company>
	<title>TrassirHealth</title>
	<version>0.1</version>
</parameters>
'''

import socket
import json

# Коннект с приложением обработки
sock = socket.socket()
sock.connect(('188.243.150.127', 7778))

# Переменная с переданной информацией
data = {}


def getDeviceData(servName=None):
    deviceInfo = {}
    setts = host.settings("/{}/ip_cameras".format(servName)).ls() if servName is not None else host.settings(
        "ip_cameras").ls()
    for sett in setts:
        if sett.type == "Grabber":
            if sett["grabber_enabled"]:
                deviceInfo["status"] = sett["channels_enabled"]
                deviceInfo["name"] = sett["name"]
                deviceInfo["ip"] = sett["connection_ip"]
                deviceInfo["port"] = sett["connection_port"]
                deviceInfo["model"] = sett["model"]

                yield deviceInfo


def getServerInfo(servName=None):
    servInfo = {}
    for device in getDeviceData(servName):
        servInfo[device["ip"]] = device["status"]
    return servInfo


data = {}

for server in objects_list("Server"):
    if server[0] != '':
        data[server[0]] = getServerInfo(server[0])

# Отправка на приложение обработки
sock.send(json.dumps(data, indent=4))
sock.close()