import sys
import os

import threading

import datetime
from timeit import default_timer as timer
from time import sleep

from BrowserConfig import Config
from Checkers import Checkers

# Configurations
configurations = Config()
wait = configurations.wait
driver = configurations.driver

# Main function
print("Robô Viva Real Semiautomático v1.0.1 iniciado")
sleep(2)
start_time_hour = datetime.datetime.now().hour
start_time_minute = datetime.datetime.now().minute
start_time_second = datetime.datetime.now().second
start_time = f"{start_time_hour}h {start_time_minute}m {start_time_second}s"

_exit = threading.Event()
pause = threading.Event()
pause.set()
loading = threading.Event()
loading.clear()
messaging = threading.Event()
messaging.clear()

timer_start = timer()
thread_checador_exit = threading.Thread(target=Checkers.exit_shortcut_checker, args=(wait, driver, timer_start, start_time, _exit,))
thread_checador_next_page = threading.Thread(target=Checkers.next_page_detection, args=(wait, driver, _exit, pause,))
thread_checador_start_pause = threading.Thread(target=Checkers.pause_restart_shortcut_checker, args=(_exit, pause, messaging,))

thread_checador_exit.start()
thread_checador_next_page.start()
thread_checador_start_pause.start()

thread_checador_exit.join()
thread_checador_next_page.join()
thread_checador_start_pause.join()

os.system('echo Robô finalizado com sucesso')
os.system('pause')
sys.exit()













