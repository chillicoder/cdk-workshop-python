from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    core
)

from hitcounter import HitCounter

class CdkworkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='hello.handler'
        )

        hello_with_counter = HitCounter(
            self, 'HelloWithCounter',
            downstream=my_lambda
        )

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=hello_with_counter.handler,
        )