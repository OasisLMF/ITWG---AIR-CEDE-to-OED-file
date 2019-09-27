# -*- coding: utf-8 -*- 
"""
Created on Mon Jun 24 14:30:13 2019

@author: kumar.shivam(kumar.shivam@xceedance.com)
"""

from location_mapping import mapping
from location_pre_process import pre_process
from logger import logging_process
from file_helper import filehelper
from constants import constants
from generic_mapping import genericmapping
from account_mapping import mapping_account
from account_pre_process import AIR_base_file
import time


def main():
    """
    This is the main script..
    Logger is initiated for logging purpose.
    Calling all the instances here in this block.
    """
    start_time = time.time()
    print("Process started!")    
    logger, logging = logging_process()
    print("Loggging process started...")
    AIR_location_file, database, server = pre_process().read_sql_data(logger)
    print("Starting to convert CEDE %s on %s to OED file..." %(database, server))
    print("AIR location data prepared for mapping...")
    filehelper_obj = filehelper()
    OED_location_file = filehelper_obj.OED_location_file_preprocess(logger)
    print("OED blank location file prepared...")
    mapping_obj = mapping()
    OED_location_file_direct_mapped = mapping_obj.direct_mapping(OED_location_file,AIR_location_file,logger)
    print("Direct mapping is done for OED location file...")
    OED_location_file_value_mapped = mapping_obj.value_mapping(OED_location_file_direct_mapped,AIR_location_file,logger)
    print("Value mapping is done for location...")
    OED_location_file_final = mapping_obj.conditional_mapping(OED_location_file_value_mapped,AIR_location_file,logger)
    print("Conditional mapping done for location file...")
    filehelper_obj.output_write(OED_location_file_final,constants.OP_LOCATION,logger)

    OED_account_file_blank = filehelper().OED_account_file_blank(logger)
    print("OED blank account file prepared...")
    AIR_account_file = AIR_base_file().AIR_account_read(logger) 
    print("AIR account data prepared for mapping...")
    genericmapping_obj = genericmapping()
    OED_direct_mapped = genericmapping_obj.direct_mapping(OED_account_file_blank, AIR_account_file, constants.ACCOUNT_DIRECT_MAPPING_JSON, logger)
    print("OED account direct mapping done...")
    OED_file_value_mapped = genericmapping_obj.peril_mapper(OED_direct_mapped, AIR_account_file,[constants.OED_ACC_PERIL_COL,constants.OED_POL_PERIL_COV,constants.OED_POL_PERIL,constants.OED_COND_PERIL],logger)
    print("OED account peril mapping done...")
    OED_conditional_mapped = mapping_account().conditional_mapping(OED_file_value_mapped, AIR_account_file,logger)
    print("OED conditional mapping done...")
    filehelper_obj.output_write(OED_conditional_mapped, constants.OP_ACCOUNT , logger)
    logging.shutdown()
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()


