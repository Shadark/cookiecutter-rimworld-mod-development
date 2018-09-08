import os
import sys


pathlist = os.getcwd().split('\\')
if pathlist[-2] != "Mods":
    print("Needs to be ran inside the 'Mods' Directory of rimworld. Template aborted.")
    sys.exit(1)

if not os.path.exists('\\'.join(pathlist[:-2]) + "\RimWorldWin64.exe"):
    print("Could not find '" '\\'.join(pathlist[:-2]) + "\RimWorldWin64.exe'. Template aborted.")
    sys.exit(1)
