import logging
import random
import threading
import time

from util import logcfg


def thread_worker():
    logging.info("Thread iniciado")
    time.sleep(random.random() * 10)
    logging.info("Thread acabado")


def main():
    threads = [threading.Thread(target=thread_worker, name=f"Hilo {i + 1}") for i in range(10)]
    for t in threads:
        t.start()

    while threads:
        time.sleep(0.2)
        for t in threads:
            if not t.is_alive():
                t.join()
                threads.remove(t)

    logging.info("Todos los hilos finalizados.")


if __name__ == '__main__':
    logcfg(__file__)
    logging.info("Programa iniciado")
    main()
    logging.info("Programa finalizado")
