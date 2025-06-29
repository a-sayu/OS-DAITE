# Fase 17

## O contexto, um conjunto de informações armazenados nos registradores a cada instante

label phase_17:

    jorge "Mas estamos passando muito tempo conversando."

    jorge "Acho que podemos ir, eu tenho um carro na próxima cidade, podemos usar ele."

    player "Na próxima cidade? O que você está fazendo aqui?"

    "Vocês conversam, andando."

    computer "Existe algum problema em [jorgeName] estar aqui?"

    jorge "Você poderia mudar esse nome para mim, né?"

    jorge "Bem, de qualquer forma eu posso contar o motivo, não é como se eu estivesse escondendo."

    computer "Motivo?"

    player "Sim, motivo, razão, o que ele deixou de fazer na cidade dele para estar aqui."

    computer "Desculpe, mas parece que houve um erro na transferência de dados para o tablet e não entendi o que você quis dizer."

    menu p17_menu:

        computer "Poderia usar uma explicação computacional para explicar essa situação?"

        "O motivo seria basicamente como o contexto de um processo, o estado que foi armazenado antes da trocar para esse processo, que seria ele fazer alguma coisa aqui.":
            
            computer "Ah sim, você quis dizer então que o motivo foi a última coisa que ele fez antes de dar o quantum para outro processo."
            computer "No caso estar aqui."
            jorge "Que?"
            player "O que ele quis dizer foi que você estava envolvido em alguma tarefa anterior."
            player "E agora o tempo para ela acabou e você está executando uma nova."
            player "Como se tivesse trocado o foco da execução."
            player "Mas não necessariamente a tarefa acabou."
            player "Só que o tempo que você tinha para ela acabou."
            player "Um processo é pausado para dar lugar a outro."
            jorge "Ah sim, faz sentido."
            player "Resumindo o motivo, é como o contexto em sistemas operacionais."
            player "Um conjunto de informações sobre o que você fazia antes armazenado para quando você retomar o processo."
            jump p17_end

        "O motivo seria basicamente o porquê de ele estar aqui, alguma coisa aconteceu... e agora ele está aqui.":
            computer "Desculpe, não entendi. 'alguma coisa aconteceu... e agora ele está aqui' não é uma informação muito explicativa."
            jorge "Eu entendi, mas tá muito por cima não?"
            player "Tá, fui vago demais."
            player "Eu queria falar só que um processo estava acontecendo e por algum motivo ele trocou de processo."
            computer "Desculpe, mas a definição de motivo não foi bem definida."
            player "Vamos tentar de novo..."
            jump p17_menu

        "O motivo seria basicamente que deve ser a sequencia dos passos do programa que ele estava executando?":
            computer "Ah, então o motivo seria como uma linha contínua de código, sem interrupções, que ele está seguindo para completar o que quer fazer aqui."
            jorge "Não acho que tenha sido uma sequencia de passos na minha opinião."
            jorge "Eu ainda tinha coisa pra fazer na minha cidade..."
            player "É, não faria sentido ser uma sequencia de passos, ele não parou porque era o próximo passo, mas porque ele mudou de contexto."
            computer "De fato, o que ele fazia em outra cidade pode ser considerado outro processo diferente do atual."
            jump p17_menu

label p17_end:
    return