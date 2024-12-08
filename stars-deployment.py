from prefect import serve
from serve_retrieve_github_stars import retrieve_github_stars  # import your actual flow

if __name__ == "__main__":
  serve(
      retrieve_github_stars,
      name="github-stars-deployment",
      pool_name="default-pool",
      interval="1 minute"  # or cron="0 0 * * *" for daily at midnight
  )