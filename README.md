# Detailed Roadmap: Generative AI implementation in serverless computing using AWS Bedrock, SageMaker, LangChain, and Boto3

AWS Bedrock, SageMaker, LangChain, and Boto3 are powerful tools that allow you to build, deploy, and fine-tune generative AI models within the AWS ecosystem. Whether you're working with natural language processing, devops automation, computer vision,  or other AI tasks, these services provide the infrastructure , development toolkits and APIs you need to succeed.

## Steps

CDK will create an Api Gateway, along with a resource and a POST method. There's a AWS Lambda function that will be taking the prompt and invoking an Amazon Bedrock model (anthropic.claude-v2) synchronously. If you wish to try other models, make sure to modify the policy attached to the Lambda function and invoke the right model. 


### Prerequisites:
Before we get into the good stuff, first we need to make sure we have the required services on our local machine or dev server, which are:

- Basic knowledge of AWS CDK.
- AWS Account
- GitHub Account
- AWS CLI installed and configured.
- Docker installed locally.
- AWS CDK installed.
- Typescript installed
- Postman
- Python 3
- NPM
- NodeJS

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/apigw-lambda-bedrock-cdk-python
    ```
1. Create virtual environment for Python
    ```
    python3 -m venv .venv
    ```
    For a Windows platform, activate the virtualenv like this:
    ```
    .venv\Scripts\activate.bat
    ```
1. Install the Python required dependencies:
    ```
    pip install -r requirements.txt
    ```

!pip install -U boto3 langchain
!pip install amazon-textract-textractor amazon-textract-prettyprinter pypdf Pillow
1. Run the command below to bootstrap your account. CDK needs it to deploy
    ```
    cdk bootstrap
    ```
1. Review the CloudFormation template the cdk generates for you stack using the following AWS CDK CLI command:
    ```
    cdk synth
    ```
1. From the command line, use AWS CDK to deploy the AWS resources.
    ```
    cdk deploy
    ```


## Testing


Follow the example below and replace `{your-api-url}` with your api url. 

    ```
    curl -X POST \
    https://77gtvoj9lg.execute-api.us-east-1.amazonaws.com/prod/text_gen \
    -H "Content-Type: application/json" \
    -d '{"prompt": "AI tell me about the coupon code in ecommerce website"}'
    ```



