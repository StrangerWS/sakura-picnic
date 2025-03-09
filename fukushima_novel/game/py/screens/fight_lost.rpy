screen fight_lost(enemies, label_to_jump):
    modal True
    zorder 200

    window:
        background "#333333"
        vbox:
            align (0.5, 0.5)
            spacing 25

            text "YOU DIED" size 36 color "#FF0000"
           
            hbox:
                xalign 0.5
                spacing 30
                textbutton "Вернуться к битве (за очки)" action [Hide("fight_lost"), Jump(label_to_jump)]
                textbutton "Загрузить сохранение" action [Hide("fight_lost"), ShowMenu("load")]
                textbutton "Выйти в меню" action MainMenu()

    key "game_menu" action MainMenu()