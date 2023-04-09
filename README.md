# Apache StreamPipes for Pythonistas

This repository contains additional material for the talk [`Apache StreamPipes for Pythonistas: IIoT data handling made easy!`](https://pretalx.com/pyconde-pydata-berlin-2023/talk/LXBGZS/) given by [@bossenti](https://www.github.com/bossenti) and [@SvenO3](https://www.github.com/SvenO3) at PyConDE 2023, Berlin.
It contains the following elements:
* Presentation slides
* Material for the first demo
* Material for the second demo

## First Demo - Ingest data (Modbus source)
The first demo comprehends using Apache StreamPipes to ingest data from an IIoT data source,
in this case a Modbus device.
A precondition for that is a running StreamPipes instance.
There are three ways to start/deploy StreamPipes (CLI, Docker Compose, and Kubernetes), of which we recommend using Docker Compose for end users.
All you need to do is run the following command in `installer/compose` within the StreamPipes repository/source code:
```bash
docker-compose -f docker-compose.yaml up -d
```
For more detailed information about how to start StreamPipes, visit our [docs](https://streampipes.apache.org/docs/docs/deploy-docker.html).

The second precondition of this demo is a running Modbus device, which we simulate by using two Python scripts:
* `demo-one/modbus_server.py`: This script runs a Modbus server capable of receiving data from producers and serving as data source
* `demo-one/modbus_data_insert.py`: This script reads data from a given CSV file and publishes it to the given Modbus device.

To run both scripts, you need to ensure that the required dependencies are in place, as specified by `demo-one/requirements.txt.`.
Then you can initialize the Modbus server via executing the following command:
```bash
python demo-one/modbus_server.py
```
The server runs until you terminate the Python process.

In the next step we want to read the data from the file `demo-one/heat_pump.csv` into the Modbus server with the following command:
```bash
python demo-one/modbus_data_insert.py --drop timestamp --file ./demo-one/heat_pump.csv
```
The script publishes one row of the specified CSV file per second and drops all columns specified by the `--drop`flag using `0` as node identifier, when all rows are published it terminates.

Now you can read the data from StreamPipes via a connection to the Modbus server listening on `localhost:5002`.
Be aware that you need to pass `host.docker.internal` as host inside StreamPipes.


## Second Demo - StreamPipes Python