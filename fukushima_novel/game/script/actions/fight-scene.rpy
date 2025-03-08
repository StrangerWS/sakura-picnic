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