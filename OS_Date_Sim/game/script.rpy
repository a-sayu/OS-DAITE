# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Variáveis
# scrpt
default playerImage = "female.png"    # String
default computerImage = "computer.png"    # String
default jorgeImage = "jorge-placeholder.png"    # String
default playerName = ""                 # String
default computerName = ""               # String
default jorgeName = "Jorge"               # String
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
define jorge = Character("Jorge", image="jorge")
define thoughts = Character("[playerName]", what_suffix='"', what_prefix='"')

# Imagens
image side computer = "[computerImage]"
image side player = "[playerImage]"
image side thoughts = "[playerImage]"
image side jorge = "[jorgeImage]"
image female = "female.png"
image male = "male.png"

# Backgrounds
image bg-blackScreen = "#000"
image bg-whiteScreen = "#FFF"
image bg-desolatedCity = "desolatedCity.png"
image bg-computerRoom-day-off = "computerRoom_day_off.png"
image bg-computerRoom-day-on = "computerRoom_day_on.png"
image bg-computerRoom-night-off = "computerRoom_night_off.png"
image bg-computerRoom-night-on = "computerRoom_night_on.png"
image bg-cloudy = "cloudy.png"
image bg-computerScreen-fail = "computerScreen_fail.png"

image bg-keyEnterSpace = "keyEnterSpace.png"
image bg-keyEsc = "keyEsc.png"
image bg-mouseRoll = "mouseRoll.png"
image bg-keyShiftA = "keyShiftA.png"
image bg-mouseClick = Movie(play="images/mouseClick.ogv", size=(1920, 1080))

# Adjusting images
transform half_size:
    zoom 1.2

transform profile_picture:
    zoom 0.9

transform alert:
    matrixcolor TintMatrix("#F27E7E")

# The game starts here.

label start:

# Introduction
label beginning:
    scene bg-whiteScreen

    "Jogo feito por Abigail e Miguel para a matéria de Sistemas Operacionais 1 & 2.
    Clique para prosseguir."

    menu confirm_tutorial:
        "Você gostaria de conhecer os comandos?"
        
        "Sim.":
            jump tutorial

        "Não.":
            jump character_creation
        
        

label p2_computer_naming:
    $ computerName = renpy.input(prompt="Como deseja me chamar?", length=10);
    $ computerName = computerName.strip()

    "Você digita \'[computerName]\' na caixa de entrada de texto."
    if not computerName:
        computer "Esse Nome é Inválido :C"
        jump p2_computer_naming

    menu p2_computer_naming_menu:
        computer "[computerName]! Esse mesmo?"

        "Sim.":
            return

        "Não.":
            jump p2_computer_naming


# Tutorial
label tutorial:
    scene bg-mouseClick
    "Aqui vai um tutorial simples, então!
    Para avançar no diálogo, clique com o botão esquedo do mouse."

    scene bg-keyEnterSpace
    "Ou aperte ESPAÇO/ENTER no teclado."

    scene bg-keyEsc
    "Para acessar o menu de configurações aperte ESC no teclado ou
    no botão Preferências abaixo."

    "É possível alterar configurações, mas também permite acessar o
    menu principal ou as suas jogatinas salvas na aba Salvos."

    scene bg-whiteScreen
    "Para salvar, aperte o botão Salvar abaixo."

    scene bg-mouseRoll
    "Rolar o botão do meio do mouse avança ou volta na conversa,
    use quando tiver esquecido algo."

    scene bg-keyShiftA
    "Caso precise de assistência, o Ren'Py possui um menu de
    acessibilidade apertanto o SHIFT + A."

    scene bg-whiteScreen
    "Agora, uma ótima jogatina para você!"


# Character creation 
label character_creation:
    scene bg-cloudy
    $ playerName = renpy.input(prompt="Qual o seu nome?", length=10);
    $ playerName = playerName.strip()

    if not playerName:
        "Nome Inválido!"
        jump character_creation

    menu player_name:
        "[playerName] é seu nome?"
        
        "Sim.":

            jump gender_choice
            
        "Não.":

            jump character_creation

label gender_choice:
    show female at right, half_size
    show male at left, half_size

    menu gender_choice_menu:
        "Como você se parece?"
        
        "<-------":
            
            $ playerImage = "male.png"
            jump intro

        "------->":
            
            $ playerImage = "female.png"
            jump intro

label intro:

    scene bg-desolatedCity

    "O silêncio das ruas era predominante, o vento frio batia em seu rosto enquanto você 
    caminhava discretamente até o prédio que fica sua atual 'casa', retirando suas chaves
    do bolso, você destranca a porta."

    call phase_1 from _call_phase_1
    call phase_2 from _call_phase_2
    call phase_3 from _call_phase_3
    call phase_4 from _call_phase_4
    call phase_5 from _call_phase_5
    call phase_6 from _call_phase_6
    call phase_7 from _call_phase_7
    call phase_8 from _call_phase_8
    call phase_9 from _call_phase_9
    call phase_10 from _call_phase_10
    call phase_11 from _call_phase_11
    call phase_12 from _call_phase_12
    call phase_13 from _call_phase_13
    call phase_14 from _call_phase_14
    call phase_14 from _call_phase_14_1
    call phase_15 from _call_phase_15
    call phase_16 from _call_phase_16
    call phase_17 from _call_phase_17
    call phase_18 from _call_phase_18
    call phase_19 from _call_phase_19
    call phase_34 from _call_phase_34