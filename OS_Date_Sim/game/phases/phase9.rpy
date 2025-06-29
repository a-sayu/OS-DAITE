# Fase 9

## Qual a relação entre Memória RAM, Sistema Operacional e Programas de Usuário?

label phase_9:

    "Quando termina de se perguntar sobre a relação de processos, é possível observar que o número na tela do computador estava concluído."

    computer "Completo! [playerName], você encontrou o tablet?"

    player "Ah sim, aqui."

    "Você diz, conectando o tablet ao computador."

    "Olhando para o número se movendo lentamente, você se pergunta quanto tempo levaria."

    scene bg-computerRoom-night-on

    "A resposta veio depois de algumas horas, ao fim da tarde, ou o começo da noite."

    player "Bem, não posso desperdiçar o dia agora né?"

    "A chuva que parava próximo as 19h parecia diminuir agora, e você começa a se preparar para sair."

    scene bg-computerRoom-night-off

    player "Vamos [computerName]?"

    $ computerImage = "tablet.png"

    computer "Claro!"

    "A interface e o sistema podia ser diferente, mas a presença dele traz um pouco de tranquilidade com a longa viagem que você vai ter."

    "Coloca-o na mochila, o que te incomoda um pouco, já que ele não iria realmente poder estar contigo constantemente."

    "Saindo do local, você tranca a porta, colocando o molho de chaves no bolso da calça."
    
    scene bg-desolatedCity

    player "Primeiro, passar no mercado, pegar comida."

    player "Depois descansar."

    player "E por fim, é hora de partir para a capital."

    "Você caminha pelas ruas iluminadas pelo luar e em pouco tempo estava diante de um supermercado com as portas abertas."

    scene bg-supermarketFront

    "O interior estava visivelmente destruído."

    "Entrando no local, você tira sua bolsa para retirar uma lanterna e pega uma cestinha largada, colocando a bolsa nas costas de volta."

    "Até estar em um local com um cheiro um tanto putrido."

    "Cobrindo suas narinas, você olha para a seção ao lado, de comidas com uma data de válidade longa."

    scene bg-supermarketFoodSection

    "Colocando elas na cesta: bolacha, sopas prontas, macarrão e aproveita para pegar um conjunto de talheres para cozinhar e comer."

    "Saindo do local até uma seção com roupas e sapatos, você se senta, observando suas compras."

    scene bg-supermarketClothSection

    thoughts 'Se eu colocar na minha mochila, vai ficar cada vez mais dificil de tirar as coisas dela...'

    "Você retira o tablet da bolsa, e o desbloqueia."

    computer "Olá [playerName]! Com que posso ajudar? Estava bem solitário dentro da sua mochila..."

    player "Oi, é só que, eu to sem ideias agora, se eu continuar pegando coisas vai ficar mais dificil de conversar com você..."

    player "Ou pegar algum lanchinho ou equipamento..."

    computer "Por que não pega uma memória RAM para o seu armazenamento?"

    player "Memória RAM? Esqueceu que isso é termo de computador?"

    "O tablet faz um som como se fosse de conquista."

    "Você sorri, observando o tablet aparecer em carregamento, como se pensasse, uma animação de roda acontecia."

    player "Espera, a tradução de RAM é memória de acesso aleatório."
    
    menu p9_menu:

        computer "E você precisa de um armazenamento de acesso aleatório, similar à uma memória de acesso aleatório!"

        "E se eu deixar sempre os itens mais usados no topo da mochila? Tipo a lanterna, os lanches... daí o acesso fica mais rápido!": # fdp
            computer "Melhor que nada, mas isso ainda não transforma sua mochila em uma memória de acesso rápido... só reorganiza o atraso."
            player "Realmente, além de que eu provavelmente teria que reorganizar várias vezes e isso iria atrasar mais ainda."
            computer "Mais do que o tempo de retirar da mochila."
            jump p9_menu

        "Se for assim, minha mochila é uma memória secundária, e eu deveria ter uma primária para armazenar você, [computerName] o sistema operacional de decisões e os programas como a lanterna e lanchinhos rápidos.": # vdd
            computer "Nem precisei te ajudar."
            jump p9_end

        "Ah! Já sei! Posso fazer uma lista de tudo que está na mochila. Aí, mesmo se estiver bagunçada, eu sei o que pegar.": # fdp
            computer "A lista ajuda, mas não acelera o acesso... é como ter um índice sem memória — ainda leva tempo para encontrar as coisas."
            "Além de ainda vai levar o mesmo tempo pra tirar coisas da mochila."
            jump p9_menu

label p9_end:
    return