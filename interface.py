"""
MIDPEM "all" command interface.

:author: Max Milazzo
"""


import time
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
    
    with open(DEVICES_FILE, "r") as f:
        for line in f:
            WEBHOOK.send(cmd % line.strip())
            # send formatted command
            
            time.sleep(DELAY)
            

if __name__ == "__main__":
    main()