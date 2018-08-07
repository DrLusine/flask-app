
from measurement.utils import guess
from abc import ABC, abstractmethod

class BuildingVolCalculator(ABC):
    def __init__(self, areaParams, floorHeightParams): 
        self.areaParams = guess(areaParams['areaValue'], areaParams['areaUnit'])
        self.floorHeightParams = guess(floorHeightParams['heightValue'], floorHeightParams['heightUnit'])
        super().__init__()

    @abstractmethod
    def calculateVolume(self):        
        pass
