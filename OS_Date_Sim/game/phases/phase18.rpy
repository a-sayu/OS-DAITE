# Fase 18

## Como voltar ao ponto que ele foi interrompido (Com o contexto – salvando e recuperando-o)

label phase_18:

    "Jorge suspira com uma risadinha ao final."

    jorge "Com tanta informação, acho que meu contexto nem importa mais, né?"

    "Ele diz enfatizando a palavra contexto."

    computer "[jorgeName], você poderia recuperar o contexto"

    jorge "[playerName] traduz pra mim por favor?"

    menu p18_menu:

        player "o que ele quis dizer foi..."

        "Com recuperar contexto, ele quer dizer pra voltar no ponto que ele foi interrompido.":
            computer "Exato! Contextos são salvos e podem ser recuperados para serem retomados"
            player "Eu também gostaria de saber"
            player "Por que você está aqui?"
            jorge "Minha namorada estava fazendo faculdade aqui, eu vim visitar ela porque ela tinha uma surpresa para mim"
            jorge "Mas o apocalipse chegou antes... Eu tinha vindo de viagem no carro dela"
            jorge "Só resta suposições até eu encontrar ela novamente"
            "Ele ri, mas visivelmente um pouco chateado."
            thoughts 'Porque ela abandonaria ele para ir pra capital?'
            jump p18_end
            
        "Com recuperar contexto, ele quer dizer ignorar o que ficou pra trás e seguir em frente com outra tarefa.":
            computer "Negativo"
            computer "Recuperar o contexto significa retomar exatamente do ponto onde a tarefa parou."
            player "Ah, é mesmo"
            jorge "Bem, agora você vai falar a mesma coisa que ele disse..."
            jump p18_menu

        "Com recuperar contexto, ele quer dizer salvar tudo pra depois decidir o que fazer.":            
            computer "Salvamento de contexto é parte do processo, mas do processo anterior"
            computer "Salvar o contexto faz parte do processo, mas agora o que queremos é recuperar o estado do processo anterior."
            jorge "Ah então salvar o contexto é parecido com aquela opção de salvar antes de fechar documentos"
            computer "Boa analogia"
            player "Ah, é mesmo"
            jorge "Bem, agora você vai falar a mesma coisa que ele disse..."
            jump p18_menu

label p18_end:
    return