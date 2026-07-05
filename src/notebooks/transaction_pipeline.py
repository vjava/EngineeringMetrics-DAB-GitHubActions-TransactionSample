from pyspark.sql import functions as F
df=spark.range(1000).withColumn("amount",F.col("id")*10)
df.write.mode("overwrite").option("header",True).csv("/Volumes/engmetrics/landing/transactions/data")
df.write.mode("overwrite").saveAsTable("engmetrics.landing.transactions")
display(df)
