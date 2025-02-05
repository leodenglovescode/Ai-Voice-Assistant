import google.generativeai as genai
import speech_recognition as sr
import time
import os

#Config
#Initialize the AI API key
genai.configure(api_key="YOUR_API_KEY")
#Intialize the Generative Model
model = genai.GenerativeModel("gemini-1.5-flash")
# Initialize voice recognition
r = sr.Recognizer()


def voice_recognition():
    with sr.Microphone() as source:
        print("Listening...")
        audio_text = r.listen(source)
        print("Finished listening...\n\n\n")
        try:
            print("Text: "+r.recognize_google(audio_text))
            print("Processing...")
            chat = str(r.recognize_google(audio_text))
            response = model.generate_content(chat)
            print(response.text)
            entertocontinue = input("Press Enter to Continue...")
            
        except:
            print("Sorry, I did not get that")
            entertocontinue = input("Press Enter to Continue...")
            
            
def text_input():
    chat = input("Please Input Your Prompt Here >>>")
    response = model.generate_content(chat)
    print(response.text)

os.system("clear")            
print("AiAssistant v1.0\nMade By: Leodeng (with code from google)\nPowered by Gemini-1.5-flash (Support for ChatGPT, DeepSeek, and Anthropic coming up...)")
print("\n\nType '1' for text input and '2' for voice input")
choice = input(">>>")
if choice == '1':
    os.system("clear")
    text_input()
elif choice == '2':
    os.system("clear")
    while True:
        voice_recognition()
print("\n\nPress Ctrl+C to exit this Program...")












