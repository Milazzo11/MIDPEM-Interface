"""
MIDPEM "all" command interface.

:author: Max Milazzo
"""


import time
import discord
from discord import SyncWebhook


DEVICES_FILE = "devices.txt"
# devices file


DELAY = 1
# execuation delay


WEBHOOK = SyncWebhook.from_url(
    "https://discord.com/api/webhooks/1152756239156129852/tx2f8MmGAZoP79QvU1Ex_WfDICvZYdyMqGhXewP3vsd4Yxgh1At4FkcuoAWqkojmzcQa"
)
# comand webhook


def main():
    """
    Program entry point.
    """
    
    print("Enter formatted command")
    cmd = input("> ")
    # get command
    
    print("Enter attached filename (or ENTER if none)")
    filename = input("> ")
    # get attached filename (if applicable)
        
    with open(DEVICES_FILE, "r") as f:
        lines = f.readlines()
        # read device data
        
    for line in lines:
    # execute command for each device
        
        if filename.strip() == "":
            WEBHOOK.send(cmd % line.strip())
            # send formatted command

        else:
            with open(filename, "rb") as f:
                WEBHOOK.send(cmd % line.strip(), file=discord.File(fp=f))
                # send formatted command with attached file
            
        time.sleep(DELAY)
                

if __name__ == "__main__":
    main()
