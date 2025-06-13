# Fase 15

## Como funciona um algoritmo de escalonamento e quanto tempo há para a realização de cada um dos trabalhos

label phase_15:

    "Pela tela do tablet, percebia que já estava há um bom tempo no supermercado."

    thoughts 'Já é quase meia noite, faz um bom tempo que eu não sabia a exatidão das horas'

    thoughts 'Eu precisaria ir dormir agora, para ter um pouco de descanso'

    "Você diz, e logo deixa um alarme no tablet para acordar pouco antes do sol nascer."

    "Quando acorda... Um alarme que não era o seu está tocando."

    "Olhando a tela, você percebe um aviso, e suas mãos começam a soar."

    computer "[playerName], inteligência artificial de versão maliciosa identificada nas proximidades"

    "Essa mensagem aparecia na tela. Ao olhar ao redor, você percebe um ser de aparência humanóide próximo à saída do supermercado."

    "Ele vaga sem rumo, como se estivesse patrulhando."

    "Você cancela o alarme, o anúncio do tablet e o silencia."

    thoughts 'Eu tenho que sair daqui'

    "Você guarda as coisas que teria colocado para fora da bolsa, e se prepara para sair."

    'Em meio a sua escapada no entanto, sua mochila bate em um copo de vidro e ele cai.'

    "O som é o suficiente para alertar o robô, que começa a correr em sua direção."

    "Você se desespera e começa a correr em direção à saída mais próxima."

    "O robô se aproxima rapidamente em sua direção, você fecha os olhos se preparando para o pior."

    "Porém, Quando você menos espera, você ouve um forte som de impacto metálico e o som de um grande objeto caindo no chão."

    "Você alcança a saída ofegante e olha para trás. Você vê uma pessoa batendo com um cano de metal no robô, que está caído no chão."

    "A pessoa olha para você, e você se esconde atrás de um carro por perto."

    jorge "Ei! Eu vi você, não sou inimigo!"

    "Ele grita, e você pensa por alguns segundos até se revelar."

    jorge "Você está bem?"

    "Ele pergunta guardando o cano de metal na mochila."

    player "Ah... Sim..."

    jorge "Meu nome é Jorge, e você?"

    player "Ah, é [playerName]"

    jorge "Desculpa a pergunta, mas você tem comida sobrando?"

    player "Tenho apenas para mim, se você precisa, você pode procurar lá dentro, eu não peguei tudo..."

    jorge "Ah, claro, valeu!"

    "Jorge diz indo em direção ao mercado, porém ele para e olha para você com uma voz tímida"

    jorge "Você está indo em direção a capital?"

    jorge "Eu estou querendo ir para lá a uma semana, mas..."

    jorge "Ir sozinho é perigoso..."

    jorge "Um robô pode não parecer muita coisa, mas perto da capital está bem pior... E eu realmente preciso ir pra lá"

    player "Você pode esperar um pouco? Eu preciso pensar"

    "Você diz, achando que foi muita informação e decisão de uma vez só."

    thoughts 'No meu plano de escalonamento, eu só considerei o meu tempo de execução...'

    thoughts 'Eu poderia delegar algumas das funções pra ele não?'

    thoughts 'Ele pode ficar com toda a parte de segurança e nós vamos juntos para lá...'

    thoughts 'Não isso não parece certo em escalonamento'

    "Lembrando do [computerName], você pensa um pouco sobre o escalonamento. Você se vira para Jorge, pronto para respondê-lo."

    menu p15_menu:

        "Sendo vocês dois programas, pensa em como deveria ser a distribuição das tarefas."

        "Não, eu prefiro ir só.":
            jorge "Ah, entendo, foi bem súbito a ideia né?"
            jorge "Valeu de qualquer forma por ter pensado sobre isso"
            "Jorge agradece e acena, entrando no supermercado."
            "Você continua seu caminho, seguindo pela rodovia até a capital a sós, apenas com o tablet."
            "Quando você para para comer, você acaba sendo atacado por um grupo de robôs."
            call phase_34
            jump p15_menu

        "Se você aceitar ser responsável por toda a segurança e deixar a gerência de toda a sua comida comigo, eu ajudo.":            
            thoughts 'Eu vou estar mais seguro, a gente é dois programas separados, então a gente lida conforme nossas habilidades'
            jorge "Eu entendo..."
            jorge "Desculpa, mas não posso fazer assim"
            jorge "Valeu por falar sobre a comida apesar disso"
            "Jorge agradece e acena, entrando no supermercado."
            "Você continua seu caminho, seguindo pela rodovia até a capital a sós, apenas com o tablet."
            "Quando você para para comer, você acaba sendo atacado por um grupo de robôs."
            call phase_34
            jump p15_menu

        "Se você aceitar dividir a segurança e a comida igualmente, a gente reveza e tudo mais e qualquer coisa a gente cuida um do outro, eu ajudo":
            thoughts 'Quando se escalona, devemos dar à um programa tempos iguais e que ele pudessem completar todas as suas atividades, sem controlar todo o tempo'
            thoughts 'O escalonamento deve ser justo e igualitário, se formos pensar como um sistema operacional, dois processos precisam de tempo de CPU equilibrado. Se um monopolizar o tempo, o outro falha.'
            jorge "Claro, valeu, eu estou de acordo em dividir"
            jorge "Achei que fosse pedir algo absurdo"
            player "É sempre importante ser justo nessas horas, estamos igualmente buscando coisas importantes na capital, certo?"
            jorge "Certo, valeu demais"
            jump p15_end

label p15_end:
    return