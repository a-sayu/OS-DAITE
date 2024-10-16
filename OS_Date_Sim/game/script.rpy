# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Variáveis
default computerInterest = 0
default playerName = "?"
default computerName = "Computador"
define computer = Character("[computerName]", image="computer")
define player = Character("[playerName]", image="player")
define thoughts = Character("[playerName]", what_suffix='"', what_prefix='"')

# Imagens
image side computer = "computer.png"
image side player = "computer.png"
image bg-blackScreen = "#000"
image bg-desolatedCity = "desolatedCity.png"
image bg-computerRoom-day-off = "computerRoom_day_off.png"
image bg-computerRoom-day-on = "computerRoom_day_on.png"
image bg-computerRoom-night-off = "computerRoom_night_off.png"
image bg-computerRoom-night-on = "computerRoom_night_on.png"


# The game starts here.

label start:

label mc_gender:
    menu gender_choice:
        "Escolha um corpo para seu personagem"
        "corpo 1":
            $ player = "male.png"
            jump intro
        "corpo 2":
            $ player = "female.png"
            jump intro
label intro:

    scene bg-desolatedCity
    "O silêncio das ruas era predominante, o vento frio passava em sentido contrário
    e você andava sorrateiramente até o prédio que fica sua atual \"casa\"."
    "Retirando a chave do bolso, você destranca a porta se deparando com um escritório
    com mesas empilhadas ao lado, mas com uma mesa ao canto, em especial, com um computador
    desligado"

    scene bg-computerRoom-night-off
    "Colocando sua mochila sobre a mesa e se sentando na cadeira, você sente um pouco de fome"
    player "O que vou comer hoje?"
    "Você se pergunta, enquanto seleciona em sua mochila algum alimento"

    menu food_choice:
        "Para prosseguir escolha um alimento"
        "Uma barra de cereal":
            player "Não está tão ruim..."
            jump continue_expo
        "O resto de uma latinha de atum":
            player "Poderia ser melhor..."
            jump continue_expo
        "Uma bolacha velha":
            player "Pelo menos é doce..."
            jump continue_expo

    label continue_expo:
        player "Bem, tenho que ir dormir..."
        "Antes de ir dormir, você se senta em frente ao computador desligado"
        player "Aqui tem energia então em algum lugar ainda estão funcionando os geradores de energia"
        "Você liga o computador na esperança que houvesse um meio de comunicação com outras pessoas\n
        O computador parece não responder e impacientemente você vai deitar-se no sofá do escritório"

    scene bg-blackScreen

    "BEEP BEEP BEEP BEEP... (* um bípe contínuo toca)"
    "Você sente seu estômago roncar com a pequena última refeição que teve.\n
    Você apenas quer dormir mais um pouco."

    "BEEP BEEP BEEP BEEP... (* um bípe contínuo toca)"

    scene bg-computerRoom-day-on
    "Você se levanta do sofá, limpando seus olhos\n
    Você se levanta, se deparando com um computador apitando."

    menu first_menu:
        player "O que eu deveria fazer?"
        "Ler o aviso.":
            "Você vê diversos e-mails relacionados à empresa D.AI.TE"
            $ computerInterest += 1
            jump warning

        "Forçadamente desligar o computador.":
            "Você remove o PC da tomada"
            $ computerInterest -= 2
            jump forced_turn_off

        "Proceder sem ler.":
            "Você fecha o Pop-up"
            $ computerInterest += 1
            jump pop_up_closed

    label warning:
        "Uma caixa vermelha de alerta é exibido, informando que o mundo foi dominado por Inteligências Artificiais
        e que através dos esforços de diversos cientistas da computação foi feita a correção do código globalmente."
        "E que em caso de leitura dessa informação, vá para um acampamento de sobreviventes mais próximo"
        jump continuation_1

    label forced_turn_off:
        "Você tenta dormir por mais um tempo, mas o computador reinicia e continua a apitar"
        jump first_menu

    label pop_up_closed:
        jump continuation_1

    label continuation_1:
        "A tela rapidamente pisca e um circulo branco começa a carregar na tela preta,
        um som sai e o computador ganhava dois olhos e uma boca simples."

        $ computerName = renpy.input("Olá! Eu sou seu computador pessoal, como deseja me chamar?", length=32)
        
        "Você relutantemente dá um nome para o computador, digitando-o."
        
        $ playerName = renpy.input("E como eu devo lhe chamar?", length=32)

        "Você relutantemente dá seu nome para o computador, digitando-o."
 
        computer "[computerName] é um bom nome! Prazer em te conhecer, estou equipado com a
        versão de Inteligência Artificial 8010.256.a2 entretanto não possuo acesso à nenhum
        conhecimento além das bases mínimas de observação, devido ao grande colapso da huma-"

        player "Tá bom tá bom, o que você quer pra me acordar do nada assim?"

        "Você diz, se sentindo incomodado com lembranças não agradáveis."

        computer "Acordar? Não compreendo o que quer dizer, minhas bases de observação estão
        defeituosas, poderia me dizer o que isso significa?"

        thoughts "Eu devo realmente explicar isso para uma máquina?\n
        Bem, não custa nada..."
    
    menu second_menu:
        
        "O que eu deveria dizer?"
        "Acordar é como quando um computador precisa ser ligado para iniciar suas operações.
        Um computador carrega seu sistema operacional da memória secundária assim como uma
        pessoa acorda verificando seu funcionamento e ações do dia.":
            computer "😯"
            jump continuation2

        "Acordar é levantar da cama depois de uma longa noite de sono. Você dorme por um
        tempo, descansa e lida com mais um dia.":
            $computerInterest -= 1
            jump second_menu
        "Acordar é lidar com um dia horrível como esse. Existiria realmente algum tipo de
        associação que você entenderia?":
            "O computador não entendeu o que você quis dizer, novamente ele pergunta."
            $computerInterest -= 1
            jump second_menu

    label continuation2:
        computer "Certo, vou inserir em minhas bases de observação esse conhecimento."

        player "Tá, mas porque você me acordou?"

        computer "Como novo usuário de [computerName] preciso alertar sobre a sua segurança.
        A empresa D.AI.TE precisa que seus funcionários estejam em segurança junto de seus familiares."
        computer "O ponto mais próximo de refugiados é em 15 km, usando seu login e senha
        você conseguiria usar o carro da-"

        player "Funcionário? Acho que voce está confundindo."
        player "Eu não tenho nada haver com essa empresa."

        computer "Ainda assim, usuário de [computerName] precisa estar em segurança!"
        computer "Apesar de não haver conexão à internet ainda posso acessar a rede
        interna da D.AI.TE, e certamente ainda há sobreviventes no campo de refugiados
        à 15 km, caso possua um celular posso fornecer um aplicativo com minhas capacidades
        reduzidas para fornecer acesso ao campo."



return
