import pyautogui
import pyperclip
import time


def test_po():
    time.sleep(4)
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()
    print(pyautogui.position())


# this test is created to test the registe followed with login uses case
# !!!!!!! be careful when running this test
# !!!!!!! don't move your mouse it can  make changes automaticaly to your code

def test_login_ui():
    time.sleep(4)
    print(pyautogui.position())
    # moving the app window to the top left corner

    listwindows=pyautogui.getWindowsWithTitle('PentRacker')
    if(len(listwindows)!=0):
        appwindow=listwindows[0]
        window_width=appwindow.width
        window_height=appwindow.height
        window_position = appwindow.moveTo(0,0)

        # clicking the register button
        registerXposition= int(window_width/2)
        registerYposition= window_height -25
        pyautogui.moveTo(registerXposition, registerYposition)
        pyautogui.click()

        # filling the form
        email_input_x=556
        email_input_y=263
        pyautogui.moveTo(email_input_x, email_input_y)
        pyautogui.click()
        pyautogui.typewrite('benslama13souheil', interval=0.25)
        pyperclip.copy("@")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.typewrite('gmail.com', interval=0.25)
        username_input_x=556
        username_input_y=346
        pyautogui.moveTo(username_input_x, username_input_y)
        pyautogui.click()
        pyautogui.typewrite('souheil', interval=0.25)
        phone_input_x=588
        phone_input_y=415
        pyautogui.moveTo(phone_input_x, phone_input_y)
        pyautogui.click()
        pyautogui.typewrite('12343223', interval=0.25)
        password_input_x = 610
        password_input_y = 490
        pyautogui.moveTo(password_input_x, password_input_y)
        pyautogui.click()
        pyperclip.copy("Testing123!")
        pyautogui.hotkey("ctrl", "v")
        confirmpassword_input_x = 619
        confirmpassword_input_y = 565
        pyautogui.moveTo(confirmpassword_input_x,confirmpassword_input_y)
        pyautogui.click()
        pyperclip.copy("Testing123!")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.moveTo(registerXposition, registerYposition)
        pyautogui.click()
        # we need to login  after creating the user
        time.sleep(2)
        email_input_x = 595
        email_input_y = 431
        pyautogui.moveTo(email_input_x, email_input_y)
        pyautogui.click()
        pyautogui.typewrite('benslama13souheil', interval=0.25)
        pyperclip.copy("@")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.typewrite('gmail.com', interval=0.25)
        pass_input_x = 603
        pass_input_y = 506
        pyautogui.moveTo(pass_input_x, pass_input_y)
        pyautogui.click()
        pyperclip.copy("Testing123!")
        pyautogui.hotkey("ctrl", "v")
        # clicking login button
        login_input_x = 575
        login_input_y = 575
        pyautogui.moveTo(login_input_x, login_input_y)
        pyautogui.click()
        time.sleep(5)
    else:
        print("the app window is not found")

