# Databricks e Data Factory | Criando e orquestrando pipelines com Azure

## 💡Objetivos
Desenvolver um pipeline de engenharia de dados, usando recursos da ferramenta de Cloud utilizada pela Microsoft Azure, agendando a execução dos notebooks no ambiente do Azure Databricks, utilizando ferramentas como PySpark, Databricks e requisições de API. Incluindo, utilização do Data Factory e o Databricks com Python para ler e manipular os dados nas camadas bronze e silver de um Data Lake que será criado no Azure.

###### Imagem 1: Etapas do pipeline
<img src="/img/etapas-pipeline.png">

Para execução de todas as etapas desse pipeline, foi utilizado o Trello para organizar todas as atividades necessárias para concluir este projeto.

###### Imagem 2: Projeto Trello 
<img src="/img/trello-projeto.png">

## 🖥️Desafios do Projeto
Para configurar os recursos na Azure e estruturar nosso Data Lake para armazenar e organizar os dados, foi utilizada a tecnologia Data Lake Gen 2 da Azure. Inicialmente, configurando o registro de aplicativo e atribuindo permissões adequadas para gerenciar o acesso aos dados no Data Lake.

###### Imagem 3: Integrando Databricks com GitHub
<img src="/img/img-databricks-github.png">

Em seguida, realizada configuração no Databricks para executar as transformações nos dados, aproveitando os recursos da Azure. Criação do workspace Databricks dentro da própria Azure, garantindo acesso à ferramenta e configurando-a conforme necessário. Conexão estabelecida entre o Databricks e o Data Lake para acesso e manipulação dos dados.

Para a transformação dos dados, inicialmente os salvando na camada bronze, aplicando transformações iniciais com base nas necessidades das equipes que utilizarão esses dados. Em seguida, aplicando transformação novamente e os salvando na camada silver, convertendo cada campo do JSON em uma coluna individual e removendo informações desnecessárias sobre as características dos imóveis.

Posteriormente, foi criado e configurado o Data Factory para agendar e executar os notebooks de forma programada, garantindo a integridade e eficiência pipeline para os novos lotes de dados de imóveis que chegarão ao Data Lake. Configurando também o acesso workspace do Databricks, permitindo que o Data Factory se conecte e utilize os recursos do Databricks para executar as atividades planejadas no pipeline.

Realizado testes essenciais para garantir a execução correta do pipeline e identificar possíveis erros. Ao final, configuração de um gatilho de execução, já que novos dados de imóveis serão periodicamente adicionados ao Data Lake, com uma frequência de atualização de uma vez por hora. Isso garantirá que o pipeline seja executado de acordo com esse intervalo de tempo.

###### Imagem 4: Criação de um pipeline do Data Factory
<img src="/img/pipeline-datafactory.png">

## 📄Conhecimentos Desenvolvidos
|Atividades|Realizadas |
|----------|-----------|
| Criar uma conta na Azure | Definir um orçamento e configurar alerta de gastos |
| Navegar no Trello do projeto do curso | Criar um grupo de recursos |
| Criar uma conta de armazenamento na Azure | Estruturar um Data Lake |
| Entender o que são as camada inbound, bronze e silver | Configurar um registro de aplicativo |
| Atribuir permissões em um Data Lake | Utilizar o IAM e o Gerenciamento de ACL da Azure |
| Criar o workspace do Databricks na Azure | Conectar o Databricks ao GitHub |
| Criar um cluster no Databricks | Ativar e encerrar a execução de um cluster |
| Lidar com possíveis erros na criação do cluster | Conectar o Databricks ao Data Lake |
| Utilizar Python no Databricks | Aplicar transformações nos dados |
| Salvar dados no formato Delta | Armazenar os dados nas diferentes camadas do Data Lake |
| Criar e configurar o Data Factory na plataforma da Azure | Navegar pela interface do Data Factory |
| Entender as diferenças do Data Factory para o Airflow | Integrar o Data Factory com o GitHub |
| Desenvolver um pipeline no Data Factory | Conectar o Databricks ao Data Factory |
| Depurar o pipeline | Criar um gatilho de execução |
| Publicar e colocar o pipeline em produção | Deletar os recursos da Azure |

##  🗂️Organização dos Arquivos Databricks e Data Factory
* Notebooks | Databricks
    - Transformações nos dados e salvando-os em um arquivo Delta Lake no repositório Azure Data Lake.

* Factory | Azure Data Factory
    - Arquivos de configuração carregados no repositório GitHub após conexão Data Factory

* Databricks-pcm
    - Arquivos de configuração da conexão do Databricks ao Data Factory

* Pipeline
    - Arquivos de configuração do pipeline

* Trigger
    - Arquivos de configuração do gatilho de execução

## 🎞️Imagens do Projeto

###### Imagem 5: Monitorando execução do pipeline no Data Factory
<img src="/img/monitorando-execucao-pipeline.png">

###### Imagem 6: Monitorando execução do pipeline no Databricks / Job runs
<img src="/img/monitorando-execucao-pipeline-databricks.png">

###### Imagem 7: Tela inicial do estúdio Azure Data Factory
<img src="/img/estudio-azure-data-factory.png">

## 🔍Referências
- [Alura](https://www.alura.com.br/)