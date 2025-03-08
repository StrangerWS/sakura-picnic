define audio.battle_hymn = "res/audio/music/battle_hymn.mp3"

# $ battle_transition =  ImageDissolve(sdGetImage("res/gui/effect/battle_transition.png"), 2.0, 50, reverse = False)


label init_fight_demo:
    image bg epic_fight_scene = "res/images/dev/bg/epic_fight_scene.png"

    image gang angry = "res/images/dev/char/battle_gang_demo_angry.png"
    image gang2 angry = "res/images/dev/char/battle_gang2_demo_angry.png"

    return

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

transform hit_effect:
    ease 0.1 xoffset 25
    ease 0.1 xoffset -25
    ease 0.1 xoffset 25
    ease 0.1 xoffset -25
    ease 0.1 xoffset 25
    ease 0.1 xoffset -25
    ease 0.1 xoffset 25
    ease 0.1 xoffset -25
    ease 0.1 xoffset 0

label fight_testing:
    call init_fight_demo

    scene bg epic_fight_scene with Dissolve(5)

    play music battle_hymn fadein 3    

    "This is a battle system test"
    "Meet your fight!"

    show gang angry at left with dissolve
    show gang2 angry at right with dissolve

    $ playerActor = BattleActor("Player", 5, 5, 1, 0)
    $ gang1Actor = BattleActor("Gang 1", 5,5,1,0)
    $ gang2Actor = BattleActor("Gang 2",5,5,1,0)
    $ enemies =  [gang1Actor, gang2Actor]

    show screen fight_hud(
        playerActor, 
        enemies
    )

    "Oh no! There are two of them!"


    "1"
    call damageGang1
    "2"
    call damageGang2
    "3"
    call damageGang2
    "4"
    call damagePlayer

    "Ouch!"
    return


label damageGang1:
    $ playerActor.doDamage(gang1Actor)
    show gang angry at hit_effect
    play sound hit
    return

label damageGang2:
    $ playerActor.doDamage(gang2Actor)
    show gang2 angry at hit_effect
    play sound hit
    return

label damagePlayer:
    $ gang1Actor.doDamage(playerActor)
    play sound hit_hard 
    hide black with flash_red
    return