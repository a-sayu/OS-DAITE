# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Variáveis
default computerInterest = 0
default playerName = "?"
default computerName = "Computador"
define computer = Character("[computerName]", image="computer")
define player = Character("[playerName]")
define thoughts = Character("[playerName]", what_suffix='"', what_prefix='"')

# Imagens
image computer = "computer.png"
image bg-blackScreen = "#000"
image bg-compurterRoom-day-off = "computerRoom-day-off.png"
image bg-compurterRoom-day-on = "computerRoom-on-day.png"
image bg-compurterRoom-night-off = "computerRoom-off-night.png"
image bg-compurterRoom-night-on = "computerRoom-on-day.png"


# The game starts here.

label start:

    scene bg-desolatedCity
    "O silêncio das ruas era predominante, o vento corria por sua pele"
    $ playerName = renpy.input("Você retira do bolso um chaveiro com seu nome: ", length=8)
    "Um conjunto de chaves de uma casa distante, você caminha para o prédio em silêncio, atento aos seus arredores.
    \nAbrindo calmamente a porta, você se depara com a sua atual \'casa\'"

    scene bg-computerRoom-night-off
    "Colocando sua mochila sobre uma mesa de escritório vazia"
    player "Mais um dia sobre o olhar solitário do vigia
    \nO que vamos comer hoje?"
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
        "Você liga o computador"
        "Na esperança de que pudesse encontrar alguma forma de se comunicar com outros sobreviventes"
        "O computador parece não ligar"
        "Você apenas suspira e vai deitar-se no sofá do escritório"

    scene bg-blackScreen

    "BEEP BEEP BEEP BEEP... (* um bípe contínuo toca)"
    "Você sente seu estômago roncar com a pequena última refeição que teve."
    "Você apenas quer dormir mais um pouco."

    "BEEP BEEP BEEP BEEP... (* um bípe contínuo toca)"

    scene bg-computerRoom-day-on
    "Você se levanta do sofá, limpando seus olhos"
    "Você se levanta, se deparando com um computador antigo, que esta no canto do quarto, apitando."

    menu first_menu:
        "O que eu devo fazer?"
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
        "Lendo os e-mails, você encontra o vê um e-mail vermelho de alerta, em que é um alerta de que o mundo foi dominado por Inteligências Artificiais mortíferas e que foi possível através dos esforços de diversos cientistas da computação a correção do código globalmente."
        "Assim como as mais de 90\% de baixas humanas, e que está ocorrendo a busca por sobreviventes em cada continente, pedindo que busquem os pontos de socorro em posições estratégicas."
        jump continuation_1

    label forced_turn_off:
        "Você dorme por mais um dia"
        "Na manhã do dia seguinte, você se depara com o computador ligado novamente"
        jump continuation_1

    label pop_up_closed:
        jump continuation_1

    label continuation_1:
        "A tela rapidamente pisca e um circulo branco começa a carregar na tela preta, um som sai e o computador ganhava dois olhos e uma boca simples."

        $ computerName = renpy.input("Olá! Eu sou seu computador pessoal, como deseja me chamar?", length=32)
        
        "Você relutantemente dá um nome para o computador, digitando-o."
        
        $ playerName = renpy.input("E como eu devo lhe chamar?", length=32)

        "Você relutantemente dá seu nome para o computador, digitando-o."

        show computer
        computer "[computerName] é um bom nome! Prazer em te conhecer, estou equipado com a versão de Inteligência Artificial 8010.256.a2 entretanto não possuo acesso à nenhum conhecimento além das bases mínimas de observação, devido ao grande colapso da huma-"

        player "Tá bom tá bom, o que você quer pra me acordar do nada assim?"

        "Você diz, se sentindo incomodado com lembranças não agradáveis."

        computer "Acordar? Não compreendo o que quer dizer, minhas bases de observação estão defeituosas, poderia me dizer o que isso significa?"

        thoughts "Eu devo realmente explicar isso para uma máquina?"
        thoughts "Bem, não custa nada..."
    
    menu second_menu:
        
        "O que eu deveria dizer?"
        "Acordar é como quando um computador precisa ser ligado para iniciar suas operações. Um computador carrega seu sistema operacional da memória secundária assim como uma pessoa acorda verificando seu funcionamento e ações do dia.":
            computer "😯"
            jump continuation2

        "Acordar é levantar da cama depois de uma longa noite de sono. Você dorme por um tempo, descansa e lida com mais um dia.":
            $computerInterest -= 1
            jump second_menu
        "Acordar é lidar com um dia horrível como esse. Existiria realmente algum tipo de associação que você entenderia?":
            "O computador não entendeu o que você quis dizer, novamente ele pergunta."
            $computerInterest -= 1
            jump second_menu

    label continuation2:
        computer "Certo, vou inserir em minhas bases de observação esse conhecimento."

        player "Tá, mas porque você me acordou?"

        computer "Como novo usuário de [computerName] preciso alertar sobre a sua segurança. A empresa D.AI.TE precisa que seus funcionários estejam em segurança junto de seus familiares."
        computer "O ponto mais próximo de refugiados é em 15 km, usando seu login e senha você conseguiria usar o carro da-"

        player "Funcionário? Acho que voce está confundindo."
        player "Eu não tenho nada haver com essa empresa."

        computer "Ainda assim, usuário de [computerName] precisa estar em segurança!"
        computer "Apesar de não haver conexão à internet ainda posso acessar a rede interna da D.AI.TE, e certamente ainda há sobreviventes no campo de refugiados à 15 km, caso possua um celular posso fornecer um aplicativo com minhas capacidades reduzidas para fornecer acesso ao campo."

return
