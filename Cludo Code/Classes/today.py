from datetime import date
import pyttsx3
import speech_recognition
import pyaudio

today = date.today()
d2 = today.strftime("%B %d, %Y")
print(d2)

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
while True:
    with speech_recognition.Microphone() as mic:
        print("I'm listening")
        audio = robot_ear.listen(mic)
    print("Robot: ...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you == ""
    print(you)

    if "Hello" in you:
        robot_brain = "Hi"
    elif "What's your name?" in you:
        robot_brain = "My name is Cluedo"
    # elif "bye" in you:
    #     robot_brain == " Good buy"
    #     print(robot_brain)
    #     robot_mouth.say(robot_brain)
    #     robot_mouth.runAndWait()
    #     break
    else:
        robot_brain = "I don't understand what you say"
    print(robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
