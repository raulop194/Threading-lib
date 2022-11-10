import logging
import threading
import time

from util import logcfg


def thread_worker():
    logging.info("Buenas! Soy un hilo")
    time.sleep(2.)
    logging.info("Aqui me despido...")


def main():
    a_thread = threading.Thread(target=thread_worker, name="My beautiful Thread")
    logging.info(f"Nuevo hilo creado en estado nuevo. (New)")

    logging.info(f"Hilo listo para correr, pronto empezara... (Runnable)")
    a_thread.start()

    logging.info(f"Esperando a que el hilo termine.")
    a_thread.join()
    logging.info(f"El hilo a terminado. (Dead)")


if __name__ == '__main__':
    logcfg(__file__)
    main()
