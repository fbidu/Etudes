# Notas de Estudo

## Informações Novas

### Fundamentos

* Relembrando - no paradigma funcional, contamos ao computador como as coisas
  `são` e não o que o computador deve `fazer`
* Haskell é funcional e pura. Sem efeitos colaterais
* Haskell usa _lazy evaluation_ para tudo
* Instruções de instalação no [site oficial](https://www.haskell.org/platform/linux.html)
* Haskell tem um REPL bem interessante, o ghci
* Booleanos são na forma True, False
* Operadores booleanos são `&&`, `||` e `not`
  (interessante como misturaram os estilos)
* Diferença é dada pelo operador `/=`.
  Os outros operadores aritméticos são os de costume
* Funções são infixas ou pré-fixas
* Funções são invocadas por **um espaço depois dos nomes**

```haskell
succ 8  -- função que retorna o sucessor
min 9 10
min 100 101
```

* Funções prefixas podem ser feitas infixas com `

```haskell
9 `min` 10 == min 9 10
```

* Parênteses servem *apenas* para alterar a precedência,
  e não para embrulhar argumentos
* Chamadas de função têm **precedência máxima**
  (estamos numa linguagem funcional, afinal kkkk):

```haskell
succ 9 * 10 == 10 * 10
succ (9 * 10) == 91
```

* Funções são declaradas de forma direta, igual como são chamadas:

```haskell
doubleMe x = x + x

-- e podem ser encadeadas como de costume também
doubleUs x y = doubleMe x + doubleMe y
```

* `ifs` são **expressões** - portanto blocos `if` **precisam ter algum valor**
* Portanto, `else` é **obrigatório**

```haskell
-- dobra o número só se ele for menor que 100
doubleSmallNumber x = if x > 100  
                        then x  
                        else x*2 
```

Note o uso do if-como-expressão:

```haskell
    doubleSmallNumber' x = (if x > 100 then x else x*2) + 1  
```

* O caracter ` é válido em nomes de funções e é usualmente colocado para denotar
  que uma função é "estrita" - em oposição à "lazy" - ou que é uma versão
  levemente modificada de outra função
* Nomes de funções não podem começar com letra maiúscula
* Funções que não tem parâmetros são chamadas de "definições" ou nomes - me
  parecem como constantes, em outras linguagens:

```haskell
felipe = "Bidu"
```

## Listas

* Listas são homogêneas - apenas guardam elementos de um tipo
* Strings são listas
* Concatenação de listas é com o operador `++`

```haskell
[1, 2, 3, 4, 5] ++ [6, 7, 8] == [1, 2, 3, 4, 5, 6, 7, 8]
"eae" ++ " " ++ "planetaa"
```

* Assim como em Erlang/Elixir, adicionar itens ao final da lista é custoso e
  depende de escanear todos os elementos da lista à esquerda
* Para adicionar itens ao começo de uma lista, use o operador `:`

```haskell
'o':"lar"
1:[2, 3, 4, 5]
```

Note:

```haskell
"o":"lar"

<interactive>:34:5: error:
    • Couldn't match type ‘Char’ with ‘[Char]’
      Expected type: [[Char]]
        Actual type: [Char]
    • In the second argument of ‘(:)’, namely ‘"lar"’
      In the expression: "o" : "lar"
      In an equation for ‘it’: it = "o" : "lar"
```

* Para obter um item pelo índice, use `!!`

```haskell
[1, 2, 3] !! 0 == 1
[1, 2, 3] !! 2 == 3
```


* O tipo do elemento dentro da lista compõe o tipo da lista. Isso é
  você não pode ter uma lista aninhanda onde uma lista interna contém
  inteiros e outra contém caracteres:

```haskell
[[1, 2], [3, 4], ['a']] --erro!
```

* Curiosamente, na minha versão atual do Haskell, em casos assim o erro sempre
  é apontado como estando no _número_:

```
[[1, 2], ["a", "b"]]

<interactive>:48:3: error:
    • No instance for (Num [Char]) arising from the literal ‘1’
    • In the expression: 1
      In the expression: [1, 2]
      In the expression: [[1, 2], ["a", "b"]]

[["a", "b"], [1, 2]]

<interactive>:50:15: error:
    • No instance for (Num [Char]) arising from the literal ‘1’
    • In the expression: 1
      In the expression: [1, 2]
      In the expression: [["a", "b"], [1, 2]]

[['a'], [1]]

<interactive>:51:10: error:
    • No instance for (Num Char) arising from the literal ‘1’
    • In the expression: 1
      In the expression: [1]
      In the expression: [['a'], [1]]

[[1], ['a']]

<interactive>:52:3: error:
    • No instance for (Num Char) arising from the literal ‘1’
    • In the expression: 1
      In the expression: [1]
      In the expression: [[1], ['a']]
```

* Eu achei esse comportamento bem curioso e, para mim, indica que a ordem de
  computação de tipos não é simplesmente "da esquerda para direita". Talvez
  o cômputo de "coisas envolvendo texto" tenha precedência?

### Operando com Listas

#### Obtendo Elementos e sublistas

```haskell
head [5, 4, 3] == 5 -- o primeiro elemento
tail [5, 4, 3] == [4, 3] -- tudo menos o primeiro
last [5, 4, 3] == 3 -- o último elemento
init [5, 4, 3] == [5, 4] -- tudo menos o último
```

```haskell
length [1, 2, 3] == 3
null [] == True
reverse [1, 2, 3] == [3, 2, 1]

take 2 [1, 2, 3, 4] == [1, 2]
take 20 [1, 2, 3, 4] == [1, 2, 3, 4]
take 0 [1, 2, 3, 4] == []

drop 2 [1, 2, 3, 4] == [3, 4]
drop 1 [1, 2, 3, 4] == [2, 3, 4]
drop 3 [1, 2, 3, 4] == [4]

minimum [1, 2, 3, 4] == 1
maximum [1, 2, 3, 4] == 4

sum [1, 2, 3] == 6
product [1, 2, 3, 0] == 0
```

#### Checaem de Continência

Com a função `elem`, normalmente usada de forma infixa:

```haskell
2 `elem` [1, 2, 3] == True
4 `elem` [1, 2, 3] == False
```

## Ranges

Em geral, muito similar ao Python, tirando a parte
do passo e a borda superior é incluída

```haskell
[1..10] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
['a'..'d'] == "abcd" -- também temos ranges de chars! 
```

Como pegamos todos os pares de 2 até 20?

```haskell
[2,4..20] == [2,4,6,8,10,12,14,16,18,20]
```

**Note**: O passo não é 2 porque o primeiro elemento é dois. O passo é dois
porque `4 - 2 = 2`. Ou seja, o tamanho do passo é dado pelo primeiro argumento
do range menos o primeiro elemento incluso.

```haskell
[2,10..20] == [2, 10, 18] -- passo->10-2=8
[2,2..20] -- loop infinito pois tem passo 0
```

Como de costume, cuidado com pontos flutuantes:

```haskell
[0.1, 0.3..1] == [0.1,0.3,0.5,0.7,0.8999999999999999,1.0999999999999999]
```

### Listas Infinitas

Ranges sem limite superior são infinitos

```haskell
[1..] -- lista infinita começando em um
take 30 [12,24..] -- retorna os primeiros 30 múltiplos de 12
```

Adicionalmente, as seguintes funções criam listas infinitas:

```haskell
cycle [1, 2, 3] ==[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3...]
take 10 (cycle [1,2,3]) == [1,2,3,1,2,3,1,2,3,1] 
take 12 (cycle "LOL ") == "LOL LOL LOL "

take 10 (repeat 5) == [5,5,5,5,5,5,5,5,5,5] -- repete um elemento infinitamente
```

Por fim, podemos replicar um elemento um número _finito_ de vezes com `replicate`

```haskell
replicate 3, 11 == [11, 11, 11]
```

## List Comprehensions

Sintaxe mais enxuta que do python

```haskell
[x*2 | x <- [1..10]] == [2,4,6,8,10,12,14,16,18,20] -- pipe separando variável do gerador
[x*2 | x <- [1..10], x*2 >= 12] -- condicionais separadas por vírgula
```

Múltiplas listas são iteradas por todos os pares

```haskell
[x * y | x <- [3, 2], y <- [5, 6]] == [15,18,10,12]
```

Como strings _são_ listas, elas podem passar por comprehension também:

```haskell
removeNonUppercase st = [ c | c <- st, c `elem` ['A'..'Z']]

removeNonUppercase "IdontLIKEFROGS" == "ILIKEFROGS"
```

## Tuplas

Tuplas são marcadas por `(), não precisam ser homogêneas como listas e o
seu **tipo depende do seu número de elementos**

```haskell
[(1, 2), (5, 6), (0, 1)] -- ok!
[(1, 2), (5, 6, 7), (0, 1)] -- erro! O elemento do meio tem tamanho errado
[("one", 1),("two", 2)] -- ok! Não precisa ser homogênea
[("one", 1), (2, 2)] -- erro! Os tipos precisam ser iguais
```

Em 2-tuplas (duplas) podemos acessar a primeira e a segunda componente com
`fst` e `snd`:

```haskell
fst (1, 2) == 1
snd (1, 2) == 2
```

Em Haskell, `zip` também gera 2-tuplas de listas:

```haskell
zip [1, 2, 3] [4, 5, 6] == [(1, 4), (2, 5), (3, 6)]
zip [1..] ["a", "b", "c", "d"] == [(1, "a"), (2, "b"), (3, "c"), (4, "d")]
```

## O Sistema de Tipos

* Podemos inspecionar tipos no GHCI com `:t <expressão>`

```haskell
ghci> :t 'a'  
'a' :: Char  
ghci> :t True  
True :: Bool  
ghci> :t "HELLO!"  
"HELLO!" :: [Char]  
ghci> :t (True, 'a')  
(True, 'a') :: (Bool, Char)  
ghci> :t 4 == 5  
4 == 5 :: Bool  
```

* Os `::` podem ser lidos como "tem tipo"
* Tipos explícitos sempre começam com letra maiúscula
* Note como tuplas tem um tipo próprio. Enquanto `"HELLO!"` é uma lista de `Char`,
  `(True, 'a')` tem tipo `(Bool, Char)`
* **Funções tem tipos** no sentido usual de `entrada -> saída`. É considerado
  boa prática dar os tipos explícitos, exceto quando lidando com funções curtas

```haskell
removeNonUppercase :: [Char] -> [Char]  
removeNonUppercase st = [ c | c <- st, c `elem` ['A'..'Z']]   
```

* Funções com múltiplas entradas são tipadas com `->` também

```haskell
addThree :: Int -> Int -> Int -> Int  
addThree x y z = x + y + z  
```

* Se você não tem certeza do tipo da função, pode só declarar a função e então
  usar o operador `:t` para checar seu tipo

### Tipos Comuns

#### Int

Inteiro limitado ao tamanho da `word` da máquina (32bits, 64bits, etc)

#### Integer

Inteiros não limitados. Menos eficientes que `Int`;

#### Float

Ponto flutuante de precisão simples

#### Double

Ponto flutuante de precisão dupla

#### Bool e Char

Como de costume

#### Tuplas

O tipo de uma tupla depende de seu tamanho e do tipo dos seus membros, portanto
em teoria nós temos infinitos tipos diferentes de tupla. Note que uma tupla
vazia `()` é também um tipo.

### Tipos Variáveis

* A função `head` aceita uma lista genérica e retorna seu primeiro elemento

```haskell
ghci> :t head  
head :: [a] -> a
```

* O tipo dela é então denotado `[a] -> a`. Pois ela aceita uma lista de tipo
  qualquer "a" e retorna seu primeiro elemento que, por definição de lista,
  também terá o tipo "a"

* Note que `a` está escrito em minúsculo. Tipos em letra maiúscula são tipos
  explícitos

* A função `fst` retorna o primeiro elemento de uma tupla. Por definição, o
  primeiro e segundo elementos de uma tupla podem ter valores diferentes.
  Qual será seu tipo?

```
ghci> :t fst  
fst :: (a, b) -> a  
```

* Note como ele toma uma tupla e tem como retorno o tipo do seu primeiro elemento

## Typeclasses 101

* Uma typeclass é similar à uma interface
* Se um tipo faz parte de uma _typeclass_ é porque ele suporta e implementa
  o comportamento definido por aquela typeclass

* Note o tipo do operador `==`:

```haskell
ghci> :t (==)  
(==) :: (Eq a) => a -> a -> Bool 
```

* O símbolo `=>` é a novidade aqui. Ele é chamado de _class constraint_
* Essa definição pode ser lida como:

> A função `==` faz faz parte da typeclass `Eq`. Essa typeclass aceita dois
> membros que sejam do mesmo tipo e retorna um booleano.

* A função `elem` tem tipo `(Eq a) => a -> [a] -> Bool` pois usa de `==` para
  determinar se um valor que queremos está na lista

### Algumas Typeclasses

#### Eq

* Suportam testes de igualdade com `==` e `/=`

#### Ord

* Possuem ordenação
* A função `compare` toma dois membros `Ord` e returna sua ordenação,
  que pode ser `GT`, `LT` ou `EQ`

```haskell
ghci> "Abrakadabra" < "Zebra"  
True  
ghci> "Abrakadabra" `compare` "Zebra"  
LT  
ghci> 5 >= 2  
True  
ghci> 5 `compare` 3  
GT
```

#### Show

* Membros de `Show` têm representação como string - similar à uma classe que
  define `__str__` em Python
* A função `show` faz exatamente isso, exibe a representação como string do tipo

```haskell
ghci> show 3  
"3"  
ghci> show 5.334  
"5.334"  
ghci> show True  
"True"
```

#### Read

* Oposto de `Show`, converte uma string em um membro de outro tipo

```haskell
ghci> read "5" - 2
3
ghci> read "True" || False
True
ghci> read "8.2" + 3.8
12.0
ghci> read "[1,2,3,4]" ++ [3]
[1,2,3,4,3]
```

* Note que em todos esses casos Haskell pode _inferir_  o tipo pra ser retornado
  com base no tipo que vinha depois das operações. Se não tiver uma operação,
  teremos um problema com os tipos:

```haskell
ghci> read "4"  
<interactive>:1:0:  
    Ambiguous type variable `a' in the constraint:  
      `Read a' arising from a use of `read' at <interactive>:1:0-7  
    Probable fix: add a type signature that fixes these type variable(s)  
```

* Nesse caso, precisamos fazer uma anotação explícita de tipos

```haskell
ghci> read "5" :: Int  
5  
ghci> read "5" :: Float  
5.0  
ghci> (read "5" :: Float) * 4  
20.0  
ghci> read "[1,2,3,4]" :: [Int]  
[1,2,3,4]  
ghci> read "(3, 'a')" :: (Int, Char)  
(3, 'a')  
```

#### Enum

* Tipos que são enumeráveis
* Podem ser usados em `ranges`!
* Possuem sucessores e antecessores bem definidos que podem ser descobertos com
  `succ` e `pred`:

```haskell
ghci> ['a'..'e']  
"abcde"  
ghci> [LT .. GT]  
[LT,EQ,GT]  
ghci> [3 .. 5]  
[3,4,5]  
ghci> succ 'B'  
'C'
```

#### Bounded

* Possuem limitantes superiores e inferiores

```haskell
ghci> minBound :: Int
-2147483648
ghci> maxBound :: Char
'\1114111'
ghci> maxBound :: Bool
True 
ghci> minBound :: Bool
False
```

#### Num

* Typeclass numérica, seus membros podem atuar como números
* Note que os números em si são polimórficos:

```haskell
ghci> :t 20  
20 :: (Num t) => t
ghci> 20 :: Int  
20  
ghci> 20 :: Integer  
20  
ghci> 20 :: Float  
20.0  
ghci> 20 :: Double  
20.0  
```

* Observe o tipo das operações algébricas:

```haskell
ghci> :t (*)  
(*) :: (Num a) => a -> a -> a  
```

* No caso elas tomam dois números quaisquer do mesmo tipo e retorna outro
  número do mesmo tipo
* Operações como `5 * (6 :: Integer)` funcionam bem pois `5` pode agir como
  um elemento do tipo `Integer`
* Porém operações do tipo `(5 :: Int) * (6 :: Integer)` vão falhar

#### Integral

* Números que são inteiros, como `Int` e `Integer`
* Uma função útil ao lidar com números é a `fromIntegral`, que transforma
  elementos de `Integral` em elementos numéricos mais genéricos, da
  typeclass `Num`.
* Isso é útil pois algumas funções como `lenghth` não retornam `Num`, mas sim
  `Int`. Portanto, isso falha:

```haskell
Prelude> list = [1, 2, 3]
Prelude> (length list) / 2

<interactive>:63:1: error:
    • No instance for (Fractional Int) arising from a use of ‘/’
    • In the expression: (length list) / 2
      In an equation for ‘it’: it = (length list) / 2

Prelude> fromIntegral(length list) / 2
1.5
```

#### Floating

* Pontos flutuantes `Float` e `Double`
