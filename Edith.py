from Brain.AIbrain import ReplyBrain
from Body.Listener import MicExecution
from Features.Wakeup import WakeupDetected
from Body.speaker import speak

def MainExecution():
    speak("Hello boss how can i help you")
    while True:
        data = MicExecution()
        data = str(data)
        reply = ReplyBrain(data)
        speak(reply)
        
def unlock():
    query = WakeupDetected()
    if "True-Mic" in query:
        print("")
        print("Edith ready")
        print("")
        MainExecution()
    else:
        pass
    
unlock()
