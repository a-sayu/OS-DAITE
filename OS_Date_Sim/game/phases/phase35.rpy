label phase_35:
    
    scene bg-whiteScreen

    "Oi!"

    "Se você está vendo esta tela, é porque o jogo ainda não foi terminado..."

    "Nos desculpem pelo inconveniente!"
    
    jump p35_end

label p35_end:
    $ MainMenu(confirm=False)()
