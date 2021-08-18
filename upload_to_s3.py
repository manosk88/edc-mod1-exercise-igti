import boto3
import pandas as pd

# Criar um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

s3_client.upload_file("data/annual-enterprise.csv",
                      "datalake-manoel-385970729661"#,
                      # "raw-data/enem/year=2019/MICRODADOS_ENEM_2019.csv"
                     )
#
# df = pd.read_csv("data/annual-enterprise.csv")
# print(df)


# s3 = boto3.resource('s3')
# # Print out bucket names
# for bucket in s3.buckets.all():
#     print(bucket.name)


# s3 = boto3.client('s3')
# s3.download_file('datalake-manoel2-igti-edc', 's3://datalake-manoel2-igti-edc/data/annual-enterprise.csv', 'data/annual-enterprise.csv')