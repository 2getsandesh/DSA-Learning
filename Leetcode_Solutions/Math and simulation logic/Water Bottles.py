'''There are numBottles water bottles that are initially full of water. 
You can exchange numExchange empty water bottles from the market with one full water bottle.
The operation of drinking a full water bottle turns it into an empty bottle.
Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.'''

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        fullBottles = 0 #Already drank all the initial bottles
        emptyBottles = numBottles
        drank = numBottles

        while emptyBottles >= numExchange:
            fullBottles = emptyBottles//numExchange
            balanceEmpty = emptyBottles%numExchange
            drank += fullBottles
            emptyBottles = fullBottles + balanceEmpty
        return drank