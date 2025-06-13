# Fase 7

## Tema: O que é um processo

"Mas você então não iria comigo, outra versão sua iria..."

computer "Se você sincronizar meus dados com o tablet, eu irei contigo!"

"Okay, mas onde eu vou encontrar um tablet aqui."

computer "Eu não tenho certeza da localidade, mas estamos nas proximidades de um escritório da DAITE."

"Sim, acredito que estamos nesse escritório..."

Você diz, colocando a mão sobre a face, incrédulo que essa informação não era óbvia.

computer "Eu enviei um sinal para cá, tem um sinal que respondeu por aqui!"

"Não pode ter sido você mesmo?"

computer "Eu considerei isso antes de repassar a informação {player} bobinho."

A máquina exibia uma animação de risada.

"Complicado, ainda assim, não da para saber os específicos né?"

computer "Talvez quem trabalhava nesse escritório pode ter deixado pistas de onde está?"

"Provável."

computer "Vou deixar contigo a busca enquanto faço uma limpeza para o novo dispositivo."

{computer} diz, e parece estar tentando fazer um backup de todos os dados e programas relevantes.

// Troca de cena para a planta-baixa do escritório.

"Olhando bem, esse lugar é bem empoirado né?"

1 - Janela
2 - Armário
3 - Mesa de Escritório
4 - Mesas Velhas Empilhadas

Caso 1:
    Você vai até a janela.
    // Troca a cena para uma visão melhor do cenário através da janela
    "Ah ali fica a minha universidade."
    Você toca o vidro da janela posicionando seu indicador sobre uma área verde.
    "É uma bela vista..."
    "Era... Antes do apocalipse..."
    Você divaga um pouco, mas volta ao foco da busca.
    // Volta na troca de cena para a planta-baixa.
Caso 2:
    Você vai até o grande armário verde no canto da parede da janela.
    // Troca a cena para uma visão melhor do armário
    "Deve ter algo aqui, provavelmente deve estar aqui."
    Você tenta abrir as portas, sem sucesso, parecem emperradas.
    1 - Tentar de Novo?
    2 - Deixar para lá.
    Caso 1:
        Você força um pouco, e consegue abrir porta por porta.
        "Aqui tem Documentos."
        "Mais Documentos..."
        "Caramba... Só Documentos?"
        "Uh, um cofre?"
        Você vê que tem um bilhete no cofre: Abrir um cofre é um processo, não?
        "Imagino que sim?"
        Você pensa um pouco, mas agora com a intenção de abrir o cofre.
        // Volta na troca de cena para a planta-baixa.
    Caso 2:
        Você pensa um pouco, mas volta ao foco da busca.
        // Volta na troca de cena para a planta-baixa.
Caso 3:
    // Troca para uma visão direta da mesa com o computador.
    Você fica de frente ao computador novamente, observando sua mochila e o amontoado de diversos documentos que você já deu uma olhada antes.
    computer "Achou?"
    // caso tenha visto o cofre:
    // "Talvez"
    // computer "Ainda falta muito pra compactar todos os arquivos infelizmente."
    // caso não tenha visto o cofre:
    //"Não ainda..."
    computer "Bem, boa sorte, pode levar seu tempo."
    pensamento "Será que vai ter algo sobre o tablet aqui, não lembro de ter visto grande coisa..."
    1 - Procurar nos documentos da mesa.
    2 - Olhar debaixo da mesa.
        Caso 1:
        // Troca para a cena aproximando dos documentos sobre a mesa.
        Você vasculha os arquivos, mas nada muito relevante sobre o tablet.
        'Hmm... Nada...'
        // Volta para a visão direta da mesa com o computador.
        Caso 2:
        // Troca para a cena aproximando dos documentos abaixo da mesa.
        Você nota um cadeninho vermelho que parece ter caído dentro de uma caixa de mais documentos.
        "Não seria isso né?"
        Pegando o caderninho, você lê várias linhas com dados, parecem senhas e charadas sobre cada senha em cada página.
        'Pelo menos cada senha é diferente...'
        // caso tenha visto o cofre:
        // 'Provavelmente a senha do cofre está aqui'
        // caso não tenha visto o cofre:
        // 'Talvez o tablet esteja bloqueado? De qualquer forma pode ser útil'
        Você se levanta com o caderninho vermelho.
        // Volta na troca de cena para a planta-baixa. --> segue próxima parte.
