from prefect_azure.repositories import AzureRepository

git_block = AzureRepository(
    repository="https://dev.azure.com/tysonium/versana-sandbox/_git/prefect-flows",
    reference="main"
)

git_block.save("azure-devops", overwrite=True)