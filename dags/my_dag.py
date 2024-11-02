from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

with DAG(
    'my_dag',
    default_args=default_args,
    description='DAG que executa três scripts',
    schedule_interval=None,
) as dag:

    task_1_op = BashOperator(
        task_id='task_1',
        bash_command='python /opt/airflow/scripts/task_1_script.py',
    )

    task_2_op = BashOperator(
        task_id='task_2',
        bash_command='python /opt/airflow/scripts/task_2_script.py',
    )

    task_3_op = BashOperator(
        task_id='task_3',
        bash_command='python /opt/airflow/scripts/task_3_script.py',
    )

    # Definindo a sequência de execução das tasks
    task_1_op >> task_2_op >> task_3_op
