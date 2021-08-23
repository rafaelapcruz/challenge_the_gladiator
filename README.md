# Challenge the Gladiator
This is a PvE game in Python! The game is based on positioning the Gladiator (at random) and the player (asking the player for input) and checking after each round if the player survived, died or killer the Gladiator.

This is the final project for the Python course from "As Raparigas do Código". This exercise is a good summary of the programming concepts taught during the Python course.

### Instructions (PT):

Na Roma Antiga, os Gladiadores lutavam entre si na arena, para entretimento do Imperador e do público. O espetáculo, violento e sangrento, era até à morte. Hoje, vamos escrever um pequeno jogo em Python, que nos permita simular um jogo de gladiadores com o computador!

Um gladiador (computador) está escondido numa arena de 5 por 5 metros. A cada jogada, é colocado numa posição aleatória (x,y) na arena.

O utilizador deve então também colocar o seu jogador (adversário) na arena. O gladiador tem uma zona de ataque de raio *r*, como mostra a figura, e o jogo respeita as seguintes regras:

  - Se o adversário estiver longe do gladiador, escapa com vida!
  - Se o adversário estiver na zona de ataque do gladiador **e se o gladiador estiver em modo de ataque**, então o gladiador decapitará o seu adversário instantaneamente. Estar “em modo de ataque” deverá ser um comportamento aleatório;
  - Se o adversário estiver na zona de ataque do gladiador **e o gladiador não estiver em modo de ataque**, então o gladiador é morto.

Podemos assumir o seguinte:

  - São permitidas no máximo 10 jogadas;
  - O raio de ataque do gladiador é de 2 metros;
  - A cada jogada, o programa deverá indicar se o adversário escapou ou não com vida;
  - No final de todas as jogadas, deve ser impresso o número total de vítimas e sobreviventes. No entanto, se o gladiador for morto numa jogada, o programa deverá parar e indicar o número de vítimas e sobreviventes até ao momento e o número de jogadas que foram necessárias para o aniquilar!

**Nota:**
A distância entre dois pontos A e B é medida da seguinte forma: $d(A,B) = \sqrt{(xA - xB)^2 + (yA - yB)^2}$

Source: As Raparigas do Código


### SOLUÇÃO TOP-DOWN

	1. Randomizar a posição do gladiador => Função!
		1.1. X, Y do gladiador aleatória
		1.2. Gerar modo de ataque 
	2. Pedir ao utilizador as posições do jogador adversário
		2.1. Input
	3. Calcular a distância entre o gladiador e o jogador => Função!
		3.1. Calcular expressão
	4. Verificar se é possível o ataque
		4.1. Verificar se a distância entre eles é menor que r (área de ataque)
		4.2. Verificar se o gladiador está em modo de ataque (True/False e tem de ser aleatório) => Função
		4.3. Verificar se o gladiador foi morto. Nesse caso acaba o jogo, caso contrário, o jogador pode ter até 10 jogadas.
	5. Atualizar as estatísticas: mortos, sobreviventes
