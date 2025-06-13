# Fase 20

## Como controlar o compartilhamento de recursos entre processos

Fase 20 – Compartilhamento de recursos entre processos

Eles encontram um carro funcionando.

jorge: "Você dirige ou eu?"

"Vamos revezar. Cada parada, a gente troca. Um dirige, outro descansa."

tablet: "Como se fosse controle de mutex entre processos."

"Isso. Só um no volante por vez."

---

Vocês pararam cerca de 4 vezes pelo caminho, e o tablet indicava já ser 13h.

"Estamos chegando?"

jorge "Não..."

"Falta muito?"

jorge "Eu não sei... Porque você não pergunta para o tablet?"

"Ele está sem acesso a internet agora..."

jorge "Espera, ali, a rotatória, finalmente!"

Vocês chegam a rotatória e seguem para a cidade de Jorge.

A cidade estava deserta, mas nenhuma máquina estava a vista.

A cada de Jorge era perto, e abrindo o portão, lá estava um celta digamos que arrumadinho.

Jorge tira a chave do bolso e destranca o carro.

jorge "Você sabe dirigir?"

"Eu tenho carteira de motorista, mas não cheguei a dirigir depois de tirar."

jorge "Bem, eu não consigo dirigir por todas as 7 horas até a capital."

computer "Eu tenho uma ideia!"

jorge "Diga."

"Qual?"

Vocês perguntam em uníssono.

computer "Porque vocês não compartilham os recursos?"

jorge "Bem, era o que eu estava pensando, mas como a gente vai compartilhar o volante?"

"Podemos usar um meio de comunicar que precisamos trocar."

1- Como um semáforo, em que o volante vai estar ocupado ou desocupado, e há um local para parar ou não, para sinalizar a troca.
2- Você pode só dirigir até se cansar, ai a gente troca.
3- Como um mutex, em que o volante vai estar ocupado ou desocupado, sinalizando para a troca.

Caso 1:

jorge "Semáforo?"
