# ================================================================================== #
#                   ОФИЦИАЛЬНАЯ ДОКУМЕНТАЦИЯ ФАЙЛА СЦЕНАРИЯ                          #
# ================================================================================== #
# Файл сценария визуальной новеллы «Пикник под Сакурой».                             #
# Разработчик — StrangerWS / The Lore of the Worlds Team, 2025-2026.                 #
# ================================================================================== #

init:
    call initBgImg                  # initialize backgrounds

label start:
    call renew_stage

    menu beta_test_menu:
        "Test Battle System":
            jump fight_testing
        "Choice 2":
            "Ну, хоть не в жопу раз выбрал"
        "Drop ALL persistense":
            "Nothing to drop"
        
    jump intro

label renew_stage:
    stop music fadeout 5
    stop sound
    stop audio
    stop voice
    pause 3
    return