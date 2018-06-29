#!/bin/bash -e

s3_bucket="kaonashi-aws-sam-deploy-test-dev"

echo "** Start to deploy and build. **"
mkdir -p deploy
pip3 install -r src/requirements.txt -t deploy
cp -r src/* deploy
cd deploy
zip -r ../function.zip *
cd ..

echo "Upload swagger spec to s3 bucket..."
#aws s3 cp api/swagger.yaml s3://${s3_bucket}/ \
#  --region us-west-2 \
#  --profile default 

echo "Build kaonashi api..."
#aws cloudformation package \
#  --template-file aws-sam.yaml \
#  --output-template-file aws-sam-deploy.yaml \
#  --s3-bucket ${s3_bucket} \
#  --region us-west-2 \
#  --profile default 

echo "Deploy kaonashi api..."
#aws cloudformation deploy \
#  --template-file aws-sam-deploy.yaml \
#  --stack-name kaonash-aws-sam-deploy-dev \
#  --capabilities CAPABILITY_IAM \
#  --parameter-overrides ArtifactBucket=${s3_bucket} \
#  --region us-west-2 \
#  --profile default 

echo "** All complete! **"
#rm -rf deploy