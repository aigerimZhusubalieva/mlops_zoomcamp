from datetime import datetime

from airflow.sdk import dag, task


@dag(
    dag_id="hello_world",
    description="First MLOps Zoomcamp Airflow workflow",
    schedule=None,
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["mlops-zoomcamp"],
)
def hello_world():

    @task
    def say_hello():
        print("Hello from Apache Airflow!")
        return "hello"

    @task
    def say_goodbye(message: str):
        print(f"Received: {message}")
        print("Airflow workflow completed!")

    say_goodbye(say_hello())


hello_world()