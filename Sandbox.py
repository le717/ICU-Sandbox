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

# ICU Sandbox V1
# Part of ICU (LEGO Island Configuration Utility)
# https://github.com/le717/ICU
# Copyright 2012-2013 Triangle717 (http://triangle717.wordpress.com).

# Import only certain items instead of "the whole toolbox"
import winreg
from sys import version_info
import os, subprocess
from webbrowser import open_new_tab
from time import sleep
# GUI elements
import tkinter
from tkinter import filedialog
# App logging
import logging
import yourscorecube

# GLobal variables
app = "ICU Sandbox"
majver = "Version 1.0"
minver = "Beta 2"
creator = "Triangle717"
game = "LEGO Island"

# ------------ Begin ICU Sandbox Initialization ------------ #

def preload():
    '''Python 3.3.0 check'''

    logging.info("Begin logging to {0}".format(yourscorecube.logging_file))
    logging.info('''
                                #############################################
                                        {0} {1} {2}
                                        Copyright 2013 {3}
                                            YourScoreCube.log


                                    If you run into a bug, open an issue at
                                    https://github.com/le717/ICU/issues
                                    and attach this file for an easier fix!
                                #############################################
                                '''.format(app, majver, minver, creator))

     # You need to have at least Python 3.3.0 to run ICU Sandbox
    if version_info < (3,3,0):
        logging.warning("You are not running Python 3.3.0 or higher!\nYou need to get a newer version to run {0}".format(app))
        print("\nYou need to download Python 3.3.0 or greater to run {0} {1} {2}.".format(app, majver, minver))

        # Don't open browser immediately
        sleep(2)
        logging.info("Open new tab in web browser to http://python.org/download")
        open_new_tab("http://python.org/download") # New tab, raise browser window (if possible)

        # Close ICU Sandbox
        logging.info("Display error message for three seconds")
        sleep(3)
        logging.info("{0} is shutting down.".format(app))
        raise SystemExit

    # If you are running Python 3.3.0
    else:
        logging.info("You are running Python 3.3.0 or greater. {0} will continue.".format(app))
        logging.info("Swiching to main menu")
        main()

# ------------ End ICU Sandbox Initialization ------------ #


# ------------ Begin ICU Sandbox Menu Layout ------------ #

def main():
    '''ICU Sandbox Menu Layout'''

    print("\nHello, and welcome to {0} {1} {2}\nCopyright 2013 {3}!".format(app, majver, minver, creator))
    print('''\nPlease make a selection:\n
[c] Create Sandbox
[d] Delete Sandbox
[q] Quit''')
    logging.info("Display menu to user")
    menuopt = input("\n> ")
    while True:
        if menuopt.lower() == "c":
            logging.info("User pressed '[c] Create Sandbox'")
            logging.info("Switching to Sandbox Creation process (createsandbox())")
            createsandbox()

        elif menuopt.lower() == "d":
            logging.info("User pressed '[s] Delete Sandbox'")
            logging.info("Switching to Sandbox Deletion process (deletesandbox())")
            deletesandbox()

        elif menuopt.lower() == "q":
            logging.info("User pressed '[q] Quit'")
            logging.info("Switching to shutdown routine (closeapp())")
            closeapp()

        # Undefined input
        else:
            logging.info("User pressed an undefined key")
            main()

# ------------ End ICU Sandbox Menu Layout ------------ #


# ------------ Begin Sandbox Creation Code ------------ #

