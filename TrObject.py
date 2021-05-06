import datetime
import socket
import json


class TrObject():
    """
    Класс объекта трассир
    """

    def __init__(self, name: str, info: dict or None):
        self._name = name
        self._info = info

    @staticmethod
    def loadFromServer():
        """
        Функция ожидает получения информации с сервера трассир, лочится на sock.listen
        После запуска скрипта на сервере, функция составляет список серверов
        :return: Возвращает словарь со всеми серверами и устройствами
        """
        print("Старт ожидания информации с сервера")
        sock = socket.socket()
        sock.connect(("office.icstech.ru",6969))
        print('Соеднинение с сервером:', "office.icstech.ru")
        result = b''
        while True:
            data = sock.recv(4096)
            if not data:
                break
            result += data
        sock.close()
        result = json.loads(result)
        servList = TrObject.dictToClasses(result)
        result["scanDateTime"] = str(datetime.datetime.now())
        return result, servList

    @staticmethod
    def dictToClasses(result):
        serverList = []
        for servName, devices in list(result.items()):
            tempS = TrServer(servName, devices)
            for device, devInfo in devices.items():
                tempD = TrDevice(device, devInfo)
                tempS.addDevice(tempD)
            serverList.append(tempS)
        return serverList

    @staticmethod
    def saveToFile(devices):
        """
        Сохраняет текущее значение в json файл
        """
        with open ("deviceStatus.json", "w") as f:
            json.dump(devices, f, indent=4)

    @staticmethod
    def loadFromFile(devices, path="deviceStatus.json"):
        """
        Заргужает информацию из файла
        """
        with open(path, "r") as f:
            devices = json.load(f)


class TrServer(TrObject):
    __devices = []

    def __init__(self, name: str, info: dict or None):
        super().__init__(name, None)

    def addDevice(self, device):
        self.__devices.append(device)

    def offlineDevice(self):
        result = []
        for device in self.__devices:
            if device._status == 0:
                result.append(device)
        return result


class TrDevice(TrObject):
    def __init__(self, name: str, info: dict or None):
        super().__init__(name, None)
        self._name = info["name"]
        self._status = info["status"]
        self._ip = info["ip"]
        self._port = info["port"]
        self._model = info["model"]





