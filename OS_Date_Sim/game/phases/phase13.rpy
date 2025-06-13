# Fase 13

## Quando a memória RAM deve ser particionada?

label phase_13:

    "Por alguns minutos era buscado a bolsa, deixando o tablet sobre o banco que antes estava."

    thoughts 'Não é como se fosse roubar ele nessas ruas vazias'

    "Encontrando uma bolsa parecida com o conceito que o tablet havia mostrado."

    "Você chega até ele mostrando a bolsa."

    player "Achei! Aqui olha, exatamente igual."

    computer "Que bom!"

    player "Eu decido como vai ser o tamanho de toda as partições agora?"

    computer "Não, isso é algo que um particionamento fixo faria."

    menu p13_menu:
        "Sim, mas seria durante as atividades do Sistema Operacional para mim."

        "Ou seja, quando eu tiver os itens em mãos e eu precisar guardá-los.": # vdd
            computer "Exatamente, conforme você tem programas a sua disposição."
            computer "Você adiciona partições para cada programa."
            jump p13_end

        "Ou seja, Agora. Eu só preciso tirar os itens da mochila agora, e começar a particionar já planejando o que vem.":
            computer "Não... Isso é particionamento fixo."
            computer "Agora seria o início das atividades do sistema operacional."
            player "Ah, sim, eu basicamente acabei de iniciar o processo de gerência da memória."
            jump p13_menu


        "Não entendi...":
            computer "Recapitulando, se os itens forem como programas."
            computer "A bolsa a memória RAM, cada compartimento uma partição variável."
            computer "Colocar os programas na memória RAM é como colocar itens na bolsa separados por compartimento, certo?"
            computer "Mas para isso você tem que ter os compartimentos montados."
            computer "Você tem que fazer isso em algum momento, quando?"
            player "Ah faz sentido."
            jump p13_menu

label p13_end:
    return