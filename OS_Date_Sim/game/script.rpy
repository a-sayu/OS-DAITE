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

    menu leave_tutorial:
        "Você conhece os comandos?"

        "Sim":
            jump character_creation
        
        "Não":
            jump new_player

label new_player:
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

label fase_1:

    scene bg-computerRoom-night-off

    "Você chega em um escritório, com mesas empilhadas ao fundo, e uma mesa 
    próxima a janela com um computador desligado, onde você já estava a mais de uma 
    semana."

    "Colocando sua mochila sobre a mesa, você se senta em frente ao computador, para 
    afastar a fome, você começa a pensar sobre esse computador."

    player "Eu deveria tentar ligar esse computador, apesar de o mundo ter acabado, a 
    energia e a internet ainda não acabou..."

    "Apertando o botão de ligar o computador, você apoia sua mão na mesa, vendo as leds 
    ligarem, e ficar na tela de carregamento."

    player "D.AI.TE... é o sistema operacional desse computador velho?"

    menu localizacao_SO_menu:
        player "Hmm... Se eu fosse um computador, meu sistema operacional ficaria..."

        "Na minha memória de longo prazo!":
            player "É... Um computador tem um disco rígido certo? Onde o sistema 
            operacional fica guardado mesmo quando desligado, é que nem quando eu estou 
            dormindo..."
            
            jump continue_local

        "No meu... Estômago?":
            player "Parece que eu estou com muita fome, haha, achando a resposta talvez eu 
            me distraia da fome..."

            jump localizacao_SO_menu

        "Eu não sei dizer...":
            player "Bem, se eu não sei, eu tenho que estudar..."

            "Você vasculha as pilhas de papel que pareciam estar estranhamente muito 
            relacionadas com um estudo de sistemas operacionais."

            jump localizacao_SO_menu

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

    player "Para que avisar sobre o iminente fim do mundo, se ele já aconteceu?"

    "Você conecta o teclado de fio próximo no computador e reinicia ele, e rapidamente 
    ele liga. Carregando uma tela escrita D.AI.TE, com um simbolo similar a uma flor que 
    rodava enquanto carrega o sistema."

    "Assim que o computador carrega, uma animação de uma linha surgindo e dois círculos 
    aparecia, assemelhando-se a uma cara sorrindo."

    computer "Olá! Bem-Vindo ao computador oficial da DAITE, Development of Artificial 
    Intelligence Technologies Enterprise, como um computador de auxílio adoraria que me 
    desse um nome para sermos mais amigos!"

label naming_computer:
    $ computerName = renpy.input(prompt="Como deseja me chamar?", length=10);

    $ computerName = computerName.strip()

    "Você digita \'[computerName]\' na caixa de entrada de texto."
    if not computerName:
        computer "Esse Nome é Inválido :C"
        jump naming_computer

    menu computer_name:
        computer "[computerName]! Esse mesmo?"

        "Sim":
            jump continue_computer_name

        "Não":
            jump naming_computer

label continue_computer_name:
    "Você clica no botão que confirma a sua escolha. Logo depois ele pede o seu nome, 
    digitando \'[playerName]\' na caixa de entrada de texto."

    computer "Certo, já que nos introduzimos [playerName], por que você não me atendeu 
    quando eu acordei!? Eu fiquei esperando por cerca de uma hora!"

    player "Como eu falo sobre isso com uma máquina... Você entende se eu falar que eu 
    precisava acordar, levantar com calma, checar o que está ao meu redor, o que está 
    acontecendo para então fazer as tarefas do dia?"

    computer "Desculpe, mas minhas bases de conhecimento humana são faltosas por conta 
    da última atualização, poderia explicar usando de analogias de sistema operacional?"

    menu acordar_SO_menu:
        player "Como eu respondo isso? Você reflete."

        "Eu não sei, como eu poderia entender uma máquina?":
            
            computer "E como eu poderia entender você?" 

            "A máquina pergunta. Sem muito o que fazer, para que ela te entenda, você 
            vasculha as pilhas de papel que pareciam estar estranhamente muito relacionadas 
            com um estudo de sistemas operacionais."
    
            jump acordar_SO_menu

        "Você liga e tem que fazer as coisas de computador né, leds, tela e tals, pra 
        que as coisas funcionem.":

            computer "Então você demora porque ainda não está mostrando o que está 
            acontecendo?"
            
            player "Acho que não é isso que eu quero dizer, eu não mostro coisas, eu 
            preciso sentir coisas e entender o meu arredor..."
            
            "Sem muito o que fazer, para conversar com a máquina você vasculha as pilhas 
            de papel que pareciam estar estranhamente muito relacionadas com um estudo 
            de sistemas operacionais."

            jump acordar_SO_menu
        
        "Assim que liga o computador, você não já inicia realizando processos complicados, 
        é necessário que um programa armazenado na memória ROM da sua placa-mãe, chamado 
        BIOS, confira sua memória RAM, a presença de teclado, e outros dispositivos ligados 
        à você, lendo o seu armazenamento para então carregar o sistema operacional do local 
        lido.":

            computer "Oh! Então você ainda está verificando as suas partes e o que esta conectado a você? No caso \"Lugar\", \"Corpo\" e \"Memória\""
            player "Algo assim!"

