# Apache StreamPipes for Pythonistas

This repository contains additional material for the talk [`Apache StreamPipes for Pythonistas: IIoT data handling made easy!`](https://pretalx.com/pyconde-pydata-berlin-2023/talk/LXBGZS/) given by [@bossenti](https://www.github.com/bossenti) and [@SvenO3](https://www.github.com/SvenO3) at PyConDE 2023, Berlin.
It contains the following elements:
* Presentation slides
* Material for the first demo
* Material for the second demo

## First Demo - Ingest data (Modbus source)
The first demo shows how to use Apache StreamPipes to ingest data from an IIoT data source, in this case a Modbus device.
This requires a running StreamPipes instance.
There are three ways to start/deploy StreamPipes (CLI, Docker Compose, and Kubernetes), 
of which we recommend using Docker Compose for end users.
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
python demo-one/modbus_data_insert.py --drop timestamp --file ./data/heat_pump_modbus.csv
```
The script will publish one row of the specified CSV file per second, drop all columns specified by the `--drop' flag using `0' as the node identifier, and terminate when all rows are published.

The data provided in the `data` directory is real data from a heat pump (kudos to [@SvenO3](https://www.github.com/SvenO3) for recording).
Within the this directory, there are two files:
* `..._modbus.csv`: all metrics are multiplied by 100 since modbus can only handle integer values natively (needs to be taken in account when working with the data)
* `..._float.csv`: the very same data but already divided by 100 and therefore in the correct form
* 
Now you can read the data from StreamPipes via a connection to the Modbus server listening on `localhost:5002`.
Be aware that you need to pass `host.docker.internal` as host inside StreamPipes.


## Second Demo - StreamPipes Python
This demo is all about demonstrating how to use the StreamPipes Python library.
All one need to is, to follow the Jupyter notebook in `demo-two`.
There you can see how to setup the StreamPipes client to interact with the API and
to implement a simple StreamPipes Function that allows you to interact with live data.
