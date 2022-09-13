import time

class Carousel:
    def __init__(self) -> None:
        self.totalSlots = 32
        self.slotsUsed = 0
        self.currentSlot = 0
        self.slots = [None] * self.totalSlots

    def hasSpace(self) -> bool:
        return self.slotsUsed < self.totalSlots
    
    def addBiscuit(self, time) -> None:
        for i in range(0, self.totalSlots):
            if not self.slots[i]:
                self.moveTo(i)
                # push from hopper
                self.slots[i] = time
                self.slotsUsed += 1
                return

    def checkTimeInCarousel(self) -> None:
        # get current time in same format as data is being
        # stored in the carousel
        currTime = "0000"
        # if/while based on whether we want to dispense all matching
        # biscuits at that time or only one
        while currTime in self.slots:
            self.dispense(self.slots.index(currTime))

    def dispense(self, slotNo) -> None:
        self.moveTo(slotNo)
        self.pushOut()
        self.slotsUsed -= 1
        self.slots[slotNo] = None

    def moveTo(self, slotNo) -> None:
        # Move the carousel to accompyaning slot
        pass

    def pushOut(self) -> None:
        # Push the piston to remove biscuit from carousel at
        # current position
        pass