#!/usr/bin/env python3
import os

import aws_cdk as cdk

from stacks.api_lambda_bedrock_stack.api_lambda_bedrock_stack import ApiLambdaBedrockStack


app = cdk.App()
ApiLambdaBedrockStack(app, "ApiLambdaBedrockStack",
   
    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    #env=cdk.Environment(account='123456789012', region='us-east-1'),
   
    )

app.synth()
