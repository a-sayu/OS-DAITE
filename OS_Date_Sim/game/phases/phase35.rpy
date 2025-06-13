label phase_35:
    
    scene bg-whiteScreen

    "Oi!"

    "Se você está vendo esta tela, é porque o jogo ainda não foi terminado..."

    "Nos desculpem pelo inconveniente!"

    "Total de fases jogáveis: 19 de 34 fases. Ultima questão feita: 28."
    
    jump p35_end

label p35_end:
    $ renpy.call_in_new_context("_main_menu")
