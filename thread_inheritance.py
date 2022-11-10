import logging
import threading
import time
import random

from util import logcfg


class ThreadWorker(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        logging.info("Thread iniciado")
        time.sleep(random.random() * 10)
        logging.info("Thread acabado")


def main():
    threads = [ThreadWorker(f"Hilo {i+1}") for i in range(10)]
    for t in threads: t.start()
    while threads:
        time.sleep(0.2)
        for t in threads:
            if not t.is_alive():
                t.join()
                threads.remove(t)

    logging.info("Todas las tareas finalizadas")


if __name__ == '__main__':
    logcfg(__file__)
    logging.info("Programa iniciado")
    main()
    logging.info("Programa finalizado")
