
from measurement.utils import guess
from services.building_vol_calculator.building_vol_calculator import BuildingVolCalculator

class BuildingVolMetresCalculator(BuildingVolCalculator):
    def __init__(self, areaParams, floorHeightParams): 
        super().__init__(areaParams, floorHeightParams)

    def calculateVolume(self):        
        return self.areaParams.sq_m * self.floorHeightParams.m
