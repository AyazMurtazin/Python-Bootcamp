## Preparation:

    python3 -m venv venv

    source venv/bin/activate

    pip install -r requirements.txt

## Task 00:

    console 1: 'python3 reporting_server.py'

    console 2: 'python3 reporting_client.py 17 45 40.0409 -29 00 28.118'

## Task 01:

    console 1: 'python3 reporting_server.py'

    console 2: 'python3 reporting_client.py 17 45 40.0409 -29 00 28.118'

## Task 02:

    console 1: 'python3 reporting_server.py'

    console 2: 'python3 reporting_client.py scan 17 45 40.0409 -29 00 28.118'

    console 2: 'python3 reporting_client_v3.py list_traitors'


## grpc compilation:

    python3 -m grpc_tools.protoc -I protos --python_out=./protos --grpc_python_out=./protos protos/spaceship/proto 

    Нужно будет вручную изменить пути импорта в spaceship_pb2_grpc.py(import protos.spaceship_pb2 as spaceship__pb2)

## Description

    Для проверки работоспособности task02 есть тестовая база. Для этого нужно задать в файле reporting_client_v3.py db_creator.create_database(True).

    Для проверки работы pydantiс нужно запустить файл с моделями.

    
