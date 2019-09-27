# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 13:01:09 2019

@author: kumar.shivam
"""
import sys
from file_helper import filehelper
from db_helper import dbhelper
import ConfigParser
from constants import constants


class genericmapping:
    def direct_mapping(self,output_file,base_file,json_path,logger):
        """
        The direct mapping json file is read and used as a dictionary with key value 
        and based on that the AIR data column in written to OED file using corresponding key
        values.
        """
        try:                       
            self.json_direct_mapping = filehelper().json_reader(json_path,logger)
            logger.info('Successfully loaded direct mapping json file %s' %json_path)                  
        except Exception as e:
            logger.info('Issue in loading direct mapping json file %s' %json_path) 
            logger.error(e)
            print("Error Check Log file")
            sys.exit(0)           
        try:
            for key in self.json_direct_mapping:  
                output_file[key] = base_file[self.json_direct_mapping[key]]             
            logger.info('Successfully assign data in OED file as per direct mapping json file %s' %json_path)                  
        except Exception as e:
            logger.info('Error in assigning data in OED file as per direct mapping json file %s' %json_path) 
            logger.error(e,exc_info=True)
            print("Error Check Log file")
            sys.exit(0)        
        return output_file



    def peril_mapper(self,OED_file_direct_mapped,AIR_file,mapping_columns,logger):
        """
        After the direct mapping is done then are few columns which requires data to undergo values mapping.
        These columns include peril mapping, address match level mapping, construction code mapping,
        occupancy mapping and unit mapping.
        These value mappings are written in respective json file.
        These json files are used to map values for the mentioned columns.
        
        """
        try:
            self.peril_mapping = filehelper().json_reader(constants.PERIL_MAPPING_JSON,logger)
            logger.info('Successfully read peril value mapping data for mapping column')
        except Exception as e:
            logger.info('Issue in reading peril value mapping data for mapping column')
            logger.error(e,exc_info=True)  
            print("Error Check Log file")   
            sys.exit(0)                                
            
        try:
            config = ConfigParser.ConfigParser()
            config.read(constants.CONFIG_FILE_PATH)
            self.connection_string = r'Driver='+config.get('reference_dbconnection', 'Driver') +';Server='+config.get('reference_dbconnection', 'Server')+';Database='+config.get('reference_dbconnection', 'Database')+';Trusted_Connection='+config.get('reference_dbconnection', 'TrustedConnection')+';UID='+config.get('reference_dbconnection', 'ID')+';PWD='+config.get('reference_dbconnection', 'PWD')+';'            
            self.query_PERIL_SET = config.get(constants.LOCATION_QUERY,constants.PERIL_SET_CODE,logger) 
            self.peril_set_code  = dbhelper().data_reader(self.query_PERIL_SET,self.connection_string,'PerilSetCode',logger) 
            logger.info('Successfully connected to reference database for peril mapping for mapping column %s' %mapping_columns)
        except Exception as e:
            logger.info('Issue in connectiing to reference database for peril mapping for mapping column %s' %mapping_columns)
            logger.error(e,exc_info=True)   
            print("Error Check Log file")
            sys.exit(0)

        for mapping_column in mapping_columns:
            OED_file_direct_mapped[mapping_column] = OED_file_direct_mapped[mapping_column].astype(str)
        try:
            for index in OED_file_direct_mapped.index:
                for mapping_column in mapping_columns:
                     if OED_file_direct_mapped.at[index, mapping_column] != 'nan' and OED_file_direct_mapped.at[index, mapping_column] != 'None' and OED_file_direct_mapped.at[index, mapping_column] != '-1':
                            OED_file_direct_mapped.at[index, mapping_column] = OED_file_direct_mapped.at[index,mapping_column].split(".")[0]
                            OED_file_direct_mapped.at[index,mapping_column] =  self.peril_set_code.at[int(OED_file_direct_mapped.at[index,mapping_column]),'PerilSet']
                            temp_perils =  OED_file_direct_mapped.at[index, mapping_column].split(', ')
                            OED_peril_list = []
                            for peril in temp_perils:
                                OED_peril = self.peril_mapping[peril]
                                OED_peril_list.append(OED_peril)
                            OED_peril_list = list(set(OED_peril_list))
                            OED_peril_final = ';'.join(OED_peril_list)
                            OED_file_direct_mapped.at[index, mapping_column] = OED_peril_final
                     else:
                            OED_file_direct_mapped.at[index, mapping_column] = 'AA1'
            logger.info('Successfully assigned peril value for LocPeril data for mapping column')
        except Exception as e:
            logger.info('Issue in assigning peril value for LocPeril data for mapping column %s' %mapping_column)
            logger.error(e,exc_info=True)
            print("Error Check Log file")
            sys.exit(0)
        OED_file_value_mapped = OED_file_direct_mapped
        return OED_file_value_mapped  
    
    
    def value_mapper(self, json_path,OED_file_direct_mapped,column_name,str_to_int,logger):
        """
        A json mapping file is read.
        It performs value mapping in loop with the input file length.
        """
        try:
            self.json_value_mapper = filehelper().json_reader(json_path,logger)
            if str_to_int:
                OED_file_direct_mapped[column_name] = OED_file_direct_mapped[column_name].map(self.json_value_mapper)
            else:
                OED_file_direct_mapped[column_name] = OED_file_direct_mapped[column_name].apply('{}'.format)
                OED_file_direct_mapped[column_name] = OED_file_direct_mapped[column_name].map(self.json_value_mapper)
            logger.info('Successfully assigned value as per json mapping for %s' %json_path)
            return OED_file_direct_mapped
        except Exception as e:
            logger.info('Issue in assigning value as per json mapping for %s' %json_path)
            logger.error(e,exc_info=True)   
            print("Error Check Log file")
            sys.exit(0) 
            
        