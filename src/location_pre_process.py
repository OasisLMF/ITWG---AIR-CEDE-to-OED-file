# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:55:56 2019

@author: kumar.shivam
"""
import sys
import pandas as pd
import ConfigParser
from constants import constants
from db_helper import dbhelper
import numpy as np

class pre_process:
    """
    Preprocess includes connection to the SQL server, reading all required data from the AIR CEDE table.
    These are queries which joins data from multiple table to reflect into one dataframe.
    It also includes reading column names from pre-defined csv and creating black OED table.
    """
    def read_sql_data(self,logger): 
        """
        Reading SQL data from table tLocTerm, tExposureSet, tLocation, tLocFeature, tLayerConditionLocationXref,
        tLocation and tContract.
        These data are joined as per rquirement shared in the documentation.
        """
        try:
            config = ConfigParser.ConfigParser()
            config.read(constants.CONFIG_FILE_PATH)
            self.connection_string = r'Driver='+config.get('dbconnection', 'Driver') +';Server='+config.get('dbconnection', 'Server')+';Database='+config.get('dbconnection', 'Database')+';Trusted_Connection='+config.get('dbconnection', 'TrustedConnection')+';UID='+config.get('dbconnection', 'ID')+';PWD='+config.get('dbconnection', 'PWD')+';'
            logger.info('Successfully Connected to CEDE AIR Database')
        except Exception as e:
            logger.info('Issue in Database Connection')
            logger.error(e,exc_info=True)
            print("Error Check Log file")
            sys.exit(0)

        try:            
            self.query_tLocTm_tLoc_tExSet_tLocFeat =  config.get(constants.LOCATION_QUERY, constants.TLOCTM_TLOC_TEXPSET_TLOCFEAT)                        
            self.AIR_location_file  = dbhelper().data_reader(self.query_tLocTm_tLoc_tExSet_tLocFeat,self.connection_string,None,logger) 
            logger.info('Successfully read data from AIR DB for Tlocterm, Tloc, Texpset, tlocFeat')
        except Exception as e:
            logger.info('Issue in reading data from AIR DB for Tlocterm, Tloc, Texpset, tlocFeat')
            logger.error(e)
            print("Error Check Log file")
            sys.exit(0)

                       
        try:
            self.query_tlclx_tlc = config.get(constants.LOCATION_QUERY, constants.TLCLX_TLC) 
            self.LayerConditionSID  = dbhelper().data_reader(self.query_tlclx_tlc,self.connection_string,None,logger) 
            if len(self.LayerConditionSID) != 0:
                self.AIR_location_file = pd.merge(self.AIR_location_file, self.LayerConditionSID, how='inner', on=['LocationSID','PerilSetCode'])    
            else:
                self.AIR_location_file['CondNumber'] = None
            boolassigner = {True: '1', False: '0'}
            self.AIR_location_file['IsTenant'] = self.AIR_location_file['IsTenant'].map(boolassigner)
            self.AIR_location_file['IsPrimaryLocation'] = self.AIR_location_file['IsPrimaryLocation'].map(boolassigner)
            logger.info('Successfully read data from AIR DB for LayerconditionSID. CondNumber from tlocCondXref, tLayerCondition')
        except Exception as e:   
            logger.info('Issue in reading data from AIR DB for LayerconditionSID. CondNumber from tlocCondXref, tLayerCondition')                  
            logger.error(e,exc_info=True) 
            print("Error Check Log file")
            sys.exit(0)
        return self.AIR_location_file, config.get('dbconnection', 'Database'),config.get('dbconnection', 'Server')
