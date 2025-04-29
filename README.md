Consecutive Sum Algorithm

This project presents three algorithmic solutions to find pairs of integers where the sum of numbers preceding the first element equals the sum of consecutive numbers between the pair elements.
📝 Description

The project aims to develop efficient algorithms that can:

    Select an initial number (starting at 6)

    Calculate the sum of all preceding values

    Calculate the sum of consecutive subsequent values until it matches the preceding sum

    Generate pairs (initial number, last summed number)

The project explores three different approaches with varying efficiency levels.
🔍 Implemented Solutions
1. First Solution (Simple Iterative)

    Uses a loop to iterate through integers starting at 6

    Calculates preceding sum using Gauss's formula

    Uses a second loop to sum subsequent numbers until matching the preceding sum

    Result: 8 pairs found in ~222 seconds

2. Second Solution (Quadratic Equation)

    Uses quadratic equation to find potential pair ending

    Verifies if subsequent sum equals preceding sum

    Result: 11 pairs found in ~294 seconds

3. Third Solution (Optimized with Constant)

    Similar to second solution but with crucial optimization

    Uses constant 4.1213203 to skip to next probable house

    Result: 15+ pairs found with near-constant time

⚙️ Implementation

The pseudocode for each solution is available in corresponding files:

    Iterative Solution

    Quadratic Equation Solution

    Optimized Solution

📊 Results

The project clearly demonstrates algorithm efficiency evolution:
Solution	Pairs Found	Execution Time
1	8	~222s
2	11	~294s
3	15+	Near-constant
📚 References

    Gauss's summation formula

    Quadratic equation solving

    Algorithm optimization techniques

👨‍💻 Author

Carlos Leandro Silva Machado
São Leopoldo – RS – Brazil

--------------------------------

Algoritmo de Soma Consecutiva

Este projeto apresenta três soluções algorítmicas para encontrar pares de números inteiros onde a soma dos números anteriores ao primeiro elemento do par é igual à soma dos números consecutivos entre os elementos do par.
📝 Descrição

O objetivo do projeto é desenvolver algoritmos eficientes que possam:

    Escolher um número inicial (começando por 6)

    Calcular a soma de todos os valores que antecedem o número escolhido

    Calcular a soma dos valores posteriores consecutivos até que seja igual à soma anterior

    Gerar pares (número inicial, último número somado)

O projeto explora três abordagens diferentes com diferentes níveis de eficiência.
🔍 Soluções Implementadas
1. Primeira Solução (Iterativa Simples)

    Utiliza um laço para percorrer valores inteiros começando em 6

    Calcula o somatório anterior usando a fórmula de Gauss

    Usa um segundo laço para somar números posteriores até igualar o somatório anterior

    Resultado: 8 pares encontrados em ~222 segundos

2. Segunda Solução (Com Equação Quadrática)

    Utiliza equação quadrática para encontrar potencial par final

    Verifica se o somatório posterior iguala o anterior

    Resultado: 11 pares encontrados em ~294 segundos

3. Terceira Solução (Otimizada com Constante)

    Similar à segunda solução, mas com otimização crucial

    Usa constante 4.1213203 para pular para próxima casa provável

    Resultado: Mais de 15 pares encontrados com tempo quase constante

⚙️ Implementação

Os pseudocódigos das soluções estão disponíveis nos arquivos correspondentes:

    Solução Iterativa

    Solução com Equação Quadrática

    Solução Otimizada

📊 Resultados

O projeto demonstra claramente a evolução na eficiência dos algoritmos:
Solução	Pares Encontrados	Tempo de Execução
1	8	~222s
2	11	~294s
3	15+	Quase constante
📚 Referências

    Fórmula de Gauss para somatório

    Resolução de equações quadráticas

    Técnicas de otimização de algoritmos

👨‍💻 Autor

Carlos Leandro Silva Machado
São Leopoldo – RS – Brasil


