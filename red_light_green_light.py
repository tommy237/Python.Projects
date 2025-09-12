# import PySimpleGUI as simp
from time import sleep as wait

def message(text:str,delay:int|float):
    print(text)
    wait(delay)

def main():
    while(True):
        message(text="Currently in progress.\nCome back later to re-test.",delay=5)