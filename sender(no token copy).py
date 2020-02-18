import requests
import schedule
import time
import datetime

TOKEN = ""
sendTo = "", ""

pairList = [[2, 4], [2, 3], [3, 4], [3, 4], [2, 4], [3, 5], [4, 5], [2, 4], [3, 4], [1, 2]]

scheduleList = [[["2", "Метрология", "Бортин", "5.517", "1"], ["3", "ENGLISH", "Саргатова", "8.1110", "1"],
                 ["4", "Метрология", "Козлов", "5.515", "0"]],
                [["2", "Техн. засоби", "Даскал", "5.416", "1"], ["3", "JAVA", "Горбатюк", "5.409", "1"]],
                [["3", "Философия", "Сухова", "4.201", "0"], ["4", "Микропроц", "Кринецький", "5.407", "0"]],
                [["3", "Метрология", "Бортин", "5.517", "1"], ["4", "Микропроц.", "Кринецький", "5.411", "1"]],
                [["2", "Техн. Засоби.", "Калиниченко", "5.407", "0"], ["3", "Числ. Методи.", "Глухов", "3.216", "0"],
                 ["4", "Числ. Методи.", "Глухов", "3.2411", "1"]],
                [["3", "Метрология", "Бортин", "5.517", "1"], ["4", "Философия", "Сухова", "3.102", "1"],
                 ["5", "Метрология", "Козлов", "5.515", "0"]],
                [["4", "JAVA", "Горбатюк", "5.407", "0"], ["5", "ENGLISH", "Саргатова", "8.1110", "1"]],
                [["2", "Техн. Засоби", "Даскал", "5.416", "1"], ["3", "Числ. Методи.", "Глухов", "3.318", "0"],
                 ["4", "Микропроц.", "Кринецький", "5.407", "0"]],
                [["2", "Техн. Засоби", "Даскал", "5.416", "1"], ["3", "Числ. Методи.", "Глухов", "3.318", "0"],
                 ["4", "Микропроц.", "Кринецький", "5.407", "0"]],
                [["3", "Микропроц.", "Кринецький", "5.412а", "1"], ["4", "JAVA", "Горбатюк", "5.409", "1"]],
                [["1", "Числ. Методи.", "Глухов", "3.120", "1"], ["2", "Техн. Засоби", "Даскал", "5.407", "1"]]]


def txtmsg(msg, recipient):
    url = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + recipient + '&parse_mode=Markdown&text=' + str(
        msg)
    response = requests.get(url)
    return response.json()
    pass


def txtmsgaall(msg, recipients=sendTo):
    for i in recipients:
        print(i)
        print(txtmsg(msg, str(i)))
    pass

def identifyCurDay():
    today = datetime.datetime.today().weekday()
    # print(today)
    return today


def identifyCurWeek():
    weekNum = datetime.datetime.utcnow().isocalendar()[1]
    if weekNum % 2 == 0:
        week = 1
    else:
        week = 2
    return week


def getCurSched():
    day = 0
    if today > 4:
        return 0
    if week == 1:
        day = today
    if week == 2:
        day = today + 5
    try:
        schd = scheduleList[day]
    except:
        return 0
    # print(schd)
    return schd


def getPairNext():
    now = datetime.datetime.now()
    h = now.hour
    m = now.minute
    pairNext = 0
    if h == 7:
        pairNext = 1
    if h == 9:
        pairNext = 2
    if h == 11:
        pairNext = 3
    if h == 12:
        pairNext = 4
    if h == 14:
        pairNext = 5
    if h == 16:
        pairNext = 6
    if h == 17:
        pairNext = 7
    if h == 19:
        pairNext = 8
    return pairNext


def getNextPair():
    schd = getCurSched()
    nextpr = getPairNext()
    print(nextpr)
    if nextpr == 0:
        # try:
        #     day = identifyCurDay()
        #     schd = scheduleList[day + 1]
        #     pair = schd[nextpr]
        # except:
        return 0
    else:
        pair = schd[nextpr - 1]
    print(pair)
    return pair


def printWeekAndDay():
    print("w:" + str(week))
    print("d:" + str(today))


def sendCurSched():
    schd = getCurSched()
    pairCount = len(schd)
    txtmsgaall("Сегодня такие пары: ")
    for i in range(0, pairCount):
        if int(schd[i][4]) == 1:
            toSend = str(schd[i][0]) + ". " + str(schd[i][1]) + ", ведет " + str(schd[i][2]) + " в " + str(schd[i][3])
        else:
            toSend = str(schd[i][0]) + ". " + str(schd[i][1]) + ", ведет " + str(schd[i][2]) + " в " + str(
                schd[i][3] + ". Это лекция.")
        txtmsgaall(toSend)


def sendNextPair():
    pair = getNextPair()

    # schd = getCurSched()
    if pair == 0:
        print("NoNext")
        # pair = schd[1]
    else:
        try:
            txtmsgaall("Некст пара: ")
            if int(pair[4]) == 1:
                toSend = str(pair[0]) + ". " + str(pair[1]) + ", ведет " + str(pair[2]) + " в " + str(pair[3])
            else:
                toSend = str(pair[0]) + ". " + str(pair[1]) + ", ведет " + str(pair[2]) + " в " + str(
                    pair[3] + ". Это лекция.")
            txtmsgaall(toSend)
        except:
            print("Че-то пошло не так...")


if __name__ == '__main__':
    # txtmsg(scheduleList[3][0], sendTo[0])
    # print(scheduleList[4])
    today = identifyCurDay()
    week = identifyCurWeek()
    schedule.every(30).minutes.do(identifyCurDay)
    schedule.every(30).minutes.do(identifyCurWeek)
    schedule.every().day.at("07:30").do(sendCurSched)

    schedule.every().day.at("07:50").do(sendNextPair)
    schedule.every().day.at("09:30").do(sendNextPair)
    schedule.every().day.at("11:10").do(sendNextPair)
    schedule.every().day.at("12:50").do(sendNextPair)
    schedule.every().day.at("14:30").do(sendNextPair)
    schedule.every().day.at("16:10").do(sendNextPair)
    schedule.every().day.at("17:50").do(sendNextPair)
    schedule.every().day.at("19:30").do(sendNextPair)


    # sendCurSched()
    # schedule.every().day.at("10:30").do()
    # getNextPair()

    txtmsg("Я родился", "")
    print("start")

    while True:
        schedule.run_pending()
        time.sleep(3)
