from prefect import flow, task
from time import sleep

@task(log_prints=True)
def print_string(string):
    print(string)

@task(log_prints=True)
def sleep_num(num):
    sleep(num)

@flow(log_prints=True)
def retrieve_github_stars():
    print_string("I'm so tired...")
    sleep_num(1)
    for i in range(10):
        print_string("zzzzz...")
        sleep_num(3)