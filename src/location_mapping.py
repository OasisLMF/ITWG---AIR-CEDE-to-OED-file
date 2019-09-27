# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:40:59 2019

@author: kumar.shivam
"""
import sys
from generic_mapping import genericmapping
from constants import constants
import numpy as np

class mapping:
    """
    The dataframe created from the CEDE AIR database has few columns which are directly mapped without any alteration
    to OED file. This direct mapping is stored in a pre-written json file.
    
    """
    def direct_mapping(self,OED_location_file,AIR_location_file,logger):
        """
        The direct mapping json file is read and used as a dictionary with key value 
        and based on that the AIR data column in written to OED file using corresponding key
        values.
        """
        OED_location_file_direct_mapped = genericmapping().direct_mapping(OED_location_file, AIR_location_file, constants.LOCATION_DIRECT_MAPPING_JSON, logger)
        OED_location_file_direct_mapped['PercentComplete'] = OED_location_file_direct_mapped['PercentComplete'].replace(0.0,None)
        return OED_location_file_direct_mapped
        
    def value_mapping(self,OED_location_file_direct_mapped,AIR_location_file,logger):
        """
        After the direct mapping is done then are few columns which requires data to undergo values mapping.
        These columns include peril mapping, address match level mapping, construction code mapping,
        occupancy mapping and unit mapping.
        These value mappings are written in respective json file.
        These json files are used to map values for the mentioned columns.
        
        """
        genericmapping_obj = genericmapping()
        OED_location_file_direct_mapped = genericmapping_obj.peril_mapper(OED_location_file_direct_mapped,AIR_location_file,[constants.OED_LOC_PERIL_COV_COL,constants.OED_LOC_PERIL_COL],logger)
        OED_location_file_value_mapped = genericmapping_obj.value_mapper(constants.ADRRESS_MATCH_MAPPING,OED_location_file_direct_mapped,constants.ADDRESSMATCH_COL,True,logger)
        OED_location_file_value_mapped = genericmapping_obj.value_mapper(constants.OCCUPANCY_CODE_MAPPING,OED_location_file_direct_mapped,constants.OCCUPANCY_COL,False,logger)
        OED_location_file_value_mapped = genericmapping_obj.value_mapper(constants.CONSTRUCTION_CODE_MAPPING,OED_location_file_direct_mapped,constants.CONSTRUCTION_COL,False,logger)
        OED_location_file_value_mapped = genericmapping_obj.value_mapper(constants.UNIT_MAPPING,OED_location_file_direct_mapped,constants.FLOORAREA_COL,False,logger)
        OED_location_file_value_mapped = genericmapping_obj.value_mapper(constants.UNIT_MAPPING,OED_location_file_direct_mapped,constants.FIRSTFLOOR_COL,False,logger)
        OED_location_file_value_mapped = genericmapping_obj.value_mapper(constants.UNIT_MAPPING,OED_location_file_direct_mapped,constants.GROUNDELEV_COL,False,logger)
        OED_location_file_value_mapped = genericmapping_obj.value_mapper(constants.UNIT_MAPPING,OED_location_file_direct_mapped,constants.BASEFLDELEV_COL,False,logger)
        OED_location_file_value_mapped = genericmapping_obj.value_mapper(constants.UNIT_MAPPING,OED_location_file_direct_mapped,constants.BUILDINGHT_COL,False,logger)

        try:
            OED_location_file_value_mapped['GeogScheme1'] = "XSUBA"
            OED_location_file_value_mapped['GeogScheme2'] = "XSUB2"
            logger.info('Successfully assigning Geographic scheme with constant')
        except Exception as e:
            logger.info('Issue in assigning Geographic scheme with constant')
            logger.error(e,exc_info=True)
            print("Error Check Log file")
            sys.exit(0)
        return OED_location_file_value_mapped

    def conditional_mapping(self,OED_location_file_value_mapped, AIR_location_file,logger):
        """
        There are columns which are related financial terms and condition.
        These columns are based on LimitTypeCode and DeductibleTypeCode.
        The conditional mapping are done on basis of these two columns with condditions.
        """
        try:
            """
            Limit Cases
            """

            OED_location_file_value_mapped['LocLimit6All'] = np.where(AIR_location_file['LimitTypeCode'] == 'S',AIR_location_file['Limit1'],None)
            OED_location_file_value_mapped['LocLimit1Building'] = np.where(AIR_location_file['LimitTypeCode'] == 'C',AIR_location_file['Limit1'],None)
            OED_location_file_value_mapped['LocLimit2Other'] = np.where(AIR_location_file['LimitTypeCode'] == 'C', AIR_location_file['Limit2'],None)
            OED_location_file_value_mapped['LocLimit3Contents'] = np.where(AIR_location_file['LimitTypeCode'] == 'C', AIR_location_file['Limit3'],None)
            OED_location_file_value_mapped['LocLimit4BI'] = np.where(AIR_location_file['LimitTypeCode'] == 'C',AIR_location_file['Limit4'],None)

            """
            Deductible Cases
            """
            OED_location_file_value_mapped['LocDed1Building'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'PL',AIR_location_file['Deductible1'],None)
            OED_location_file_value_mapped['LocDed2Other'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'PL',AIR_location_file['Deductible2'],None)
            OED_location_file_value_mapped['LocDed3Contents'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'PL',AIR_location_file['Deductible3'],None)
            OED_location_file_value_mapped['LocDed4BI'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'PL',AIR_location_file['Deductible4'],None)
            OED_location_file_value_mapped['LocDedType1Building'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'PL',1,None)
            OED_location_file_value_mapped['LocDedType2Other'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'PL',1,None)
            OED_location_file_value_mapped['LocDedType3Contents'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'PL',1,None)
            OED_location_file_value_mapped['LocDedType4BI'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'PL',1,None)

            OED_location_file_value_mapped['LocDedType2Other'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'MP',AIR_location_file['Deductible1'], OED_location_file_value_mapped['LocDedType2Other'])
            OED_location_file_value_mapped['LocDedType3Contents'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'MP', 5, OED_location_file_value_mapped['LocDedType3Contents'])
            OED_location_file_value_mapped['LocDed4BI'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'MP',2, OED_location_file_value_mapped['LocDed4BI'])

            OED_location_file_value_mapped['LocDed5PD'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'ML', AIR_location_file['Deductible2'], None)
            OED_location_file_value_mapped['LocDedType5PD'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'ML', 1, None)
            OED_location_file_value_mapped['LocMaxDed5PD'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'ML', AIR_location_file['Deductible1'], None)
            OED_location_file_value_mapped['LocDed4BI'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'ML', AIR_location_file['Deductible4'], OED_location_file_value_mapped['LocDed4BI'])

            AIR_location_file['Deductible1'] = np.where(AIR_location_file['Deductible1']<1,AIR_location_file['Deductible1']*AIR_location_file['Limit1'],AIR_location_file['Deductible1'])
            AIR_location_file['Deductible2'] = np.where(AIR_location_file['Deductible2']<1,AIR_location_file['Deductible2']*AIR_location_file['Limit2'],AIR_location_file['Deductible2'])
            AIR_location_file['Deductible3'] = np.where(AIR_location_file['Deductible3']<1,AIR_location_file['Deductible3']*AIR_location_file['Limit3'],AIR_location_file['Deductible3'])
            AIR_location_file['Deductible4'] = np.where(AIR_location_file['Deductible4']<1,AIR_location_file['Deductible4']*AIR_location_file['Limit4'],AIR_location_file['Deductible4'])

            OED_location_file_value_mapped['LocDed1Building'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'C', AIR_location_file['Deductible1'], OED_location_file_value_mapped['LocDed1Building'])
            OED_location_file_value_mapped['LocDed2Other'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'C', AIR_location_file['Deductible2'], OED_location_file_value_mapped['LocDed2Other'])
            OED_location_file_value_mapped['LocDed3Contents'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'C', AIR_location_file['Deductible3'], OED_location_file_value_mapped['LocDed3Contents'])
            OED_location_file_value_mapped['LocDed4BI'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'C', AIR_location_file['Deductible4'], OED_location_file_value_mapped['LocDed4BI'])

            OED_location_file_value_mapped['LocDed5PD'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'CB', AIR_location_file['Deductible1']+AIR_location_file['Deductible2']+AIR_location_file['Deductible3'], OED_location_file_value_mapped['LocDed5PD'])
            OED_location_file_value_mapped['LocDed5PD'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'CT', AIR_location_file['Deductible1']+AIR_location_file['Deductible2']+AIR_location_file['Deductible3'], OED_location_file_value_mapped['LocDed5PD'])
            OED_location_file_value_mapped['LocDed4BI'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'CT',AIR_location_file['Deductible4'], OED_location_file_value_mapped['LocDed4BI'])

            OED_location_file_value_mapped['LocDed6All'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'S', AIR_location_file['Deductible1']+AIR_location_file['Deductible2']+AIR_location_file['Deductible3']+AIR_location_file['Deductible4'], None)
            OED_location_file_value_mapped['LocDed6All'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'FR', AIR_location_file['Deductible1']+AIR_location_file['Deductible2']+AIR_location_file['Deductible3']+AIR_location_file['Deductible4'], OED_location_file_value_mapped['LocDed6All'])
            OED_location_file_value_mapped['LocDedCode6All'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'FR',1,None)

            OED_location_file_value_mapped['LocDed5PD'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'CT',AIR_location_file['Deductible1'], OED_location_file_value_mapped['LocDed5PD'])
            OED_location_file_value_mapped['LocDedType5PD'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'CT',1, OED_location_file_value_mapped['LocDedType5PD'])
            OED_location_file_value_mapped['LocDed4BI'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'CT',AIR_location_file['Deductible4'], OED_location_file_value_mapped['LocDed4BI'])
            OED_location_file_value_mapped['LocDedCode4BI'] = np.where(AIR_location_file['DeductibleTypeCode'] == 'CT',1, None)
            logger.info('Successfully assigning Limit and Deductible term value as per DeductibleTypeCode condition')
        except Exception as e:
            logger.info('Issue in assigning Limit Deductible term value as per DeductibleTypeCode condition')
            logger.error(e,exc_info=True)
            print("Error Check Log file")
            sys.exit(0)

        try:
            OED_location_file_value_mapped['LocParticipation'] = AIR_location_file['Participation2']
            OED_location_file_value_mapped['FloodDefenseHeightUnit'] = 1
            OED_location_file_value_mapped['CondPriority'] = 1
            logger.info('Successfully assigning CondPriority, LocParticipation term value')
        except Exception as e:
            logger.info('Issue in assigning CondPriority, LocParticipation term value')
            logger.error(e,exc_info=True)
            print("Error Check Log file")
            sys.exit(0)    
        OED_location_file_final = OED_location_file_value_mapped
        return OED_location_file_final