def createsandbox():
    '''Creates LEGO Island Sandbox'''

    # Draw (then withdraw) the root Tk window
    logging.info("Drawing root Tk window")
    root = tkinter.Tk()
    logging.info("Withdrawing root Tk window")
    root.withdraw()

    # Select your LEGO Island files
    # TODO: Make dialog active window automatically and do the same to main window when closed.
    logging.info("Display folder selection dialog LEGO Island installation.")
    gamepath = filedialog.askdirectory(title="Select your {0} installation".format(game))

    # The user clicked cancel
    if len(gamepath) == 0:
        logging.warning("User canceled {0} Sandbox creation!".format(game))
        print("\nCanceling creation of {0} Sandbox...".format(game))
        sleep(1)
        logging.info("Swiching to main menu")
        main()

    # The user selected a folder
    else:
        logging.info("User selected a {0} installation at {1}".format(game, gamepath))

         # Make it seem like the app is not running so fast that is is bugged
        sleep(0.5)
        logging.info("Create required game registry strings")
        print("\nCreating Sandbox...\n")

        try:
            # TODO: Correct to support both x64 and x86 Windows in one script without WOW64 or multiple EXEs.
            with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, 'Software\Mindscape') as createkey:
                createstrings = winreg.CreateKey(createkey, "LEGO Island") # Explicity create all keys
                winreg.SetValueEx(createstrings, "3D Device Name", 0, winreg.REG_SZ, "Ramp Emulation")
                winreg.SetValueEx(createstrings, "3DSound", 0, winreg.REG_SZ, "YES")
                winreg.SetValueEx(createstrings, "Back Buffers in Video RAM", 0, winreg.REG_SZ, "YES")
                winreg.SetValueEx(createstrings, "diskpath", 0, winreg.REG_SZ, gamepath)
                winreg.SetValueEx(createstrings, "Display Bit Depth", 0, winreg.REG_SZ, "16")
                winreg.SetValueEx(createstrings, "Draw Cursor", 0, winreg.REG_SZ, "NO")
                winreg.SetValueEx(createstrings, "Flip Surfaces", 0, winreg.REG_SZ, "YES")
                winreg.SetValueEx(createstrings, "Full Screen", 0, winreg.REG_SZ, "YES")
                winreg.SetValueEx(createstrings, "Island Quality", 0, winreg.REG_SZ, "2")
                winreg.SetValueEx(createstrings, "Island Texture", 0, winreg.REG_SZ, "1")
                winreg.SetValueEx(createstrings, "JoystickIndex", 0, winreg.REG_SZ, "-1")
                winreg.SetValueEx(createstrings, "moviespath", 0, winreg.REG_SZ, gamepath)
                winreg.SetValueEx(createstrings, "Music", 0, winreg.REG_SZ, "YES")
                winreg.SetValueEx(createstrings, "savepath", 0, winreg.REG_SZ, gamepath)
                winreg.SetValueEx(createstrings, "UseJoystick", 0, winreg.REG_SZ, "NO")
                winreg.SetValueEx(createstrings, "Wide View Angle", 0, winreg.REG_SZ, "YES")


            logging.info("Create App Path registry string")
            with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, 'Software\Microsoft\Windows\CurrentVersion\App Paths') as createapppath:
                winreg.SetValue(createapppath, "LEGOISLE.exe", winreg.REG_SZ, gamepath)

            logging.info("Displaying names of Registry strings")
            logging.info("(This creates the illusion that the strings are being created as the name is printed)")

            for line in stringnames:
                # Print list of string names one at a time
                print(line, end="\n")
                sleep(0.5)

            logging.info("Sandbox sucessfully created")
            print("\n{0} Sandbox sucessfully created!".format(game))

            # Launch LEGO Island?
            logging.info("Do you want to play LEGO Island now?")
            print("\nDo you want to play {0} now? ".format(game) + r"(y\N)")
            rungame = input("\n> ".format(game))

            # No, don't launch it
            if rungame.lower() != "y":
                logging.warning("User does not want to play LEGO Island right now!")
                main()

            # Yes, launch it
            else:
                sleep(1)
                try:
                    logging.info("Display exit message")
                    print("See ya later, Brickulator!")


                    # Load game, exit app
                    logging.info("Run LEGOISLE.EXE, located at {0}".format(gamepath))
                    subprocess.call([gamepath + "/LEGOISLE.EXE"])
                    logging.info("ICU Sandbox is shutting down.")
                    raise SystemExit

                # Cannot find EXE at gamepath entered
                except WindowsError:
                    logging.warning('Cannot find {0} installation at "{1}"!'.format(game, gamepath))
                    print('Cannot find {0} installation at "{1}"!'.format(game, gamepath))
                    logging.info("Switching to main menu")
                    main()

        except PermissionError:
            logging.warning("Cannot create Sandbox!")
            logging.warning("ICU Sandbox was not run with Administrator rights, which are needed to create the Sandbox!")
            print("\n{0} does not have the user rights to operate!\nPlease relaunch {1} as an Administrator.".format(app, app))
            sleep(3)
            logging.info("Switching to main menu")
            main()
