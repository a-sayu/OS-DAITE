# Fase 16

## Como definir para onde ele deve alternar?

label phase_16:

    player "Precisamos no entanto conversar sobre uma coisa agora."

    "Você retira o tablet da bolsa, retirando ele do silencioso."

    player "Esse é [computerName]"

    computer ":D"

    jorge "Hmm...? Isso é um tablet com um fundo animado nâo?"

    player "Não, esse é o [computerName], ele é um tablet com o sistema DAITE."

    player "Basicamente ele tem o mesmo sistema de IA que os robôs."

    jorge "Por que você carrega isso com você?"

    jorge "Equipamentos da DAITE são tipo imãs de robôs, ele é perigoso."

    player "Mas ele me ajudou até agora, e gostaria que você confiasse nele."

    jorge "Complicado..."

    jorge "Eu vou aceitar por enquanto, se alguma coisa acontecer por causa dele, eu to fora."

    computer "Obrigado pelo voto de confiança, como posso te chamar?"

    jorge "Não vou dar informações pessoais pra vocês IAs."

    computer "Seu nome é muito comprido, Não vou dar informações pra vocês IAs."

    computer "Posso te chamar de Não vou dar?"

    $ jorgeName = "Não vou dar."

    "Jorge apenas não responde, apenas olha para você com um olhar de julgamento."

    player "Ele apenas está sendo engraçado... Certo [computerName]?"

    computer "Como você não respondeu, irei assumir que seja esse seu nome."

    computer "Caso queira mudar [jorgeName] você pode pedir para [playerName] mudar nas configurações."

    player "Okay..."

    player "Mas, okay, vamos para o outro tópico que eu tenho pra falar."

    jorge "Vai me dizer que você tem outro amigo."

    "Jorge diz, fazendo sinal de aspas quando fala amigo."

    player "Não!"

    player "Só, ah..."

    player "O que eu quero dizer, é que como nós vamos escalonar as atividades."

    jorge "Escalonar?"

    player "Sim, com escalonar eu quero dizer agendar cada tarefa que iremos fazer."

    computer "Nesse caso, você quer saber a ordem que cada ação vai ter."

    jorge "Ah faz sentido... Eu acho?"

    "No entanto você olha para a cara e percebe que ele não entendeu."

    thoughts 'Será que eu conversei tanto com o [computerName] que eu esqueci como conversar com pessoas normais?'

    player "Uh..."

    thoughts 'Sabendo de tudo que eu sei sobre prioridade e processos'

    menu p16_menu_1:

        thoughts 'Como eu explicaria sobre como definir quando alternar entre tarefas para uma pessoa normal...'

        "O que eu queria dizer é que podemos usar um algoritmo Round Robin para definir para quem alternar...":
            jorge "Oi?"
            computer "Esse algoritmo não implementa prioridade."
            jorge "E eu não faço ideia do que você está falando."
            computer "O escalonamento round robin é quando se tem uma fila, e cada processo tem acesso à um quantum do processador."
            player "Basicamente a gente faz uma sequencia de tarefas e a gente vai separando algo como 5 minutos para cada, e vai revezando entre elas."
            player "Resultando em um ciclo."
            jorge "Ah sim, realmente isso não tem prioridade nenhuma."
            jump p16_menu_1

        "O que eu queria dizer é que a gente precisaria definir uma forma de agendar de forma prioritária, com prioridade nas tarefas e pessoas.":
            jorge "Ah... Sim."
            jump p16_menu_2

        "O que eu queria dizer é que podemos usar um algoritmo Filas Múltiplas para definir para quem alternar...":
            jorge "Oi?"
            computer "Esse algoritmo implementa prioridade, mas acho que nosso amigo [jorgeName] não entendeu..."
            player "Ah sim..."
            jorge "Sim, eu não faço ideia do que vocês estão falando."
            computer "O escalonamento filas múltiplas tem várias filas separadas por prioridades, em que as tarefas são executadas em uma sequencia descendente de prioridades."
            player "O que eu quis dizer foi executarmos as tarefas mais importantes por completo e ir gradualmente alocando tempo para atividades de menor prioridade."
            jorge "Ah sim, faz sentido fazer algo assim."
            jump p16_menu_1

    menu p16_menu_2:

        jorge "Mas isso é só o geral né? Qual o plano?"

        "Então... Filas Múltiplas...?":
            jorge "Oi?"
            computer "O escalonamento filas múltiplas tem várias filas separadas por prioridades, em que as tarefas são executadas em uma sequencia descendente de prioridades."
            player "O que eu quis dizer foi executarmos as tarefas mais importantes por completo e ir gradualmente alocando tempo para atividades de menor prioridade."
            jorge "Ah sim... Isso parece interessante!"
            jump p16_end
        
        "Então... Round Robin...?":
            jorge "Oi?"
            computer "O escalonamento round robin é quando se tem uma fila, e cada processo tem acesso à um quantum do processador."
            player "Basicamente a gente faz uma sequencia de tarefas e a gente vai separando algo como 5 minutos para cada, e vai revezando entre elas."
            player "Resultando em um ciclo."
            jorge "Mas isso... Não é prioritária?"
            jump p16_menu_2

label p16_end:
    return