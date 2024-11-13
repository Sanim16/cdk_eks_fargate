#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_new_app.cdk_new_app_stack import CdkNewAppStack


app = cdk.App()
CdkNewAppStack(app, "CdkNewAppStack")

app.synth()
