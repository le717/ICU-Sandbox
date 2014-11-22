#! python3
"""
    This file is part of ICU (LEGO Island Configuration Utility)

    ICU - A collection of LEGO Island Configuration Tools
    Created 2012-2014 Triangle717 <http://triangle717.wordpress.com>

    ICU is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    ICU is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ICU. If not, see <http://www.gnu.org/licenses/>.
"""

# ICU Sandbox V1
# Part of ICU (LEGO Island Configuration Utility)
# https://github.com/le717/ICU

# General use modules
import os
import sys
import time

# Main use modules
import winreg
import platform

# Special purpose modules
import webbrowser
import subprocess

# Logging Code
import logging
import yourscorecube

# GUI elements
import tkinter
from tkinter import filedialog

# Global variables
app = "ICU Sandbox"
majver = "Version 1.0.1"
minver = "Stable"
creator = "Triangle717"
game = "LEGO Island"


# ------------ Begin ICU Sandbox Initialization ------------ #


def preload():
    """Python 3.3.0 and Windows Architecture check"""

    logging.info("Begin logging to {0}".format(yourscorecube.logging_file))
    logging.info('''
                                #############################################
                                        {0} {1} {2}
                                        Created 2013-2014 {3}
                                            YourScoreCube.log


                                    If you run into a bug, open an issue at
                                    https://github.com/le717/ICU/issues
                                    and attach this file for an easier fix!
                                #############################################
                                '''.format(app, majver, minver, creator))

    # You need to have at least Python 3.3.0 to run ICU Sandbox
    if sys.version_info[:2] < (3, 3):
        logging.warning('''User is not running Python 3.3.0 or higher!
You need to get a newer version to run {0}'''.format(app))
        sys.stdout.write('''\nYou need to download Python 3.3.0 or greater
to run {0} {1} {2}.'''.format(app, majver, minver))

        # Don't open browser immediately
        time.sleep(2)
        logging.info("Open Python download page in a new tab in web browser")
        # New tab, raise browser window (if possible)
        webbrowser.open_new_tab("http://python.org/download")

        # Close ICU Sandbox
        logging.info("Display error message for three seconds")
        time.sleep(3)
        logging.info("{0} is shutting down.".format(app))
        raise SystemExit(0)

        # Mac OS X/Linux
        if "Windows" not in platform.platform():
            logging.warning("User is running an unsupported OS!")
            print("\nYou are running an unsupported OS! {0} will now close."
                  .format(app))
            time.sleep(3)
            logging.info("{0} is shutting down".format(app))
            raise SystemExit(0)
    main()


# ------------ End ICU Sandbox Initialization ------------ #


# ------------ Begin ICU Sandbox Menu Layout ------------ #


def main():
    """ICU Sandbox Menu Layout."""
    print("\n{0} {1} {2}\nCreated 2013-2014 {3}".format(
          app, majver, minver, creator))
    print("""
Please make a selection:

[c] Create Sandbox
[d] Delete Sandbox
[q] Quit""")

    menuopt = input("\n> ")
    while True:
        if menuopt.lower() == "c":
            logging.info("User pressed '[c] Create Sandbox'")
            logging.info("Switching to Sandbox Creation process")
            createSandbox()

        elif menuopt.lower() == "d":
            logging.info("User pressed '[s] Delete Sandbox'")
            logging.info("Switching to Sandbox Deletion process")
            deleteSandbox()

        elif menuopt.lower() == "q":
            logging.info("User pressed '[q] Quit'")
            logging.info("Switching to shutdown routine")
            close()

        # Undefined input
        else:
            logging.info("User pressed an undefined key")
            main()


# ------------ End ICU Sandbox Menu Layout ------------ #


# ------------ Begin Sandbox Creation Intro ------------ #


def createSandbox():
    """Sandbox Creation Launcher."""
    # Draw (then withdraw) the root Tk window
    logging.info("Drawing root Tk window")
    root = tkinter.Tk()
    logging.info("Withdrawing root Tk window")
    root.withdraw()

    # Select your LEGO Island files
    # TODO: Make dialog active window automatically and do the same
    # to main window when closed.
    logging.info("Display folder selection dialog for LEGO Island installation.")
    gamepath = filedialog.askdirectory(
        title="Please select your {0} installation".format(game))

    # The user clicked cancel
    if len(gamepath) == 0:
        logging.warning("User canceled Sandbox creation!")
        print("\nCanceling creation of Sandbox...\n")
        time.sleep(1)
        logging.info("Swiching to main menu")
        main()

    # The user selected a folder
    else:
        logging.info("User selected a {0} installation at {1}".format(game,
        gamepath))
        print("\nCreating Sandbox...\n")

        # Display names of registry strings
        logging.info("Displaying names of Registry strings")

        for line in stringnames:
            # Display string names one at a time, each on a new line
            print("{0}\n".format(line))
            time.sleep(0.2)

        # Switch to 64-bit registry string code
        if osbit:
            sixfourbitStrings(gamepath)

        # Switch to 32-bit registry string code
        else:
            threetwobitStrings(gamepath)


