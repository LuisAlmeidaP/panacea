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
        pyp_img = str(public / 'PYP.png')

        if not os.path.isfile(pyp_img):
            print(f"❌ Imagen no encontrada: {pyp_img}")
            return
        
        press_pyp = pyautogui.locateOnScreen( pyp_img, confidence=0.6 )
        if press_pyp:
            pyautogui.click(press_pyp)
            
        
        for _ in range(10):
            pyautogui.press("pagedown")
            time.sleep(0.2)


    def time_duration_schedule( self ):
        time_img = str(public / 'prioritaria.png')
        time.sleep(2)

        if not os.path.isfile(time_img):
            print(f"❌ Imagen no encontrada: {time_img}")
            return       
        
        time_img_one = pyautogui.locateOnScreen(time_img, confidence=0.7)
        if time_img_one:
            open_pr = pyautogui.center(time_img_one)
            print(open_pr)
            pyautogui.click(x=open_pr.x - 100, y=open_pr.y)
            time.sleep(2)
            pyautogui.write("Cita 30 minutos", interval=0.01)
            pyautogui.press('enter')

            time.sleep(2)
            calendar_img = str(public / 'calendar.png')
            if not os.path.isfile(calendar_img):
                print(f"❌ Imagen no encontrada: {calendar_img}")
                return
            
            calendar = pyautogui.locateOnScreen(calendar_img, confidence=0.6)
            if calendar:
                pyautogui.click(calendar)
                pyautogui.write("18/04/2025", interval=0.01)
                pyautogui.press('enter')


                # button_availa_img = str(public / 'button_disponibilidad.png')

                # if not os.path.isfile(button_availa_img):
                #     print(f"❌ Imagen no encontrada: {button_availa_img}")
                #     return
                
                # button_available = pyautogui.locateOnScreen(button_availa_img, confidence=0.7)
                # if button_available:
                #     pyautogui.click(button_available)
                


    # ! pendiente
    def move_to_date_hour_professional( self ) :

        time_input_img = str(public / 'date_hour_professional.png')
        time.sleep(2)

        if not os.path.isfile(time_input_img):
            print(f"❌ Imagen no encontrada: {time_input_img}")
            return   
        
        input_img = pyautogui.locateOnScreen(time_input_img, confidence=0.7)
        if input_img:
            pyautogui.moveTo(input_img)

        button_max = str( public / 'button_max.png' )
        if not os.path.isfile(button_max):
            print(f"❌ Imagen no encontrada: {button_max}")
            return
        
        button_max_img = pyautogui.locateOnScreen(button_max, confidence=0.7)
        if button_max_img:
            pyautogui.click(button_max_img)


    def get_table( self, path_imagen: str ) :
        imagen = cv2.imread(path_imagen)

        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

        _, binaria = cv2.threshold(gris, 180, 255, cv2.THRESH_BINARY_INV)

        kernel_h = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))
        kernel_v = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 20))

        horizontal = cv2.erode(binaria, kernel_h)
        horizontal = cv2.dilate(horizontal, kernel_h)

        vertical = cv2.erode(binaria, kernel_v)
        vertical = cv2.dilate(vertical, kernel_v)

        tabla = cv2.add(horizontal, vertical)

        contornos, _ = cv2.findContours(tabla, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        celdas = []
        for cnt in contornos:
            x, y, w, h = cv2.boundingRect(cnt)
            if w > 50 and h > 20:
                celdas.append((x, y, w, h))

        celdas_ordenadas = sorted(celdas, key=lambda b: (b[1] // 10, b[0]))

        filas = []
        fila_actual = []
        ultimo_y = -1

        for celda in celdas_ordenadas:
            x, y, w, h = celda
            if abs(y - ultimo_y) > 15:
                if fila_actual:
                    filas.append(fila_actual)
                fila_actual = []
            fila_actual.append(celda)
            ultimo_y = y
        if fila_actual:
            filas.append(fila_actual)

        tabla_extraida = []
        for fila in filas:
            fila_texto = []
            for x, y, w, h in fila:
                roi = imagen[y:y+h, x:x+w]
                texto = pytesseract.image_to_string(roi, config='--psm 7').strip()
                fila_texto.append(texto)
            tabla_extraida.append(fila_texto)

        return tabla_extraida



    def test( self ):
        ulr = 'image.png'
        resultado = self.get_table(ulr)
        print(json.dumps(resultado, indent=2, ensure_ascii=False))


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
        self.press_pyp()
        self.time_duration_schedule()
        # self.move_to_date_hour_professional()

   

    



