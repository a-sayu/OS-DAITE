label fase_3:

    "Enquanto a chuva caia, você se acomoda na cadeira, ficando em silêncio ouvindo apenas a forte chuva cair, restando a você quebrar o silêncio."

    player "[computerName]... Você é um computador de auxílio certo? Eu preciso de ajuda, um guia e tals"

    computer "Qual seria o problema [playerName]?"

    player "Eu estou aqui nesse prédio, mas eu moro meio longe daqui, minha irmã(o) foi levado pelo ônibus da escola quando tudo isso começou, e eu preciso de um ponto de começo"

    computer "Ponto de começo?"

    #endereco memoria menu
    menu f3_menu:
        player "Sim tipo..."

        "Quando seu sistema operacional é carregado da memória secundária e você tem que colocar o endereço da primeira instrução do seu Escalonador de Processos no Contador de Instruções e no registrador do Escalonador de Processos.":
            
            computer """Entendo, então significa que você precisa do primeiro passo essencial para encontrar sua irmã(o)
            
                Você pode tentar primeiramente checar as possíveis rotas que eles podem ter pego, para planejar em volta disso, apesar das bases defeituosas de conhecimento humano, sou ótimo com cálculos e previsões"""
        
            jump f3_final

        "Eu não sei se consigo te explicar isso, sabe a primeira coisa, que antecede tudo...":
            computer "Como isso se relaciona? Eu também não sei dizer sobre o que é a primeira coisa, que antecede tudo"

            player "Huh... Você tem uma base bem defeituosa de conhecimento..."
            
            "Para tentar respondê-lo melhor você vasculha as pilhas de papel que pareciam estar estranhamente muito relacionadas com um estudo de sistemas operacionais."

            jump f3_menu

        "É tipo o oposto do fim!":
            computer "Interessante! Mas não acho que é uma resposta que explique o que é um ponto de começo!"
            
            player "Okay, fazer piada não vai ajudar... " 
            
            "Você vasculha as pilhas de papel que pareciam estar estranhamente muito relacionadas com um estudo de sistemas operacionais."

            jump f3_menu

label f3_final:
    return
