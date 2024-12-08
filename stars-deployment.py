from prefect import serve, deploy
from serve_retrieve_github_stars import retrieve_github_stars  # import your actual flow

if __name__ == "__main__":
    deployment = deploy(
        retrieve_github_stars,
        name="github-stars-deployment",
        pool="default-pool",
        interval="1 minute"
    )