# Projeto ALS-Burger

Este repositório contém o código e a documentação do projeto desenvolvido para a hamburgueria ALS-Burger, 
utilizando a infraestrutura de nuvem do Google Cloud Platform (GCP). O objetivo deste projeto é realizar o processamento e 
análise dos dados de vendas e operações da hamburgueria,proporcionando insights valiosos para a administração.

## Visão Geral do Projeto

O projeto envolve as seguintes etapas e tecnologias:

1. **Armazenamento de Dados**: Utilização de um bucket no Google Cloud Storage (GCS) para armazenar os arquivos de dados em formato CSV.
2. **Processamento de Dados (ETL)**: Uso do Google Dataflow para realizar a extração, transformação e carga (ETL) dos dados, preparando-os para análise.
3. **Data Warehouse**: Armazenamento dos dados transformados no BigQuery, onde é possível realizar consultas SQL para análise avançada.
4. **Transformação de Dados**: Desenvolvimento de scripts em JavaScript para transformar os arquivos CSV em JSON e construir o schema do BigQuery.
5. **Consultas SQL**: Utilização de SQL para realizar consultas e análises sobre os dados armazenados no BigQuery.
6. **Dashboard Interativo**: Criação de um dashboard interativo no Looker Studio (antigo Data Studio) para visualização e análise dos dados pela equipe administrativa.

## Estrutura do Repositório

- `data/`: Contém exemplos de arquivos CSV usados para armazenar dados de vendas.
- `scripts/`: Scripts em JavaScript para transformação dos dados e construção do schema do BigQuery.
- `sql/`: Consultas SQL utilizadas para análise dos dados no BigQuery.
- `dashboards/`: Configurações e templates do dashboard no Looker Studio.
- `docs/`: Documentação adicional sobre o projeto.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter:

- Conta no Google Cloud Platform (GCP).
- Permissões para criar e acessar recursos no GCP (Cloud Storage, Dataflow, BigQuery, Looker Studio).
- Node.js instalado para executar os scripts em JavaScript.

## Configuração e Execução

### Armazenamento de Dados

1. Faça o upload dos arquivos CSV para um bucket no Google Cloud Storage.

### Processamento de Dados (ETL)

1. Execute o pipeline de ETL no Google Dataflow utilizando os scripts em `scripts/`.
2. Certifique-se de que os dados transformados estão sendo carregados corretamente no BigQuery.

### Análise de Dados

1. Utilize as consultas SQL em `sql/` para analisar os dados no BigQuery.
2. Crie novas consultas conforme necessário para obter insights adicionais.

### Dashboard Interativo

1. Configure o dashboard no Looker Studio utilizando os templates em `dashboards/`.
2. Personalize o dashboard para atender às necessidades da equipe administrativa.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias e correções.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---
