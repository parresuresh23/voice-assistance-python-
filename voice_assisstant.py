import pyttsx3
import speech_recognition as sr
import datetime
import pyjokes
import webbrowser
import pyaudio
def sptext():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.adjust_for_ambient_noise(source)
        audio =r.listen(source)
        try:
            print("recognizing.....")
            data =r.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("not understand")    

def speech(x):
    engine =pyttsx3.init()
    voices =engine.getProperty("voices")
    engine.setProperty('voice',voices[1].id)
    rate =engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()




if __name__=='__main__':
    if sptext()== "hai suresh":
        

        data1 = sptext()
        if " what is your name" in data1:
            name ="my name is suresh"
            sptext(name)

        elif "how old are you" in data1:
            age ="i am twenty five years old"
            sptext(age)

        elif "time now" in data1:
            time =datetime.datetime.now().strftime("%I%M%p")
            speech(time)


        elif "youtube" in data1:
            webbrowser.open("https://www.youtube.com/")


        elif "jock" in data1:
            joke1=pyjokes.get_joke(language="en",category="neutral")
            print(jock1)

            sptext(jock1)


        






    else:

        print("thank you")



    


