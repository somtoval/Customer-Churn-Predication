import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

import pandas as pd

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
                 AccountWeeks:float,
                 ContractRenewal:float,
                 DataPlan:float,
                 DataUsage:float,
                 CustServCalls:float,
                 DayMins:float,
                 DayCalls:float,
                 MonthlyCharge:float,
                 OverageFee:float,
                 RoamMins:float):
        
        self.AccountWeeks=AccountWeeks
        self.ContractRenewal = ContractRenewal
        self.DataPlan = DataPlan
        self.DataUsage=DataUsage
        self.CustServCalls = CustServCalls
        self.DayMins=DayMins
        self.DayCalls=DayCalls
        self.MonthlyCharge=MonthlyCharge
        self.OverageFee=OverageFee
        self.RoamMins = RoamMins

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'AccountWeeks':[self.AccountWeeks],
                'ContractRenewal':[self.ContractRenewal],
                'DataPlan':[self.DataPlan],
                'DataUsage':[self.DataUsage],
                'CustServCalls':[self.CustServCalls],
                'DayMins':[self.DayMins],
                'DayCalls':[self.DayCalls],
                'MonthlyCharge':[self.MonthlyCharge],
                'OverageFee':[self.OverageFee],
                'RoamMins':[self.RoamMins],
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)