from typing import *

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        result = 0
        
        for box, units in boxTypes:
            if truckSize < box:
                result += truckSize * units
                break
            else:
                truckSize -= box
                result += box * units
        
        return result