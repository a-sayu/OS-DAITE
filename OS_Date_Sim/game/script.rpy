# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Variáveis
default computerInterest = 0
default playerImage = "computer.png"
default playerName = "?"
default computerName = "Computador"
define computer = Character("[computerName]", image="computer")
define player = Character("[playerName]", image="player")
define thoughts = Character("[playerName]", what_suffix='"', what_prefix='"')

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
    zoom 0.5

transform profile_picture:
    zoom 0.9

# The game starts here.

label start:

label character_creation:

    $ playerName = renpy.input(prompt="Qual o seu nome?", length=10);

    show female at right, half_size
    show male at left, half_size
    menu gender_choice:
        "Como você se parece?"
        "Esquerda":
            $ playerImage = "male.png"
            jump intro
        "Direita":
            $ playerImage = "female.png"
            jump intro

label intro:

    scene bg-desolatedCity
    "O silêncio das ruas era predominante, o vento frio passava em sentido contrário, e você caminhava discretamente até o prédio que fica sua atual 'casa', retirando suas chaves do bolso, você destranca a porta."
    scene bg-computerRoom-night-off
    "Você se depara com o escritório de mesas empilhadas ao fundo, mas com uma mesa próxima a janela com um computador desligado, onde você já estava a mais de uma semana."

    "Colocando sua mochila sobre a mesa, você se senta em frente ao computador, para afastar a fome você começa a pensar sobre esse computador."

    player "Eu deveria tentar ligar esse computador, apesar de o mundo ter acabado, a energia e a internet ainda não acabou..."

    "Apertando o botão de ligar o computador, você apoia sua mão na mesa, vendo as leds ligarem, e ficar na tela de carregamento."

    player "D.AI.TE... é o sistema operacional desse computador velho?"

    menu localizacao_SO:
        player "Hmm... Se eu fosse um computador, onde ficaria meu sistema operacional?"

        "Na minha memória de longo prazo!":
            player "É... Um computador tem um disco rígido certo? Onde o sistema operacional fica guardado mesmo quando desligado, é que nem quando eu estou dormindo..."
            jump continue_local

        "No meu... Estômago?":
            player "Parece que eu estou com muita fome, haha, achando a resposta talvez eu me distraia da fome..." 
            "Você vasculha as pilhas de papel que pareciam estar estranhamente muito relacionadas com um estudo de sistemas operacionais."
            jump localizacao_SO
        "Eu não sei dizer...":
            player "Bem, se eu não sei, eu tenho que estudar..."
            "Você vasculha as pilhas de papel que pareciam estar estranhamente muito relacionadas com um estudo de sistemas operacionais."
            jump localizacao_SO

    
    label continue_local:
    "Você boceja, o cansaço de vasculhar por comida na área parecia que já estava te atingindo, você come uma barra de cereal, e vai se deitar no sofá, cobrindo-se com um fino lençol."

return
