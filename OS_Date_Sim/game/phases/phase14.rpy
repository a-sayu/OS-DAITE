# Fase 14

## Quem o sistema também particiona e como ele particiona?

label phase_14:

    computer "Como a gente tem tempo, quer particionar a mochila também?"

    player "Como assim? Achei que só a RAM fosse particionada assim..."

    computer "Claro que não."

    menu p14_menu:
        computer "A mochila também deve ficar organizada."

        "Ah, sim, no SO o núcleo organiza em setor.":            
            computer "Não exatamente, não podemos confundir setor com bloco."
            computer "Setor é um termo mais de hardware, e é o menor tamanho de uma unidade de armazenamento."
            player "Ah... minha mochila tem espaços grandes demais pra serem chamados de setores, né?"
            jump p14_menu

        "Ah, sim, no SO o núcleo organiza em blocos.": # vdd
            player "Cada compartimento e separação são blocos, certo?"
            computer "Isso, pois facilitam a transferência de dados entre o sistema operacional e a memória secundária."
            player "E blocos são vários setores, seria como se cada setor fosse uma parte do compartimento."
            player "Todos do mesmo tamanho e que juntos formam o compartimento."
            "Enquanto vocês conversavam sobre esses assuntos, você termina de arrumar sua mochila."
            jump p14_end

label p14_end:
    return