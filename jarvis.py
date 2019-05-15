import pyttsx3, datetime, speech_recognition as sr, wikipedia, webbrowser, os,random, smtplib, ctypes,platform
import subprocess


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]


def wifi():
    for i in profiles:
      results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
      results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print ("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(i, ""))


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Master Asim! ")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon Master Asim!")
    else:
        speak("Good Evening Master Asim!")

    speak("This is your virtual assistance, ATP. Please tell me how can i help you sir ?")
    

def takeInput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining.........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Rocognizing Voice........")
        query = r.recognize_google(audio, language="en-in")
        print(f"Sir you said : {query}\n")
    except Exception as e:
        print(e)
        print("Please Say that again Sir.....")
        return "None"
    return query


#def sendEmail(to,content):
#   server = smtplib.SMTP("mail.asimpathak.com.np",465)
#    server.ehlo()
#    server.starttls() we can also use text file for password for security reason and use path instead of password
#    server.login("your login@emailid.com","password")
#    server.sendmail("your sending mail identity i.e your email address",to,content)
#    server.close()



if __name__ == "__main__":
    speak(" Welcome To The System Master Asim")

    while True:
      query = takeInput().lower()
      
      if "wikipedia" in query:
          speak("Searching information on Wikipedia.....")
          query = query.replace("wikipedia","")
          results = wikipedia.summary(query,sentences=2)
          print("Speaking........\n")
          speak("Sir, According to Wikipedia")
          print(results)
          speak(results)

      elif "open youtube" in query:
         webbrowser.open("youtube.com")

      elif "open facebook" in query:
         webbrowser.open("facebook.com")

      elif "open instagram" in query:
         webbrowser.open("instagram.com")

      elif "open twitter" in query:
         webbrowser.open("twitter.com")

      elif "open google" in query:
         webbrowser.open("google.com")

      elif "homepage" in query:
         webbrowser.open("asimpathak.com.np")

      elif "home page" in query:
         webbrowser.open("asimpathak.com.np")

      elif "watch movie" in query:
         webbrowser.open("watchonlinemovies.com.pk")

      elif "debug" in query:
         webbrowser.open("stackoverflow.com")

      elif "online course" in query:
         webbrowser.open("udemy.com")

      elif "music" in query:
          music_dir = "E:\\Musics\\"
          select = random.randint(0,396)
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir,songs[select]))
      
      elif "song" in query:
          music_dir = "E:\\Musics\\"
          select = random.randint(0,396)
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir,songs[select]))

      elif "time" in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"Sir, the time is {strTime}")

      elif "watch video" in query:
          webbrowser.open("watchonlinemovies.com.pk")

      elif "powerpoint" in query:
          path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\PowerPoint 2013.lnk"
          os.startfile(path)

      elif "power point" in query:
          path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\PowerPoint 2013.lnk"
          os.startfile(path)

      elif "presentation" in query:
          path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\PowerPoint 2013.lnk"
          os.startfile(path)

      elif "slides" in query:
          path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\PowerPoint 2013.lnk"
          os.startfile(path)

      elif "document" in query:
          path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013.lnk"
          os.startfile(path)

      elif "excel" in query:
          path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Excel 2013.lnk"
          os.startfile(path)

      elif "data entry" in query:
          path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Excel 2013.lnk"
          os.startfile(path)

      elif "opera" in query:
         path="C:\\Program Files\\Opera\\launcher.exe"
         os.startfile(path)

      elif "browser" in query:
         path="C:\\Program Files\\Opera\\launcher.exe"
         os.startfile(path)

      elif "internet" in query:
         path="C:\\Program Files\\Opera\\launcher.exe"
         os.startfile(path)

      elif "virtual machine" in query:
          path="C:\\Program Files (x86)\\VMware\\VMware Player\\vmplayer.exe"
          os.startfile(path)

      elif "os" in query:
          path="C:\\Program Files (x86)\\VMware\\VMware Player\\vmplayer.exe"
          os.startfile(path)

      elif "remix" in query:
          path="C:\\Program Files (x86)\\Audacity\\audacity.exe"
          os.startfile(path)

      elif "my mobile driver" in query:
          path="C:\\Program Files (x86)\\HiSuite\\HiSuite.exe"
          os.startfile(path)

      elif "i fun box" in query:
          path="C:\\Program Files (x86)\\i-Funbox DevTeam\\iFunBox.exe"
          os.startfile(path)

      elif "iphone driver" in query:
          path="C:\\Program Files\\iTunes\\iTunes.exe"
          os.startfile(path)

      elif "java" in query:
          path="C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2018.2.2\\bin\\idea64.exe"
          os.startfile(path)

      elif "java programming" in query:
          path="C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2018.2.2\\bin\\idea64.exe"
          os.startfile(path)

      elif "python programming" in query:
          path="C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2018.2.2\\bin\\idea64.exe"
          os.startfile(path)

      elif "virus scan" in query:
          path="C:\\Program Files (x86)\\K7 Computing\\K7TSecurity\\K7TSMain.exe"
          os.startfile(path) 

      elif "antivirus" in query:
          path="C:\\Program Files (x86)\\K7 Computing\\K7TSecurity\\K7TSMain.exe"
          os.startfile(path) 

      elif "k7" in query:
          path="C:\\Program Files (x86)\\K7 Computing\\K7TSecurity\\K7TSMain.exe"
          os.startfile(path)

      elif "notepad" in query:
          path="C:\\Program Files\\Notepad++\\notepad++.exe"
          os.startfile(path)

      elif "transfer file" in query:
          path="C:\\Program Files (x86)\\SHAREit Technologies\\SHAREit\\SHAREit.exe"
          os.startfile(path)

      elif "share file" in query:
          path="C:\\Program Files (x86)\\SHAREit Technologies\\SHAREit\\SHAREit.exe"
          os.startfile(path)

      elif "text editor" in query:
          path="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
          os.startfile(path)

      elif "swastik" in query:
          path="C:\\Program Files (x86)\\Swastik\\Swastik.exe"
          os.startfile(path)

      elif "remote connect" in query:
          path="C:\\Program Files (x86)\\UltraViewer\\UltraViewer_Desktop.exe"
          os.startfile(path)

      elif "remote pc" in query:
          path="C:\\Program Files (x86)\\UltraViewer\\UltraViewer_Desktop.exe"
          os.startfile(path)

      elif "connect pc" in query:
          path="C:\\Program Files (x86)\\UltraViewer\\UltraViewer_Desktop.exe"
          os.startfile(path)

      elif "ultraviewer" in query:
          path="C:\\Program Files (x86)\\UltraViewer\\UltraViewer_Desktop.exe"
          os.startfile(path)

      elif "vs code" in query:
          path="C:\\Users\\Pathak\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          os.startfile(path)

      elif "visual code" in query:
          path="C:\\Users\\Pathak\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          os.startfile(path)

      elif "hello" in query:
           wishMe()

      elif "hi" in query:
           wishMe()

      elif "what's up" in query:
           wishMe()

      elif "hey" in query:
           wishMe()

      elif "who" in query:
          print("Searching.....")
          speak("Searching")
          webbrowser.open(f"https://www.google.com/search?client=opera&q={query}")

      elif "which" in query:
          print("Searching.....")
          speak("Searching")
          webbrowser.open(f"https://www.google.com/search?client=opera&q={query}")

      elif "what" in query:
          print("Searching.....")
          speak("Searching")
          webbrowser.open(f"https://www.google.com/search?client=opera&q={query}")

      elif "how" in query:
          print("Searching.....")
          speak("Searching")
          webbrowser.open(f"https://www.google.com/search?client=opera&q={query}")

      elif "why" in query:
          print("Searching.....")
          speak("Searching")
          webbrowser.open(f"https://www.google.com/search?client=opera&q={query}")

      elif "search" in query:
          print("Searching.....")
          speak("Searching")
          webbrowser.open(f"https://www.google.com/search?client=opera&q={query}")

      elif "exit" in query:
          print("Good bye sir, Have a good day!")
          speak("Good bye Sir, Have a good day!")
          exit()

      elif "bye" in query:
          print("Good bye sir, Have a good day!")
          speak("Good bye Sir, Have a good day!")
          exit()

      elif "goodbye" in query:
          print("Good bye sir, Have a good day!")
          speak("Good bye Sir, Have a good day!")
          exit()

      elif "have a break" in query:
          print("Good bye sir, Have a good day!")
          speak("Good bye Sir, Have a good day!")
          exit()

      elif "turnoff yourself" in query:
          print("Good bye sir, Have a good day!")
          speak("Good bye Sir, Have a good day!")
          exit()

      elif "shutdown yourself" in query:
          print("Good bye sir, Have a good day!")
          speak("Good bye Sir, Have a good day!")
          exit()

      elif "do a greeting" in query:
          print("Hello Sir !")
          speak("Hello Sir !")

      elif "type" in query:
          print("Sure Sir, as your Wish!")
          speak("Sure Sir, as your Wish!")
          print(query)

      elif "thank you" in query:
          print("You're extremly Welcome Sir. Good to hear this.")
          speak("You're extremly Welcome Sir. Good to hear this.")

      elif "okey" in query:
          print("Got it Sir !")
          speak("Got it Sir !")

      elif "okay" in query:
          print("Got it Sir !")
          speak("Got it Sir !")
        
      elif "ok" in query:
          print("Got it Sir !")
          speak("Got it Sir !")

      elif "logout system" in query:
          speak("Are you Sure Sir, Do you want to Log Out the System ?")
          choice = takeInput().lower()

          if "yes" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
          elif "s" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
          elif "yeah" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
          elif "yup" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
          else:
              print("Oops! Sorry Sir, continuing the system....")
              speak("Oops! Sorry Sir, continuing the system....")
              continue

      elif "log out system" in query:
          speak("Are you Sure Sir, Do you want to Log Out the System ?")
          choice = takeInput().lower()

          if "yes" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
          elif "s" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
          elif "yeah" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
          elif "yup" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
          else:
              print("Oops! Sorry Sir, continuing the system....")
              speak("Oops! Sorry Sir, continuing the system....")
              continue

      elif "logout from the system" in query:
          speak("Are you Sure Sir, Do you want to Log Out the System ?")
          choice = takeInput().lower()

          if "yes" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
          elif "s" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
          elif "yeah" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
          elif "yup" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
          else:
              print("Oops! Sorry Sir, continuing the system....")
              speak("Oops! Sorry Sir, continuing the system....")
              continue

      elif "introduce" in query:
          print("Hello! I am ATP , Virtual Assistance of Asim Tara Pathak.")
          speak("Hello! I am ATP , Virtual Assistance of Asim Tara Pathak.")
          print(f"OS Type {platform.system()}")
          speak(f"OS Type {platform.system()}")
          print(f"Platform {platform.platform()}")
          speak(f"Platform {platform.platform()}")
          print(f"OS Version {platform.version()}")
          speak(f"OS Version {platform.version()}")
          print(f"Processor {platform.processor()}")
          speak(f"Processor {platform.processor()}")
          print(f"Processor Architecture {platform.architecture()}")
          speak(f"Processor Architecture {platform.architecture()}") 
          print("RAM 4 Giga bytes")
          speak("RAM 4 Giga bytes")
          print("Hard Disk 1 Tera Bytes")
          speak("Hard Disk 1 Tera Bytes")
          print(f"Machine Type {platform.machine()}")
          speak(f"Machine Type {platform.machine()}") 
         #print(f"Desktop Name {platform.uname()}")
         #speak(f"Desktop Name {platform.uname()}")
          print("That's it Sir !")
          speak("That's it Sir !")

      elif "introduction" in query:
          print("Hello! I am ATP , Virtual Assistance of Asim Tara Pathak.")
          speak("Hello! I am ATP , Virtual Assistance of Asim Tara Pathak.")
          print(f"OS Type {platform.system()}")
          speak(f"OS Type {platform.system()}")
          print(f"Platform {platform.platform()}")
          speak(f"Platform {platform.platform()}")
          print(f"OS Version {platform.version()}")
          speak(f"OS Version {platform.version()}")
          print(f"Processor {platform.processor()}")
          speak(f"Processor {platform.processor()}")
          print(f"Processor Architecture {platform.architecture()}")
          speak(f"Processor Architecture {platform.architecture()}") 
          print("RAM 4 Giga bytes")
          speak("RAM 4 Giga bytes")
          print("Hard Disk 1 Tera Bytes")
          speak("Hard Disk 1 Tera Bytes")
          print(f"Machine Type {platform.machine()}")
          speak(f"Machine Type {platform.machine()}") 
         #print(f"Desktop Name {platform.uname()}")
         #speak(f"Desktop Name {platform.uname()}")
          print("That's it Sir !")
          speak("That's it Sir !")

      
      elif "shutdown computer" in query:
          speak("Are you Sure Sir, Do you want to Shut Down the System ?")
          choice = takeInput().lower()

          if "yes" in choice:
                print("As your Wish Sir !. Shutting down the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Shutting down System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /s /t 1")
                exit()
          elif "s" in choice:
                print("As your Wish Sir !. Shutting down the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Shutting down System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /s /t 1")
                exit()
          elif "yeah" in choice:
                print("As your Wish Sir !. Shutting down the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Shutting down System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /s /t 1")
                exit()
          elif "yup" in choice:
                print("As your Wish Sir !. Shutting down the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Shutting down System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /s /t 1")
                exit()
          else:
              print("Oops! Sorry Sir, continuing the system....")
              speak("Oops! Sorry Sir, continuing the system....")
              continue

      elif "shutdown system" in query:
          speak("Are you Sure Sir, Do you want to Shut Down the System ?")
          choice = takeInput().lower()

          if "yes" in choice:
                print("As your Wish Sir !. Shutting down the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Shutting down System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /s /t 1")
                exit()
          elif "s" in choice:
                print("As your Wish Sir !. Shutting down the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Shutting down System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /s /t 1")
                exit()
          elif "yeah" in choice:
                print("As your Wish Sir !. Shutting down the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Shutting down System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /s /t 1")
                exit()
          elif "yup" in choice:
                print("As your Wish Sir !. Shutting down the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Shutting down System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /s /t 1")
                exit()
          else:
              print("Oops! Sorry Sir, continuing the system....")
              speak("Oops! Sorry Sir, continuing the system....")
              continue

      elif "restart system" in query:
          speak("Are you Sure Sir, Do you want to Restart the System ?")
          choice = takeInput().lower()

          if "yes" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
          elif "s" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
          elif "yeah" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
          elif "yup" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
          else:
              print("Oops! Sorry Sir, continuing the system....")
              speak("Oops! Sorry Sir, continuing the system....")
              continue

        
      elif "restart computer" in query:
          speak("Are you Sure Sir, Do you want to Restart the System ?")
          choice = takeInput().lower()

          if "yes" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
          elif "s" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
          elif "yeah" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
          elif "yup" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
          else:
              print("Oops! Sorry Sir, continuing the system....")
              speak("Oops! Sorry Sir, continuing the system....")
              continue

      elif "reboot system" in query:
          speak("Are you Sure Sir, Do you want to Restart the System ?")
          choice = takeInput().lower()

          if "yes" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
          elif "s" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
          elif "yeah" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
          elif "yup" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
          else:
              print("Oops! Sorry Sir, continuing the system....")
              speak("Oops! Sorry Sir, continuing the system....")
              continue

      elif "say" in query:
          speak(query)

      elif "wi-fi password" in query:
          speak(wifi())
 

      elif "email" in query:
          print("Sorry Sir, Due to Security Reason I am Unable to send this email at the Moment !")
          speak("Sorry Sir, Due to Security Reason I am Unable to send this email at the Moment !")
 #         try:
 #             speak("What should i say sir ?")
 #             content = takeInput()
 #             to = "destination email address"
 #             sendEmail(to,content)
 #             speak(f"Sir, Email has been sent! to {to}")
 #         except Exception as e:
 #             print(e)
 #             speak("Sorry Sir, I am Unable to send this email at the moment!")


 #     End Line of The Project