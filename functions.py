import global_variables as g
import substitution as sub
import insertion as ins
import spectro as spec
import os
import time
import signal

# Capture "Ctrl+C" to prevent it from displaying faults
def signal_handler(sig, frame):
    print("\n\nGoodbye :)")
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

def animation():
    print('''\u001b[35m

       ,..__
  |  _  `--._                                  _.--"""`.
  |   |._    `-.        __________         _.-'    ,|' |
  |   |  `.     `-..--""_.        `""-..,-'      ,' |  |
  L   |    `.        ,-'                      _,'   |  |
   .  |     ,'     ,'            .           '.     |  |
   |  |   ,'      /               \            `.   |  |
   |  . ,'      ,'                |              \ /  j
   `   "       ,                  '               `   /
 ♫ `,         |                ,'                  '+  ♪♫
    /          |             _,'                     `
   /     .-"""'L          ,-' \  ,-'""""`-.           `  ♪
  j    ,' ,.+--.\        '    ',' ,.,-"--._`.          \\      ♫
  |   / .'  L    `.        _.'/ .'  |      \ \          .  ♪
 j   | | `--'     |`+-----'  . j`._,'       L |         |
 |   L .          | |        | |            | |         | ♪
 |   `\ \        / j         | |            | |         |  ♪
 |     \ `-.._,.- /           . `         .'  '         |
 l      `-..__,.-'             `.`-.....-' _.'          '
 '                               `-.....--'            j
  .                  -.....                            |    ♪♫
   L                  `---'                            '
    \\                                                 /
     ` \                                        ,   ,'
      `.`.    |🎤                      /      ,'   .
        . `._,                        |     ,'   .'     ♪♪
         `.                           `._.-'  ,-'    ♪
    _,-""""`-,                             _,'"-.._
  ,'          `-.._                     ,-'        `.
 /             _,' `"-..___     _,..--"`.            `.
|         _,.-'            `"""'         `-._          \\
`-....---'              Hidegglypuff         `-.._      |
                                                  `--...'\u001b[0m

''')

def menuMain():
    os.system('clear')
    animation()

    detect_file()
   
    while True:
        os.system('clear')
        animation()

        print_file()

        print ("""\n\u001b[34m[*]\u001b[0m Choose the method:
    \u001b[32m[1] Insertion-Based\u001b[0m
    \u001b[32m[2] Substitution-Based\u001b[0m
    \u001b[31m[3] Generation-Based\u001b[0m
    [4] Exit/Quit
    """)

        ans=input("What would you like to do? ") 
        
        if ans=="1": 
            ins.options()
        elif ans=="2":
            print("\nOuh yeah baby, let's go!") 
            menuSub()
        elif ans=="3":
            print("\nNot implemented yet") 
        elif ans=="4":
            print("\nGoodbye :)") 
            break
        elif ans !="":
            print("\n Not Valid Choice! Try again bitch") 

def menuSub():
    while True:
        os.system('clear')
        animation()

        print ("""Choose the method:
    \u001b[31m[1] Echo Hiding\u001b[0m
    \u001b[31m[2] Phase Coding\u001b[0m
    \u001b[31m[3] Parity Coding\u001b[0m
    \u001b[32m[4] Spread Spectrum\u001b[0m
    \u001b[31m[5] Tone insertion\u001b[0m
    \u001b[32m[6] LSB (Least Significant Bit)\u001b[0m
    [7] Go back
    """)

        ans=input("What would you like to do? ") 

        if ans=="1": 
            print("\nNot implemented yet") 
        elif ans=="2":
            print("\nNot implemented yet") 
        elif ans=="3":
            print("\nNot implemented yet") 
        elif ans=="4":
            spec.options()
        elif ans=="5":
            print("\nNot implemented yet") 
        elif ans=="6":
            sub.options()
        elif ans=="7":
            print("\nGoing back! :)") 
            break
        elif ans !="":
            print("\n Not Valid Choice! Try again bitch") 

def load_file():
    ### To use this function you need to install the following modules:
    # from tkinter import Tk     # from tkinter import Tk for Python 3.x
    # from tkinter.filedialog import askopenfilename

    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    global filename 
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

    if len(filename) == 0:
        print("\u001b[31m[!]\u001b[0m You have not entered any songs or wav files ¬¬ Come back when you have some!")
        exit()
    else:
        if filename.endswith('.wav'):
            print("\u001b[34m[*]\u001b[0m You have selected the song: "+filename)
        else:
            print("\u001b[31m[!]\u001b[0m You have not entered a correct song file ¬¬ This programm only accept WAV files!")
            exit()


def detect_file():
    count_wav=0
    count_mp4=0

    for file in os.listdir("./resources"):
        if file.endswith(".wav"):
            g.filename_wav=file
            count_wav+=1
        elif file.endswith(".mp4"):
            g.filename_mp4=file
            count_mp4+=1

    if count_wav > 1 or count_mp4 > 1:
        print("\u001b[31m[!]\u001b[0m You have more than one file in resources folder ¬¬")
        print("\u001b[34m[*]\u001b[0m Come back when you have only one WAV file!")
        exit()
    elif g.filename_wav=="" and g.filename_mp4=="":
        print("\u001b[31m[!]\u001b[0m You have not entered any MP4 or WAV files in resources folder ¬¬")
        print("\u001b[34m[*]\u001b[0m Come back when you have some!")
        exit()

def print_file():
    if g.filename_mp4 != "":
        print("\u001b[34m[*]\u001b[0m You have selected the video: \u001b[33m"+g.filename_mp4+"\u001b[0m")
    if g.filename_wav != "":
        print("\u001b[34m[*]\u001b[0m You have selected the song: \u001b[33m"+g.filename_wav+"\u001b[0m")
    
def create_folders():
    folders = ["tmp", "resources", "media"] 

    for name_folder in folders:
        if not os.path.exists(name_folder):
            os.mkdir("./"+name_folder)