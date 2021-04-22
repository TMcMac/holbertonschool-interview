#!/usr/bin/python3
"""
This program takes in a list of lists known as boxes
each position in the list boxes is a box, and each box
may contain one of more keys. The goal of the program is
to check if based on the keys we have are we able to unlock
all boxes. The box in position 0 of the list boxes will
always be unlocked. Once we open the 0th box we will need
to unlock all boxes that the 0th boxes contains keys for
and contnue on collecting keys and unlocking boxes until
we have unlocked all boxes or do not have keys to continue.
If we unlock all we return True, else return False
"""
if __name__ == '__main__':
    def canUnlockAll(boxes):
        """
        Description:
            Determines if all boxes can be opened
            Return True if all boxes can be opened, else return False
        Args:
            @boxes: a list of lists, which represents boxes
                    filled with keys (int values) to other boxes
        """

        n = len(boxes)  # The number of positions or 'boxes' in list boxes
        unlocked = [0]  # The first (0th position) box is always unlocked
        if n is not 0:
            keys = boxes[0]  # If at least 1 box in boxes first set of keys comes from that box
        else:
            return True  # If boxes is an empty list, technically all boxes are unlocked

        locksOpened = True  # This is our flag condition for did we open any new boxes
        while(locksOpened):  # So long as at least one new box was opend we are still working
            locksOpened = False  # We need this set to false so that we can see if we failed to open new boxes with our new keys
            for i in range(n):
                if i in unlocked:
                    continue  # If our i'th position is already in our list of unlocked boxes we have it's keys and can move on
                else:
                    if i in keys:  # If the i'th box was not previously opened we need to check if we have a key to it in keys
                        aBox = boxes[i]  # If we have the key we open the box and add any non-repeated keys to our list of available keys
                        for key in aBox:
                            if key not in keys:
                                keys.append(key)
                        unlocked.append(i)  # We opened a new box with line 31 so add the box number to unlocked
                        locksOpened = True  # We opened a box so locksOpened is again True

        # If we manage to exit our while condition it means we were unable to open any new boxes
        # If this is the case either all boxes are unlocked or we don't have the keys to continue
        if len(unlocked) == n:
            return True
        if locksOpened is False:
            return False
