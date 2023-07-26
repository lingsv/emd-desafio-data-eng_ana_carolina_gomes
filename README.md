# Desafio de Data Engineer - EMD

Repositório de instrução para o desafio técnico para vaga de Pessoa Engenheira de Dados no Escritório de Dados do Rio de Janeiro

## Árvore de diretórios

```bash
.
├── docs
│   └── README.md
├── logs
│   └── dbt.log
├── pipelines
│   ├── credentials.json
│   ├── data
│   │   └── dados_brt.csv
│   ├── flows.py
│   ├── __init__.py
│   ├── run.py
│   ├── tasks.py
│   └── utils.py
├── README.md
├── requirements.txt
└── rio_brt_data
    ├── dbt_project.yml
    ├── dev
    │   ├── compiled
    │   │   └── rio_brt_data
    │   │       └── models
    │   │           └── example
    │   │               ├── my_first_dbt_model.sql
    │   │               └── my_second_dbt_model.sql
    │   ├── graph.gpickle
    │   ├── manifest.json
    │   ├── partial_parse.msgpack
    │   ├── run
    │   │   └── rio_brt_data
    │   │       └── models
    │   │           └── example
    │   │               ├── my_first_dbt_model.sql
    │   │               └── my_second_dbt_model.sql
    │   └── run_results.json
    ├── logs
    │   └── dbt.log
    ├── models
    │   ├── rio_brt_data.sql
    │   ├── schema.yml
    │   └── select_data_brt.sql
    ├── README.md
    └── tests
```

## Pastas e arquivos

### Pipelines

**Descrição**: Pasta com os arquivos do pipeline Prefect.

|Nome|Descrição|
|-------|---------|
|flows.py| Arquivo com os flows a serem executados|
|tasks.py| Arquivo com as tasks a serem executadas.|
|utils.py| Arquivo de utilidades do projeto Prefect.|
|run.py| Arquivo que executa o pipeline.|
|data| Pasta que recebe o arquivo CSV gerado no pipeline.|

### rio_brt_data

**Descrição**: Pasta com os arquivos do projeto dbt.

|Nome|Descrição|
|-------|---------|
|models| Pasta com os modelos dbt.|
|models/rio_brt_data.sql| Modelo que cria a tabela.|
|models/select_data_brt.sql| Modelo que cria a view do desafio.|
|models/schema.yml| Arquivo que documenta os modelos.|
|dbt_project_yml| Arquivo com as configurações do dbt.|

## Como executar o pipeline

1. Clone o repositório `https://github.com/lingsv/emd-desafio-data-eng_ana_carolina_gomes.git`;
3. Navegue até a pasta do projeto;
4. Crie um ambiente Python localmente
5. Ative o ambiente e digite `pip install -r requirements.txt`;
6. Configure uma instância local do PostgreSQL;
7. Crie um arquivo credentials.json na pasta **pipelines**;
8. O arquivo deve ter este template:
```json
{
  "host": "host",
  "database": "database",
  "user": "user",
  "password": "password"
}
```
9. Ainda no diretório **pipeline**, digite `python run.py`;

## Como executar o projeto dbt

1. No mesmo ambiente criado para executar o pipeline Prefect, navegue até a pasta **rio_brt_data**;
2. Digite `dbt run`;
3. Confira se os modelos foram criados com sucesso;
4. Para ver a documentação, digite `dbt docs generate`;
5. Em seguida, digite `dbt docs serve`, uma página web se abrirá com os dados das tabelas;
6. Para limpar a pasta do projeto, digite `dbt clean`.