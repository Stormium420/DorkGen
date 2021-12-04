from DorkOptions import KFT_Dork
from tkinter import *
from tkinter import filedialog
import time
import sys
sys.dont_write_bytecode = True


name = """
   _____ _                       
  / ____| |                      
 | (___ | |_ ___  _ __ _ __ ___  
  \___ \| __/ _ \| '__| '_ ` _ \ 
  ____) | || (_) | |  | | | | | |
 |_____/ \__\___/|_|  |_| |_| |_|
                                 
                                 
"""
print(name)

time.sleep(1)

keyWordPath = filedialog.askopenfilename(title="Open KeyWords file.")
pageTypePath = filedialog.askopenfilename(title="Open Page Type file.")
pageFormatPath = filedialog.askopenfilename(title="Open Page Format file.")


run = KFT_Dork(keyWordPath, pageTypePath, pageFormatPath)

run.createString() #Create dorks



input("Dorks generated, press any key to close.")

#Hope This is a good first project :)
