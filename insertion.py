import base64
import shutil
import os
import io
from cryptography.fernet import Fernet


#Insert the message into the .wav file
def insert_encryptb64():
    # Check path
    dirname = os.getcwd()
    original_song_name = dirname + "/resources/" + "The Local Guy - Jump By Van Halen.wav"
    edit_song_name = dirname + "/media/" + "The Local Guy - Jump By Van Halen (stego).wav"

    shutil.copy(original_song_name, edit_song_name)

    #Open the file
    song_open = open(edit_song_name, 'a')
    
    #User input the secret
    print("\n\u001b[33m[!]\u001b[0m Tell me your secret: ", end='')
    secret = input()
    encoded = base64.b64encode(secret.encode())

    #This will be the characters used to detect the secret later
    detect_final="$$$"

    #Write the message at the end of the file
    song_open.write(detect_final + encoded.decode("utf-8"))
    print("\n\u001b[34m[*]\u001b[0m Original string: ", secret)
    print("\u001b[34m[*]\u001b[0m Encoded string: "+encoded.decode("utf-8")+"\n")
    song_open.close()

#Read the message from the .wav file  
def insert_decryptb64():
    # Check path
    dirname = os.getcwd()
    song_name = dirname + "/media/" + "The Local Guy - Jump By Van Halen (stego).wav"

    #Open the file and read all the lines
    song_open = io.open(song_name,'r', encoding="cp437").readlines()

    #The message is in the last line
    last_line = song_open[len(song_open) - 1]
    rev = last_line[::-1]

    #Read the last line and get the message
    msg_list = []
    i=0
    
    for i in range(len(rev)): #The message is at the end, so it's easier to read it reversed
        a=rev[i]
        b=rev[i+1]
        c=rev[i+2]
        if a=="$" and b=="$" and c=="$":
            break
        else:
            msg_list.append(rev[i])
    msg_list.reverse() #The correct message is composed reversing it again
    msg = "".join(msg_list)

    #The message is decoded
    decoded = base64.b64decode(msg)
    print("\n\u001b[34m[*]\u001b[0m Succesfully extracted audio file")
    print("\u001b[32m[*]\u001b[0m The hidden text is: "+str(decoded.decode("utf-8"))+"\n")




def encrypt (message, key):

    # Instance the Fernet class with the key
    fernet = Fernet(key)  

    # then use the Fernet class instance 
    # to encrypt the string string must must 
    # be encoded to byte string before encryption
    encMessage = fernet.encrypt(message.encode())
      
    #print("original string: ", message)
    #print("encrypted string: ", encMessage.decode("utf-8"))
    return encMessage

def decrypt (encMessage, key):
    # Instance the Fernet class with the key
    fernet = Fernet(key)
    # decrypt the encrypted string with the 
    # Fernet instance of the key,
    # that was used for encrypting the string
    # encoded byte string is returned by decrypt method,
    # so decode it to string with decode methos
    decMessage = fernet.decrypt(encMessage).decode()
      
    #print("decrypted string: ", decMessage)
    return decMessage

def insert_encryptfernet():
    # Check path
    dirname = os.getcwd()
    original_song_name = dirname + "/resources/" + "The Local Guy - Jump By Van Halen.wav"
    edit_song_name = dirname + "/media/" + "The Local Guy - Jump By Van Halen (stego).wav"

    shutil.copy(original_song_name, edit_song_name)

    #Open the file
    song_open = open(edit_song_name, 'a')
    
    #User input the secret and password
    print("\n\u001b[33m[!]\u001b[0m Tell me your secret: ", end='')
    secret = input()
    key = Fernet.generate_key()
    print("\n\u001b[36m[*]\u001b[0m The key is: "+str(key.decode("utf-8")))
    print("\t*Please share it with the receiver")

    #encrypted message generated
    encMessage = encrypt (secret, key)

    #This will be the characters used to detect the secret later
    detect_final="$$$"

    #Write the message at the end of the file
    song_open.write(detect_final + encMessage.decode("utf-8"))

    print("\n\u001b[34m[*]\u001b[0m Original string: "+secret)
    print("\u001b[34m[*]\u001b[0m Encoded string: "+encMessage.decode("utf-8")+"\n")
    song_open.close()

def insert_decryptfernet():
    # Check path
    dirname = os.getcwd()
    song_name = dirname + "/media/" + "The Local Guy - Jump By Van Halen (stego).wav"

    #Open the file and read all the lines
    song_open = io.open(song_name,'r', encoding="cp437").readlines()

    #The message is in the last line
    last_line = song_open[len(song_open) - 1]
    rev = last_line[::-1]

    #Read the last line and get the message
    msg_list = []
    i=0
    for i in range(len(rev)): #The message is at the end, so it's easier to read it reversed
        a=rev[i]
        b=rev[i+1]
        c=rev[i+2]
        if a=="$" and b=="$" and c=="$":
            break
        else:
            msg_list.append(rev[i])
            
    msg_list.reverse() #The correct message is composed reversing it again
    encMessage = str("".join(msg_list))
    
    print("\n\u001b[33m[!]\u001b[0m Please insert the key: ", end='')
    key = input()
    message = decrypt(encMessage.encode(), key)
    print("\n\u001b[34m[*]\u001b[0m Succesfully extracted audio file")
    print("\u001b[32m[*]\u001b[0m The hidden text is: "+ message)


def options():

    while True:
        print ("""\nChoose the option:
    \u001b[33m[a] Generate audio stego using base64\u001b[0m
    \u001b[33m[b] Generate audio stego using Fernet\u001b[0m
    \u001b[33m[c] Extract base64 from audio stego\u001b[0m
    \u001b[33m[d] Extract Fernet from audio stego\u001b[0m
    [e] Exit""")
        
        option = input("Please select an option: ")
      
        if option == "a":
            insert_encryptb64()
        elif option == "b":
            insert_encryptfernet()
        elif option == "c":
            insert_decryptb64()
        elif option == "d":
            insert_decryptfernet()
        elif option == "e":
            break
        else:
            print ("Please select a valid option")