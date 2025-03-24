# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Variáveis
default computerInterest = 0
default playerImage = "computer.png"
default playerName = ""
default computerName = ""
define computer = Character("[computerName]", image="computer")
define player = Character("[playerName]", image="player")
define thoughts = Character("[playerName]", what_suffix='"', what_prefix='"')
define confirmation = 1
define correct = [False, False, False] #False == erro && True == acerto

# Imagens
image side computer = "computer.png"
image side player = "[playerImage]"
image female = "female.png"
image male = "male.png"
image bg-blackScreen = "#000"
image bg-desolatedCity = "desolatedCity.png"
image bg-computerRoom-day-off = "computerRoom_day_off.png"
image bg-computerRoom-day-on = "computerRoom_day_on.png"
image bg-computerRoom-night-off = "computerRoom_night_off.png"
image bg-computerRoom-night-on = "computerRoom_night_on.png"

#transform
transform half_size:
    zoom 1.2

transform profile_picture:
    zoom 0.9

# The game starts here.

label start:

# Teach Player how to do things!

label ask_new_player:
    scene bg-whiteScreen

    "Jogo feito por Abigail e Miguel para Sistemas Operacionais.
    Clique para prosseguir."

    menu confirm_tutorial:
        "Você conhece os comandos?"

        "Sim":
            jump character_creation
        
        "Não":
            jump tutorial

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

label character_creation:

    $ playerName = renpy.input(prompt="Qual o seu nome?", length=10);
    $ playerName = playerName.strip()

    if not playerName:
        "Nome Inválido"
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

    call fase_1
    call fase_2
    call fase_3
    call fase_4
    call fase_5