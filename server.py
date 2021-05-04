import datetime
import socket
import json



class TrDevice():
    """
    Класс хранения в себе информации о состоянии камер и взаимодействия с переданной информацией
    """
    serverList = []

    __devices = {}

    def __init__(self):
        pass

    def loadInfo(self):
        """
        Функция ожидает получения информации с сервера трассир, лочится на sock.listen
        После запуска скрипта на сервере, функция составляет список серверов
        :return: Возвращает словарь со всеми серверами и устройствами
        """
        print("Старт ожидания информации с сервера")
        sock = socket.socket()
        sock.bind(('', 8000))
        sock.listen(1)
        try:
            conn, addr = sock.accept()
            print('Внешнее подключение:', addr)
            result = b''
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                result += data
            conn.close()
            result = json.loads(result)
            self.serverList = list(result.keys())
            result["scanDateTime"] = str(datetime.datetime.now())
            self.__devices = result

            return result.decode("utf-8")
        except Exception as e:
            return "Ошибка получения информации с сервера\n"+str(e)

    def getDevices(self, online=None):
        """
        Выводит все устройства по названию сервера
        :return:
        """
        if online is None:
            return self.__devices
        elif online == 0:
            return

        elif online == 1:
            return


    def saveToFile(self):
        """
        Сохраняет текущее значение в json файл
        """
        with open ("deviceStatus.json", "w") as f:
            json.dump(self.__devices, f, indent=4)

    def loadToClass(self, path="deviceStatus.json"):
        """
        Заргужает информацию из файла
        """
        with open(path, "r") as f:
            self.__devices = json.load(f)


devices = TrDevice()
devices.loadToClass()
print(devices.getDevices(online=0))