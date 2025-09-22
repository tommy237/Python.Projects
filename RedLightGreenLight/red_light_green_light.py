#### SERVICES
# this project uses Python's tk-inter package
# to create the main user interface for the program.
import tkinter as tk
from time import sleep as wait

round=0

#### FUNCTIONS
def message(text:str,delay:int|float):
    print(text)
    wait(delay)

def begin_program():
    print("Starting")

def setupWindow():
    root=tk.Tk()

    root.geometry("500x500")
    root.title("")
    
    title=tk.Label(root,text="RED LIGHT GREEN LIGHT",font=("Arial",6))
    title.pack(padx=20,pady=10)

    frame=tk.Frame(root,)

    bt1=tk.Button(frame,text="begin",font=("Arial",15))
    bt1.config(command=begin_program)
    bt1.pack(pady=1)

    root.mainloop()
    return root

def main():
    webs=setupWindow()
    # while(True):
    #     message(text="Currently in progress.\nCome back later to re-test.",delay=5)

main()