# ------------ End Sandbox Creation Code ------------ #


# ------------ Begin Sandbox Deletion Code ------------ #

def deletesandbox():
    '''Deletes LEGO Island Sandbox'''

    try:
        logging.info("Delete game registry strings")
        print("\nDeleting Sandbox...\n")

        # Open root key
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'Software\Mindscape', 0, winreg.KEY_ALL_ACCESS) as deletestrings:

            # All game registry value
            winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, 'Software\Mindscape\LEGO Island')
            # Delete all created keys and values
            winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, 'Software\Mindscape')

            # Delete App Path
            logging.info("Delete App Path registry string")
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'Software\Microsoft\Windows\CurrentVersion\App Paths', 0, winreg.KEY_ALL_ACCESS) as deletestrings:
               winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, 'Software\Microsoft\Windows\CurrentVersion\App Paths\LEGOISLE.exe')

        for line in stringnames:
            print(line, end="\n") # Again, display string names one at a time
            sleep(0.2)

        # The sandbox was sucessfully deleted
        logging.info("LEGO Isand Sandbox sucessfully deleted!")
        print("\n{0} Sandbox sucessfully deleted!".format(game))
        logging.info("Switching to main menu")
        main()

    # The sandbox has already been deleted
    except WindowsError:
        logging.warning("Cannot find a Sandbox to delete!")
        print("\nCannot find a Sandbox to delete!")
        sleep(2)
        logging.info("Switching to main menu")
        main()

# ------------ End Sandbox Deletion Code ------------ #


# ------------ Begin ICU Sandbox Shutdown Routine ------------ #

def closeapp():
    '''Custom Exit Routine'''
    try:
        # The sandbox still exists
        logging.warning("The Sandbox still exists!")
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'Software\Mindscape\LEGO Island', 0, winreg.KEY_ALL_ACCESS) as findsandbox:
            logging.info("Do you want to exit without deleting your Sandbox?")
            print("\nDo you want to close {0} before deleting your sandbox?\nNot doing so can pose a security hazard! ".format(app) + r"(y\N)")
            closeapp = input("\n> ")

            # Yes, I want the sandbox to remain
            if closeapp.lower() == "y":
                logging.warning("User chose to exit without deleting the Sandbox!")
                print("\nThanks for the visit. You're welcome anytime! We'll miss you!")
                sleep(3)
                logging.info("ICU Sandbox is shutting down")
                raise SystemExit

            # No, I will delete the sandbox
            else:
                logging.info("User chose to delete the Sandbox before exiting")
                logging.info("Switching to Sandbox Deletion process (deleteSandbox())")
                deleteSandbox()

    # The sandbox has already been deleted
    except WindowsError:
        logging.info("Sandbox has already been deleted")
        print("\nIf you select the green brick, you go! If you select the red brick, you stay! \nGreen go, red stay.")
        sleep(4)
        logging.info("ICU Sandbox is shutting down")
        raise SystemExit

# ------------ End ICU Sandbox Shutdown Routine ------------ #


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
    # Run preload() to begin ICU Sandbox Initialization
    preload()