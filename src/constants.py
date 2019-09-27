# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:34:03 2019

@author: kumar.shivam
"""

class constants:
    """
    All the constants are stored in this constants class which is used in different methods 
    of the surce code.
    """
    
    """
    File Paths
    """
    CONFIG_FILE_PATH = r"..\augmentations\config.ini"  
    LOCATION_COLUMN_NAMES = r"..\augmentations\location_column_names.csv"
    ACCOUNT_COLUMN_NAMES = r"..\augmentations\account_column_names.csv"
    LOCATION_DIRECT_MAPPING_JSON = r"..\augmentations\location_direct_mapping.json"
    ACCOUNT_DIRECT_MAPPING_JSON = r"..\augmentations\account_direct_mapping.json"
    PERIL_MAPPING_JSON = r"..\augmentations\peril_mapping.json"
    ADRRESS_MATCH_MAPPING = r"..\augmentations\address_match_mapping.json"
    CONSTRUCTION_CODE_MAPPING = r"..\augmentations\construction_codes.json"
    OCCUPANCY_CODE_MAPPING = r"..\augmentations\occupancy_codes.json"
    UNIT_MAPPING = r"..\augmentations\unit_mapping.json"

    """
    Queries tags in the config files.
    """
    ACCOUNT_QUERY = 'queries_account'
    TLC_DISTINCT = 'query_tlc_distinct'
    TLC_TL_TC_TEXP = 'query_tlc_tl_tc_texp'
    PERIL_SET_CODE = 'query_peril_setcode'
        
    LOCATION_QUERY = 'queries_location'
    TLOCTM_TLOC_TEXPSET_TLOCFEAT = 'query_tLocTm_tLoc_tExSet_tLocFeat'
    TLCLX_TLC = 'query_tlclx_tlc_tlt'
        
    """
    Column names in the code.
    """
    OED_LOC_PERIL_COL = "LocPeril"
    OED_LOC_PERIL_COV_COL = 'LocPerilsCovered'
    OED_ACC_PERIL_COL = "AccPeril"
    OED_POL_PERIL_COV = 'PolPerilsCovered'
    OED_POL_PERIL = 'PolPeril'
    OED_COND_PERIL = 'CondPeril'
    ADDRESSMATCH_COL = 'AddressMatch' 
    OCCUPANCY_COL = 'OccupancyCode'
    CONSTRUCTION_COL = 'ConstructionCode'
    FLOORAREA_COL = 'FloorAreaUnit'
    FIRSTFLOOR_COL = 'FirstFloorHeightUnit'
    GROUNDELEV_COL = 'GroundElevationUnit'
    BASEFLDELEV_COL = 'BaseFloodElevationUnit'
    BUILDINGHT_COL = 'BuildingHeightUnit'

    """
    Output file for writting files.
    """
    OP_ACCOUNT = r"..\output\OED_account_input.csv"
    OP_LOCATION = r"..\output\OED_location_input.csv"