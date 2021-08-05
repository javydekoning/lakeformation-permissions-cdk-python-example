#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

from lf_cdk_python.cool_team_permissions import CoolTeamPermissionsStack


app = cdk.App()
CoolTeamPermissionsStack(app, "LfCdkPythonStack",
                         # Uncomment the next line if you know exactly what Account and Region you
                         # want to deploy the stack to. */

                         #env=core.Environment(account='123456789012', region='us-east-1'),
                         )

app.synth()
