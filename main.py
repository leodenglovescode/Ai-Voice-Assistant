# Imports
import google.generativeai as genai
import speech_recognition as sr
from openai import OpenAI


import os
import json



# Define ALL Functions
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
    os.system("clear")
    chat = input("Please Input Your Prompt Here >>>")
    response = model.generate_content(chat)
    print(response.text)
    
def Settings(): 
    os.system("clear")
    print("Settings")
    print("1. Set API Keys")
    print("2. Change Model")
    print("3. Exit")
    choice = input(">>>")
    if choice == '1':
        os.system("clear")
        print("Please Input Your API Key Here >>>")
        api_key = input(">>>")
        genai.configure(api_key=api_key)
        


        
        
        
        
        
# Main Program


# Write config if not already written
cfg_exists = str(os.path.isfile("./config/cfg.json"))
if cfg_exists == "True":
    pass

elif cfg_exists == "False":
    os.system("clear")
    print("Config File Not Found. Creating...\n\n")
    print("Please Input Your OpenAI API Key Here (Skip if none)")
    openaiapi_key = str(input(">>>"))
    #print("Please Input Your Deepseek Key Here (Skip if none)")
    #deepseekapi_key = input(">>>")
    print("Please Input Your Gemini API Key Here (Skip if none)")
    geminiapi_key = str(input(">>>"))
    #print("Please Input Your Anthropic Key Here (Skip if none)")
    #anthropicapi_key = input(">>>")
    
    dictionary = {
    #"newfile?" : "",
    "OpenAI_APIKEY": openaiapi_key,
    "Gemini_APIKEY": geminiapi_key
    #"DeepSeek_APIKEY": "",
    #"Anthropic_APIKEY": ""
    }
    
    json_object = json.dumps(dictionary, indent=4)
    
    with open("./config/cfg.json", "w") as outfile:
        outfile.write(json_object)
    
    


    
    
        
    
    




# Configuration Settings

with open('./config/cfg.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)
 
#print(json_object)
#print(type(json_object))
openai_api_key = json_object['OpenAI_APIKEY']
gemini_api_key = json_object['Gemini_APIKEY']
    
# Initialize the Google AI API key
genai.configure(api_key=gemini_api_key)
# Intialize the Generative Model
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize the OpenAI API key
client = OpenAI(api_key=openai_api_key)

# Initialize voice recognition
r = sr.Recognizer()    
    
    
    
    
os.system("clear")            
print("AiAssistant v1.0\nMade By: Leodeng (with code from google)\nPowered by Gemini-1.5-flash (Support for ChatGPT, DeepSeek, and Anthropic coming up...)")
print("\n\nType '1' for text input,  '2' for voice input, and '3' for settings.")
choice = input(">>>")
if choice == '1':
    text_input()
elif choice == '2':
    os.system("clear")
    while True:
        voice_recognition()
elif choice == '3':
    Settings()
print("\n\nPress Ctrl+C to exit this Program...")












