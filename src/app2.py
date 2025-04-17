import time
import pyautogui 
import subprocess
import ctypes
import pygetwindow as gw
import os
from pathlib import Path

base_dir = Path(__file__).resolve().parent
image_path = base_dir / 'public'

def open_edge():
    subprocess.Popen(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    time.sleep(3)


def config_window():
    windows = [w for w in gw.getWindowsWithTitle('Edge') if w.visible]
    if windows:
        win = windows[0]
        win.moveTo(0, 0)
        win.resizeTo(1200, 600)
        win.activate()
        return win
    else:
        return None
    

def go_to_URL():
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.2)
    pyautogui.write('http://200.116.211.51/Panacea/', interval=0.001)
    pyautogui.press('enter')
    time.sleep(2)

def open_menu():
    pyautogui.hotkey('alt', 'f')
    time.sleep(1)
    pyautogui.press('down')  
    time.sleep(0.1)  
    for _ in range(18):  
        pyautogui.press('down')
        time.sleep(0.0001)
    pyautogui.press('enter')
    time.sleep(7) 

def check_dpi_scaling():
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)  

        hdc = ctypes.windll.user32.GetDC(0)
        dpi_x = ctypes.windll.gdi32.GetDeviceCaps(hdc, 88)  
        ctypes.windll.user32.ReleaseDC(0, hdc)

        scaling = int((dpi_x / 96) * 100)  

        if scaling != 100:
            return False
        else:
            return True

    except Exception as e:
        print(f"⚠️ No se pudo verificar el escalado de pantalla: {e}")

def write_credentials(): 
    user_img = str(image_path / 'input_username.png')
    pass_img = str(image_path / 'input_password.png')
    button_img = str(image_path / 'button_login.png')

    if not os.path.isfile(user_img):
        print(f"❌ Imagen no encontrada: {user_img}")
        return
    
    if not os.path.isfile(pass_img):
        print(f"❌ Imagen no encontrada: {pass_img}")
        return
    
    if not os.path.isfile(button_img):
        print(f"❌ Imagen no encontrada: {button_img}")
        return

    input_username = pyautogui.locateOnScreen(user_img, confidence=0.7)
    input_password = pyautogui.locateOnScreen(pass_img, confidence=0.7)
    button_login   = pyautogui.locateOnScreen(button_img, confidence=0.7)

    if input_username:
        pyautogui.click(input_username)
        pyautogui.write('stellez', interval=0.01)

    if input_password:
        pyautogui.click(input_password)
        pyautogui.write('Stm1098709240', interval=0.01)

    if button_login: 
        pyautogui.click(button_login)
        time.sleep(5)

   
def select_sede():
    sede_select = str(image_path / 'input_sede.png')

    if not os.path.isfile(sede_select):
        print(f"❌ Imagen no encontrada: {sede_select}")
        return

    open_sede = pyautogui.locateOnScreen(sede_select, confidence=0.7)

    if open_sede:
        pyautogui.click(open_sede)
        time.sleep(2)

        confirm_button = str(image_path / 'button_confirm.png')
        
        if not os.path.isfile(confirm_button):
            print(f"❌ Imagen no encontrada: {confirm_button}")
            return
        button_confirm = pyautogui.locateOnScreen(confirm_button, confidence=0.7)

        if button_confirm:
            pyautogui.click(button_confirm)
            time.sleep(2)

def programs_code( self ): 
    programs_code = str(image_path / 'programs.png')
    time.sleep(2)

    if not os.path.isfile(programs_code):
        print(f"❌ Imagen no encontrada: {programs_code}")
        return
    
    open_program = pyautogui.locateOnScreen(programs_code, confidence=0.7)







open_edge()
window = config_window()

if window:
    check = check_dpi_scaling()
    if check:
        go_to_URL()
        open_menu()
        write_credentials()
