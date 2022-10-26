# aws-ecs-gcp-workload-identity-federation

AWS to GCP Workload Identity Federation in Amazon ECS.

This is a package for working with [Workload Identity Federation](https://cloud.google.com/iam/docs/workload-identity-federation) on Amazon ECS (EC2 or Fargate).

When you import this package, the ECS task role credentials are set as environment variables, so you can use them without any special awareness.

## Quick start

Refer to the [documentation](https://cloud.google.com/iam/docs/configuring-workload-identity-federation#aws), set up Workload Identity federation and enable access to GCP resources from AWS.

Download credential configuration file (e.g. `config-aws-provider.json`) and point it to the credential configuration file path.

```console
$ export GOOGLE_APPLICATION_CREDENTIALS=/path/to/config-aws-provider.json
```

For Amazon ECS, by task definitions, you can pass environment variables to a container ([documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/taskdef-envfiles.html)).

## Example

For example, when executing a query from AWS to BigQuery, it will be as follows.

```python
import aws_ecs_gcp_workload_identity
from google.cloud import bigquery

project_id = 'my-workload-identity'
bqclient = bigquery.Client(project=project_id)

sql = """
SELECT name, age
FROM `my-data-project.my_dataset.my_table`
"""

query_job = bqclient.query(sql)
results = query_job.result()
for row in results:
    print("{}, {}".format(row.name, row.age))
```

## Contribution

1. Fork ([https://github.com/ohsawa0515/aws-ecs-gcp-workload-identity-federation/fork](https://github.com/ohsawa0515/aws-ecs-gcp-workload-identity-federation/fork))
2. Create a feature branch
3. Commit your changes
4. Rebase your local changes against the master branch
5. Create new Pull Request

## License

See [LICENSE](https://github.com/ohsawa0515/aws-ecs-gcp-workload-identity-federation/blob/master/LICENSE).
