# ICU Logging code

# logging.BasicConfig code based on example from A Byte of Python
# http://www.swaroopch.com/notes/Python

import os, logging, time, winreg

# ------------ Begin ICU Logging Code ------------ #

def adminRights():
    '''Check for Administrator Rights'''
    try:
        # This string I'm opening actually defines what version of Windows is being run. You could use this to make OS-only options. :)
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\Microsoft\Windows NT\CurrentVersion', 0, winreg.KEY_READ) as regkey:
            regvalue = winreg.QueryValueEx(regkey, 'CurrentVersion')

    # User does not have Admin rights
    except PermissionError:
        print("\nICU Sandbox does not have the user rights to operate!\nPlease relaunch ICU Sandbox as an Administrator.")
        # Display message long enough so user can read it
        time.sleep(5)
        # Close program
        raise SystemExit


def appLoggingFolder():
    '''Checks for (and creates) ICU Logs folder'''

        # The Logs folder does not exist in the current directory
    if not os.path.exists(os.path.join(os.getcwd(), "Logs")):
        # Create the Logs folder
        logsfolder = os.mkdir(os.path.join(os.getcwd(), "Logs"))


# AKA if this is imported as a module
if "__main__" != __name__:
    adminRights()
    appLoggingFolder()

    # -- Begin Logging Config -- #

    logging_file = os.path.join(os.getcwd(), "Logs", 'YourScoreCube.log')

    logging.basicConfig(
        level = logging.DEBUG,
        format = "%(asctime)s : %(levelname)s : %(message)s",
        filename = logging_file,
        filemode = 'a+',
    )

    # -- End Logging Config -- #

# ------------ End ICU Logging Code ------------ #