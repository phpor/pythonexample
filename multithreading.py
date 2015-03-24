import threading

def work(x):
    while x > 0:
        print(x)
        x = x - 1

if __name__ == '__main__':
    t = threading.Thread(target=work, args=(3,))
    #t.setDaemon(True)
    t.start()

