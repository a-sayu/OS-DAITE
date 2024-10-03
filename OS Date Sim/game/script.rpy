# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


default interest = 0
default playerName = "Jogador"
default computerName = "Computador"


define computer = Character("[computerName]")

define player = Character("[playerName]")

define thoughts = Character("[playerName]", what_suffix='"', what_prefix='"')

# The game starts here.

# scene "name of the file without quotes and without .png"
# show "name of the file without quotes and without .png"
# char variable "String in quotes"

label start:

    scene blackScreen

    computer "BEEP BEEP BEEP BEEP... (* um bípe contínuo toca)"

    scene computer room

    "Você sente seu estômago revirar com o último almoço que teve."
    thoughts "Você apenas quer dormir mais um pouco."

    computer "BEEP BEEP BEEP BEEP... (* um bípe contínuo toca)"

    thoughts "Você se levanta, se deparando com um computador antigo, que esta no canto do quarto, apitando."

    menu first_menu:
        "O que eu devo fazer?"
        "Ler o aviso.":
            "Você vê diversos e-mails relacionados à empresa D.AI.TE"
            "+1 ponto de Interesse."
            $ interest += 1
            jump warning

        "Forçadamente desligar o computador.":
            "Você remove o PC da tomada"
            "-2 pontos de Interesse."
            $ interest -= 2
            jump forced_turn_off

        "Proceder sem ler.":
            "Você fecha o Pop-up"
            "+1 ponto de Interesse."
            $ interest += 1
            jump pop_up_closed

    label warning:
        "Lendo os e-mails, você encontra o vê um e-mail vermelho de alerta, em que é um alerta de que o mundo foi dominado por Inteligências Artificiais mortíferas e que foi possível através dos esforços de diversos cientistas da computação a correção do código globalmente."
        "Assim como as mais de 90\% de baixas humanas, e que está ocorrendo a busca por sobreviventes em cada continente, pedindo que busquem os pontos de socorro em posições estratégicas."
        jump continuation1

    label forced_turn_off:
        "Você dorme por mais um dia"
        jump continuation1

    label pop_up_closed:
        "Nada de mais acontece"
        jump continuation1

    label continuation1:
        "A tela rapidamente pisca e um circulo branco começa a carregar na tela preta, um som sai e o computador ganhava dois olhos e uma boca simples."
        
        $ computerName = renpy.input("Olá! Eu sou seu computador pessoal, como deseja me chamar?", length=32)

        "Você relutantemente dá um nome para o computador, digitando-o."

        computer "[computerName] é um bom nome! Prazer em te conhecer, estou equipado com a versão de Inteligência Artificial 8010.256.a2 entretanto não possuo acesso à nenhum conhecimento além das bases mínimas de observação, devido ao grande colapso da huma-"

        player "Tá bom tá bom, o que você quer pra me acordar do nada assim?"

        "Você diz, se sentindo incomodado com lembranças não agradáveis."

        computer "Acordar? Não compreendo o que quer dizer, minhas bases de observação estão defeituosas, poderia me dizer o que isso significa?"

        thoughts "Eu devo realmente explicar isso para uma máquina?"
        thoughts "Bem, não custa nada..."
    
    menu second_menu:
        "O que eu deveria dizer?"
        "Acordar é como quando um computador precisa ser ligado para iniciar suas operações. Um computador carrega seu sistema operacional da memória secundária assim como uma pessoa acorda verificando seu funcionamento e ações do dia.":
            "O computador mostra um rosto semelhante ao emoji: 😯"
            jump continuation2

        "Acordar é levantar da cama depois de uma longa noite de sono. Você dorme por um tempo, descansa e lida com mais um dia.":
        "Acordar é lidar com um dia horrível como esse. Existiria realmente algum tipo de associação que você entenderia?":
            "O computador não entendeu o que você quis dizer, novamente ele pergunta."
            $interest -= 1
            jump second_menu

    label continuation2:
        computer "Certo, vou inserir em minhas bases de observação esse conhecimento."

        player "Tá, mas porque você me acordou?"

        computer "Como novo usuário de [nome] preciso alertar sobre a sua segurança. A empresa D.AI.TE precisa que seus funcionários estejam em segurança junto de seus familiares."
        computer "O ponto mais próximo de refugiados é em 15 km, usando seu login e senha você conseguiria usar o carro da-"

        player "Funcionário? Acho que voce está confundindo."
        player "Eu não tenho nada haver com essa empresa."

        computer "Ainda assim, usuário de [nome] precisa estar em segurança!"
        computer "Apesar de não haver conexão à internet ainda posso acessar a rede interna da D.AI.TE, e certamente ainda há sobreviventes no campo de refugiados à 15 km, caso possua um celular posso fornecer um aplicativo com minhas capacidades reduzidas para fornecer acesso ao campo."

return
