init -5 python:
    def fill_actions(playerActor, enemies):
        result = []

        for enemy in enemies:
            result.append(("Attack %s" % (enemy.name), enemy.name))

        result.append(("Do nothing", "pass"))

        return result