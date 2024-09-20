import polars as pl


print(pl.scan_parquet("parquet/iris.parquet").collect())