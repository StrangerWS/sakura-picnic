screen fight_hud(you, enemies):
    style_prefix "ac"
    
    # Блок игрока
    hbox:
        xpos 50
        ypos 50
        spacing 10
        
        # Аватар игрока
        add "res/gui/battle/ui/player_avatar.png"
        
        vbox:
            # Имя и уровень
            text "%s" % (you.name) size 22 color "#F0E68C"
            
            # Контейнер здоровья
            hbox:
                spacing -5  # Наложение квадратов
                xalign 0.0
                
                $ hp_percent = you.currentHp / float(you.maxHp)
                
                # Отображаем полные сегменты
                for i in range(you.maxHp):
                    if i < you.currentHp:
                        add "res/gui/battle/ui/player_hp_full.png"
                    else:
                        add "res/gui/battle/ui/player_hp_empty.png"

    # Блок врагов
    hbox:
        xpos 50
        ypos 150
        spacing 20
        
        for enemy in enemies:
            vbox:
                # Аватар врага
                add "res/gui/battle/ui/enemy_avatar.png"
                
                # Имя и здоровье
                text enemy.name size 18 color "#CD5C5C"
                
                hbox:
                    spacing -5
                    $ enemy_hp_percent = enemy.currentHp / float(enemy.maxHp)
                    
                    for i in range(enemy.maxHp):
                        if i < enemy.currentHp:
                            add "res/gui/battle/ui/enemy_hp_full.png" 
                        else:
                            add "res/gui/battle/ui/enemy_hp_empty.png"