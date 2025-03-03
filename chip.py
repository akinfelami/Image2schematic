
from point import *

class chip:
    
    IcName = None
    Iclibrary = None
    # an array to store all pointers to the pcb points that are connected to this ic
    pins = []
    # up left most cornor
    UpLeftMostPoint = point()
    # down right most cornor
    DownRightMostPoint = point()
    
    ConnectedToPCB = None

    def __init__(self, UpLeftMostPoint = None, DownRightMostPoint = None, IcName = None, Iclibrary = None, pins: list[point] = None, ConnectedToPCB = None) -> None:
        #print(f"Chip init! Name: {IcName}")
        
        # NOTE: UpLeftMostPoint and DownRightMostPoint are not electrical points!
        if UpLeftMostPoint: self.UpLeftMostPoint = UpLeftMostPoint
        else: self.UpLeftMostPoint = point()
        if DownRightMostPoint: self.DownRightMostPoint = DownRightMostPoint
        else: self.DownRightMostPoint = point()

        if pins: 
            self.pins = pins
            # looping over recived pins to set the ConnectedToIC variable
            for point in pins: point.ConnectedToChip = self
        else: self.pins = [] # => avoids "shared memory"

        if IcName: self.IcName = IcName
        if Iclibrary: self.Iclibrary = Iclibrary

        if ConnectedToPCB: self.ConnectedToPCB = ConnectedToPCB

    def CalculateDistFromRightMostPointToArbPoint(self, Point: point) -> float:
        return Point.CalculateDistanceToOtherPoint(point(self.DownRightMostPoint.x, self.UpLeftMostPoint.y))

    def CalculateDistFromleftMostPointToArbPoint(self, Point) -> float:
        return Point.CalculateDistanceToOtherPoint(self.UpLeftMostPoint)

    def ConnectPINS(self, PINS: list[point]):
        self.pins = PINS
        for PIN in PINS:
            PIN.ConnectedToChip = self
            # Dont think i need this check
            if PIN.ConnectedToPCB is not None:
                PIN.ConnectedToPCB = self.ConnectedToPCB

    def printInfo(self, verbose = 0) -> None:
        print(f"Chip name: {self.IcName}")
        if verbose > 0:
            print("Pins:")
            for pin in self.pins:
                print(f"[{pin.x}, {pin.y}]")