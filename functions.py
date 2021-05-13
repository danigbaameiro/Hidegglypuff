import substitution as sub
import insertion as ins
import spectro as spec
import os
import time

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
   
    while True:
        os.system('clear')
        animation()

        print ("""[*] Choose the method:
    \u001b[32m[1] Insertion-Based\u001b[0m
    \u001b[32m[2] Substitution-Based\u001b[0m
    \u001b[31m[3] Generation-Based\u001b[0m
    [4] Exit/Quit
    """)

        ans=input("What would you like to do? ") 
        
        if ans=="1": 
            ins.options()
            time.sleep(2.4)
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
            print("\nOuh yeah baby, let's go!")
            spec.options()
        elif ans=="5":
            print("\nNot implemented yet") 
        elif ans=="6":
            print("\nOuh yeah baby, let's go!") 
            sub.options()
            time.sleep(2.4)
        elif ans=="7":
            print("\nGoing back! :)") 
            break
        elif ans !="":
            print("\n Not Valid Choice! Try again bitch") 
