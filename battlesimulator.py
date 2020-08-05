import random


class Raven():
    def __init__(self):
        self.hp = 100
        self.atk = 23
        self.defence = 14
        self.spd = 14
        self.phy_damage = 23
        self.increase_damage = False
        self.rival_def = 0
        self.i = 1

    def attack(self):
        if self.i % 3 == 0:
            if self.increase_damage:
                self.phy_damage = self.atk * 1.25 - self.rival_def + self.spatk2()
            else:
                self.phy_damage = self.atk - self.rival_def + self.spatk2()
        else:
            if self.increase_damage:
                self.phy_damage = self.atk * 1.25 - self.rival_def
            else:
                self.phy_damage = self.atk - self.rival_def
        self.i += 1
        return self.phy_damage

    def spatk1(self):
        p = random.random()
        if p < 0.25:
            self.increase_damage = True
    
    def spatk2(self):
        if self.increase_damage:
            extra_phy_damage = 7 * (16 * 1.25 - self.rival_def)
        else:
            extra_phy_damage = 7 * (16 - self.rival_def)
        return extra_phy_damage


class Theresa():
    def __init__(self):
        self.hp = 100
        self.atk = 19
        self.defence = 12
        self.spd = 22
        self.phy_damage = 19
        self.rival_def_decrease = False
        self.rival_def = 0
        self.i = 1

    def attack(self):
        if self.i % 3 == 0:
            self.phy_damage = self.atk - self.rival_def + self.spatk2()
        else:
            self.phy_damage = self.atk - self.rival_def
        self.spatk1()
        self.i += 1
        return self.phy_damage

    def spatk1(self):
        p = random.random()
        if p < 0.3:
            self.rival_def_decrease = True
        else:
            self.rival_def_decrease = False

    def spatk2(self):
        extra_phy_damage = 5 * (16 - self.rival_def)
        return extra_phy_damage


theresa_win = 0
raven_win = 0

# simulate
# @epoch = 100000
for j in range(100000):
    # init
    raven = Raven()
    theresa = Theresa()
    raven.rival_def = theresa.defence
    theresa.rival_def = raven.defence
    raven.spatk1()
    for k in range(50):
        theresa_dmg = theresa.attack()
        raven.hp -= theresa_dmg
        if raven.hp <= 0:
            theresa_win += 1
            break
        elif theresa.rival_def_decrease:
            if raven.defence < 5:
                raven.defence = 0
            else:
                raven.defence -= 5
            theresa.rival_def = raven.defence
        raven_dmg = raven.attack()
        theresa.hp -= raven_dmg
        if theresa.hp <= 0:
            raven_win += 1
            break

print("Theresa winning times: %d" % theresa_win)
print("Raven winning times: %d\n" % raven_win)
