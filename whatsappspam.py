from socketserver import ThreadingTCPServer
import pyautogui
import time
count_spam=int(input('Enter how many time u want to Spam:-'))
for i in range(count_spam):
    time.sleep(3)
    pyautogui.write(f"Hey you there")
    time.sleep(1)
    pyautogui.press("ENTER")