# Fase 10

## Qual a importância de armazenar o sistema operacional na memória RAM

label phase_10:


    "Na tela de [computerName] aparece um símbolo de carregamento."

    player "Você está pensando? Pensando em quê?"

    computer "Pensando em por que você precisaria me colocar em uma memória primária"


    menu p10_menu:

        computer "Mesmo que seja mais rápido, você estaria carregando mais peso, e seria mais prático só ter uma única mochila"
    
        "Sim, mas conveniência, sei lá?":
            computer "Se for só por isso, não é melhor manter o que estava antes?"
            player "Mas, demoraria para buscar"
            computer "Então explique melhor como isso importa"
            jump p10_menu

        "Sim, demora mais para acessar a mochila, mas minha busca é mais rápida se estiver ao alcance das minhas mãos":
            computer "Realmente, a busca é uma operação principal"
            player "Se ela for lenta, como que eu poderia responder imediatamente?"
            computer "Agora só falta qual vai ser a sua memória primária, então"
            jump p10_end

label p10_end:
    return