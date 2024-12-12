# src/player.py
import json
import os
class LeagueMember:
    def __init__(self,name, wins, commanderW1, commanderW2, commanderW3, commanderW4, Week1Opponents, Week2Opponents, Week3Opponents, Week4Opponents, favcolor, mostBeatColor, leastBeatColor):
        self.name = name
        self.wins = wins
        self.commanderW1 = commanderW1
        self.commanderW1Color = commanderW1# add to self
        self.commanderW2 = commanderW2
        self.commanderW3 = commanderW3
        self.commanderW4 = commanderW4
        self.Week1Opponents = Week1Opponents
        self.Week2Opponents = Week2Opponents
        self.Week3Opponents = Week3Opponents
        self.Week4Opponents = Week4Opponents
        self.favcolor = favcolor
        self.mostBeatColor = mostBeatColor
        self.leeastBeatColor = leastBeatColor
        #add leauge rival
        
    def updateplayer(self,name):
        self.name = name
        
    def update_week1_opponents(self, Week1Opponents):
        self.Week1Opponents = Week1Opponents
    def update_week2_opponents(self, Week2Opponents):
        self.Week2Opponents = Week2Opponents

    def update_week3_opponents(self, Week3Opponents):
        self.Week3Opponents = Week3Opponents

    def update_week4_opponents(self, Week4Opponents):
        self.Week4Opponents = Week4Opponents

    def update_commanderW1(self, commanderW1):
        self.commanderW1 = commanderW1

    def update_commanderW2(self, commanderW2):
        self.commanderW2 = commanderW2

    def update_commanderW3(self, commanderW3):
        self.commanderW3 = commanderW3

    def update_commanderW4(self, commanderW4):
        self.commanderW4 = commanderW4
        
    def updatefavcolor(self, favcolor):
        self.favcolor = favcolor
            
    def updatemostBeatColor(self, mostBeatColor):
        self.mostBeatColor = mostBeatColor
        
    def updateleastBeatColor(self, leastBeatColor):
        self.leeastBeatColor = leastBeatColor
    def get_name(self):
        return self.name

    def get_wins(self):
        return self.wins

    def get_commanderW1(self):
        return self.commanderW1

    def get_commanderW2(self):
        return self.commanderW2

    def get_commanderW3(self):
        return self.commanderW3

    def get_commanderW4(self):
        return self.commanderW4

    def get_Week1Opponents(self):
        return self.Week1Opponents

    def get_Week2Opponents(self):
        return self.Week2Opponents

    def get_Week3Opponents(self):
        return self.Week3Opponents

    def get_Week4Opponents(self):
        return self.Week4Opponents

    def get_favcolor(self):
        return self.favcolor

    def get_mostBeatColor(self):
        return self.mostBeatColor

    def get_leastBeatColor(self):
        return self.leastBeatColor
    def to_dict(self):
        return {'name': self.name, 'Week 1 Commander': self.commanderW1, 'Week 1 Opponesnt': self.Week1Opponents, 'Week 2 Commander': self.commanderW2, 'Week 2 Opponents':self.Week2Opponents, 'Week 3 Commander': self.commanderW3, 'Week 3 Opponents':self.Week3Opponents, 'Week 4 Commander': self.commanderW4, 'Week 4 Opponents':self.Week4Opponents, 'Favorite Color': self.favcolor}
    