# ------------ End Sandbox Creation Intro ------------ #


# ------------ Begin 64-bit Sandbox Creation Code ------------ #


def sixfourbitStrings(gamepath):
    """Creates x64 LEGO Island Sandbox"""

    logging.info('''
''')

    logging.info("Creating required game registry strings (x64)")
    try:

        # Tip: Always use the with handle for this kind of stuff
        with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE,
        'Software\Wow6432Node\Mindscape') as createkey:
            # Explicitly create all keys
            createstrings = winreg.CreateKey(createkey, "LEGO Island")

            # Use highest quality, almost guanteed-to-work-on-any-OS settings
            winreg.SetValueEx(createstrings, "3D Device Name", 0, winreg.REG_SZ,
            "Ramp Emulation")
            winreg.SetValueEx(createstrings, "3DSound", 0, winreg.REG_SZ, "YES")
            winreg.SetValueEx(createstrings, "Back Buffers in Video RAM", 0,
                winreg.REG_SZ, "YES")
            winreg.SetValueEx(createstrings, "diskpath", 0, winreg.REG_SZ,
                gamepath)
            winreg.SetValueEx(createstrings, "Display Bit Depth", 0,
                winreg.REG_SZ, "16")
            winreg.SetValueEx(createstrings, "Draw Cursor", 0, winreg.REG_SZ,
                "NO")
            winreg.SetValueEx(createstrings, "Flip Surfaces", 0, winreg.REG_SZ,
                "YES")
            winreg.SetValueEx(createstrings, "Full Screen", 0, winreg.REG_SZ,
                "YES")
            winreg.SetValueEx(createstrings, "Island Quality", 0, winreg.REG_SZ,
                "2")
            winreg.SetValueEx(createstrings, "Island Texture", 0, winreg.REG_SZ,
                "1")
            winreg.SetValueEx(createstrings, "JoystickIndex", 0, winreg.REG_SZ,
                "-1")
            winreg.SetValueEx(createstrings, "moviespath", 0, winreg.REG_SZ,
                gamepath)
            winreg.SetValueEx(createstrings, "Music", 0, winreg.REG_SZ, "YES")
            winreg.SetValueEx(createstrings, "savepath", 0, winreg.REG_SZ,
                gamepath)
            winreg.SetValueEx(createstrings, "UseJoystick", 0, winreg.REG_SZ,
                "NO")
            winreg.SetValueEx(createstrings, "Wide View Angle", 0,
                winreg.REG_SZ, "YES")

        logging.info("Create App Path registry string")
        with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE,
            'Software\Microsoft\Windows\CurrentVersion\App Paths') as createapppath:
            winreg.SetValue(createapppath, "LEGOISLE.exe", winreg.REG_SZ,
                gamepath)

        logging.info("Sandbox sucessfully created")
        print("\nSandbox sucessfully created!\n")
        letheIsland(gamepath)

    except WindowsError:
        logging.warning("Cannot create Sandbox!")
        logging.warning('''{0} was not run with Administrator rights,
which are needed to create the Sandbox!'''.format(app))
        print('''\n{0} does not have the user rights to operate!
Please relaunch {1} as an Administrator.'''.format(app))
        time.sleep(3)
        main()


# ------------ End 64-bit Sandbox Creation Code ------------ #


# ------------ Begin 32-bit Sandbox Creation Code ------------ #


