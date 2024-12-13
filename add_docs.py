import polars as pl

df = pl.read_csv("datasets_info.csv").with_columns(
    pl.col("source").alias("docs")
)
    
print(df.head())

df.write_csv("datasets_info.csv")