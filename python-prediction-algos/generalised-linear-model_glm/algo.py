# This file is the actual code for the custom Python algorithm dev-glm_glm
from dataiku.doctor.plugins.custom_prediction_algorithm import BaseCustomPredictionAlgorithm
from generalisedlinearmodel.dku_glm import GLM

class CustomPredictionAlgorithm(BaseCustomPredictionAlgorithm):    
    
    def __init__(self, prediction_type=None, params=None):   
        
        self.params = params
        self.clf = GLM(
            link=params.get("link"),
            family=params.get("family"),
            alpha=params.get("alpha"),
            power=params.get("power")
        )
        super(CustomPredictionAlgorithm, self).__init__(prediction_type, self.params)
                                     
    def get_clf(self):

        return self.clf