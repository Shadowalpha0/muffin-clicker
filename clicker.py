class MuffinClicker:
    def __init__(self): #Base amounts of stuff
        self.muffins = 0
        self.muffinsper = 1
        self.muffinmultiplier = 1
        self.muffinprice = 10
        self.bakeryprice = 10000
        self.automuffins = 0
        self.autoprice = 500
    
    def bake(self): #Bakes a muffin every click
        self.muffins += self.muffinsper * self.muffinmultiplier
        return f"You have {self.muffins} Muffins."
    
    def checkupgrade(self): #Checks if amount of muffins is enough to buy an upgrade and displays whether or not you can buy it
        if self.muffins >= self.muffinprice:
            return f"Upgrade to {self.muffinsper + 1} Muffins per click"
        else:
            return f"You don't have enough muffins :( (Required - {self.muffinprice} Muffins)"
        
    def upgrade(self): #Upgrades the muffins per click
        if self.muffins >= self.muffinprice: 
            self.muffinsper += 1
            self.muffins -= self.muffinprice
            self.muffinprice *= 2
    
    def checkmultiplier(self): #Checks if amount of muffins is enough to buy an upgrade and displays whether or not you can buy it
        if self.muffins >= self.bakeryprice:
            return f"Upgrade multiplier to x{self.muffinmultiplier + 1} (Note - Resets upgrades and Muffins)"
        else:
            return f"You don't have enough muffins :( (Required - {self.bakeryprice} Muffins)"
        
    def multiplier(self): #Upgrades the multiplier
        if self.muffins >= self.bakeryprice:
            self.muffinmultiplier += 1
            self.muffins = 0 
            self.muffinsper = 1
            self.muffinprice = 10
            self.bakeryprice *= 2

    def muffin(self): #Displays the amount of muffins
        return f"You have {self.muffins} Muffins."
    
    def upgrades(self): #Displays the muffins per click
            return f"You make {self.muffinsper} Muffins per click"
    
    def bakery(self): #Displays the multiplier
            return f"Your multiplier is x{self.muffinmultiplier}. The multiplier affects all Muffin makers"

if __name__ == '__main__':
    game = MuffinClicker()