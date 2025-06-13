label phase_35:
    
    scene bg-cloudy

    "Oi!"

    "Se você está vendo esta tela, é porque o jogo ainda não foi terminado... Ou você perdeu..."

    "Nos desculpem pelo inconveniente!"

    "Total de fases jogáveis: 20 de 34 fases. Ultima questão feita: 29."
    
    jump p35_end

label p35_end:
    $ renpy.call_in_new_context("_main_menu")
