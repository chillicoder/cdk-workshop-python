import json
import pytest

from aws_cdk import core
from cdkworkshop.cdkworkshop_stack import CdkworkshopStack


def get_template():
    app = core.App()
    CdkworkshopStack(app, "cdkworkshop")
    return json.dumps(app.synth().get_stack("cdkworkshop").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
