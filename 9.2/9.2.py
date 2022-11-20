import random as rd

class Person:

    def __init__(self, name, health, speed, attack, defence, agility, critical_chance):
        self.name = name
        self.health = health
        self.speed = speed
        self.attack = attack
        self.defence = defence
        self.agility = agility
        self.critical_chance = critical_chance

    def decrease_hp(self, arg):
        self.health -= arg

    def dodge(self):
        conditions = (True, False)  #True - уклон, False - пропустил
        dodge_chance = (self.agility / 100)
        return rd.choices(conditions, weights = [dodge_chance, 1 - dodge_chance])[0]
    
    def critical_hit(self):
        conditions = (True, False) 
        crit_chance = (self.critical_chance / 100)
        return rd.choices(conditions, weights = [crit_chance, 1 - crit_chance])[0]

    def to_attack(self, other):  
        
        if not other.dodge():
            damage = self.attack - other.defence
            if self.critical_hit():
                damage = 2 * damage
                other.decrease_hp(damage)
            else:
                other.decrease_hp(damage)
    
    def is_dead(self):
        if (self.health <= 0):
            return True
        else:
            return False
    
    def is_alive(self):
        if (self.health > 0):
            return True
        else:
            return False

    def __str__(self):
        chars = []
        chars.append(self.name)
        chars.append(self.health)
        chars.append(self.speed)
        chars.append(self.attack)
        chars.append(self.defence)
        chars.append(self.agility)
        chars.append(self.critical_chance)
        return ''.join(str(chars))

def battle(P1, P2):
    s1, s2 = P1.speed, P2.speed

    if s1 >= s2:
        av1, av2 = P1, P2
    elif s1 < s2:
        av1, av2 = P2, P1
    
    while  (av1.is_alive() * av2.is_alive()):

        av1.to_attack(av2)
        if av2.is_dead():
            return av1
        
        av2.to_attack(av1)
        if av1.is_dead():
            return av2

winners = []

for i in range(100):
    P1 = Person('Tank',10,1,2,1,0,50)
    P2 = Person('Dexter',10,1,2,1,50,0)
    winners.append(battle(P1, P2).name)

T_wins = winners.count('Tank')
D_wins = winners.count('Dexter')

print ('Tank:',T_wins,', Dexter:', D_wins)
if (T_wins > D_wins):
    print('winner:', 'Tank,', T_wins / 100)
elif(T_wins < D_wins):
    print('winner:', 'Dexter,', D_wins / 100)
elif(T_wins == D_wins):
    print('Draw')
    








    



