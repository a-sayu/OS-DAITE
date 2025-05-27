label phase_2:
    #TODO: cena de alerta

    scene bg-computer-day-on

    "ALERTA! ALERTA! ALERTA!"
    "O som te assusta, seu corpo ainda está lento, por causa do cansaço do dia anterior, 
    observando os seus arredores, você estranha, mas relembra dos eventos dos últimos 
    meses, e como o mundo que você conhecia se foi, indo em direção ao computador, você 
    se senta em frente a ele."
    
    player "O que você quer?"
    "Você pergunta, colocando a mão sobre a sua testa."

    thoughts "O que um computador iria querer também né? Haha, parece que eu estou 
    enlouquecendo..."

    "Você suspira e olha para as letras escritas no computador, avisando a falta de um 
    teclado e também um alerta de emergência mundial sobre um assunto que você já estava 
    bem familiarizado."

    thoughts "Para que avisar sobre o iminente fim do mundo, se ele já aconteceu?"

    "Você conecta o teclado de fio próximo no computador e reinicia ele, e rapidamente 
    ele liga. Carregando uma tela escrita D.AI.TE, com um simbolo similar a uma flor que 
    rodava enquanto carrega o sistema."

    "Assim que o computador carrega, uma animação de uma linha surgindo e dois círculos 
    aparecia, assemelhando-se a uma cara sorrindo."

    computer "Olá! Bem-Vindo ao computador oficial da DAITE, Development of Artificial 
    Intelligence Technologies Enterprise, como um computador de auxílio adoraria que me 
    desse um nome para sermos mais amigos!"

    call p2_computer_naming

    "Você clica no botão que confirma a sua escolha. Logo depois ele pede o seu nome, 
    digitando \'[playerName]\' na caixa de entrada de texto."

    computer "Certo, já que nos introduzimos [playerName], por que você não me atendeu 
    quando eu acordei!? Eu fiquei esperando por cerca de uma hora!"

    player "Como eu falo sobre isso com uma máquina... Você entende se eu falar que eu 
    precisava acordar, levantar com calma, checar o que está ao meu redor, o que está 
    acontecendo para então fazer as tarefas do dia?"

    computer "Desculpe, mas minhas bases de conhecimento humana são faltosas por conta 
    da última atualização, poderia explicar usando de analogias de sistema operacional?"

    menu p2_menu:
        "Como eu respondo isso? Você reflete."

        "Eu não sei, como eu poderia entender uma máquina?":
            
            computer "E como eu poderia entender você?" 

            "A máquina pergunta. Sem muito o que fazer, para que ela te entenda, você 
            vasculha as pilhas de papel que pareciam estar estranhamente muito relacionadas 
            com um estudo de sistemas operacionais."
    
            jump p2_menu

        "Você liga e tem que fazer as coisas de computador né, leds, tela e tals, pra 
        que as coisas funcionem.":

            computer "Então você demora porque ainda não está mostrando o que está 
            acontecendo?"
            
            player "Acho que não é isso que eu quero dizer, eu não mostro coisas, eu 
            preciso sentir coisas e entender o meu arredor..."
            
            "Sem muito o que fazer, para conversar com a máquina você vasculha as pilhas 
            de papel que pareciam estar estranhamente muito relacionadas com um estudo 
            de sistemas operacionais."

            jump p2_menu
        
        "Assim que liga o computador, você não já inicia realizando processos complicados, 
        é necessário que um programa armazenado na memória ROM da sua placa-mãe, chamado 
        BIOS, confira sua memória RAM, a presença de teclado, e outros dispositivos ligados 
        à você, lendo o seu armazenamento para então carregar o sistema operacional do local 
        lido.":

            computer "Oh! Então você ainda está verificando as suas partes e o que esta conectado a você? No caso \"Lugar\", \"Corpo\" e \"Memória\""
            
            player "Algo assim!"

            jump p2_end

#naming computer or computer naming?
label p2_computer_naming:
    $ computerName = renpy.input(prompt="Como deseja me chamar?", length=10);
    $ computerName = computerName.strip()

    "Você digita \'[computerName]\' na caixa de entrada de texto."
    if not computerName:
        computer "Esse Nome é Inválido :C"
        jump p2_computer_naming

    menu p2_computer_naming_menu:
        computer "[computerName]! Esse mesmo?"

        "Sim":
            return

        "Não":
            jump p2_computer_naming

label p2_end:
    return