Caso 4:
    Você se vira para o fundo dessa sala de escritório, onde várias mesas estavam empilhadas.
    'Não parece ter nada por aqui além de poeira.'
    Você se senta um pouco sobre o sofá que tinha ido dormir na primeira noite aqui.
    'Faz alguns dias que eu estou aqui já...'
    A dureza do sofá te incomoda como sempre, e você se levanta.
    // Volta na troca de cena para a planta-baixa.

Com o caderninho em mãos, resta apenas o tablet.

// cofre:
// Parece até que eu tenho os dados de entrada do cofre agora.

Encontrar esse tablet está sendo trabalhoso, que nem encontrar as minhas chaves quando eu saía de casa...

1 - Janela
2 - Armário
3 - Mesas Velhas Empilhadas

Caso 1:
    Você vai até a janela.
    // Troca a cena para uma visão melhor do cenário através da janela
    "Eu gostava daquela sorveteria."
    Você toca o vidro da janela posicionando seu indicador sobre um loja azul mais ao centro da cidade perto de uma praça.
    "Realmente, é uma bela vista..."
    "Mesmo depois do apocalipse..."
    Você divaga um pouco, mas volta ao foco da busca.
    // Volta na troca de cena para a planta-baixa.
Caso 2:
    Você vai até o grande armário verde no canto da parede da janela.
    // Troca a cena para uma visão melhor do armário
    // skip se cofre:
    "Deve ter algo aqui, provavelmente deve estar aqui."
    Você tenta abrir as portas, sem sucesso, parecem emperradas.
    1 - Tentar de Novo.
    Caso 1:
        Você força um pouco, e consegue abrir porta por porta.
        "Aqui tem Documentos."
        "Mais Documentos..."
        "Caramba... Só Documentos?"
        "Uh, um cofre?"
        Você vê que tem um bilhete no cofre: Abrir um cofre é um processo, não?
        "Imagino que sim?"
        Você pensa um pouco, mas agora com a intenção de abrir o cofre.
        // Troca para cena do cofre.
    'O tablet deve estar nesse cofre, ou ele pode ser totalmente não relacionado...'
    'O primeiro é mais provável'
    Você abre o caderninho vermelho, e folheia ele, procurando a charada que combinava com o questionamento do bilhete.
    'Abrir um cofre é um processo... Abrir um cofre é um processo... Abrir um cofre é um processo... Qual a frase que melhor combina?'
    1 - Programas são um conjunto de instruções, se a instrução é um loop "n0v0 numer0" uma hora o programa vai resultar em "&4B3RT0!"
    2 - Processos são os dados de entrada, que precisam ser inseridos no programa do cofre, enquanto você lê o caderno, o programa espera em um estado "Bl0que4d0", e quando você insere a "$3NH4" ele sai do estado bloqueado e entra em "3xecuçã0" ficando "p7onto." abrindo e "conclu1ndo." o processo.
    3 - Faz cerca de "d01$" dias que estou tendo que lidar com um processo jurídico, a empresa parece ter vendido algum dado na "1nt&7n3t" e eu sou o bode espiatório.
    Caso 1:
        "Talvez?"
        'Não... Processos são mais que programas, eles incluem dados de entrada e os estados do processo...'
    Caso 2:
        Aparece um texto escrito: Esperando...
        > Caixa de texto para receber o dado de entrada:
        [040$343071]
        Quando inserido troca para: Reconhecendo...
        Ao aceitar troca para: Pronto!
        Abrindo em seguida, mostrando o conteúdo do cofre sendo o tablet
        "Boa!"
    Caso 3:
        "Não é isso... Isso nem haver com cofre tem..."
        'Além de que estamos falando de um processo do sistema operacional...'
Caso 3:
    Você se vira para o fundo dessa sala de escritório, onde várias mesas estavam empilhadas.
    'É... Só há poeira'
    Você se senta sobre o sofá e sente a dureza dele.
    A dureza do sofá te incomoda como sempre, e você se levanta.
    // Volta na troca de cena para a planta-baixa.
