'''
Created on Jun 8, 2014

@author: tbanda
'''
#from tkinter import *
import sys

print (sys.version)

# class MyFrame(tkinter.Frame):
# 
#     def __init__(self):
#         """ 
#         Places the controls onto the Frame. 
#         """
#         tkinter.Frame.__init__(self)   # initializes the superclass
#         self.pack()   #  required in order for the Buttons to show up properly
# 
#         #set up the increment Button
#         self.incrementButton = tkinter.Button(self)   
#         self.incrementButton["text"] = "Increment"
#         self.incrementButton.pack({"side": "left"})
# 
#         #set up the Label
#         self.labelForOutput = tkinter.Label(self)
#         self.labelForOutput["text"] = 0
#         self.labelForOutput.pack({"side": "left"})
# 
#         #set up the quit Button
#         self.quitButton = tkinter.Button(self)
#         self.quitButton["text"] = "Quit"
#         self.quitButton.pack({"side": "left"})
#         
# """ 
# This main program creates a MyFrame object that contains two Buttons and a Label. 
# """
# import week9                # contains class MyFrame
# if __name__ == "__main__":
#     view = myFrame.MyFrame()  # puts the Frame onto the user's screen
