from aws_cdk import core as cdk
from lf_all_table_permissions import LfAllDbTablePermissions
import aws_cdk.aws_lakeformation as lf


class CoolTeamPermissionsStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        LfAllDbTablePermissions(self, 'CoolTeamPermissions',
                                data_lake_principal_identifier='991880991323',
                                permissions=['SELECT', 'DESCRIBE'],
                                database_name='sampledb'
                                )
