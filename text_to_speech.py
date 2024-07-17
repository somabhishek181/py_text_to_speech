import pyttsx3

def arr_of_word_list():
    with open("text_to_speech.txt", "r") as Word_list:
        lines = Word_list.read().split(',')
    return lines 

engine = pyttsx3.init()
lines = arr_of_word_list()
engine.say(lines)
engine.runAndWait()
