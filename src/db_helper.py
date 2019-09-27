# -*- coding: utf-8 -*-
"""
Created on Wed Jul 03 12:44:23 2019

@author: kumar.shivam
"""
import pyodbc
import pandas as pd
import sys

class dbhelper:
    def data_reader(self,query,connection_string,col_name,logger):
        """
        reading data from sql.
        col_name is taken as index.
        query is also taken as argument in this function.
        """
        try:
            self.sql_conn_AIR = pyodbc.connect(connection_string)
            self.read_data = pd.read_sql(query, self.sql_conn_AIR, index_col = col_name) 
            self.sql_conn_AIR.close()
            logger.info('Read data for connection string %s' %connection_string)
            return self.read_data
        except Exception as e:
            logger.info('Issue in reading data for connection string %s'%connection_string)
            logger.error(e,exc_info=True)
            print("Error Check Log file")
            sys.exit(0)
         
    
