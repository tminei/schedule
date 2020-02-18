import requests
from time import sleep as sleep
import datetime

TOKEN = ""
sendTo = "", ""

pairStart = ("7:50", "9:30", "11:10", "12:50", "14:30", "16:10", "17:50", "19:30",)

mon1p = (2, 3, 4)
tue1p = (2, 3)
wed1p = (3, 4)
thu1p = (3, 4)
fri1p = (2, 3, 4)

mon2p = (3, 4, 5)
tue2p = (4, 5)
wed2p = (2, 3, 4)
thu2p = (3, 4)
fri2p = (1, 2)

mon1pl = [["2", "Метрология", "Бортин", "5.517", "1"], ["3", "ENGLISH", "Саргатова", "8.1110", "1"],
          ["4", "Метрология", "Козлов", "5.515", "0"]]
tue1pl = [["2", "Техн. засоби", "Даскал", "5.416", "1"], ["3", "JAVA", "Горбатюк", "5.409", "1"]]

wed1pl = [["3", "Философия", "Сухова", "4.201", "0"], ["4", "Микропроц", "Кринецький", "5.407", "0"]]
thu1pl = [["3", "Метрология", "Бортин", "5.517", "1"], ["4", "Микропроц.", "Кринецький", "5.411", "1"]]
fri1pl = [["2", "Техн. Засоби.", "Калиниченко", "5.407", "0"], ["3", "Числ. Методи.", "Глухов", "3.216", "0"],
          ["4", "Числ. Методи.", "Глухов", "3.2411", "1"]]
mon2pl = [["3", "Метрология", "Бортин", "5.517", "1"], ["4", "Философия", "Сухова", "3.102", "1"],
          ["5", "Метрология", "Козлов", "5.515", "0"]]

tue2pl = [["4", "JAVA", "Горбатюк", "5.407", "0"], ["5", "ENGLISH", "Саргатова", "8.1110", "1"]]

wed2pl = [["2", "Техн. Засоби", "Даскал", "5.416", "1"], ["3", "Числ. Методи.", "Глухов", "3.318", "0"],
          ["4", "Микропроц.", "Кринецький", "5.407", "0"]]

thu2pl = [["3", "Микропроц.", "Кринецький", "5.412а", "1"], ["4", "JAVA", "Горбатюк", "5.409", "1"]]

fri2pl = [["1", "Числ. Методи.", "Глухов", "3.120", "1"], ["2", "Техн. Засоби", "Даскал", "5.407", "1"]]


def txtmsg(msg, recipient):
    url = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + recipient + '&parse_mode=Markdown&text=' + str(
        msg)
    response = requests.get(url)
    return response.json()


def txtmsgaall(msg, recipients=sendTo):
    for i in recipients:
        print(i)
        print(txtmsg(msg, str(i)))


def pairComing(data):
    toSend = "**№" + str(data[0]) + ": " + str(data[1]) + "** скоро начнется! Препод: **" + str(
        data[2]) + ".** Аудитория: **" + str(data[3]) + ".**"
    print(toSend)
    txtmsgaall(toSend)


def checkjobs(now):
    global pairData
    h = now.hour
    m = now.minute
    hm = str(h) + ":" + str(m)
    # print(hm)
    if str(hm) in pairStart:
        pairNum = pairStart.index(hm)
        # print(today)
        if today > 4:
            return 0
        if week == 1:
            if today == 0:
                if pairNum in mon1p:
                    pairData = mon1pl[pairNum - 1]
            if today == 1:
                if pairNum in tue1p:
                    pairData = tue1pl[pairNum - 1]
            if today == 2:
                if pairNum in wed1p:
                    pairData = wed1pl[pairNum - 1]
            if today == 3:
                if pairNum in thu1p:
                    pairData = thu1pl[pairNum - 1]
            if today == 4:
                if pairNum in fri1p:
                    pairData = fri1pl[pairNum - 1]
        if week == 2:
            if today == 0:
                if pairNum in mon2p:
                    pairData = mon2pl[pairNum - 1]
            if today == 1:
                if pairNum in tue2p:
                    pairData = tue2pl[pairNum - 1]
            if today == 2:
                if pairNum in wed2p:
                    pairData = wed2pl[pairNum - 1]
            if today == 3:
                if pairNum in thu2p:
                    pairData = thu2pl[pairNum - 1]
            if today == 4:
                if pairNum in fri2p:
                    pairData = fri2pl[pairNum - 1]
        pairComing(pairData)
        sleep(56)

    pass

txtmsgaall("test")
while True:
    weekNum = datetime.datetime.utcnow().isocalendar()[1]
    if weekNum % 2 == 0:
        week = 1
    else:
        week = 2

    today = datetime.datetime.today().weekday()

    now = datetime.datetime.now()
    checkjobs(now)
    sleep(5)
