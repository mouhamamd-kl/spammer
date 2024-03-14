import sys
import time
from ahk import AHK
import re
# Initialize the AHK object
ahk = AHK()

running = True
def getText(text):
    print("the function gex text")
    # match = re.search(r'spam:(\d+) (\w+)', text)
    # match = re.search(r'spam:\s*(\d+)\s+(\w+)', text, re.IGNORECASE)
    # match = re.search(r'spam:(\d+) ([^ ]+)', text)
    match = re.search(r'spam:(\d+) (.*)', text)


    if match:
        number = match.group(1)
        word = match.group(2)
        print(f"Number: {number}, Word: {word} from get text")
        return number,word;
    else:
        return 0,"";

 

def spam():
    global running
    number,word=convert_to_arabic()
    print("the text:",word," the number:",number,"from spam")

    if(word!=""and int(number)>0):
        i = 1
        while running and i <=int(number):
            ahk.send(word)
            time.sleep(0.2)
            ahk.key_press('Enter')
            i += 1

def stop_process():
    global running
    running = False

def convert_to_arabic():
    clipboardOld=ahk.get_clipboard_all()
    ahk.send("^c")
    clipboardNew = ahk.get_clipboard_all()            
    if (clipboardNew != clipboardOld):
        text = ahk.get_clipboard()       
        ahk.set_clipboard("")
    else:
        ahk.send("{Home}")
        ahk.send("+{End}")
        ahk.send("^c")
        text=ahk.get_clipboard()
        ahk.set_clipboard("")
    if (clipboardOld):  # Check if clipboardOld is not empty
            # Use set_clipboard for text, ensure clipboardOld is a string
        ahk.set_clipboard_all((clipboardOld)) 
    number,text= getText(text)    
    print(f"Number: {number}, Word: {text} from translate")
    return number,text


# Add hotkeys
ahk.add_hotkey('!s', callback=spam)
ahk.add_hotkey('!q', callback=stop_process) # Ensure this is correctly set up

# Start the hotkey process thread
ahk.start_hotkeys()

# Block forever to keep the script running
ahk.block_forever()
