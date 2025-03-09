# $ battle_transition =  ImageDissolve(sdGetImage("res/gui/effect/battle_transition.png"), 2.0, 50, reverse = False)

label init_fight_demo:
    image bg epic_fight_scene = "res/images/dev/bg/epic_fight_scene.png"

    image gang angry = "res/images/dev/char/battle_gang_demo_angry.png"
    image gang2 angry = "res/images/dev/char/battle_gang2_demo_angry.png"

    return

label fight_testing:
    call init_fight_demo

    scene bg epic_fight_scene with Dissolve(5)

    play music battle_hymn fadein 3    

    "This is a battle system test"
    "Meet your fight!"

    show gang angry at left with dissolve
    show gang2 angry at right with dissolve

    $ playerActor = BattleActor("Player", 5, 5, 1, 0)
    $ gang1Actor = BattleActor("Gang 1", 5, 5, 1, 0)
    $ gang2Actor = BattleActor("Gang 2", 5, 5, 1, 0)
    $ enemies =  [gang1Actor, gang2Actor]

    show screen fight_hud(
        playerActor, 
        enemies
    )

    "Oh no! There are two of them!"

    while len(enemies) > 0 and playerActor.currentHp > 0:
        $ actions = fill_actions(playerActor, enemies)

        $ result = renpy.display_menu(actions)
        if result == "Gang 1":
            call damageGang1
        elif result == "Gang 2":
            call damageGang2
        elif result == "pass":
            pass
           
        call try_attack_gang1
        call try_attack_gang2

    if (playerActor.currentHp == 0):
        stop music fadeout 3
        play music dark_echo fadein 3
        show screen fight_lost(enemies, "fight_testing")
        pause

    "Phew! Not bad, strong man!"
    return

label try_attack_gang1:
    if renpy.random.random() < 0.2 and gang1Actor.currentHp > 0:
        $ gang1Actor.doDamage(playerActor)
        play sound hit_hard 
        hide black with flash_red
    return

label try_attack_gang2:
    if renpy.random.random() < 0.2 and gang2Actor.currentHp > 0:
        $ gang2Actor.doDamage(playerActor)
        play sound hit_hard 
        hide black with flash_red
    return

label damageGang1:
    $ playerActor.doDamage(gang1Actor)
    show gang angry at hit_effect
    play sound hit

    if (gang1Actor.currentHp == 0):
        $ enemies.remove(gang1Actor)
        hide gang with easeoutbottom
    return

label damageGang2:
    $ playerActor.doDamage(gang2Actor)
    show gang2 angry at hit_effect
    play sound hit
    if (gang2Actor.currentHp == 0):
        $ enemies.remove(gang2Actor)
        hide gang2 with easeoutbottom
    return