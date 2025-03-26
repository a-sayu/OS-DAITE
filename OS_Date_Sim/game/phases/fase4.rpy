
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

    #escalonamento
    menu f4_menu:
        player "Certo..."

        "Você quer dizer para eu definir um meio de agendar as tarefas que eu preciso fazer?":

            computer "Correto, podemos fazer cada coisa um pouco de cada vez!"

            jump f4_final

        "Eu tenho apenas um cérebro, não tem como processar mais de uma coisa ao mesmo tempo...":

            computer "Eu entendo que você possa ter essa limitação humana, mas mesmo com um único processador, um computador consegue ser multitarefa"

            player "Você quer dizer que isso se aplica também a mim?"

            computer "Bem, essa é minha suposição"

            jump f4_menu

        "Você quer que eu reduza meu escopo para um processo por vez? Algo como fazer até terminar?":

            "Isso acaba sendo exatamente o que eu havia pensado... E eu falei para você que não daria certo"

            computer "Não exatamente. Escalonamento não é sobre fazer uma coisa até terminar, e sim decidir qual processo será executado primeiro, alternando entre eles."

            "Okay, faz mais sentido, talvez eu tenha perdido algo na explicação anterior..."

            jump f4_menu

label f4_final:
    return
