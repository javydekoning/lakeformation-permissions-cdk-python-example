# CDK Example for vending Lake Formation permissions

Files: 

`app.py` - Creates all the CDK (CloudFormation) stacks.
`lf_cdk_python\lf_all_table_permissions` - Construct to assign permissions to all tables in a LakeFormation DataBase
`cool_team_permissions` - Grants `SELECT`, and `DESCRIBE` to all tables in the `sampledb` database. To another AWS account (cool team's account).

## Notes

- This example uses 'Named data catalog resources', cross account shares use Resource Access Manager. 
- If accounts belong to the same org, no acceptance nor linking is required in the target account.