from tkinter import*
from gpiozero import LED
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
LED = LED(16)
win = Tk()
l1=Label(win, text= "Enter the comment below") 
l1.grid(row=1, column=1) 
win.geometry("400x150")
win.title("Text to Morse code")




def MorsecodeBlink(Input):
    for letter in Input:
        if(letter=='a'):
            dot()
            dash()
            
        elif(letter=='b'):
            dash()
            dot()
            dot() 
            dot()

        elif(letter == 'c') :
            dash()
            dot()
            dash()
            dot()

        elif (letter == 'd'):
            dash()
            dot()
            dot()

        elif (letter == 'e'):
            dot()
        
        elif (letter == 'f'):
            dot()
            dot()
            dash()
            dot()
            
        elif (letter == 'g'):
            dash()
            dash()
            dot()
            
        elif (letter == 'h'):
            dot()
            dot()
            dot()
            dot()
            
        elif (letter == 'i'):
            dot()
            dot()
            
        elif (letter == 'j'):
            dot()
            dash()
            dash()
            dash()
            
        elif (letter == 'k'):
            dash()
            dot()
            dash()
            
        elif (letter == 'l'):
            dot()
            dash()
            dot()
            dot()
            
        elif (letter == 'm'):
            dash()
            dash()
            
        elif (letter == 'n'):
            dash()
            dot()
            
        elif (letter == 'o'):
            dash()
            dash()
            dash()
            
        elif (letter == 'p'):
            dot()
            dash()
            dash()
            dot()
            
        elif (letter == 'q'):
            dash()
            dash()
            dot()
            dash()

        elif (letter == 'r'):
            dot()
            dash()
            dot()
            
        elif (letter == 's'):
            dot()
            dot()
            dot()
            
        elif (letter == 't'):
            dash()
        
        elif (letter == 'u'):
            dot()
            dot()
            dash()
            
        elif (letter == 'v'):
            dot()
            dot()
            dot()
            dash()
            
        elif (letter == 'w'):
            dot()
            dash()
            dash()
            
        elif (letter == 'x'):
            dash()
            dot()
            dot()
            dash()
            
        elif (letter == 'y'):
            dash()
            dot()
            dash()
            dash()
            
        elif (letter == 'z'):
            dash()
            dash()
            dot()
            dot()
    
    
def dot():
    LED.on()
    time.sleep(0.3)
    LED.off()
    time.sleep(0.3)

def dash():
    LED.on()
    time.sleep(0.9)
    LED.off()
    time.sleep(0.3)
    
def enter():
    input=text_box.get("1.0", "end-1c")
    i=1
    for c in input:
        if(i>12):
            break
        print(c, end="")
        MorsecodeBlink(input)

    
text_box = Text(win, height=3, width=25, bg='white', font='Arial')
text_box.grid(row=2, column=1, padx=16, pady=12)

    
enter = Button(win, text="Enter", command=enter, bg='green3',fg='white', font='Arial', height=2, width = 8)
enter.grid(row=2, column=3, padx=12, pady=6)

win.mainloop()










