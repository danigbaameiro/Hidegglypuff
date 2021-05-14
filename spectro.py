#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
from cryptography.fernet import Fernet
import wave, math, array, sys, timeit, os, subprocess, contextlib
import moviepy.editor as mpe
import global_variables as g

#Function to retrieve duration of the audio
#Based on the piece of code available at: https://stackoverflow.com/questions/7833807/get-wav-file-length-or-duration
def lenghtAudio(fname):
    with contextlib.closing(wave.open(fname,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration

def video_stego():
    audio_stego()
    dirname = os.getcwd()
    gif_filename = dirname + "/resources/"+g.filename_mp4
    wav_filename = dirname + "/media/out.wav"
    avi_filename = dirname + "/media/antena.avi"
    
    my_clip = mpe.VideoFileClip(gif_filename)
    my_clip.set_duration(lenghtAudio(wav_filename)).write_videofile(avi_filename, fps=25, audio=wav_filename, codec="rawvideo")

    #Remove audio with secret
    os.remove(wav_filename)
    
def video_stego_extraction():
    print("\t*Please remember that the video should be in AVI format and the output file will be in WAV format")
    videoPath = input("\u001b[33m[!]\u001b[0m Please insert the path of the video: ")
    command = "ffmpeg -i "+ videoPath +" -ab 160k -ac 2 -ar 44100 -vn audio.wav"
    subprocess.call(command, shell=True)
    print("\n\u001b[34m[*]\u001b[0m Succesfully extracted audio file")

def retrieve_message():
    print("\n\u001b[33m[!]\u001b[0m Please insert the encrypted text: ", end='')
    encMessage = input()
    print("\u001b[33m[!]\u001b[0m Please insert the key: ", end='')
    key = input()
    message = decrypt(encMessage.encode(), key)
    print("\n\u001b[34m[*]\u001b[0m Succesfully extracted audio file")
    print("\u001b[32m[*]\u001b[0m The hidden text is: "+ message)
    

def audio_stego():
    dirname = os.getcwd()

    #Values of the generate audio file
    minfreq = 200
    maxfreq = 20000
    wavrate = 44100
    pxs     = 30
    output  = dirname+"/media/"+"out.wav"
    rotate  = False
    invert  = False

    
    #User input the secret and password
    print("\n\u001b[33m[!]\u001b[0m Tell me your secret: ", end='')
    secret = input()
    key = Fernet.generate_key()
    print("\n\u001b[36m[*]\u001b[0m The key is: "+key.decode("utf-8"))
    print("\t*Please share it with the receiver")

    #encrypted message generated
    encMessage = encrypt (secret, key)
    encMessage = encMessage.decode("utf-8")

    #Generate image that will display the secret
    #Since the lenght of user's input can be variable, image lenght will be eight times the encryption message
    img = Image.new('RGB', (len(encMessage)*8,100), color = (255, 255, 255))

    #Use Arial font with letter size of 11
    font_path = dirname+"/fonts/arial.ttf"
    fnt = ImageFont.truetype(font_path, 11)

    #Drawing the secret into the image
    d = ImageDraw.Draw(img)
    d.text((10,10), encMessage, font=fnt,  fill=(0,0,0))
    
    #Generate image with the secret
    bmp_filename = dirname + "/tmp/secret.bmp"
    img.save(bmp_filename)   

    #Returns a converted copy of the image interpreted as greyscale
    imagen = Image.open(bmp_filename).convert('L')

    #Based on solusipse spectrology script 
    ## Code avaible at: https://github.com/solusipse/spectrology 
    output = wave.open(output, 'w')
    output.setparams((1, 2, wavrate, 0, 'NONE', 'not compressed'))

    freqrange = maxfreq - minfreq
    interval = freqrange / imagen.size[1]

    fpx = wavrate // pxs
    data = array.array('h')

    tm = timeit.default_timer()

    for x in range(imagen.size[0]):
        row = []
        for y in range(imagen.size[1]):
            yinv = imagen.size[1] - y - 1
            amp = imagen.getpixel((x,y))
            if (amp > 0):
                row.append( genwave(yinv * interval + minfreq, amp, fpx, wavrate) )

        for i in range(fpx):
            for j in row:
                try:
                    data[i + x * fpx] += j[i]
                except(IndexError):
                    data.insert(i + x * fpx, j[i])
                except(OverflowError):
                    if j[i] > 0:
                      data[i + x * fpx] = 32767
                    else:
                      data[i + x * fpx] = -32768

        sys.stdout.write("Conversion progress: %d%%   \r" % (float(x) / imagen.size[0]*100) )
        sys.stdout.flush()

    output.writeframes(data.tobytes())
    output.close()

    tms = timeit.default_timer()

    print("\u001b[33m[!]\u001b[0m Conversion progress: 100%")
    print("\u001b[34m[*]\u001b[0m Success. Completed in %d seconds." % int(tms-tm))

    #Remove image with secret
    os.remove(bmp_filename)

def genwave(frequency, amplitude, samples, samplerate):
    cycles = samples * frequency / samplerate
    a = []
    for i in range(samples):
        x = math.sin(float(cycles) * 2 * math.pi * i / float(samples)) * float(amplitude)
        a.append(int(math.floor(x)))
    return a    

def encrypt (message, key):

    # Instance the Fernet class with the key
  
    fernet = Fernet(key)  

    # then use the Fernet class instance 
    # to encrypt the string string must must 
    # be encoded to byte string before encryption
    encMessage = fernet.encrypt(message.encode())
      
    print("\n\u001b[34m[*]\u001b[0m Original string: ", message)
    print("\u001b[34m[*]\u001b[0m Encrypted string: ", encMessage.decode("utf-8"))
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


def options():
    while True:
        print("""\nOptions
    \u001b[33m[a] Generate audio stego\u001b[0m
    \u001b[33m[b] Generate video stego\u001b[0m
    \u001b[33m[c] Extract audio stego from video\u001b[0m
    \u001b[33m[d] Decrypt message\u001b[0m
    [e] Exit""")
    
        option = input("Please select an option: ")

        if option == "a":
            if g.filename_wav == "":
                print("\u001b[31m[!]\u001b[0m This option is only for music files")
            else:
                audio_stego()
        elif option == "b":
            if g.filename_mp4 == "":
                print("\u001b[31m[!]\u001b[0m This option is only for video files")
            else:
                video_stego()
        elif option == "c":
            if g.filename_mp4 == "":
                print("\u001b[31m[!]\u001b[0m This option is only for video files")
            else:
                video_stego_extraction()
        elif option == "d":
            if g.filename_wav == "":
                print("\u001b[31m[!]\u001b[0m This option is only for music files")
            else:
                retrieve_message()
        elif option == "e":
            break
        else:
            print ("Please select a valid option")
