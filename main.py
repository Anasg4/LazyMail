import smtplib
from email.message import EmailMessage
import speech_recognition as sr
import pyttsx3
import sys


def bio():
    linknew = open("Sender.txt", "r")
    link = linknew.read().split('\n')
    return link

def commandbot():
    try:
        with sr.Microphone() as source:
            voice = listen.listen(source)
            command = listen.recognize_google(voice, language=lang)
            command = command.lower()
            return command
    except:
        pass


def email():
    done = False
    while not done:
        try:
            print("\nsend email to")
            pyttsx3.speak("Send your email to ? " )
            talk = commandbot()
            print(talk)
            target = email_list[talk]
            print(f"Your target {target}")
            print("="*20)
            print("What is your subject ")
            pyttsx3.speak("What is your subject ? ")
            subject = commandbot()
            print(f"Your subject is  {subject}")
            print("=" * 20)
            print("Tell me the text")
            pyttsx3.speak("Tell me the text for your email ")
            text = commandbot()
            print(f"Your text is >> {text}")
            send(target,subject,text)
            break
        except:
            print("="*20,"\nSuara tidak terdeteksi, silahkan cek mic anda\nCant detect your voice, pls check your mic\n")
            pyttsx3.speak("Voice isn't detected, please check your mic ")


def send(target,subject,text):
    email = EmailMessage()
    email['from'] = gmail_user
    email['To'] = target
    email['Subject'] = subject
    email.set_content(text)
    server.send_message(email)


def target():
    d = {}
    with open("Receiver.txt") as f:
        for line in f:
            (key, val) = line.split()
            d[(key)] = val
        return d

if __name__=="__main__":
    listen = sr.Recognizer()
    print("""
 _                    ___  ___      _ _ 
| |                   |  \/  |     (_) |
| |     __ _ _____   _| .  . | __ _ _| |
| |    / _` |_  / | | | |\/| |/ _` | | |
| |___| (_| |/ /| |_| | |  | | (_| | | |
\_____/\__,_/___|\__, \_|  |_/\__,_|_|_|
                  __/ |                 
                 |___/                  
    """)
    print("Use Your Voice For Send Email\nAuthor : github.com/Anasg4\n")
    a = int(input("Choose your speak language: \n1. Indonesia\n2. English\n Answer with number >> "))
    if a ==1:
        lang = "id"
    else:
        lang = "en-US"
    target()
    bio()
    tes = bio()
    gmail_user = tes[0]
    gmail_password = tes[1]
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
    except:
        print ('Error , make sure your email and password in Sender.txt was right or your gmail less secure apps activated , for more info  >>> https://myaccount.google.com/lesssecureapps ')

    email_list = target()
    print("Receiver list\n",email_list)
    email()
    print("Email Sent")
    ask = input("Again ??? y/n >> ")
    if ask == "y":
        email()
    else:
        sys.exit()