def threetwobitStrings(gamepath):
    """Creates x86 LEGO Island Sandbox"""

    logging.info('''
''')

    logging.info("Creating required game registry strings (x86)")
    try:
        with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE,
            'Software\Mindscape') as createkey:
            # Explicitly create all keys
            createstrings = winreg.CreateKey(createkey, "LEGO Island")

            # Use highest quality, almost guanteed-to-work-on-any-OS settings
            winreg.SetValueEx(createstrings, "3D Device Name", 0, winreg.REG_SZ,
                "Ramp Emulation")
            winreg.SetValueEx(createstrings, "3DSound", 0, winreg.REG_SZ, "YES")
            winreg.SetValueEx(createstrings, "Back Buffers in Video RAM", 0,
                winreg.REG_SZ, "YES")
            winreg.SetValueEx(createstrings, "diskpath", 0, winreg.REG_SZ,
                gamepath)
            winreg.SetValueEx(createstrings, "Display Bit Depth", 0,
                winreg.REG_SZ, "16")
            winreg.SetValueEx(createstrings, "Draw Cursor", 0, winreg.REG_SZ,
                "NO")
            winreg.SetValueEx(createstrings, "Flip Surfaces", 0, winreg.REG_SZ,
                "YES")
            winreg.SetValueEx(createstrings, "Full Screen", 0, winreg.REG_SZ,
                "YES")
            winreg.SetValueEx(createstrings, "Island Quality", 0, winreg.REG_SZ,
                "2")
            winreg.SetValueEx(createstrings, "Island Texture", 0, winreg.REG_SZ,
                "1")
            winreg.SetValueEx(createstrings, "JoystickIndex", 0, winreg.REG_SZ,
                "-1")
            winreg.SetValueEx(createstrings, "moviespath", 0, winreg.REG_SZ,
                gamepath)
            winreg.SetValueEx(createstrings, "Music", 0, winreg.REG_SZ, "YES")
            winreg.SetValueEx(createstrings, "savepath", 0, winreg.REG_SZ,
                gamepath)
            winreg.SetValueEx(createstrings, "UseJoystick", 0, winreg.REG_SZ,
                "NO")
            winreg.SetValueEx(createstrings, "Wide View Angle", 0,
                winreg.REG_SZ, "YES")

        logging.info("Create App Path registry string")
        with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE,
            'Software\Microsoft\Windows\CurrentVersion\App Paths') as createapppath:
            winreg.SetValue(createapppath, "LEGOISLE.exe", winreg.REG_SZ,
                gamepath)

        logging.info("Sandbox sucessfully created")
        print("\nSandbox sucessfully created!\n")
        letheIsland(gamepath)

    except WindowsError:
        logging.warning("Cannot create Sandbox!")
        logging.warning('''{0} was not run with Administrator rights,
    which are needed to create the Sandbox!'''.format(app))
        print('''\n{0} does not have the user rights to operate!
Please relaunch {0} as an Administrator.'''.format(app))
        time.sleep(3)
        main()


# ------------ End 32-bit Sandbox Creation Code ------------ #


# ------------ Begin Game Launching Code ------------ #


def letheIsland(gamepath):
    """Launches LEGO Island"""

    logging.info('''
''')

    # Launch LEGO Island?
    logging.info("Do you want to play LEGO Island now?")
    print("\nDo you want to play {0} now? ".format(game) + r"(y\N)")
    rungame = input("\n> ".format(game))

    # No, don't launch it
    if rungame.lower() != "y":
        logging.warning("User does not want to play LEGO Island right now!")
        main()

    # Yes, launch it (User presses 'y', which is the only key
    # that will run the game)
    else:
        time.sleep(1)
        try:
            # Run game
            logging.info("Run ISLE.EXE, located at {0}".format(gamepath))
            subprocess.call([os.path.join(gamepath, "ISLE.EXE")])

            # Display message
            logging.info("Display exit message")
            print("\nSee ya later, Brickulator!")

            # Close app
            logging.info("{0} is shutting down".format(app))
            raise SystemExit(0)

        # Cannot find EXE at gamepath entered
        except OSError:
            logging.warning('Cannot find {0} installation at "{1}"!'.format(
                game, gamepath))
            print('\nCannot find {0} installation at\n"{1}"!'.format(game,
            gamepath))
            time.sleep(3)
            main()


# ------------ End Game Launching Code ------------ #


# ------------ Begin Sandbox Deletion Intro ------------ #


def deleteSandbox():
    """Sandbox Deletion Launcher."""
    # Again, if user is running 64-bit Windows
    if osbit:
        del64bitSandbox()

    # If user is running 32-bit Windows
    else:
        del32bitSandbox()


# ------------ End Sandbox Deletion Intro ------------ #


# ------------ Begin 32-bit Sandbox Deletion Code ------------ #


