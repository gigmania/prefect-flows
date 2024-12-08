from prefect import serve
from serve_retrieve_github_stars import retrieve_github_stars  # import your actual flow

serve(
    retrieve_github_stars,
    name="github-stars-deployment",
    work_pool_name="default-pool",
    interval="1 minute"  # or cron="0 0 * * *" for daily at midnight
)