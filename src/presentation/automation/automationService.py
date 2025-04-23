import subprocess
import time
import pygetwindow as gw
import pyautogui
from pathlib import Path
import os
from config.config import PROJECT_ROOT
import cv2
import pytesseract
import numpy as np
import json

public = PROJECT_ROOT / "public"
script = PROJECT_ROOT / "script"


class AutomationService:


    def open_edge( self ):
        subprocess.Popen(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        time.sleep(3)


    def config_window( self ):
        windows = [w for w in gw.getWindowsWithTitle('Edge') if w.visible]
        if windows:
            win = windows[0]
            win.moveTo(0, 0)
            win.resizeTo(1200, 600)
            win.activate()
            return win
        else:
            return None
        

    def go_to_URL( self ):
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.2)
        pyautogui.write('http://200.116.211.51/Panacea/', interval=0.001)
        pyautogui.press('enter')
        time.sleep(2)

    def open_menu( self ):
        pyautogui.hotkey('alt', 'f')    
        time.sleep(1)
        pyautogui.press('down')  
        time.sleep(0.1)  
        for _ in range(18):  
            pyautogui.press('down')
            time.sleep(0.0001) 
        pyautogui.press('enter')
        time.sleep(5) 

    def write_credentials( self ):
        pyautogui.write('stellez', interval=0.01)
        pyautogui.press('tab')
        pyautogui.write('Stm1098709240', interval=0.01)
        pyautogui.press('tab')
        pyautogui.press('enter')

    def select_sede(self):
        sede_select = str(public / 'input_sede.png')

        if not os.path.isfile(sede_select):
            print(f"❌ Imagen no encontrada: {sede_select}")
            return

        time.sleep(2) 

        try:
            open_sede = pyautogui.locateOnScreen(sede_select, confidence=0.6)
        except pyautogui.ImageNotFoundException:
            print("❌ No se encontró la imagen de sede en pantalla.")
            return

        if open_sede:
            pyautogui.click(open_sede)
            time.sleep(2)

            confirm_button = str(public / 'button_confirm.png')

            if not os.path.isfile(confirm_button):
                print(f"❌ Imagen no encontrada: {confirm_button}")
                return
            
            time.sleep(2)

            try:
                button_confirm = pyautogui.locateOnScreen(confirm_button, confidence=0.6)
            except pyautogui.ImageNotFoundException:
                print("❌ No se encontró el botón de confirmar.")
                return

            if button_confirm:
                pyautogui.click(button_confirm)
                time.sleep(2)
        else:
            print("❌ No se encontró la opción de sede.")


    def query_schedule( self, paid: str ):
        schedule_create = str(public / 'image.png')

        if not os.path.isfile(schedule_create):
            print(f"❌ Imagen no encontrada: {schedule_create}")
            return

        time.sleep(2)

        try:
            open_schedule = pyautogui.locateOnScreen(schedule_create, confidence=0.6)
        except pyautogui.ImageNotFoundException:
            print("❌ No se encontró la imagen de sede en pantalla.")
            return
    
        if open_schedule:
            pyautogui.click(open_schedule)

            time.sleep(5)   
            search = str(public / 'search_and_create_schedule.png')
            if not os.path.isfile(search):
                print(f"❌ Imagen no encontrada: {search}")
                return
            
            search_one = pyautogui.locateOnScreen(search, confidence=0.6)
            if search_one:
                pyautogui.click(search_one)
                time.sleep(1)
                pyautogui.write( paid, interval=0.01 )
                pyautogui.press('enter')
                time.sleep(5)   
        else:
            print("❌ No se encontró la opción de agendar cita.")

    def full_output( self ):
        medio_solicitud = str(public / 'medio_solicitud.png')
        if not os.path.isfile(medio_solicitud):
            print(f"❌ Imagen no encontrada: {medio_solicitud}")
            return

        medio_solicitud_one = pyautogui.locateOnScreen(medio_solicitud, confidence=0.6)
        if medio_solicitud_one:
            center = pyautogui.center(medio_solicitud_one)
            pyautogui.click(x=center.x + 200, y=center.y)
            time.sleep(1)
            pyautogui.write("Telefonico", interval=0.01)
            pyautogui.press('enter')
            time.sleep(2)

    def search_code( self ):
        search_code = str(public / 'search_and_create_schedule.png')
        if search_code:
            pyautogui.click( search_code )
            time.sleep( 1 )
            pyautogui.write("8902015", interval=0.01 )
            pyautogui.press('enter')


    def programs_code( self ): 
        programs_code = str(public / 'programs.png')
        time.sleep(2)

        if not os.path.isfile(programs_code):
            print(f"❌ Imagen no encontrada: {programs_code}")
            return
        
        open_program = pyautogui.locateOnScreen(programs_code, confidence=0.7)
        if open_program:
            open_pr = pyautogui.center(open_program)
            pyautogui.click(x=open_pr.x + 100, y=open_pr.y)
            time.sleep(2)
            pyautogui.write("ADULTEZ", interval=0.01)
            pyautogui.press('enter')

            

    def press_pyp( self ):
        ahk_script_path = str(script / 'press_DHP.ahk')

        ahk_exe_path = r"C:\Program Files\AutoHotkey\v1.1.37.02\AutoHotkeyU64.exe"
        try:
            subprocess.run([ahk_exe_path, ahk_script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el script AHK: {e}")
        except FileNotFoundError:
            print(f"No se encontró AutoHotkey en: {ahk_exe_path}")


    # def time_duration_schedule( self ):

        ## REFACTOR
        # time_img = str(public / 'prioritaria.png')
        # time.sleep(2)

        # if not os.path.isfile(time_img):
        #     print(f"❌ Imagen no encontrada: {time_img}")
        #     return          
        
        # time_img_one = pyautogui.locateOnScreen(time_img, confidence=0.7)
        # if time_img_one:
        #     open_pr = pyautogui.center(time_img_one)
        #     print(open_pr)
        #     pyautogui.click(x=open_pr.x - 100, y=open_pr.y)
        #     time.sleep(2)
        #     pyautogui.write("Cita 30 minutos", interval=0.01)
        #     pyautogui.press('enter')

        #     time.sleep(2)
        #     calendar_img = str(public / 'calendar.png')
        #     if not os.path.isfile(calendar_img):
        #         print(f"❌ Imagen no encontrada: {calendar_img}")
        #         return
            
        #     calendar = pyautogui.locateOnScreen(calendar_img, confidence=0.6)
        #     if calendar:
        #         pyautogui.click(calendar)
        #         pyautogui.write("18/04/2025", interval=0.01)
        #         pyautogui.press('enter')

    def executeAHK_script( self ):
        ahk_script_path = str(script / 'press_DHP.ahk')
        press_dhp = str(script / 'press_DHP.ahk')

        ahk_exe_path = r"C:\Program Files\AutoHotkey\v1.1.37.02\AutoHotkeyU64.exe"
        try:
            subprocess.run([ahk_exe_path, ahk_script_path], check=True)
            subprocess.run([ahk_exe_path, press_dhp], check=True)
            print("Script AHK ejecutado con éxito.")
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el script AHK: {e}")
        except FileNotFoundError:
            print(f"No se encontró AutoHotkey en: {ahk_exe_path}")



    def principal( self, paid: str, date: str ): 
        self.open_edge()
        self.config_window()
        self.go_to_URL()
        self.open_menu()
        self.write_credentials()
        self.select_sede()
        self.query_schedule( paid=paid )
        self.full_output()
        self.search_code()
        self.programs_code()
        self.press_pyp()

        # self.time_duration_schedule()
        # time.sleep(10)
        # self.executeAHK_script()

   

    



