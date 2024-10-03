# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define computer = Character("Computador")

define player = Character("Jogador")

define pensamento = Character("jogador", what_suffix='"', what_prefix='"')

# The game starts here.

# scene "name of the file without quotes and without .png"
# show "name of the file without quotes and without .png"
# char variable "String in quotes"

label start:

    scene blackScreen

    computer "BEEP BEEP BEEP BEEP... (* um bípe contínuo toca)"

    scene computer room

    pensamento "Você sente seu estômago revirar com o último almoço que teve."
    pensamento "Você apenas quer dormir mais um pouco."

    computer "BEEP BEEP BEEP BEEP... (* um bípe contínuo toca)"

    pensamento "Você se levanta, se deparando com o computador antigo que você tinha tentado ligar antes de dormir."

    menu first_menu:
        "O que eu devo fazer?"
        "Ler o aviso.":
            pensamento "Você vê diversos e-mails relacionados à empresa D.AI.TE"

        "Forçadamente desligar o computador.":
            jump forced_turn_off

        "Proceder sem ler.":
            "..."
            jump first_menu

    label forced_turn_off:
    




    


    return
