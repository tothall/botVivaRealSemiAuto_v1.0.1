import sys
import os

from time import sleep

import keyboard

from Data import Extraction
from Data import MetaData


class Checkers:
    """Todas as funções dessa classe tem o objetivo de checar determinadas condições"""

    @staticmethod
    def exit(driver, _exit, wait, time_start):
        _exit.set()  # não mexer
        MetaData.get_extraction_info(wait, driver, time_start)
        Extraction.delete_temp_sheet()
        driver.quit()
        sys.exit()

    @staticmethod
    def exit_shortcut_checker(wait, driver, timer_start, start_time, _exit):
        """Checa se o usuário deseja finalizar o programa"""
        while True:
            if keyboard.is_pressed("esc"):
                _exit.set()  # não mexer
                print("Salvando extração...")
                sleep(0.5)
                MetaData.get_extraction_info(wait, driver, timer_start, start_time, _exit)
                Extraction.delete_temp_sheet()
                driver.quit()
                sys.exit()

    @staticmethod
    def pause_restart_shortcut_checker(_exit, pause, messaging):
        """Checa se o usuário deseja pausar ou iniciar a extração"""
        while True:
            if keyboard.is_pressed("p"):
                print("Extração pausada")
                pause.set()
                if _exit.isSet():
                    os.system('cls')

            elif keyboard.is_pressed("i") and pause.isSet():
                print("Extração retomada")
                pause.clear()
            elif keyboard.is_pressed("i") and not messaging.isSet():
                os.system('cls')
                print("Extração iniciada")
                sleep(2)
                messaging.set()
                pause.clear()
            elif _exit.isSet():
                print("FIM do programa")
                os.system('cls')
                sys.exit()

    @staticmethod
    def next_page_detection(wait, driver, _exit, pause):
        """Checa se a página foi passada, essa é a condição que chama a função para extrair os anúncios da página"""
        ref_page = driver.current_url
        pages_counter = 0
        ads_counter = 0
        while True:
            if _exit.isSet(): #or (_exit.isSet() and not pause.isSet()):
                sys.exit()
            elif driver.current_url != ref_page and pause.isSet():
                pass
            elif driver.current_url != ref_page and not pause.isSet():
                if _exit.isSet():
                    sys.exit()
                elif driver.current_url.find("google", 0) == -1 and driver.current_url.find("vivareal", 0) != -1:
                    ref_page = driver.current_url  # Atualiza a url de referência
                    extracted_ads = Extraction.all_page_ads_extraction(wait, driver, _exit, pause)  # Extrai todos os anúncios da página
                    pages_counter += 1
                    ads_counter += extracted_ads
                    print(f"{ads_counter} Anúncios extraídos")
                    print(f"{pages_counter} Páginas extraídas")