label fase_3:

    "Enquanto a chuva caia, você se acomoda na cadeira, ficando em silêncio ouvindo apenas a forte chuva cair, restando a você quebrar o silêncio."

    player "[computerName]... Você é um computador de auxílio certo? Eu preciso de ajuda, um guia e tals"

    computer "Qual seria o problema [playerName]?"

    player "Eu estou aqui nesse prédio, mas eu moro meio longe daqui, minha irmã(o) foi levado pelo ônibus da escola quando tudo isso começou, e eu preciso de um ponto de começo"

    computer "Ponto de começo?"

    menu endereco_memoria_menu:
        player "Sim tipo..."

        "Quando seu sistema operacional é carregado da memória secundária e você tem que colocar o endereço da primeira instrução do seu Escalonador de Processos no Contador de Instruções e no registrador do Escalonador de Processos.":
            computer """Entendo, então significa que você precisa do primeiro passo essencial para encontrar sua irmã(o)
            
                Você pode tentar primeiramente checar as possíveis rotas que eles podem ter pego, para planejar em volta disso, apesar das bases defeituosas de conhecimento humano, sou ótimo com cálculos e previsões"""
        
            jump fase_4

        "Eu não sei se consigo te explicar isso, sabe a primeira coisa, que antecede tudo...":
            computer "Como isso se relaciona? Eu também não sei dizer sobre o que é a primeira coisa, que antecede tudo"

            player "Huh... Você tem uma base bem defeituosa de conhecimento..."
            
            "Para tentar respondê-lo melhor você vasculha as pilhas de papel que pareciam estar estranhamente muito relacionadas com um estudo de sistemas operacionais."

            jump endereco_memoria_menu

        "É tipo o oposto do fim!":
            computer "Interessante! Mas não acho que é uma resposta que explique o que é um ponto de começo!"
            
            player "Okay, fazer piada não vai ajudar... " 
            
            "Você vasculha as pilhas de papel que pareciam estar estranhamente muito relacionadas com um estudo de sistemas operacionais."

            jump endereco_memoria_menu

