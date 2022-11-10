import logging
import random
import threading
import time

from util import logcfg


def thread_daemon():
    while True:
        logging.info("Bum bum!")
        time.sleep(1)


def main():
    daemon = threading.Thread(target=thread_daemon, name=f"Diablin uwu", daemon=True)
    logging.info(f"Comenzando el daemon {daemon.name}...")
    daemon.start()
    time.sleep(10)
    logging.info(f"Termina el hilo principal")


if __name__ == '__main__':
    logcfg(__file__)
    main()

