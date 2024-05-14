# Website-as-IAC
This repo contains the IAC for my own personal portfolio website. It primarily uses AWS SAML as the IAC tool since the website along with all other components are hosted on AWS. 


Firstly the architecture of the AWS components which host the website consists of 
1. a `AWS gateway` exposing a URL 
2. which when called triggers a `AWS Lambda` whose code is defined in this repo as app.py
3. this python code then calls the API on the backend `Amazon DynamoDB` which stores a count called visitors count for the number of http req sent from browsers
4. when any push is made to this repo, the `github action` yaml file is triggerd which then uses the `AWS SAM CLI` to deplpoy any changes to the infrastructure
