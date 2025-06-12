## Tema: Fazer coisas ao "mesmo tempo"/ser multiprogramado
label phase_6:


    player "Certo, já que acertei, vamos começar com comida."

    player "Minhas reservas já estão bem baixas, e pra uma viagem longa
    como essa..."

    "Você olha para o computador, os dois pontos feitos de pixels na
    tela do computador parecem te encarar."

    player "Vai ser uma viagem longa..."

    computer "Correto. Uma longa viagem presumindo que sua irmã esteja
    na capital"

    "Você olha em direção à janela, encarando o horizonte por alguns 
    instantes e volta seu olhar para o computador."

    player "Você é um computador, eu não vou poder te levar"

    computer "Como assim?"

    player "Bem, você é um computador de mesa, você não pode ser usado
    enquanto eu estou andando"

    computer "Mas eu posso ser levado a vários lugares! E você me usaria
    de vez enquando."

    player "É imprático isso, você entende, né?"

    computer "Pelo meu entendimento, não."

    label p6_question:
        player "Ahm... Vamos pensar nas classificações de sistemas operacionais"

        player "Você como um computador seria o sistema operacional"

        menu p6_menu:
            player "E programas como se fossem lugares"

            "Você é multiprogramado, porque você pode estar sendo usado em um lugar A, B e C ao decorrer do tempo": # fdp
                computer "Se eu posso estar em vários locais, você pode me levar..."
                player "Não, não posso! Deixa eu explicar de novo, talvez eu tenha
                confundido algo..."
                jump p6_question

            "Você é monoprogramado, porquê você pode estar em apenas um lugar A por uso, que seria a mesa.": # vdd
                computer "Ah... Entendo..."
                player "Se você portátil, eu poderia, tipo um celular ou um tablet"
                computer "Se eu for um tablet você me levaria?"
                player "Um computador não pode magicamente se tornar um tablet"
                computer "Mas existem tablets com o sistema D.AI.T.E!"
                jump p6_end
                
label p6_end:
    return