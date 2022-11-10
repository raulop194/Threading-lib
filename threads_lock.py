import logging
import time
from threading import Thread, Lock
from util import logcfg

counter = 0
counter_lock = Lock()


def inc_worker():
    global counter, counter_lock
    counter_lock.acquire()
    c = counter
    time.sleep(0.0001)
    counter = c + 1
    counter_lock.release()


def main():
    threads = [Thread(target=inc_worker, name=f"Hilo {i+1}") for i in range(10)]
    for t in threads: t.start()
    for t in threads: t.join()

    logging.info(f"El valor del contador es {counter}")


if __name__ == '__main__':
    logcfg(__file__)
    main()
