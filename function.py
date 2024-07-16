from googleapiclient.discovery import build

def trigger_df_job(cloud_event,enviroment):

    service = build('dataflow', 'v1b3')
    project = 'ALS-Hamburgueria'

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_text_to_BigQuery"

    template_body = {
        "jobName": "bq-bkt-load",
        "parameters": {
        "inputFilePattern": "gs://bkt-als-hamburgueria/dados/vendas_hamburgueria_1000_linhas_corrigido.csv",
        "JSONPath": "gs://bkt-als-hamburgueria/metadados/metadados_bd-schema.json",
        "outputTable": "als-hamburgueria:bd_alshamburgueria.tabela-vendas",
        "bigQueryLoadingTemporaryDirectory": "gs://bkt-als-hamburgueria/temp/",
        "javascriptTextTransformGcsPath": "gs://bkt-als-hamburgueria/metadados/metadados_transform.js",
        "javascriptTextTransformFunctionName": "transform"
        }
        
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)