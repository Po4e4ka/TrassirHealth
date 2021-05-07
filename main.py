from TrObject import *

# -------------------------------------------------------------
# Загрузка с клиента трассир информации. внесение в переменную
# в переменной хранится кортеж (a, b),
# где а - выгрузка с трассира в джсон формате,
# b - список серверов в формате TrObject
devices = TrObject.loadFromTrassir(SERVER_IP="office.icstech.ru")
# -------------------------------------------------------------
# Сохранение выгрузки в файл (на всякий случай)
TrObject.saveToFile(devices[0])
TrObject.modelInfo(devices[0]["ipDevices"], toExcel=True)  # Создание файла excel с инфой о количестве камер
devices = devices[1]  # удаляю ненужный результат, уже записанный в файле
# -------------------------------------------------------------
# Cоздание строки для мессаджа бота
for server in devices:
    off = server.offlineDevice("name", "ip")  # Получение неактивных устройств
    if off is not None:  # Если есть неактивные устройства
        botMessage = server.name + '\n' + ''.join(off)
        botMessage += '\n------------------------\n'  # Для красоты в коммандной строке
        print(botMessage)