def del32bitSandbox():
    """Deletes x86 LEGO Island Sandbox"""
    logging.info('''
''')

    try:
        logging.info("Deleting required game registry strings (x86)")
        print("\nDeleting Sandbox...\n")

        # Open root key
        logging.info("Delete all game strings, inlcuding root string")
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'Software\Mindscape', 0,
            winreg.KEY_ALL_ACCESS):

            # All game registry values
            winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE,
                'Software\Mindscape\LEGO Island')
            # Delete root key
            winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, 'Software\Mindscape')

            # Delete App Path
        logging.info("Delete App Path registry string")
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
            'Software\Microsoft\Windows\CurrentVersion\App Paths', 0,
            winreg.KEY_ALL_ACCESS):
            winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE,
                'Software\Microsoft\Windows\CurrentVersion\App Paths\LEGOISLE.exe')

        # Display names of registry strings
        logging.info("Displaying names of Registry strings")

        for line in stringnames:
            # Again, display string names one at a time
            print("{0}\n".format(line))
            time.sleep(0.2)

        # The sandbox was sucessfully deleted
        logging.info("Sandbox sucessfully deleted!")
        print("\nSandbox sucessfully deleted!")
        main()

    # The sandbox has already been deleted
    except WindowsError:
        logging.warning("Cannot find a Sandbox to delete!")
        print("\nCannot find a Sandbox to delete!")
        time.sleep(2)
        main()


# ------------ End 32-bit Sandbox Deletion Code ------------ #


# ------------ Begin 64-bit Sandbox Deletion Code ------------ #


def del64bitSandbox():
    """Deletes x64 LEGO Island Sandbox"""
    logging.info('''
''')

    try:
        logging.info("Deleting required game registry strings (x64)")
        print("\nDeleting Sandbox...\n")

        # Open root key
        logging.info("Delete all game strings, inlcuding root string")
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
            'Software\Wow6432Node\Mindscape', 0,
            winreg.KEY_ALL_ACCESS):

            # All game registry values
            winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE,
                'Software\Wow6432Node\Mindscape\LEGO Island')
            # Delete root key
            winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE,
                'Software\Wow6432Node\Mindscape')

            # Delete App Path
        logging.info("Delete App Path registry string")
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
            'Software\Microsoft\Windows\CurrentVersion\App Paths', 0,
            winreg.KEY_ALL_ACCESS):
            winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE,
                'Software\Microsoft\Windows\CurrentVersion\App Paths\LEGOISLE.exe')

        # Display names of registry strings
        logging.info("Displaying names of Registry strings")
        for line in stringnames:
            # Again, display string names one at a time
            print("{0}\n".format(line))
            time.sleep(0.2)

        # The sandbox was sucessfully deleted
        logging.info("Sandbox sucessfully deleted!")
        print("\nSandbox sucessfully deleted!")
        main()

    # The sandbox has already been deleted
    except WindowsError:
        logging.warning("Cannot find a Sandbox to delete!")
        print("\nCannot find a Sandbox to delete!")
        time.sleep(2)
        main()


# ------------ End 64-bit Sandbox Deletion Code ------------ #


# ------------ Begin ICU Sandbox Shutdown Routine ------------ #


def close():
    """Custom Exit Routine with Sandbox Detection"""
    logging.info('''
''')

    try:
        if osbit:
            # The x64 sandbox still exists
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                "Software\Wow6432Node\Mindscape\LEGO Island",
                0, winreg.KEY_READ):
                logging.warning("The (X64) Sandbox still exists!")

        else:
            # The x86 sandbox still exists
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                "Software\Mindscape\LEGO Island", 0, winreg.KEY_READ):
                logging.warning("The (X86) Sandbox still exists!")

    # The sandbox has already been deleted
    except EnvironmentError:
        logging.info("Sandbox has already been deleted")
        print('''\nIf you select the green brick, you go!
If you select the red brick, you stay! Green go, red stay.''')
        time.sleep(4)
        logging.info("ICU Sandbox is shutting down")
        raise SystemExit(0)

    # Do you want to close without deleting the Sandbox?
    logging.info("Do you want to exit without deleting your Sandbox?")
    print("""
Do you want to close {0} without deleting your sandbox?
Not doing so can pose a security hazard! {0}""".format(app, r"(y\N)"))
    closeapp = input("\n> ")

    # Yes, I want the sandbox to remain
    # User must press 'y' to exit, anything else deletes it.
    if closeapp.lower() == "y":
        logging.warning("User chose to exit without deleting the Sandbox!")
        logging.info("ICU Sandbox is shutting down")
        raise SystemExit(0)

    # No, I will delete the sandbox
    else:
        logging.info("User chose to delete the Sandbox before exiting")

        if osbit:
            del64bitSandbox()
        else:
            del32bitSandbox()


# ------------ End ICU Sandbox Shutdown Routine ------------ #

# List of registry string names.
# Are printed during the Sandbox creation and deletion process.
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
    # Get the Windows architecture
    if platform.machine() == "AMD64":
        # x64 Windows == True
        osbit = True
    else:
        # x86 Windows == False
        osbit = False

    os.system("title {0} {1} {2}".format(app, majver, minver))
    preload()
