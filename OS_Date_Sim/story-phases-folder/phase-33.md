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
