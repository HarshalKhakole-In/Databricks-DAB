import dlt

@dlt.table
def transormed():
    return spark.range(10)