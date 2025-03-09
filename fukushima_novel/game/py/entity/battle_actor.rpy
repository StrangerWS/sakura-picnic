init -5 python:
    class BattleActor(store.object):
        def __init__(self, name, currentHp, maxHp, damage, armor):
            self.name = name
            self.currentHp = currentHp
            self.maxHp = maxHp
            self.damage = damage
            self.armor = armor
        
        def doDamage(self, actor: 'BattleActor'):
            damageDealt = self.damage - actor.armor
            if (damageDealt >= actor.currentHp):
                actor.currentHp = 0
            elif damageDealt > 0:
                actor.currentHp -= damageDealt