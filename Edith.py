from Brain.AIbrain import ReplyBrain
from Body.Listener import MicExecution
print("Edith starting please wait")
from Body.speaker import speak
from Features.Clap import Tester

def MainExecution():
    speak("Hello boos how can i help you")
    while True:
        data = MicExecution()
        data = str(data)
        reply = ReplyBrain(data)
        speak(reply)
        
def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        print("")
        print("Clap Detect")
        print("")
        MainExecution()
    else:
        pass
    
    
ClapDetect()