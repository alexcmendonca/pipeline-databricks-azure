# Databricks notebook source
# MAGIC %md
# MAGIC **Conferindo se os dados foram montados e se temos acesso a pasta inbound**

# COMMAND ----------

# listando conteúdo do diretório
dbutils.fs.ls('/mnt/dados/inbound')

# COMMAND ----------

# MAGIC %md
# MAGIC ##Leitura dos dados na camada de inbound

# COMMAND ----------

path = 'dbfs:/mnt/dados/inbound/dados_brutos_imoveis.json'
dados = spark.read.json(path)

# COMMAND ----------

# visualizando os dados
display(dados.head(10))

# COMMAND ----------

# MAGIC %md
# MAGIC ##Removendo colunas

# COMMAND ----------

dados = dados.drop('imagens', 'usuario')

# COMMAND ----------

display(dados.head(5))

# COMMAND ----------

# MAGIC %md
# MAGIC ##Criando uma coluna de identificação

# COMMAND ----------

# importação da biblioteca functions
from pyspark.sql.functions import col

# COMMAND ----------

# executando duas operações no dataframe do Spark
# criando nova coluna chamada 'id' e carregando seus valores da coluna 'id' do dataframe original
df_bronze = dados.withColumn('id', col('anuncio.id'))
display(df_bronze.head(5))

# COMMAND ----------

# listando conteúdo do diretório
dbutils.fs.ls('/mnt/dados/')

# COMMAND ----------

# MAGIC %md
# MAGIC ##Salvando na camada bronze

# COMMAND ----------

path = 'dbfs:/mnt/dados/bronze/dataset_imoveis'
df_bronze.write.format('delta').mode('overwrite').save(path)
