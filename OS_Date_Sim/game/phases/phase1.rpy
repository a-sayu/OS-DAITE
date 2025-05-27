label phase_1:
    
    scene bg-computerRoom-night-off

    "Você chega em um escritório, com mesas empilhadas ao fundo, e uma mesa 
    próxima a janela com um computador desligado, onde você já estava a mais de uma 
    semana."

    "Colocando sua mochila sobre a mesa, você se senta em frente ao computador, para 
    afastar a fome, você começa a pensar sobre esse computador."

    player "Eu deveria tentar ligar esse computador, apesar de o mundo ter acabado, a 
    energia e a internet ainda não acabou..."

    scene bg-computerRoom-night-on

    "Apertando o botão de ligar o computador, você apoia sua mão na mesa, vendo as leds 
    ligarem, e ficar na tela de carregamento."

    player "D.AI.TE... é o sistema operacional desse computador velho?"

    menu p1_menu:
        player "Hmm... Se eu fosse um computador, meu sistema operacional ficaria..."

        "Na minha memória de longo prazo!":
            player "É... Um computador tem um disco rígido certo? Onde o sistema 
            operacional fica guardado mesmo quando desligado, é que nem quando eu estou 
            dormindo..."

            "Você boceja, o cansaço de vasculhar por comida na área parecia que já estava te 
            atingindo, você come uma barra de cereal, e vai se deitar no sofá, cobrindo-se com um 
            fino lençol."
            
            jump p1_end

        "No meu... Estômago?":
            player "Parece que eu estou com muita fome, haha, achando a resposta talvez eu 
            me distraia da fome..."

            jump p1_menu

        "Eu não sei dizer...":
            player "Bem, se eu não sei, eu tenho que estudar..."

            "Você vasculha as pilhas de papel que pareciam estar estranhamente muito 
            relacionadas com um estudo de sistemas operacionais."

            jump p1_menu

label p1_end:
    return
