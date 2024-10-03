# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

playerName = "Jogador"
computerName = "Computador"
define computer = Character(computerName)

define player = Character(playerName)

define thoughts = Character(playerName, what_suffix='"', what_prefix='"')

interest = 0

# The game starts here.

# scene "name of the file without quotes and without .png"
# show "name of the file without quotes and without .png"
# char variable "String in quotes"

label start:

    scene blackScreen

    computer "BEEP BEEP BEEP BEEP... (* um bípe contínuo toca)"

    scene computer room

    thoughts "Você sente seu estômago revirar com o último almoço que teve."
    thoughts "Você apenas quer dormir mais um pouco."

    computer "BEEP BEEP BEEP BEEP... (* um bípe contínuo toca)"

    thoughts "Você se levanta, se deparando com um computador antigo, que esta no canto do quarto, apitando."

    menu first_menu:
        "O que eu devo fazer?"
        "Ler o aviso.":
            action "Você vê diversos e-mails relacionados à empresa D.AI.TE"
            action "+1 ponto de Interesse."
            interest++;
            jump warning

        "Forçadamente desligar o computador.":
            action "Você remove o PC da tomada"
            action "-2 pontos de Interesse."
            interest -= 2;
            jump forced_turn_off

        "Proceder sem ler.":
            action"Você fecha o Pop-up"
            action "+1 ponto de Interesse."
            jump pop_up_closed

    label warning:
        action "Lendo os e-mails, você encontra o vê um e-mail vermelho de alerta, em que é um alerta de que o mundo foi dominado por Inteligências Artificiais mortíferas e que foi possível através dos esforços de diversos cientistas da computação a correção do código globalmente."
        action "Assim como as mais de 90% de baixas humanas, e que está ocorrendo a busca por sobreviventes em cada continente, pedindo que busquem os pontos de socorro em posições estratégicas."
        jump continuation1

    label forced_turn_off:
        action "Você dorme por mais um dia"
        jump continuation1

    label pop_up_closed:
        action "Nada de mais acontece"
        jump continuation1

    label: continuation1:
        action "A tela rapidamente pisca e um circulo branco começa a carregar na tela preta, um som sai e o computador ganhava dois olhos e uma boca simples."

        computer "Olá! Eu sou seu computador pessoal, como deseja me chamar?"
        #TODO: Opção de INSERIR NOME

        action "Você relutantemente dá um nome para o computador, digitando-o."

        computer "{computerName} é um bom nome! Prazer em te conhecer, estou equipado com a versão de Inteligência Artificial 8010.256.a2 entretanto não possuo acesso à nenhum conhecimento além das bases mínimas de observação, devido ao grande colapso da huma-"

        player "Tá bom tá bom, o que você quer pra me acordar do nada assim?"

        action "Você diz, se sentindo incomodado com lembranças não agradáveis."




    


    return
