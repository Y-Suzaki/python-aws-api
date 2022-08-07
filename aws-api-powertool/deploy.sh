#!/bin/bash -e

s3_bucket="cf-templates-461spye58s2i-ap-northeast-1"

echo "** Start to deploy and build. **"

echo "Upload open-api.yml on s3"
aws s3 cp open-api.yml s3://${s3_bucket}/

echo "Zip python codes"
mkdir -p lambda
cp lambda_handler.py requirements.txt lambda/
cd lambda
pip install -r requirements.txt -t .
zip -r ../lambda.zip ./*
cd ..

echo "Build serverless function..."
aws cloudformation package \
  --template-file aws-sam.yml \
  --output-template-file aws-sam-deploy.yml \
  --s3-bucket ${s3_bucket} \
  --s3-prefix serverless-function \
  --region ap-northeast-1 \
  --profile default

echo "Deploy serverless function..."
aws cloudformation deploy \
  --template-file aws-sam-deploy.yml \
  --stack-name serverless-function \
  --capabilities CAPABILITY_IAM \
  --region ap-northeast-1 \
  --profile default

echo "** All complete! **"
aws s3 rm s3://${s3_bucket}/serverless-function/ \
  --region ap-northeast-1 \
  --profile default \
  --recursive

rm -rf aws-sam-deploy.yml lambda.zip lambda/
