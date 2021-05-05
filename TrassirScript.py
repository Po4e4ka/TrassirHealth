# Скрипт отправляет на включенную серверную часть список всех устройств в виде
# {Server1:{
#	 IP_adr1:
#		{dev_info}
#	 IP_adr2:
#		{dev_info}
#	 }
#  Server2:{
#	 IP_adr1:
#		{dev_info}
#	 IP_adr2:
#		{dev_info}
#	 }
# }
'''
<parameters>
	<company>ICS</company>
	<title>TrassirHealth</title>
	<version>0.1</version>
	<parameter>
        <id>SERVER_IP</id>
        <name>IP адрес сервера</name>
        <type>string</type>
        <value></value>
    </parameter>
	<parameter>
        <id>SERVER_PORT</id>
        <name>PORT сервера</name>
        <type>integer</type>
        <value>7778</value>
		<min>1</min>
		<max>100000</max>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Delay the start of the script</name>
        <id>STARTUP_DELAY</id>
        <value>10</value>
        <min>0</min>
        <max>10000</max>
    </parameter>
</parameters>
'''

import socket
import json
import time

#
#
# def start_script:
# sock = socket.socket()
# sock.connect((SERVER_IP, SERVER_PORT))
# data = {}
#
# def getDeviceData(servName=None):
#     deviceInfo = {}
#     setts = host.settings("/{}/ip_cameras".format(servName)).ls() if servName is not None else host.settings(
#         "ip_cameras").ls()
#     for sett in setts:
#         if sett.type == "Grabber":
#             if sett["grabber_enabled"]:
#                 deviceInfo["status"] = sett.ls()[2]["state"]
#                 deviceInfo["name"] = sett["name"]
#                 deviceInfo["ip"] = sett["connection_ip"]
#                 deviceInfo["port"] = sett["connection_port"]
#                 deviceInfo["model"] = sett["model"]
#
#                 yield deviceInfo
#
# def getServerInfo(servName=None):
#     servInfo = {}
#     for device in getDeviceData(servName):
#         servInfo[device["ip"]] = device.copy()
#     return servInfo
#
# for server in objects_list("Server"):
#     if server[0] != '':
#         data[server[0]] = getServerInfo(server[0])
#
# # Отправка на приложение обработки
# sock.send(json.dumps(data, indent=4))
# sock.close()