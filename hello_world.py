import time
import os
import sys
import logging

from ASL.utils.asl_logging import ASL_Logging

logger = logging.getLogger(__name__)

def hello_worldx():
   print("***Hello World")
   return "**Hello World**"

def main():
   print("main **** Hello World ****")

# *****************************************************
#
#  MAIN MAIN
# *********************************************************
if __name__ == "__main__":
    try:
        main()
        exit(0)  # cape may...:)
    except Exception as e:
      logger.critical(f"Errored out unrecoverable issue {e}")
      exit(1)
