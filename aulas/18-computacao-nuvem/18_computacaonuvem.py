# -*- coding: utf-8 -*-
"""18_ComputacaoNuvem.ipynb



Prof. Fernando Amaral

www.eia.ai

# Computação na Nuvem
"""

!pip install boto3

import boto3
import io
from io import BytesIO

s3 = boto3.resource(
    service_name ='s3',
    region_name = 'sa-east-1',
    aws_access_key_id = 'AKIAVF6XVFBSOOJOJSPU',
    aws_secret_access_key = '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'

)

bucket = 'fernandoaulapython'
prefix = 'imagens/'

for object_s3 in s3.Bucket(bucket).objects.filter(Prefix=prefix):
  if object_s3.key.endswith('jpg') or object_s3.key.endswith('JPG'):
    # print(object_s3)
    filename = object_s3.key.split('/')[1]
    print(filename)

    body = object_s3.get()['Body'].read()
    imagem = io.BytesIO(body)
    with open(filename,'wb') as f:
      f.write(imagem.getbuffer())

