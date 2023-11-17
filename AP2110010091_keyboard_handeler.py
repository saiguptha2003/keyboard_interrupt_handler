from time import sleep
from threading import Thread
from _thread import interrupt_main
import sys
def task():
    
    sleep(3)
    print('Interrupting main thread now')
    interrupt_main()
thread = Thread(target=task)
thread.start()

try:
    while True:
        print('Main thread waiting...')
        sleep(0.5)
except KeyboardInterrupt:
    print('Main interrupted! Exiting.')
    print("keyboard interrupt is handled") 
