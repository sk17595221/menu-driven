# menu-driven
# this is a python program for run a app using cmd in window
import os
import pyttsx3
while True:
    pyttsx3.speak("hi i am  sumit ")
    pyttsx3.speak("can i help you ")
    print("This is menu driven program ")
    print("\n1.chrome")
    print("\n2.notepad")
    print("\n3.media player")
    print("\n4.python")
    print("\n5.control panel")
    print("\n6.Internet Explorer")
    print("\n7.vlcplayer")
    print("\n8.Virtual player")
    print("\n9.AnyDesk")
    print("\n10.shutdown")
    print("\n11.restart")
    print("\n12.jupyternotebook")
    print("\n13.exit")
    
    print("chat with me with your requirements : "  , end='')
    p = input()
    if ("run" in p)  and ("chrome" in p):
         os.system("chrome")
    elif (("run" in p) or  ("execute" in p )) and  (("notepad" in p) or ("editor" in p) ) :
        os.system("notepad")
    elif ("run" in p)  and ("player" in p) and ("media" in p):
        os.system("wmplayer")
    elif ("run" in p) and ("python"in p):
        os.system("python")
    elif ("run"in p) and ("control panel" in p):
        os.system("control panel")
    elif ("run"in p) and ("Internet Explorer" in p):
        os.system("@start iexplore")
    elif ("run"in p) and ("vlcplayer" in p):
        os.system("vlc")
    elif ("run"in p) and ("VirtualBox" in p):
        os.system("VirtualBox")
    elif ("run"in p) and ("AnyDesk" in p):
        os.system("AnyDesk")
    elif ("run"in p) and ("poweroff" in p):
        os.system("shutdown /s")
    elif ("run"in p) and ("restart" in p):
        os.system("shutdown /r")
    elif ("run"in p) and ("jupyternotebook" in p):
        os.system("jupyter notebook")    
    elif  ("exit" in p)  or ("quit" in p):
        break
    else:
        print("don't support")
