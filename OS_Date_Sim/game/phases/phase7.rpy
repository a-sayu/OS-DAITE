## Tema: O que é um processo

label phase_7:

    player "Mas você então não iria comigo, outra versão sua iria..."

    computer "Se você sincronizar meus dados com o tablet, eu irei contigo!"

    player "Okay, mas onde eu vou encontrar um tablet aqui"

    computer "Eu não tenho certeza da localidade, mas estamos nas proximidades de um escritório da DAITE"

    player "Sim, acredito que estamos nesse escritório..."

    "Você diz, colocando a mão sobre a face, incrédulo que essa informação não era óbvia."

    computer "Eu enviei um sinal para cá, tem um sinal que respondeu por aqui!"

    player "Não pode ter sido você mesmo?"

    computer "Eu considerei isso antes de repassar a informação [player] bobinho"

    "A máquina exibia uma animação de risada."

    player "Complicado, ainda assim, não da para saber os específicos né?"

    computer "Talvez quem trabalhava nesse escritório pode ter deixado pistas de onde está?"

    player "Provável"

    computer "Vou deixar contigo a busca enquanto faço uma limpeza para o novo dispositivo."

    "[computer] diz, e parece estar tentando fazer um backup de todos os dados e programas relevantes."

    #TODO: Troca de cena para a planta-baixa do escritório.

    menu blueprint_1:

        player "Olhando bem, esse lugar é bem empoirado né?"

        "Janela":

            "Você vai até a janela."
            #TODO: Troca a cena para uma visão melhor do cenário através da janela
            player "Ah ali fica a minha universidade"
            "Você toca o vidro da janela posicionando seu indicador sobre uma área verde."
            player "É uma bela vista..."
            player "Era... Antes do apocalipse..."
            "Você divaga um pouco, mas volta ao foco da busca."
            jump blueprint_1
            
        "Armário":

            label search_closet:

            "Você vai até o grande armário verde no canto da parede da janela."
            #TODO: Troca a cena para uma visão melhor do armário
            player "Deve ter algo aqui, provavelmente deve estar aqui"

            menu try_open_closet:
                
                "Você tenta abrir as portas, sem sucesso, parecem emperradas."

                "Tentar de Novo?":

                    "Você força um pouco, e consegue abrir porta por porta."
                    player "Aqui tem Documentos"
                    player "Mais Documentos..."
                    player "Caramba... Só Documentos?"
                    player "Uh, um cofre?"
                    $ seen_safe = True
                    "Você vê que tem um bilhete no cofre: Abrir um cofre é um processo, não?"
                    player "Imagino que sim?"
                    "Você pensa um pouco, mas agora com a intenção de abrir o cofre."
                    
                    if have_notebook:
                        jump try_open_safe
                    else:
                        jump blueprint_1

                "Deixar para lá.":
                    "Você pensa um pouco, mas volta ao foco da busca."
                    jump blueprint_1

        "Mesa de Escritório":

            label computer_desk:

            #TODO: Troca para uma visão direta da mesa com o computador.
            "Você fica de frente ao computador novamente, observando sua mochila e o amontoado de diversos documentos que você já deu uma olhada antes."
            computer "Achou?"
            
            if seen_safe:
                player "Talvez"
                computer "Ainda falta muito pra compactar todos os arquivos infelizmente"
            else:
                player "Não ainda..."
            
            computer "Bem, boa sorte, pode levar seu tempo"
            
            menu search_desk:
                thoughts "Será que vai ter algo sobre o tablet aqui, não lembro de ter visto grande coisa..."
                    
                "Procurar nos documentos da mesa.":
                    
                    #TODO: Troca para a cena aproximando dos documentos sobre a mesa.
                    "Você vasculha os arquivos, mas nada muito relevante sobre o tablet."
                    thoughts "Hmm... Nada..."
                    jump search_desk

                "Olhar debaixo da mesa.":
                    #TODO: Troca para a cena aproximando dos documentos abaixo da mesa.
                    "Você nota um cadeninho vermelho que parece ter caído dentro de uma caixa de mais documentos."
                    player "Não seria isso né?"
                    "Pegando o caderninho, você lê várias linhas com dados, parecem senhas e charadas sobre cada senha em cada página."
                    player "Pelo menos cada senha é diferente..."

                    $ have_notebook = True
                    
                    if seen_safe:
                        thoughts "Provavelmente a senha do cofre está aqui"
                    else:
                        thoughts "Talvez o tablet esteja bloqueado? De qualquer forma pode ser útil"
                    "Você se levanta com o caderninho vermelho."
                    jump found_notebook

        "Mesas Velhas Empilhadas":
            
            "Você se vira para o fundo dessa sala de escritório, onde várias mesas estavam empilhadas."
            thoughts "Não parece ter nada por aqui além de poeira."
            "Você se senta um pouco sobre o sofá que tinha ido dormir na primeira noite aqui."
            thoughts "Faz alguns dias que eu estou aqui já..."
            "A dureza do sofá te incomoda como sempre, e você se levanta."
            jump blueprint_1

    label found_notebook:

        "Com o caderninho em mãos, resta apenas o tablet."

        if seen_safe:
            thoughts "Parece até que eu tenho os dados de entrada do cofre agora."

        menu blueprint_2:
            "Encontrar esse tablet está sendo trabalhoso, que nem encontrar as minhas chaves quando eu saía de casa..."

            "Janela":
            
                "Você vai até a janela."
                # TODO: Troca a cena para uma visão melhor do cenário através da janela
                player "Eu gostava daquela sorveteria"
                "Você toca o vidro da janela posicionando seu indicador sobre um loja azul mais ao centro da cidade perto de uma praça."
                player "Realmente, é uma bela vista..."
                player "Mesmo depois do apocalipse..."
                "Você divaga um pouco, mas volta ao foco da busca."
                jump blueprint_2

            "Armário":

                "Você vai até o grande armário verde no canto da parede da janela."
            
                # TODO: Troca a cena para uma visão melhor do armário
            
                if not seen_safe:
                    jump search_closet
            
                label try_open_safe:
                
                    # TODO: Troca para cena do cofre.
                    thoughts "O tablet deve estar nesse cofre, ou ele pode ser totalmente não relacionado..."
                    thoughts "O primeiro é mais provável"
                    "Você abre o caderninho vermelho, e folheia ele, procurando a charada que combinava com o questionamento do bilhete."
    
                    label password_input:

                        if wrong_input == 1:
                            thoughts "Não funcionou?"
                            thoughts "Será que a senha tem algo haver com os caracteres estrnhos nas anotações?"
                            
                        elif wrong_input >= 2:
                            thoughts "Não funcionou de novo?!?!"
                            thoughts "Será que eu digitei algo errado?"
                            thoughts "0-4-0-$-3-4-3-0-7-1"

                    menu open_safe:
    
                        thoughts "Abrir um cofre é um processo... Abrir um cofre é um processo... Abrir um cofre é um processo... Qual a frase que melhor combina?"

                        "Programas são um conjunto de instruções, se a instrução é um loop 'n0v0 numer0' uma hora o programa vai resultar em '&4B3RT0!'":
                            player "Talvez?"
                            thoughts "Não... Processos são mais que programas, eles incluem dados de entrada e os estados do processo..."
                            jump open_safe

                        "Processos são os dados de entrada, que precisam ser inseridos no programa do cofre, enquanto você lê o caderno, o programa espera em um estado 'Bl0que4d0', e quando você insere a '$3NH4' ele sai do estado bloqueado e entra em '3xecuçã0' ficando 'p7onto' abrindo e 'conclu1ndo' o processo.":
                            "Aparece um texto escrito: Esperando..."

                            $ password = renpy.input(prompt="Digite a senha: ", length=10);
                            if not (password == "040$343071"):
                                $ wrong_input = wrong_input + 1
                                jump open_safe
                        
                            "Quando inserido troca para: Reconhecendo..."
                            "Ao aceitar troca para: Pronto!"
                            "Abrindo em seguida, mostrando o conteúdo do cofre sendo o tablet"
                            player "Boa!"
                            $ password = ""
                            $ wrong_input = 0
                            jump p7_end

                        "Faz cerca de 'd01$' dias que estou tendo que lidar com um processo jurídico, a empresa parece ter vendido algum dado na '1nt&7n3t' e eu sou o bode espiatório.":
                        
                            player "Não é isso... Isso nem haver com cofre tem..."
                            thoughts "Além de que estamos falando de um processo do sistema operacional..."
                            jump open_safe

            "Mesas Velhas Empilhadas":

                "Você se vira para o fundo dessa sala de escritório, onde várias mesas estavam empilhadas."
                thoughts "É... Só há poeira"
                "Você se senta sobre o sofá e sente a dureza dele."
                "A dureza do sofá te incomoda como sempre, e você se levanta."
                jump blueprint_2

label p7_end:
    return