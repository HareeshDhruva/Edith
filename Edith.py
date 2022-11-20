from Brain.AIbrain import ReplyBrain
from Body.Listener import MicExecution
print("starting the Edith")
from Body.Speak import Speak
from Features.Clap import Tester
print("Wait for some time sir")

def MainExecution():
    
    Speak("Hello Boss")
    Speak("iam Edith how can i help you")
    
    while True :
        data =  MicExecution()
        data = str(data)
        reply = ReplyBrain(data)
        Speak(reply)
        
def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        print("")
        print("Clap Detected")
        print("")
        MainExecution()
    else:
        pass
        
ClapDetect()
        

