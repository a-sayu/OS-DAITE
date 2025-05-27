# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Variáveis
# scrpt
default playerImage = "female.png"    # String
default computerImage = "computer.png"    # String
default playerName = ""                 # String
default computerName = ""               # String
#phase 3
default correct = [False, False, False] # False == erro / True == acerto
#phase 7
default have_notebook = False           # True or False
default seen_safe = False               # True or False
default password = ""                   # String
default wrong_input = 0                 # Integers

# Characters or types of dialogue
define computer = Character("[computerName]", image="computer")
define player = Character("[playerName]", image="player")
define thoughts = Character("[playerName]", what_suffix='"', what_prefix='"')

# Imagens
image side computer = "[computerImage]"
image side player = "[playerImage]"
image female = "female.png"
image male = "male.png"

# Backgrounds
image bg-blackScreen = "#000"
image bg-desolatedCity = "desolatedCity.png"
image bg-computerRoom-day-off = "computerRoom_day_off.png"
image bg-computerRoom-day-on = "computerRoom_day_on.png"
image bg-computerRoom-night-off = "computerRoom_night_off.png"
image bg-computerRoom-night-on = "computerRoom_night_on.png"

# Adjusting images
transform half_size:
    zoom 1.2

transform profile_picture:
    zoom 0.9

# The game starts here.

label start:

# Introduction
label beginning:
    scene bg-whiteScreen

    "Jogo feito por Abigail e Miguel para a matéria de Sistemas Operacionais 1 & 2.
    Clique para prosseguir."

    menu confirm_tutorial:
        "Você gostaria de conhecer os comandos?"

        "Sim":
            jump character_creation
        
        "Não":
            jump tutorial

# Tutorial
label tutorial:
    "Aqui vai um tutorial simples, então!
    Para avançar no diálogo, clique com o botão esquedo do mouse"

    "Ou aperte espaço/enter no teclado."

    "Para acessar o menu de configurações aperte esc no teclado
    Ou no botão abaixo."

    "Rolar o botão do meio do mouse avança ou volta na conversa,
    use quando tiver esquecido algo."

    "Caso precise de assistência, o Ren'Py possui um menu de
    acessibilidade apertanto o Shift + A"


# Character creation 
label character_creation:

    $ playerName = renpy.input(prompt="Qual o seu nome?", length=10);
    $ playerName = playerName.strip()

    if not playerName:
        "Nome Inválido!"
        jump character_creation

    menu player_name:
        "[playerName] é seu nome?"
        
        "Sim":

            jump gender_choice
            
        "Não":

            jump character_creation

label gender_choice:
    show female at right, half_size
    show male at left, half_size

    menu gender_choice_menu:
        "Como você se parece?"
        
        "Esquerda":
            
            $ playerImage = "male.png"
            jump intro

        "Direita":
            
            $ playerImage = "female.png"
            jump intro

label intro:

    scene bg-desolatedCity

    "O silêncio das ruas era predominante, o vento frio batia em seu rosto enquanto você 
    caminhava discretamente até o prédio que fica sua atual 'casa', retirando suas chaves
    do bolso, você destranca a porta."

    call phase_1
    call phase_2
    call phase_3
    call phase_4
    call phase_5
    call phase_6
    call phase_7
    call phase_8
    call phase_9
    call phase_10
    call phase_11
    call phase_12