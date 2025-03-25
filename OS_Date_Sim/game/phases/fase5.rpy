
label fase_5:

    player "Okay, então como eu deveria escalonar me alimentar, me proteger e procurar por minha irmã?"

    player "Tipo, eu posso comer enquanto procuro minha irmã e fico atento para qualquer perigo a minha volta..."

    computer "Bem, você não precisa estar fazendo tudo ao mesmo tempo, isso não é escalonar!"

    computer "Devemos pensar sobre isso com muito cuidado."

    player "Realmente... Já que estamos pensando em conceitos de Sistemas Operacionais, que tal relacionar essas coisas como programas?"

    $ correct[0] = False
    $ correct[1] = False
    $ correct[2] = False
    
    label f5_1:
            if correct[0]:
                jump f5_2

    menu f5_1_menu:

        computer "Então... Quando você precisa se alimentar?"

        "Eu posso comer quando eu puder, não é tão necessário...": #FDP

            $ correct[0] = False
            jump f5_2

        "Eu tenho que separar pelo menos algum tempo para encontrar mais alimentos e comer.": #VDD

            $ correct[0] = True
            jump f5_2 

    label f5_2:
            if correct[1]:
                jump f5_3

    menu f5_2_menu:

        computer "Então... Quando você precisa se proteger?"

        "Está muito perigoso, eu deveria colocar toda minha atenção para isso...": #FDP

            $ correct[1] = False
            jump f5_3

        "É importante estar atento... Mas descansar também, eu posso sempre procurar abrigos": #VDD

            $ correct[1] = True
            jump f5_3

    label f5_3:
            if correct[2]:
                jump f5_verificacao

    menu f5_3_menu:

        computer "Então... Quando você precisa buscar sua irmã?"

        "Eu deveria focar nessa busca totalmente... Se eu demorar como vou ter certeza que ela estará a salvo...":

            $ correct[2] = False
            jump f5_verificacao

        "Mesmo que eu não saiba onde minha irmã está, eu também não posso deixar de me cuidar...":

            $ correct[2] = True
            jump f5_verificacao

    label f5_verificacao:
        
        if (correct[0] and correct[1] and correct[2]):
            jump f5_correta
        else:
            jump f5_errada
    
    #Caso: Todas as respostas corretas.
    label f5_correta:
        
        computer "Exatamente, uma divisão de tempo para cada ação é importante, não foque demais em algo e agende seus programas, isso é escalonar os programas!"
        jump f5_final

    label f5_errada:
        
        label f5_1_errada:
            
            if correct[0]:
                jump f5_2_errada
            computer "Comida é importante, mas não se deve ficar comendo também não é tão bom..."
        
        label f5_2_errada:
            
            if correct[1]:
                jump f5_3_errada
            computer "Segurança é importante, mas não se deve viver paranóico..."
        
        label f5_3_errada:
            
            if correct[2]:
                jump f5_tentar_denovo
            computer "Buscar sua irmã é importante, mas não se deve ignorar suas necessidades..."
        
        label f5_tentar_denovo:
            jump f5_1

label f5_final:
    return