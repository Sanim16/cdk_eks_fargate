import aws_cdk as core
import aws_cdk.assertions as assertions
from cdk_new_app.cdk_new_app_stack import CdkNewAppStack


def test_ec2_vpc_created():
    app = core.App()
    stack = CdkNewAppStack(app, "cdk-new-app")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::EC2::VPC", {
        "CidrBlock": "10.0.0.0/16"
    })

def test_eks_fargate_created():
    app = core.App()
    stack = CdkNewAppStack(app, "cdk-new-app")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("Custom::AWSCDK-EKS-Cluster", {
        "Config": {"name": "max-cluster"}
    })

def test_eks_fargate_profile():
    app = core.App()
    stack = CdkNewAppStack(app, "cdk-new-app")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("Custom::AWSCDK-EKS-FargateProfile", {
        "Config": {"selectors": [{"namespace": "maxapp"}]}
    })

def test_eks_fargate_profile_created():
    app = core.App()
    stack = CdkNewAppStack(app, "cdk-new-app")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("Custom::AWSCDK-EKS-FargateProfile", 2)
