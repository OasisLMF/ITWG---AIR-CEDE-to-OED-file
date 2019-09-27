# -*- coding: utf-8 -*-
"""
Created on Wed Jul 03 12:31:05 2019

@author: kumar.shivam
"""

import pandas as pd
import json
import sys
from constants import constants


class filehelper:    
    def OED_location_file_preprocess(self,logger):
        """
        Reading the column names required for the OED files from location column names csv and creating
        the empty dataframe with the same column names,
        """
        try:
            self.OED_location_column_names = pd.read_csv(constants.LOCATION_COLUMN_NAMES,header = 0, index_col=0)
            self.OED_location_column_names_list = self.OED_location_column_names['ColumnNames'].tolist()            
            self.OED_location_file = pd.DataFrame(columns = self.OED_location_column_names_list)
            return self.OED_location_file  
            logger.info('Successfully created blank OED file')                  
        except Exception as e:
            logger.info('Issue in creating blank OED file') 
            logger.error(e,exc_info=True)  
            print("Error Check Log file") 
            sys.exit(0) 
            
            
    
    """
    Method for creating blank OED account file.
    The coluumn names is read from csv file.
    """           
    def OED_account_file_blank(self,logger):
        try:
            self.OED_account_column_names = pd.read_csv(constants.ACCOUNT_COLUMN_NAMES,header = 0, index_col=0)
            self.OED_account_column_names = self.OED_account_column_names['ColumnNames'].tolist()
            self.OED_account_file = pd.DataFrame(columns = self.OED_account_column_names)
            return self.OED_account_file
            logger.info('Successfully created blank account file for OED')                  
        except Exception as e:
            logger.info('Issue in creating blank account file for OED')
            logger.error(e,exc_info=True)
            print("Error Check Log file")
            sys.exit(0)
     


    """
    Method for reading all json files required.
    """      
    def json_reader(self,FILE_PATH,logger):
        try:
            with open(FILE_PATH) as json_file:  
                    self.json_op = json.load(json_file)
            logger.info('Successfully written output file %s' %FILE_PATH)
            return self.json_op
        except Exception as e:
            logger.info('Issue in writting file %s' %FILE_PATH)
            logger.error(e,exc_info=True)
            print("Error Check Log file")
            sys.exit(0)
        
    
    
    """
    This will write an output csv in output folder in the given directory.
    """   
    def output_write(self,OED_location_file_final,filename,logger):   
        try:
            OED_location_file_final.to_csv(filename, index=False,  encoding = 'utf-8')
            logger.info('Successfully written output file %s' %filename)                  
        except Exception as e:
            logger.info('Issue in writting file %s' %filename)
            logger.error(e,exc_info=True)
            print("Error Check Log file")
            sys.exit(0)
        print("Succesfully written converted file in output folder %s" %filename)    

