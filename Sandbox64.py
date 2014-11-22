# ##### BEGIN GPL LICENSE BLOCK #####
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# LEGO Island Sandbox V1 
# Part of the LEGO Island Config Utility (ICU)
# https://github.com/le717/ICU
# Copyright 2012-2013 le717 (http://triangle717.wordpress.com).

from winreg import * # TODO: Remove * import
import os, sys, subprocess
import time, webbrowser

''' Global variables
This is like the ISPP in Inno Setup. Changing these variables changes anything else that refers back to them.
Thankfully, this is built into Python, and doesn't require installing an optional module. :)'''
app = "LEGO Island Sandbox"
majver = "Version 1.0"
minver = "Beta 1"
creator = "le717"
game = "LEGO Island"

def preload():
    '''Python 3.3 version check'''
    if sys.version_info < (3,3): # You need to have at least Python 3.3 to run this program.
        print("You need to download Python 3.3 or greater to run {0} {1} {2}.".format(app, majver, minver))
        time.sleep(2) # Don't open browser immediately
        webbrowser.open("http://python.org/download", new=2, autoraise=True) # Open in new tab, raise browser window (if possible)
        time.sleep(5) # It automatically closes after this
    else: # If you are running Python 3.3
        main()

def main():
    '''App Menu Layout'''
    print("\nHello, and welcome to {0} {1} {2}\nCopyright 2013 {3}!".format(app, majver, minver, creator))
    print('''\nPlease make a selection:\n
[c] Create Sandbox
[d] Delete Sandbox
[q] Quit''')
    menuopt = input("\n> ")
    while True:
        if menuopt.lower() == "c":
            createsandbox()
        elif menuopt.lower() == "d":
            deletesandbox()
        elif menuopt.lower() == "q":
            closeapp()
        else:
            main()

def createsandbox():
    '''Creates Sandbox'''
    gamepath = input("\nPlease enter the path to your {0} installation:\n\n> ".format(game))
    time.sleep(0.5) # Make it seem like the app is not running so fast that is is bugged
    print("\nCreating Sandbox...\n")
    for line in stringnames:
        print(line, end="\n") # Print list of string names one at a time
        time.sleep(1)
    # TODO: Correct to support both x64 and x86 Windows in one script without WOW64 or multiple EXEs.
    with CreateKeyEx(HKEY_LOCAL_MACHINE, 'Software\Wow6432Node\Mindscape') as createkey:
        createstrings = CreateKey(createkey, "LEGO Island") # Explicity create all keys
        SetValueEx(createstrings, "3D Device Name", 0, REG_SZ, "Ramp Emulation")
        SetValueEx(createstrings, "3DSound", 0, REG_SZ, "YES")
        SetValueEx(createstrings, "Back Buffers in Video RAM", 0, REG_SZ, "YES")
        SetValueEx(createstrings, "diskpath", 0, REG_SZ, gamepath)
        SetValueEx(createstrings, "Display Bit Depth", 0, REG_SZ, "16")
        SetValueEx(createstrings, "Draw Cursor", 0, REG_SZ, "NO")
        SetValueEx(createstrings, "Flip Surfaces", 0, REG_SZ, "YES")
        SetValueEx(createstrings, "Full Screen", 0, REG_SZ, "YES")
        SetValueEx(createstrings, "Island Quality", 0, REG_SZ, "2")
        SetValueEx(createstrings, "Island Texture", 0, REG_SZ, "1")
        SetValueEx(createstrings, "JoystickIndex", 0, REG_SZ, "-1")
        SetValueEx(createstrings, "moviespath", 0, REG_SZ, gamepath)
        SetValueEx(createstrings, "Music", 0, REG_SZ, "YES")
        SetValueEx(createstrings, "savepath", 0, REG_SZ, gamepath)
        SetValueEx(createstrings, "UseJoystick", 0, REG_SZ, "NO")
        SetValueEx(createstrings, "Wide View Angle", 0, REG_SZ, "YES")
        #if os.system(savepath) == 0: # TODO: Registry exit codes?
    with CreateKeyEx(HKEY_LOCAL_MACHINE, 'Software\Microsoft\Windows\CurrentVersion\App Paths') as createapppath:
        SetValue(createapppath, "LEGOISLE.exe", REG_SZ, gamepath) # Create App Path key\value
    print("\n{0} Sandbox sucessfully created!".format(game))
    print("\nDo you want to launch {0} now? ".format(game) + r"(y\N)") # Launch LEGO Island?
    rungame = input("\n> ".format(game))
    if rungame.lower() != "y": # No, don't launch it
        main()
    else: # Yes, launch it
        time.sleep(1)
        try:
            print("See ya later, Brickulator!")
            subprocess.call([gamepath + "/LEGOISLE.EXE"]) # Load game, exit app
            sys._exit(0)
        except WindowsError: # Cannot find EXE at gamepath entered
            print('Cannot find {0} installation at "{1}"!'.format(game, gamepath))
            main()

def deletesandbox():
    '''Deletes Sandbox'''
    try:
        with OpenKey(HKEY_LOCAL_MACHINE, 'Software\Wow6432Node\Mindscape', 0, KEY_ALL_ACCESS) as deletestrings: # Open root key
            DeleteKey(HKEY_LOCAL_MACHINE, 'Software\Wow6432Node\Mindscape\LEGO Island') # All game registry strings
            DeleteKey(HKEY_LOCAL_MACHINE, 'Software\Wow6432Node\Mindscape') # Delete all strings and keys created
            with OpenKey(HKEY_LOCAL_MACHINE, 'Software\Microsoft\Windows\CurrentVersion\App Paths', 0, KEY_ALL_ACCESS) as deletestrings:
                DeleteKey(HKEY_LOCAL_MACHINE, 'Software\Microsoft\Windows\CurrentVersion\App Paths\LEGOISLE.exe') # Delete the app path key\value
        print("\nDeleting Sandbox...\n")
        time.sleep(0.5)
        for line in stringnames:
            print(line, end="\n") # Again, display string names one at a time
            time.sleep(1)
        print("\n{0} Sandbox sucessfully deleted!".format(game))
        main()
    except WindowsError: # The sandbox has already been deleted
        print("\nCannot find a Sandbox to delete!")
        main()

def closeapp():
    '''Custom App Exit Routine'''
    try:
        with OpenKey(HKEY_LOCAL_MACHINE, 'Software\Wow6432Node\Mindscape\LEGO Island', 0, KEY_ALL_ACCESS) as findsandbox: # The sandbox still exists
            print("\nDo you want to delete your sandbox before you le {0}?\nNot doing so can pose a security hazard! ".format(app) + r"(y\N)")
            closeapp = input("\n> ")
            if closeapp.lower() == "y": # Yes, I will delete the sandbox
                deletesandbox()
            else: # No, I want the sandbox to remain
                print("\nThanks for the visit. You're welcome anytime! We'll miss you!")
                exit()
    except WindowsError: # The sandbox has already been deleted
        print("\nIf you select the green brick, you go! If you select the red brick, you stay! \nGreen go, red stay.")
        exit()
                

# List of registry string names. Are printed during the creation and deletion process.    
stringnames = ["3D Device Name",
               "3DSound",
               "Back Buffers in Video RAM",
               "diskpath",
               "Display Bit Depth",
               "Draw Cursor",
               "Flip Surfaces",
               "Full Screen",
               "Island Quality",
               "Island Texture",
               "JoystickIndex",
               "moviespath",
               "Music",
               "savepath",
               "UseJoystick",
               "Wide View Angle",
               "LEGOISLE.exe"]

    


if __name__ == "__main__":
    preload()
