import pyttsx3
import os

#pyttsx3.speak("welcome in my computer")

def task():
    while True:
        os.system("cls")
        os.system("COLOR 5F")
        print("how may i help you:" , end=' ')
        p = input()

        if("run" in p ) and ( "chrome" in p):
            os.system("chrome")
        elif( "run" in p ) and ( "notepad" in p):
            os.system("notepad")
        elif( "run" in p ) and ( "python" in p):
            os.system("python")
        elif( "run" in p ) and ( "poweroff" in p) :
            os.system("shutdown/s")
        elif( "run" in p ) and ( "Anydesk" in p):
            os.system("Anydesk")
        elif( "run" in p ) and ( "msinfo32" in p):
            os.system("msinfo32")
        elif( "run" in p ) and ( "netsh" in p):
            os.system("netsh")
        elif( "run" in p ) and ( "jupyter notebook" in p):
            try:
                os.system("jupyter notebook")
            except WindowsError:
                task()
        elif("exit"in p) or ("close"in p):
            break
        else:
            print("don't support")

if __name__=='__main__':
    os.system("cls")
    task()
