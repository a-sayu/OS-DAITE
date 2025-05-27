# Fase 11

## Como organizar o armazenamento na memória RAM?

label phase_11:

    player "É... Aqui começa a complicar. Bem, vamos aproveitar que a gente está na seção de moda da loja."

    computer "Bem, analisando o ambiente..."

    "O tablet fica por alguns segundos carregando."

    computer "Posso te ajudar, mas você precisa me dizer: como pretende organizar tudo?"

    player "Não cheguei a pensar tão longe... Então..."

    computer "Que tal eu dou ideias de armazenamentos e você diz o que acha?"

    menu p11_menu:

        "Na tela do tablet aparecem três imagens com opções de armazenamento:"

        "Bolsos da roupa, similar ao cache, perto do processador.":
            computer "É uma escolha simples, não iria ser necessário ficar procurando, e vai estar tudo facilmente equipado"
            player "Mas não daria para armazenar muita coisa..."
            computer "Acho que é melhor outra ideia então."
            jump p11_menu

        "Bolsas com compartimentos, similar à uma RAM com particionamento":
            computer "Bem, isso é organizado, com compartimentos você vai poder separar cada necessidade"
            player "Bem, esse era o plano inicial mesmo, além de ficar mais fácil de acessar"
            computer "Então está decidido!"
            jump p11_end

        "Mochila, manter na memória secundária.":
            computer "No fim, você desistiu então?"
            player "Como assim?"
            computer "Bem, só voltamos ao começo... E não resolve muita coisa"
            player "É, se for manter assim, eu ainda vou gastar muito tempo com a mochila"
            computer "Acho que é melhor outra ideia então."
            jump p11_menu

label p11_end:
    return