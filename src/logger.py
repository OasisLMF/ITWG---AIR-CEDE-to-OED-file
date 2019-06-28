# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:58:56 2019

@author: kumar.shivam
"""
import logging
import sys
import ConfigParser

def logging_process():
    """
    Initiating logging in a file named conversion.log for each step
    The logging would have error tags if encounter any error.
    Config.ini is configuration file which has all configuration related to logging.
    """
    try:
        config = ConfigParser.RawConfigParser()
        config.read(r"..\augmentations\config.ini")       
        logger = logging.getLogger('application')
        if logger.handlers:
            logger.handlers = []
        hdlr = logging.FileHandler(config.get('loggerdetails', 'filepath'))
        formatter = logging.Formatter(config.get('loggerdetails', 'format'))
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr) 
        logger.setLevel(logging.INFO)
        logger.info('Successfully initiated logging process')
        return logger
    except Exception as e:
        logger.info('Issue initiating logging process')
        logger.error(e)
        print("Error Check Log file")
        sys.exit(0)
