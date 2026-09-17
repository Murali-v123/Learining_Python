import win32com.client

# Initialize the default Windows voice engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Rate=1
speaker.Volume=50

list=["pradeep","murali","rohith"]
for name in list:
    message=f"shoutout for {name}"
    print(message)
    speaker.speak(message)
