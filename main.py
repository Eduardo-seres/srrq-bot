import subprocess
import pyautogui as magic
import time
import pandas as pd
from datetime import datetime
import threading
import sys
import webbrowser
from linkcred import lst
import emoji

sys.tracebacklimit = 0
read_file = pd.read_csv(r'settings.txt', header=None)
read_file.columns = ['location', 'starttime', 'meetingid', 'meetingpswd']
read_file.to_csv(r'settings.csv', index=None)

sett = pd.read_csv('settings.csv')

locate = sett['location']

def sign_in(meetingid, meetingpswd):
    subprocess.call(locate)

    time.sleep(10)
    join_btn = magic.locateCenterOnScreen('C:\\Users\\Eduardo Rivas\\Documents\\SRRQ_BOT\\core\\join_button.png')
    magic.moveTo(join_btn)
    magic.click()

    meeting_id_btn = magic.locateCenterOnScreen('C:\\Users\\Eduardo Rivas\\Documents\\SRRQ_BOT\\core\\meeting_id_button.png')
    magic.moveTo(meeting_id_btn)
    magic.click()
    magic.write(meetingid)

    media_btn = magic.locateAllOnScreen('C:\\Users\\Eduardo Rivas\\Documents\\SRRQ_BOT\\core\\media_btn.png')
    for btn in media_btn:
        magic.moveTo(btn)
        magic.click()
        time.sleep(2)

    join_btn = magic.locateCenterOnScreen('C:\\Users\\Eduardo Rivas\\Documents\\SRRQ_BOT\\core\\join_btn.png')
    magic.moveTo(join_btn)
    magic.click()

    time.sleep(5)

    meeting_pswd_btn1 = magic.locateCenterOnScreen('C:\\Users\\Eduardo Rivas\\Documents\\SRRQ_BOT\\core\\meeting_pswd.png')
    magic.moveTo(meeting_pswd_btn1)
    magic.click()
    magic.write(meetingpswd)
    magic.press('enter')

    meeting_pswd_btn2 = magic.locateCenterOnScreen('C:\\Users\\Eduardo Rivas\\Documents\\SRRQ_BOT\\core\\meeting_pswd_btn.png')
    magic.moveTo(meeting_pswd_btn2)
    magic.click()
    magic.write(meetingpswd)
    magic.press('enter')

    meeting_pswd_btn3 = magic.locateCenterOnScreen('C:\\Users\\Eduardo Rivas\\Documents\\SRRQ_BOT\\core\\meeting_pswd2.png')
    magic.moveTo(meeting_pswd_btn3)
    magic.click()
    magic.write(meetingpswd)
    magic.press('enter')

def waiting():
    while True:
        k = magic.locateCenterOnScreen('C:\\Users\\Eduardo Rivas\\Documents\\SRRQ_BOT\\core\\checkpoint.png')
        if k is None:
            print("waiting to be entered")
            time.sleep(2)
        else:
            magic.moveTo(k)
            magic.press('enter')
            magic.click()
            break

def noid(link, time_schedule):
    isStarted = False
    while not isStarted:
        if datetime.now().strftime("%H:%M") == time_schedule:
            for _ in range(1):
                webbrowser.open(link)
                time.sleep(8)
                magic.press('enter')
                time.sleep(6)
                magic.press('enter')
                magic.press('enter')
                magic.hotkey('alt', 'v')
                magic.hotkey('alt', 'h')
                for _ in range(750):
                    magic.hotkey('ctrl', 'v')
                    #📌¡APROVECHA LA OPORTUNIDAD! 📌 https://seresderiqueza.mx/01_Riqueza_infinita_sl
                    #felicit = " :smile: " + " ¡APROVECHA LA OPORTUNIDAD! " + "https://seresderiqueza.mx/01_Riqueza_infinita_sl"
                    # felicit = emoji.emojize('Python es :pulgar_hacia_arriba:', language='es')
                    #magic.write(felicit)
                    magic.press('enter')
                    time.sleep(7)
                
                magic.hotkey('alt', 'q')  # cerramos pal siguiente bot
            isStarted = True


def mainq():
    # Inicia los subprocesos solo una vez
    thread3 = threading.Thread(target=waiting, daemon=True)
    thread3.start()

    for item in lst:
        curr = datetime.now().strftime("%H:%M")
        nodataid = str(sett.iloc[0, 2])
        nodatapswd = str(sett.iloc[0, 3])
        if curr in str(sett['starttime']):
            print("Found Meeting ID and Password")
            print("Waiting for starttime")
            row1 = sett.loc[sett['starttime'] == curr]
            meetingid = str(row1.iloc[0, 2])
            meetingpswd = str(row1.iloc[0, 3])
            sign_in(meetingid, meetingpswd)
            print('signed in')
        elif nodataid == "meetingid" and nodatapswd == 'meetingpswd':
            print("Found Link")
            print("Waiting for starttime")
            noid(item[0], item[1])
            print('signed in')

    # Espera a que el bucle principal termine antes de continuar con la ejecución
    thread3.join()

if __name__ == "__main__":
    mainq()
