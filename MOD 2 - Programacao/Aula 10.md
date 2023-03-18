# Aula 10 - Variáveis


## Variáveis
- representam um espaço de memória do computador para armazenar determinado dado
- normalmente o compilador/interpretador faz para o computador a associação nome-valor dee forma que os nomes das variáveis localizam a sua posição na memória em que um determinado (ou diversos) tipo(s) de dado(s) podem ser armazenados


### Declaração
- em linguagens tipadas (ex: C), todas as variáveis precisam ser explicitamente declaradas antes de seu uso
- consiste em especificar o nome e tipo de uma variável
    - nome: serve para associar o dado armazenado ao espaço de memória da variável
    - tipo: determina a natureza do dado que será armazenado
        - quando se define o tipo, se define o tamanho da variável
- uma variável só pode receber valores do tipo de dado previamente acordado na declaração (domínio)
- os tipos diferem:
    - pelo espaço de memória que ocupa
    - pelo intervalo de valores que conseguem representar

#### Declaração em Python
- não é preciso declarar variáveis antes do uso
- não é preciso definir o tipo de dado (tipagem dinâmica)
- nomes de variáveis podem surgir ao longo do código e podem assumir dinamicamente diversos tipos

- implicações:
    - facilidade de programação
    - impossibilidade de validação dos dados pode gerar problemas em tempo de execução 


### Tipos de Variáveis
- pode-se categorizar variáveis também em termos da organização da estrutura de dados envolvida

#### Simples ou Atômicas
- associadas a dados simples
- compostos apenas por um elemento como um número ou um caractere (ex: um aminoácido)
#### Compostas
- definidas por um nome associado a diversos elementos (ex: sequência de aminoácidos de uma proteína)
##### Homogêneas
- compostas por elementos de um mesmo tipo de dado
- ex: sequência de aminoácidos
##### Heterogêneas
- armazenam conjuntos de dados formados por tipos diferentes (campos de registro) em uma mesma estrutura
- ex: uma variável proteína que armazene os campos id(string), tamanho(int), massa(float), sequência(string)


### Tipos de variáveis em Python
- há variáveis simples e compostas
- não há como garantir que uma variável composta seja homogênea (a princípio, todas as variáveis compostas são heterogêneas)


### Tipos de dados em Python
- tudo em Python são objetos
- uma variável é uma associação nome-valor
- tipos são dinâmicos

- 3 tipos de dados básicos
    - inteiro
    - ponto flutuante
    - booleano
    - complexo


### Nomes de Variáveis
- não é permitido usar palavras reservadas como identificadores


### Tipos de Variáveis ou Estruturas de Dados em Python
- com relação às variáveis compostas, o Python apresenta:
    - sequências: objetos ordenados e finitos
    - dicionários: conjunto de elementos indexados por chaves (que podem ser sequências de caracteres)

### Sequências
- sequências imutáveis: objetos ordenados e finitos
    - strings
    - tuples: 2 ou mais elementos de qualquer tipo dentro de parênteses separados por vírgula
- sequências mutáveis
    - lists (em outras linguagens: vetores ou arranjos)
    - sets: coleções não ordenadas e não indexadas escritas entre chaves
    - dictionaries: conjuntos de elementos indexados por chaves