label fase_4:
    computer "Pelas minhas previsões, os sensores estão indicando uma menor chance de chuva depois das 19h. Você precisa de uma ordem para fazer as coisas, certo?"

    player "Esse horário não é bom, tem chance de eu ser atacada por uma daquelas... Máquinas. Eu não conseguiria chegar a tempo nem mesmo na cidade mais próxima!"

    "Você se levanta, andando em círculos pelo pequeno cômodo."

    player "Não dá pra fazer isso, considerando que eu tenho que comer, ficar em segurança e explorar em busca dele(a)"

    computer "Não precisa se desesperar, é só aplicar um algoritmo de escalonamento!"

    player "Eu não sou um computador, nem uma IA pra fazer isso..."

    "Você se senta, se perguntando se essa máquina sabe do que ela está falando quando se trata de um humano."

    computer "Posso não entender corretamente um ser humano, mas suas relações de termos podem tornar isso possível"

    player "Eu nem sei o que é escalonamento..."

    computer "Em um dos meu arquivos de referência, quando um computador é multiprogramado, ele frequentemente tem múltiplos processos ou threads competindo pela CPU"

    computer "Se apenas uma CPU está disponível, uma escolha precisa ser feita de qual processo será executado no momento, quem faz isso é o escalonador do Sistema Operacional"

    computer "Ele utiliza um algoritmo de escalonamento para decidir!"

    menu escalonamento_menu:
        player "Certo..."

        "Você quer dizer para eu definir um meio de agendar as tarefas que eu preciso fazer?":

            computer "Correto, podemos fazer cada coisa um pouco de cada vez!"

            jump fase_5

        "Eu tenho apenas um cérebro, não tem como processar mais de uma coisa ao mesmo tempo...":

            computer "Eu entendo que você possa ter essa limitação humana, mas mesmo com um único processador, um computador consegue ser multitarefa"

            player "Você quer dizer que isso se aplica também a mim?"

            computer "Bem, essa é minha suposição"

            jump escalonamento_menu

        "Você quer que eu reduza meu escopo para um processo por vez? Algo como fazer até terminar?":

            "Isso acaba sendo exatamente o que eu havia pensado... E eu falei para você que não daria certo"

            computer "Não exatamente. Escalonamento não é sobre fazer uma coisa até terminar, e sim decidir qual processo será executado primeiro, alternando entre eles."

            "Okay, faz mais sentido, talvez eu tenha perdido algo na explicação anterior..."

            jump escalonamento_menu

label fase_5:

    player "Okay, então como eu deveria escalonar me alimentar, me proteger e procurar por minha irmã?"

    player "Tipo, eu posso comer enquanto procuro minha irmã e fico atento para qualquer perigo a minha volta..."

    computer "Bem, você não precisa estar fazendo tudo ao mesmo tempo, isso não é escalonar!"

    computer "Devemos pensar sobre isso com muito cuidado."

    player "Realmente... Já que estamos pensando em conceitos de Sistemas Operacionais, que tal relacionar essas coisas como programas?"
    
    
    menu relacao_1_menu:

        computer "Então... Quando você precisa se alimentar?"
        
        
        python: 
            if correct[0]:
                jump relacao_2_menu

        "Eu posso comer quando eu puder, não é tão necessário...": // FDP

            $ correct[0] = False
            jump relacao_2_menu

        "Eu tenho que separar pelo menos algum tempo para encontrar mais alimentos e comer.": // VDD

            $ correct[0] = True
            jump relacao_2_menu 
            

    menu relacao_2_menu:

        python:
            if correct[1]:
                jump relacao_3_menu

        computer "Então... Quando você precisa se proteger?"

        "Está muito perigoso, eu deveria colocar toda minha atenção para isso...": // FDP

            $ correct[1] = False
            jump relacao_3_menu

        "É importante estar atento... Mas descansar também, eu posso sempre procurar abrigos": //VDD

            $ correct[1] = True
            jump relacao_3_menu

    menu relacao_3_menu:

        python:
            if correct[2]:
                jump f5_verificacao

        computer "Então... Quando você precisa buscar sua irmã?"

        "Eu deveria focar nessa busca totalmente... Se eu demorar como vou ter certeza que ela estará a salvo...":

            $ correct[2] = False
            jump f5_verificacao

        "Mesmo que eu não saiba onde minha irmã está, eu também não posso deixar de me cuidar...":

            $ correct[2] = True
            jump f5_verificacao

    label f5_primeira_verificacao:
        
        if not (correct[0] and correct[1] and correct[2]):
            jump f5_erradas
        else:
            jump f5_corretas
    
#Caso: Todas as respostas corretas.
    label f5_corretas:
        
        computer "Exatamente, uma divisão de tempo para cada ação é importante, não foque demais em algo e agende seus programas, isso é escalonar os programas!"
        jump fase_6
    
    label f5_erradas:
        
        label f5_primeira_errada:
            if correct[0]:
                jump f5_segunda_errada
            computer "Comida é importante, mas não se deve ficar comendo também não é tão bom..."
        
        label f5_segunda_errada:
            if correct[1]:
                jump f5_terceira_errada
            computer "Segurança é importante, mas não se deve viver paranóico..."
        
        label f5_terceira_errada:
            if correct[2]:
                jump relacao_1_menu
            computer "Buscar sua irmã é importante, mas não se deve ignorar suas necessidades..."
        
        jump relacao_1_menu


label fase_6:
return
