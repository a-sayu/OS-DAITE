# Fase 33

## O que faz a MMU

Mais adiante, explorando um laboratório abandonado, o grupo encontra uma grande tela com diagramas.

tablet: "Isso... parece ser um painel antigo de MMU."

jorge: "MMU?"

"Unidade de Gerência de Memória. É tipo… um tradutor de endereços de memória."

tablet: "Correto. Ela converte endereços virtuais, que só o processo entende, em endereços reais, que a memória física compreende."

jorge: "E ela faz isso sozinha?"

tablet: "Sim. É hardware. Rápida e precisa. Usa uma tabela para mapear as páginas virtuais às molduras físicas."

personagem_estrangeiro: “Página… Moldura. Tradução!”

"Se o processo fosse um livro, a memória virtual seriam as páginas. E a MMU seria o bibliotecário que encontra onde elas estão na estante real."

jorge: "Tá… e tudo isso pra não deixar a RAM se encher com besteira?"

tablet: "Exatamente. Só o necessário vai pra RAM. O resto, espera sua vez."

---

Fase 33 – Como indicar no código uma chamada para periférico

jorge: "Se fosse código, como seria isso?"

tablet: "Algo como use(periférico_rádio)."

"Mas precisa passar por mim antes."

tablet: "O sistema operacional valida. Ele é o juiz."

personagem_estrangeiro: pisca lentamente

jorge: "Acho que ele entendeu alguma coisa..."

Fase 40 – Ciclo de vida dos processos

O grupo observa o braço robótico após ele concluir outra tarefa automática.

jorge: "Sabe… esse braço se parece muito com a gente no caminho dessa viagem."

"Como assim?"

jorge: "Ele foi ativado, fez o que tinha que fazer… e agora tá parado esperando o próximo comando."

tablet: "Você descreveu o ciclo de vida de um processo."

personagem_estrangeiro: “Processo… viver?”

"Sim. Eles nascem, entram em execução, podem esperar por algo e depois são encerrados."

tablet: "Estado 'Pronto', depois 'Em Execução'. Se aguardam algo, ficam 'Bloqueados'. Quando finalizam, vão para 'Encerrado'."

jorge: "Igual nossa viagem… Eu nasci em casa, tô em execução agora, esperando comida, e talvez um dia, encerro na capital."

tablet: "Romântico. E tecnicamente correto."

