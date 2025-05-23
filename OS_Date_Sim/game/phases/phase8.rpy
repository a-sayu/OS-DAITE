# Fase 8

## Tema: A relação do so, programas do usuário e os processos

label phase_8:

    "Você então pega o tablet e o observa, também coletando o carregador do tablet."

    "Você então se senta na cadeira novamente e apoia sobre a mesa, admirando o tablet que arduamente tinha conseguido."

    player "Por quê? Por que tanta segurança pra algo tão simples?"

    "Você olha para o computador, que marcava pouco mais de 95\%."

    thoughts 'Qual a relação entre tudo que eu fiz com a necessidade de tantas etapas?'

    "Refletindo, você pensa em cada passo que você concluiu para recuperar o tablet."

    thoughts 'Primeiro o caderno, depois onde estava sendo armazenado o tablet.'

    thoughts 'Depois encontrar a senha...'

    menu p8_menu:

        thoughts 'Espera, a senha era sobre sistemas operacionais, sobre processos, talvez o que eu fiz tenha a ver com isso pois...'

        "Em um sistema operacional, assim como esse escritório, ele contém informações necessárias para que um programa, no caso abrir um cofre sejam executados com sucesso.":
            player "E isso é um processo"
            player "Porque um processo é um programa e o conjunto de informações necessárias para que ele seja executado"
            player "To ficando craque em Sistemas Operacionais ein..."
            jump p8_end

        "Em um sistema operacional, cada programa é como uma pista, só quando se tem todas se abre o cofre, no caso o processo se inicia.":
            player "Não... Não é bem isso"
            player "As pistas são informações necessárias para o programa"
            player "Mas elas não são o programa, elas apenas fazer parte do processo"
            player "Portanto, o processo já havia começado quando as pistas foram encontradas"
            jump p8_menu
        "Em um sistema operacional, um processo é um conjunto de instruções, e para abrir esse cofre foi seguido um conjunto de intruções.":
            player "Não... Não é bem isso"
            player "Um conjunto de instruções pode ser a definição de programa"
            player "Mas não de processo"
            player "Apesar de necessárias para o real programa que era abrir o cofre"
            player "Algumas informações não fazem parte do programa, mas sim do sistema operacional"
            jump p8_menu

label p8_end:
    return