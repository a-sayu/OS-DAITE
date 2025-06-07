# Fase 12

## Partições de Tamanho Fixo, Partições de Tamanho Variável. Fragmentação Interna e Fragmentação Externa

label phase_12:

    computer "Agora... Qual tipo de bolsa você vai pegar?"

    player "A mais simples? Não tem porquê pensar muito sobre isso, não?"

    computer "Precisa sim!"

    computer "Por exemplo, a bolsa que eu te mostrei com compartimentos"

    computer "Ela pode ter partições de tamanhos fixos"

    "Uma bolsa com três compartimentos aparece na tela do tablet."

    computer "Ela pode ter partições de tamanho variável"

    "Uma bolsa com três compartimentos deslocáveis aparece na tela do tablet."

    computer "Qual você escolhe? Se quiser posso trazer os prós e os contras"

    player "Hmm, mas realmente é importante?"

    computer "Claro! Programas, no caso itens, possuem tamanhos diferentes"

    computer "Se for fixo, você vai ter fragmentação interna, se for variável você vai ter fragmentação externa"

    player "Ta, você novamente está falando muitos termos de computação"

    menu p12_menu_1:

        player "Com fragmentação interna você está querendo dizer que..."

        "Vai sobrar espaço dentro de cada compartimento da bolsa, um espaço desperdiçado.": # vdd
            computer "Exatamente!"
            player "Bem isso é ruim, particionamentos fixos não são o ideal"
            player "Iria sobrar muito espaço a não ser que eu queira manter tudo uma bagunça, o que não é ideal..."
            jump p12_menu_2


        "Vai ficar espaço entre cada compartimento que não vai caber outros programas.":
            computer "Essa é a descrição de uma fragmentação externa"
            player "Verdade, esse é o problema da partição variável..."
            player "Mas nesse caso é fácil de lidar, o meu funcionamento pode ser similar a de um sistema operacional"
            player "Mas diferente dele eu posso mudar a posição das partições quando eu quiser"
            jump p12_menu_1

    menu p12_menu_2:

        player "Então o ideal vai ser..."
        
        "Bolsa com compartimentos fixos":
            computer "Não foi esse que você falou que não daria certo"
            player "Verdade, foi mal"
            jump p12_menu_2

        "Bolsa com compartimentos variáveis": # vdd
            computer "Agora podemos ir buscar a bolsa"
            jump p12_end

label p12_end:
    return