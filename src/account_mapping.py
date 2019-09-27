# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:19:45 2019

@author: kumar.shivam
"""
import sys
import numpy as np

class mapping_account:
    """
    The dataframe created from the CEDE AIR database has few columns which are directly mapped without any alteration
    to OED file. 
    
    """
    def conditional_mapping(self,OED_file_value_mapped, AIR_account_file,logger):
        """
        The coditional mapping is on limits, deductible type code.
        Assignment is done through if else statement.
        
        """
        try:

            OED_file_value_mapped['CondLimit6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'N') & (AIR_account_file['OccLimitTypeCode'] == 'B'),AIR_account_file['OccLimit1'],None)
            OED_file_value_mapped['CondDed6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'N') & (AIR_account_file['OccLimitTypeCode'] == 'B'),AIR_account_file['Attachment1'],None)

            OED_file_value_mapped['CondLimit6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MI') & (AIR_account_file['OccLimitTypeCode'] == 'B'),AIR_account_file['OccLimit1'], OED_file_value_mapped['CondLimit6All'])
            OED_file_value_mapped['CondDed6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MI') & (AIR_account_file['OccLimitTypeCode'] == 'B'),AIR_account_file['Attachment1'], OED_file_value_mapped['CondDed6All'])
            OED_file_value_mapped['CondMinDed6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MI') & (AIR_account_file['OccLimitTypeCode'] == 'B'),AIR_account_file['Deductible1'], None)

            OED_file_value_mapped['CondLimit6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MA') & (AIR_account_file['OccLimitTypeCode'] == 'B'),AIR_account_file['OccLimit1'], OED_file_value_mapped['CondLimit6All'])
            OED_file_value_mapped['CondDed6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MA') & (AIR_account_file['OccLimitTypeCode'] == 'B'),AIR_account_file['Attachment1'], OED_file_value_mapped['CondDed6All'])
            OED_file_value_mapped['CondMaxDed6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MA') & (AIR_account_file['OccLimitTypeCode'] == 'B'),AIR_account_file['Deductible2'], None)

            OED_file_value_mapped['CondLimit6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MM') & (AIR_account_file['OccLimitTypeCode'] == 'B'),AIR_account_file['OccLimit1'], OED_file_value_mapped['CondLimit6All'])
            OED_file_value_mapped['CondDed6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MM') & (AIR_account_file['OccLimitTypeCode'] == 'B'),AIR_account_file['Attachment1'], OED_file_value_mapped['CondDed6All'])
            OED_file_value_mapped['CondMinDed6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MM') & (AIR_account_file['OccLimitTypeCode'] == 'B'),AIR_account_file['Deductible1'], OED_file_value_mapped['CondMinDed6All'])
            OED_file_value_mapped['CondMaxDed6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MM') & (AIR_account_file['OccLimitTypeCode'] == 'B'),AIR_account_file['Deductible2'], OED_file_value_mapped['CondMaxDed6All'])

            OED_file_value_mapped['CondLimit6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'N') & (AIR_account_file['OccLimitTypeCode'] == 'E'),AIR_account_file['OccLimit2'], OED_file_value_mapped['CondLimit6All'])
            OED_file_value_mapped['CondDed6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'N') & (AIR_account_file['OccLimitTypeCode'] == 'E'),AIR_account_file['Attachment1'], OED_file_value_mapped['CondDed6All'])

            OED_file_value_mapped['CondLimit6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MI') & (AIR_account_file['OccLimitTypeCode'] == 'E'),AIR_account_file['OccLimit2'], OED_file_value_mapped['CondLimit6All'])
            OED_file_value_mapped['CondDed6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MI') & (AIR_account_file['OccLimitTypeCode'] == 'E'), AIR_account_file['Attachment1'], OED_file_value_mapped['CondDed6All'])
            OED_file_value_mapped['CondMinDed6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MI') & (AIR_account_file['OccLimitTypeCode'] == 'E'), AIR_account_file['Deductible1'], OED_file_value_mapped['CondMinDed6All'])

            OED_file_value_mapped['CondLimit6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MA') & (AIR_account_file['OccLimitTypeCode'] == 'E'),AIR_account_file['OccLimit2'], OED_file_value_mapped['CondLimit6All'])
            OED_file_value_mapped['CondDed6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MA') & (AIR_account_file['OccLimitTypeCode'] == 'E'), AIR_account_file['Attachment1'], OED_file_value_mapped['CondDed6All'])
            OED_file_value_mapped['CondMaxDed6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MA') & (AIR_account_file['OccLimitTypeCode'] == 'E'), AIR_account_file['Deductible2'], None)

            OED_file_value_mapped['CondLimit6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MM') & (AIR_account_file['OccLimitTypeCode'] == 'E'),AIR_account_file['OccLimit2'], OED_file_value_mapped['CondLimit6All'])
            OED_file_value_mapped['CondDed6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MM') & (AIR_account_file['OccLimitTypeCode'] == 'E'), AIR_account_file['Attachment1'], OED_file_value_mapped['CondDed6All'])
            OED_file_value_mapped['CondMinDed6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MM') & (AIR_account_file['OccLimitTypeCode'] == 'E'), AIR_account_file['Deductible1'], OED_file_value_mapped['CondMinDed6All'])
            OED_file_value_mapped['CondMaxDed6All'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'MM') & (AIR_account_file['OccLimitTypeCode'] == 'E'),AIR_account_file['Deductible2'], OED_file_value_mapped['CondMaxDed6All'])

            OED_file_value_mapped['CondLimit5PD'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'N') & (AIR_account_file['OccLimitTypeCode'] == 'CB'), AIR_account_file['OccLimit1'], None)
            OED_file_value_mapped['CondDed5PD'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'N') & (AIR_account_file['OccLimitTypeCode'] == 'CB'), AIR_account_file['Attachment1'], None)
            OED_file_value_mapped['CondLimit4BI'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'N') & (AIR_account_file['OccLimitTypeCode'] == 'CB'),AIR_account_file['OccLimit4'], None)
            OED_file_value_mapped['CondDed4BI'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'N') & (AIR_account_file['OccLimitTypeCode'] == 'CB'), AIR_account_file['Attachment4'], None)

            OED_file_value_mapped['CondLimit1Building'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'N') & (AIR_account_file['OccLimitTypeCode'] == 'C'), AIR_account_file['OccLimit1'], None)
            OED_file_value_mapped['CondDed1Building'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'N') & (AIR_account_file['OccLimitTypeCode'] == 'C'), AIR_account_file['Attachment1'], None)
            OED_file_value_mapped['CondLimit2Other'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'N') & (AIR_account_file['OccLimitTypeCode'] == 'C'),AIR_account_file['OccLimit2'], None)
            OED_file_value_mapped['CondDed2Other'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'N') & (AIR_account_file['OccLimitTypeCode'] == 'C'), AIR_account_file['Attachment2'], None)
            OED_file_value_mapped['CondLimit3Contents'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'N') & (AIR_account_file['OccLimitTypeCode'] == 'C'), AIR_account_file['OccLimit3'], None)
            OED_file_value_mapped['CondDed3Contents'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'N') & (AIR_account_file['OccLimitTypeCode'] == 'C'), AIR_account_file['Attachment3'], None)
            OED_file_value_mapped['CondLimit4BI'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'N') & (AIR_account_file['OccLimitTypeCode'] == 'C'),AIR_account_file['OccLimit4'], OED_file_value_mapped['CondLimit4BI'])
            OED_file_value_mapped['CondDed4BI'] = np.where((AIR_account_file['DeductibleTypeCode'] == 'N') & (AIR_account_file['OccLimitTypeCode'] == 'C'), AIR_account_file['Attachment4'], OED_file_value_mapped['CondDed4BI'])


            OED_file_value_mapped['LayerParticipation'] = np.where(AIR_account_file['OccLimitTypeCodeTL'] == 'E', AIR_account_file['OccParticipation'], None)
            OED_file_value_mapped['LayerLimit'] = np.where(AIR_account_file['OccLimitTypeCodeTL'] == 'E', AIR_account_file['OccTotalLimit'], None)
            OED_file_value_mapped['LayerAttachment'] = np.where((AIR_account_file['OccLimitTypeCodeTL'] == 'E') & (AIR_account_file['AttachmentPoint'] == 0) & (AIR_account_file['DeductibleTypeCodeTL'] == 'AP') & (AIR_account_file['Deductible1TL'] > 0),AIR_account_file['Deductible1TL'], AIR_account_file['AttachmentPoint'])

            OED_file_value_mapped['LayerLimit'] = np.where(AIR_account_file['OccLimitTypeCodeTL'] == 'B', AIR_account_file['OccTotalLimit'], OED_file_value_mapped['LayerLimit'])
            OED_file_value_mapped['LayerLimit'] = np.where(AIR_account_file['OccLimitTypeCodeTL'] == 'N', 0, OED_file_value_mapped['LayerLimit'])

            OED_file_value_mapped['PolDed6All'] = np.where(AIR_account_file['DeductibleTypeCodeTL'] == 'B', AIR_account_file['Deductible1TL'], None)

            OED_file_value_mapped['PolDed6All'] = np.where(AIR_account_file['DeductibleTypeCodeTL'] == 'FR', AIR_account_file['Deductible1TL'], OED_file_value_mapped['PolDed6All'])
            OED_file_value_mapped['PolDedCode6All'] = np.where(AIR_account_file['DeductibleTypeCodeTL'] == 'FR', 2, None)

            OED_file_value_mapped['PolDed6All'] = np.where(AIR_account_file['DeductibleTypeCodeTL'] == 'PL', AIR_account_file['Deductible1TL'], OED_file_value_mapped['PolDed6All'])
            OED_file_value_mapped['PolDedType6All'] = np.where(AIR_account_file['DeductibleTypeCodeTL'] == 'PL', 1, None)

            OED_file_value_mapped['PolMinDed6All'] = np.where(AIR_account_file['DeductibleTypeCodeTL'] == 'MI', AIR_account_file['Deductible1TL'], None)

            OED_file_value_mapped['PolMaxDed6All'] = np.where(AIR_account_file['DeductibleTypeCodeTL'] == 'MA', AIR_account_file['Deductible2TL'], None)

            OED_file_value_mapped['PolMinDed6All'] = np.where(AIR_account_file['DeductibleTypeCodeTL'] == 'MM', AIR_account_file['Deductible1TL'], OED_file_value_mapped['PolMinDed6All'])
            OED_file_value_mapped['PolMaxDed6All'] = np.where(AIR_account_file['DeductibleTypeCodeTL'] == 'MM', AIR_account_file['Deductible2TL'], OED_file_value_mapped['PolMaxDed6All'])

            OED_file_value_mapped['PolNumber'] = OED_file_value_mapped['PolNumber'].apply(lambda x: "None" if x == None else x)
            logger.info('Successfully done conditional mapping for account file.')
        except Exception as e:
            logger.info('Issue in conditional mapping for account file.')
            logger.error(e,exc_info=True)
            print("Error Check Log file")
            sys.exit(0)
        return OED_file_value_mapped   
                    