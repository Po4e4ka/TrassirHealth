import datetime
import socket
import json


class TrObject():
    """
    Класс объекта трассир
    """

    def __init__(self, name: str, info: dict or None):
        self.name = name
        self.info = info

    @staticmethod
    def loadFromTrassir():
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
        serverList = TrObject.dictToClasses(result)
        result["scanDateTime"] = str(datetime.datetime.now())
        return result, serverList

    @staticmethod
    def dictToClasses(result):
        """
        Функция принимает выгрузку с клиента трасир в аргумент, а возвращает список объектов класса Сервер
        в объектах Сервер хранится список устройств - объектов Девайс
        :param result:
        :return:
        """
        serverList = []
        for servName, devices in list(result.items()):
            tempS = TrServer(servName, devices)
            for device, devInfo in devices.items():
                tempD = TrDevice(device, devInfo)
                tempS.addDevice(tempD)
                del tempD
            serverList.append(tempS)
            del tempS
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


    def __init__(self, name: str, info: dict or None):
        self.__devices = []
        super().__init__(name, None)

    def addDevice(self,device):
        self.__devices.append(device)

    def offlineDevice(self, *args):
        """
        Показывает оффлайн девайсы на сервере,
        также можно передать аргументы в виде строк, какую информацию надо выносить
        :param args: списко параметров для вывода, если None - выводит объект
        :return:
        """
        result = []
        for device in self.__devices:
            if device.status == 0:
                if args == None:
                    result.append(device)
                else:
                    result.append(''.join([f"{device[arg]}  " for arg in args])+'\n')
        return result if len(result) > 0 else None


class TrDevice(TrObject):

    def __init__(self, name: str, info: dict or None):
        super().__init__(name, None)
        self.info = info
        self.name = info["name"]
        self.status = info["status"]
        self.ip = info["ip"]
        self.port = info["port"]
        self.model = info["model"]

    def __getitem__(self, item):
        return self.info[item]





