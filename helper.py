#file log_helper.py
import os
import sys
import logging

def logHelper(fileName, logLevel=logging.INFO, useConsole=True):
    ##### init logging
    log = logging.getLogger()
    log.setLevel(logLevel)
    logFormatter = logging.Formatter("%(asctime)s | %(threadName)-12.12s | %(levelname)-5.5s | %(message)s")

    ##### file handler
    fileOut = logging.FileHandler(fileName)
    fileOut.setFormatter(logFormatter)
    log.addHandler(fileOut)
    

    ##### console handler
    if useConsole:
        consoleOut = logging.StreamHandler(sys.stdout)
        consoleOut.setFormatter(logFormatter)
        log.addHandler(consoleOut)


    return log
    logging.info('text for .info() doodeedoo')


    """
    Simple Logging Helper. Returns logger reference.

    Paramsmeters:
    fileName: Filename, may include full path, or will open a file in default folder
    logLevel: Pass logging.INFO, logging.DEBUG or other enums for logging level
    useConsole: If True, will also dump log to console
    
    Code for main file header:
        import helper
        log = helper.logHelper('logfile.log')
    """