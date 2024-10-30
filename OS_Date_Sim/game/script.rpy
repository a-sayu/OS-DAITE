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
define confirmation = 1

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
    menu player_name:
        "[playerName] é seu nome?"
        "Não":
            jump character_creation
        "Sim"

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

    "O silêncio das ruas era predominante, o vento frio passava em sentido contrário, e 
    você caminhava discretamente até o prédio que fica sua atual 'casa', retirando suas 
    chaves do bolso, você destranca a porta."

label fase_1:

    scene bg-computerRoom-night-off

    "Você se depara com o escritório de mesas empilhadas ao fundo, mas com uma mesa 
    próxima a janela com um computador desligado, onde você já estava a mais de uma 
    semana."

    "Colocando sua mochila sobre a mesa, você se senta em frente ao computador, para 
    afastar a fome você começa a pensar sobre esse computador."

    player "Eu deveria tentar ligar esse computador, apesar de o mundo ter acabado, a 
    energia e a internet ainda não acabou..."

    "Apertando o botão de ligar o computador, você apoia sua mão na mesa, vendo as leds 
    ligarem, e ficar na tela de carregamento."

    player "D.AI.TE... é o sistema operacional desse computador velho?"

    menu localizacao_SO:
        player "Hmm... Se eu fosse um computador, onde ficaria meu sistema operacional?"

        "Na minha memória de longo prazo!":
            player "É... Um computador tem um disco rígido certo? Onde o sistema 
            operacional fica guardado mesmo quando desligado, é que nem quando eu estou 
            dormindo..."
            
            jump continue_local

        "No meu... Estômago?":
            player "Parece que eu estou com muita fome, haha, achando a resposta talvez eu 
            me distraia da fome..."

            "Você vasculha as pilhas de papel que pareciam estar estranhamente muito 
            relacionadas com um estudo de sistemas operacionais."

            jump localizacao_SO

        "Eu não sei dizer...":
            player "Bem, se eu não sei, eu tenho que estudar..."

            "Você vasculha as pilhas de papel que pareciam estar estranhamente muito 
            relacionadas com um estudo de sistemas operacionais."

            jump localizacao_SO

    label continue_local:
    "Você boceja, o cansaço de vasculhar por comida na área parecia que já estava te 
    atingindo, você come uma barra de cereal, e vai se deitar no sofá, cobrindo-se com um 
    fino lençol."

label fase_2:
    # TODO: cena de alerta
    "ALERTA! ALERTA! ALERTA!"
    
    "O som te assusta, seu corpo ainda está lento, por causa do cansaço do dia anterior, 
    observando os seus arredores, você estranha, mas relembra dos eventos dos últimos 
    meses, e como o mundo que você conhecia se foi, indo em direção ao computador, você 
    se senta em frente a ele."
    
    player "O que você quer?"
    "Você pergunta, colocando a mão sobre a sua testa."

    player "O que um computador iria querer também né? Haha, parece que eu estou 
    enlouquecendo..."

    "Você suspira e olha para as letras escritas no computador, avisando a falta de um 
    teclado e também um alerta de emergência mundial sobre um assunto que você já estava 
    bem familiarizado."

    player "Para que avisar sobre o eminente fim do mundo, se ele já aconteceu?"

    "Você conecta o teclado de fio próximo no computador e reinicia ele, e rapidamente 
    ele liga. Carregando uma tela escrita D.AI.TE, com um simbolo similar a uma flor que 
    rodava enquanto carrega o sistema."

    "Assim que o computador carrega, uma animação de uma linha surgindo e dois círculos 
    aparecia, assemelhando-se a uma cara sorrindo."

    computer "Olá! Bem-Vindo ao computador oficial da DAITE, Development of Artificial 
    Intelligence Technologies Enterprise, como um computador de auxílio adoraria que me 
    desse um nome para sermos mais amigos!"

    $ computerName = renpy.input(prompt="Como deseja me chamar?", length=10);

    "Você digita \'[computerName]\' na caixa de entrada de texto."

    computer "[computerName]! Esse mesmo?"

    "Você clica no botão que confirma a sua escolha. Logo depois ele pede o seu nome, 
    digitando \'[playerName]\' na caixa de entrada de texto."

    computer "Certo, já que nos introduzimos [playerName], por que você não me atendeu 
    quando eu acordei!? Eu fiquei esperando por cerca de uma hora!"

    player "Como eu falo sobre isso com uma máquina... Você entende se eu falar que eu 
    precisava acordar, levantar com calma, checar o que está ao meu refor, o que está 
    acontecendo para então fazer as tarefas do dia?"

    computer "Desculpe, mas minhas bases de conhecimento humana são faltosas por conta 
    da última atualização, poderia explicar usando de analogias de sistema operacional?"

    menu acordar_SO:
        player "Como eu respondo isso? Você reflete."

        "Eu não sei, como eu poderia entender uma máquina?":
            
            computer "E como eu poderia entender você?" 
            "A máquina pergunta. Sem muito o que fazer, para que ela te entenda, você 
            vasculha as pilhas de papel que pareciam estar estranhamente muito relacionadas 
            com um estudo de sistemas operacionais."
    
            jump acordar_SO

        "Você liga e tem que fazer as coisas de computador né, leds, tela e tals, pra 
        que as coisas funcionem."

            computer "Então você demora porque ainda não está mostrando o que está 
            acontecendo?"
            
            player "Acho que não é isso que eu quero dizer, eu não mostro coisas, eu 
            preciso sentir coisas e entender o meu arredor..."
            
            "Sem muito o que fazer, para conversar com a máquina você vasculha as pilhas 
            de papel que pareciam estar estranhamente muito relacionadas com um estudo 
            de sistemas operacionais."

            jump acordar_SO
        
        "Assim que liga o computador, você não já inicia realizando processos complicados, 
        é necessário que um programa armazenado na memória ROM da sua placa-mãe, chamado 
        BIOS, confira sua memória RAM, a presença de teclado, e outros dispositivos ligados 
        à você, lendo o seu armazenamento para então carregar o sistema operacional do local 
        lido."

            computer "Oh! Então você ainda está verificando as suas partes e o que esta conectado a você? No caso \"Lugar\", \"Corpo\" e \"Memória\""
            player "Algo assim!"

return
