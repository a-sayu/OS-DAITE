# Fase 20

## Como controlar o compartilhamento de recursos entre processos

Vocês pararam cerca de 4 vezes pelo caminho, e o tablet indicava já ser 13h.

"Estamos chegando?"

jorge "Não..."

"Falta muito?"

jorge "Eu não sei... Porque você não pergunta para o tablet?"

"Ele está sem acesso a internet agora..."

jorge "Espera, ali, a rotatória, finalmente!"

Vocês chegam a rotatória e seguem para a cidade de Jorge.

A cidade estava deserta, mas nenhuma máquina estava a vista.

A casa de Jorge era perto, e abrindo o portão, lá estava um celta digamos que arrumadinho.

Jorge tira a chave do bolso e destranca o carro.

jorge "Você sabe dirigir?"

"Eu tenho carteira de motorista, mas não cheguei a dirigir depois de tirar."

jorge "Bem, eu não consigo dirigir por todas as 7 horas até a capital."

computer "Eu tenho uma ideia!"

jorge "Desde quando você está ouvindo nossa conversa?"

"Qual?"

Vocês perguntam em uníssono.

computer "Porque vocês não compartilham os recursos?"

jorge "Bem, era o que eu estava pensando, mas como a gente vai compartilhar o volante?"

"Podemos usar um meio de comunicar que precisamos trocar."

1- Como um semáforo, em que o volante vai estar ocupado ou desocupado, e há um local para parar ou não, para sinalizar a troca.
2- Você pode só dirigir até se cansar, ai a gente troca.
3- Como um mutex, em que o volante vai estar ocupado ou desocupado, sinalizando para a troca.

Caso 1:

jorge "O que bulhufas semáforo tem haver?"

"Nunca viu um semáforo na vida?"

jorge "Não é só que.. Ai! Só explica."

"Basicamente, enquanto um recurso do sistema está sendo utilizado por um processo, o semafóro impede que outros processos tentam utilizar o recurso."
"De maneira similar, um semafóro no trânsito sinaliza que depois de algum tempo esperando, os carros podem passar."

"Assim, nós podemos temporizar intervalos de troca para parar e trocar de lugar."

jorge "Mas e se um de nós cansar antes do tempo? ou se o outro não ter conseguido descansar direito? ou tiver robôs na pista?"

Caso 2:

jorge "Não...?"

"Por que não?"

jorge "Eu não vou deixar a pessoa que diz 'Eu tenho carteira de motorista, mas não cheguei a dirigir depois de tirar', dirigir enquanto eu tiro meu soninho de beleza."

"M-mas.... Ok"

"Deixe-me tentar de novo."

Caso 3:

jorge "O que bulhufas é um mutex?"

"Mutex é um componente de um sistema operacional, que funciona como uma placa de pare."

"Basicamente, enquanto um recurso do sistema está sendo utilizado por um processo, o mutex impede que outros processos tentem utilizar o recurso."

"De maneira similar, uma placa de pare sinaliza que carros devem parar caso outros carros estejam se aproximando do cruzamento."

"Assim, quando um de nós perceber que está cansado, a gente fala que a barra está livre, para o carro e nós trocamos de lugar."
