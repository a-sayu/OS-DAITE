# Fase 19

## Onde e como o contexto é armazenado?

label phase_19:

    computer "Entendo, [player], e [jorge], onde vocês armazenam os contextos?"

    computer "Sistemas operacionais armazenam contexto em uma tabela de processos."

    computer "E a tabela fica dentro da memória RAM, que no seu caso é a bolsa de
    fácil acesso."

    jorge "Eu não faço ideia do que você está falando."

    "Você para e olha para o tablet por alguns segundos."

    player "Tabela de processos?"

    menu p19_menu:
        computer "Sim, a estrutura de dados onde o armazenamento do contexto dos
        processos é feito."

        "Ah, é simples, é como se fosse um diário guardado dentro da bolsa, e cada entrada é um processo que aconteceu e terminou.":
            jorge "Mas eu não carrego um diário, e nem li de um diário."
            player "Sim, mas se você guardasse essas coisas no diário faria sentido não?"
            jorge "Como? Ainda não entendi tabela de processos."
            player "O diário é a tabela de processos, você veio para cá por causa de um processo."
            player "O processo anterior é como o dia anterior de um diário, e o processo atual é como o dia atual."
            jorge "Mas isso presume que o dia anterior acabou não?"
            computer "Exatamente, o que seria incorreto para uma tabela de processos, a não ser que o processo tenha acabado mesmo."
            player "Ah, errei espera..."
            jump p19_menu

        "Ah, é simples, é como se fosse um bloco de notas dentro da bolsa, que possui várias anotações de tarefas.":
            jorge "Mas eu não carrego um bloco de notas, e nem li um bloco de notas."
            player "Sim, mas se você anotasse essas coisas no bloco de notas faria sentido não?"
            jorge "Como? Ainda não entendi tabela de processos."
            player "O bloco de notas é a tabela de processos, você veio aqui por causa de um processo."
            player "Os processos são como tarefas no bloco de notas, e você vai dedicando um pouco de tempo para cada."
            player "Marcando por exemplo o quanto falta para completar aquela tarefa."
            player "E você ainda tem a tarefa anterior e a tarefa atual, representando o processo anterior e o processo atual."
            jorge "Então, eu posso marcar que tenho um novo processo na minha tabela?"
            player "Que?"
            "Você não entende por um breve momento."
            jorge "Eu só tentei me integrar nos conhecimentos de vocês, eu quis dizer adicionar encontrar minha namorada."
            jorge "Porque essa é a minha atual tarefa."
            player "Por enquanto não! Sua tarefa agora é sobreviver."
            "Você diz, dando breves tapinhas nas costas de Jorge."
            player "Inclusive, vai ser mais caminhada que isso?"
            "Você diz, sabendo que o sol já estava forte no céu."
            jorge "Não acho que esteja muito longe, quando encontrarmos uma placa."
            jorge "Falta só chegar na intercessão e pegamos para a direita para chegar, e ai mais uns 20 minutos de caminhada."
            jump p19_end
        
        "Ah, é muito complexo, nem eu entendo, afinal essas coisas estão guardadas na mente então não sei se daria para relacionar...":
            jorge "Caramba, é tão complexo assim?"
            player "Bem, eu acho..."
            computer "Mas não precisa ser um exemplo que está acontecendo agora."
            player "Realmente, eu posso pensar inclusive em obter as coisas que eu falar."
            jorge "Tipo?"
            player "Eu estava precisando de um bloco de notas ou um diário pra anotar as coisas que eu preciso fazer."
            jorge "Bem um diário armazena o seu dia, e um bloco de notas o que você precisa fazer..."
            player "É realmente, acho que eu consigo pensar em uma resposta."
            jump p19_menu

label p19_end:
    return
