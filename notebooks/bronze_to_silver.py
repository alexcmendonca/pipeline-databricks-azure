# Databricks notebook source
# listando conteúdo do diretório
dbutils.fs.ls('/mnt/dados/bronze')

# COMMAND ----------

# MAGIC %md
# MAGIC ##Lendo os dados na camada bronze

# COMMAND ----------

path = 'dbfs:/mnt/dados/bronze/dataset_imoveis'
df = spark.read.format('delta').load(path)

# COMMAND ----------

display(df.head(5))

# COMMAND ----------

# MAGIC %md
# MAGIC ##Transformando os campos do json em colunas

# COMMAND ----------

# separando os campos da coluna anúncio em colunas diferentes
display(df.select("anuncio.*").head(5))

# COMMAND ----------

# separando os campos da coluna anúncio e endereço em colunas diferentes
display(
    df.select('anuncio.*', 'anuncio.endereco.*')
    .head(5)
    )

# COMMAND ----------

# salvando os dados com as colunas individualizadas em uma nova variável
dados_detalhados = df.select('anuncio.*', 'anuncio.endereco.*')

# COMMAND ----------

# visualizando e validando os dados
display(dados_detalhados.head(5))

# COMMAND ----------

# MAGIC %md
# MAGIC ##Removendo colunas

# COMMAND ----------

df_silver = dados_detalhados.drop('caracteristicas', 'endereco')
display(df_silver.head(5))

# COMMAND ----------

# MAGIC %md
# MAGIC ##Salvando na camada silver

# COMMAND ----------

path = 'dbfs:/mnt/dados/silver/dataset_imoveis'
df_silver.write.format('delta').mode('overwrite').save(path)

# COMMAND ----------

# validando a gravação do conteúdo do diretório
display(dbutils.fs.ls('/mnt/dados/silver/dataset_imoveis'))

# COMMAND ----------


