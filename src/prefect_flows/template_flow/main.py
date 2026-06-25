from time import sleep

from prefect import task
from rpacore import WorkflowConfig, workflow


@task(tags=["sap"])
def fetch_batch():
    # Simulate fetching a batch of data
    sleep(30)


@workflow(
    config_path=r"C:\Users\fnx\Desktop\kohls_export_so_creation.yaml",
)
def hello_world(config: WorkflowConfig):
    fetch_batch()
