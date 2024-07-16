# Quantos hamburguers de cada tipo foram vendidos e o total do valor de vendas*/

SELECT PRODUTO,SUM(QUANTIDADE) AS QUANTIDADE, SUM(PRECO_TOTAL) AS VALOR_TOTAL 
FROM `bd_alshamburgueria.tabela-vendas`
GROUP BY PRODUTO



#/*  Qual dia que tem maior venda de hamburguers, qual foi o tipo que mais
#vendeu e o total de valor arrecado desse dia */

SELECT DATA_VENDA , PRODUTO,SUM(QUANTIDADE) AS QUANTIDADE , SUM(PRECO_TOTAL) AS VALOR_TOTAL
FROM `bd_alshamburgueria.tabela-vendas`
GROUP BY PRODUTO, DATA_VENDA
ORDER BY QUANTIDADE DESC

#/* Qual é o hamburguers que vende mais de 3 por pedido por venda */

SELECT PRODUTO , SUM(QUANTIDADE) AS QUANTIDADE
FROM `bd_alshamburgueria.tabela-vendas`
WHERE QUANTIDADE >= 3
GROUP BY PRODUTO
