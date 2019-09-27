# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:36:26 2019

@author: kumar.shivam
"""
import ConfigParser
from constants import constants
from db_helper import dbhelper
import sys
import pandas as pd

class AIR_base_file:    
    def AIR_account_read(self,logger):   
        """
        This function is to create AIR account consolidated data.
        This data is used as base dataframe and mapped through various mappings in subsequent steps.
        """
        try:
            config = ConfigParser.ConfigParser()
            config.read(constants.CONFIG_FILE_PATH)
            self.connection_string = r'Driver={SQL Server};Server='+config.get('dbconnection', 'Server')+';Database='+config.get('dbconnection', 'Database')+';Trusted_Connection='+config.get('dbconnection', 'TrustedConnection')+';UID='+config.get('dbconnection', 'ID')+';PWD='+config.get('dbconnection', 'PWD')+';'

            self.query_TLC_DISTINCT = config.get(constants.ACCOUNT_QUERY,constants.TLC_DISTINCT)
            self.Condname_num = dbhelper().data_reader(self.query_TLC_DISTINCT, self.connection_string,None,logger) 

            self.query_TLC_TL_TC_TEXP = config.get(constants.ACCOUNT_QUERY,constants.TLC_TL_TC_TEXP)
            self.AIR_account_file = dbhelper().data_reader(self.query_TLC_TL_TC_TEXP, self.connection_string, None, logger)

            if len(self.Condname_num) != 0:
                self.AIR_account_file = pd.merge(self.AIR_account_file, self.Condname_num, how='inner', on=['ContractSID','AppliesToTag'])
                self.AIR_account_file = self.AIR_account_file.rename(columns = {"LayerConditionSID": "CondNumber","AppliesToTag": "CondName"})
            else:
                self.AIR_account_file['CondNumber'] = None
                self.AIR_account_file['CondName'] = None

            logger.info('Successfully read AIR DB and created account file')
            return self.AIR_account_file
        except Exception as e:
            logger.info('Issue in reading AIR DB and creating account file')
            logger.error(e,exc_info=True)
            print("Error Check Log file")
            sys.exit(0)
         