# # Скрипт выводит все IP устройства, подключенные к серверу, на котором запущен скрипт.
# # Сохраняется все в файл DevicesInfo в директорию H:\\ в виде json файла в текстовом варианте
# '''
# <parameters>
# 	<company>ICS</company>
# 	<title>Device_model</title>
# 	<version>0.1</version>
# </parameters>
# '''
#
# import json
# import os
#
# PATH = "H:\\"
#
# #if not PATH:
# #    raise ParameterError("Путь к файлу не выбран")
#
# serversList = []
# for i in objects_list("Server"):
# 	if i[0] != '':
# 		serversList.append(i[0])
#
# def getDeviceData(servName=None):
#     deviceInfo = {}
#     setts = host.settings("/{}/ip_cameras".format(servName)).ls() if servName is not None else host.settings("ip_cameras").ls()
#     for sett in setts:
#         if sett.type == "Grabber":
#             if sett["grabber_enabled"]:
#                 deviceInfo["name"] = sett["name"]
#                 deviceInfo["connection_ip"] = sett["connection_ip"]
#                 deviceInfo["connection_port"] = sett["connection_port"]
#                 deviceInfo["model"] = sett["model"]
#
#                 yield deviceInfo
#
# def getDeviceInfoOnServer(servName=None):
# 	devDict = {}
# 	for i in getDeviceData(servName):
# 		if i["model"] in devDict:
# 			devDict[i["model"]] += 1
# 		else:
# 			devDict[i["model"]] = 1
# 	return devDict
#
# (host.settings("").name)
#
# os.chdir(PATH)
#
# with open("DevicesInfo.txt", "w") as f:
# 	result = {}
# 	for serv in serversList:
# 		result[serv] = getDeviceInfoOnServer(serv)
# 	f.writelines(json.dumps(result, indent=4))
# 	with open("DevicesInfo.json", "w") as l:
# 		json.dump(result, l)