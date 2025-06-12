
label phase_5:

    player "Okay, então como eu deveria escalonar me alimentar, me proteger
    e procurar por minha irmã?"

    player "Tipo, eu posso comer enquanto procuro minha irmã e fico atento
    para qualquer perigo a minha volta..."

    computer "Bem, você não precisa estar fazendo tudo ao mesmo tempo, isso
    não é escalonar!"

    computer "Devemos pensar sobre isso com muito cuidado."

    player "Realmente... Já que estamos pensando em conceitos de Sistemas
    Operacionais, que tal relacionar essas coisas como programas?"

    while not (correct[0] and correct[1] and correct[2]):
        label p5_1:
            if not correct[0]:
                jump p5_1_menu
        label p5_2:
            if not correct[1]:
                jump p5_2_menu
        label p5_3:
            if not correct[2]:
                jump p5_3_menu
        
        label p5_verification:
            if not correct[0]:
                computer "Comida é importante, mas não se deve ficar comendo também não é tão bom..."
            if not correct[1]:
                computer "Segurança é importante, mas não se deve viver paranóico..."
            if not correct[2]:
                computer "Buscar sua irmã é importante, mas não se deve ignorar suas necessidades..."
    
    computer "Exatamente, uma divisão de tempo para cada ação é importante, não
    foque demais em algo e agende seus programas, isso é escalonar os programas!"
    jump p5_end

    menu p5_1_menu:
        computer "Então... Quando você precisa se alimentar?"

        "Eu posso comer quando eu puder, não é tão necessário...": #FDP
            $ correct[0] = False
            jump p5_2

        "Eu tenho que separar pelo menos algum tempo para encontrar mais alimentos e comer.": #VDD
            $ correct[0] = True
            jump p5_2 

    menu p5_2_menu:
        computer "Então... Quando você precisa se proteger?"

        "Está muito perigoso, eu deveria colocar toda minha atenção para isso...": #FDP
            $ correct[1] = False
            jump p5_3

        "É importante estar atento... Mas descansar também, eu posso sempre procurar abrigos": #VDD
            $ correct[1] = True
            jump p5_3

    menu p5_3_menu:
        computer "Então... Quando você precisa buscar sua irmã?"

        "Eu deveria focar nessa busca totalmente... Se eu demorar como vou ter certeza que ela estará a salvo...":
            $ correct[2] = False
            jump p5_verification

        "Mesmo que eu não saiba onde minha irmã está, eu também não posso deixar de me cuidar...":
            $ correct[2] = True
            jump p5_verification

label p5_end:
    return