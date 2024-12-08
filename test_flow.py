from prefect import flow, task

@task
def say_hello(name):
    print(f"Hello {name}!")
    return name

@flow
def my_test_flow(name="world"):
    result = say_hello(name)
    return result

if __name__ == "__main__":
    my_test_flow()
    