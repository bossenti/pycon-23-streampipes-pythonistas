import click
import pandas as pd
import time
from pymodbus.client.sync import ModbusTcpClient

"""
    short script that writes the values of the flow data frame to Modbus registers
    Each value is updated after one second
"""


@click.command()
@click.option("--file", prompt="File path", help="The CSV file to be read in")
@click.option("--delimiter", default=",", prompt="File delimiter", help="The delimiter used in the CSV file.")
@click.option("--drop", default="", prompt="Columns to drop",
              help="Column names to be dropped from the input data as comma separated string.")
@click.option("--host", default="localhost", prompt="Modbus host", help="Address of the Modbus server.")
@click.option("--wait", default=1, prompt="Waiting period", help="Duration in seconds between emitting data")
def publish_data(file, delimiter, drop, host, wait) -> None:
    # read in flow data from csv
    df_data = pd.read_csv(file, sep=delimiter)

    # convert string of column names to drop in list
    col_to_drop = drop.split(",")

    # drop data that are not of interest for this use case
    df_data.drop(col_to_drop, axis=1, inplace=True)

    # start a Modbus Client on localhost
    client = ModbusTcpClient(host, port=5002)

    # iterate over each row of the data frame
    for idx, row in df_data.iterrows():

        # write each value to the holding register, using another address for each column
        for no, value in enumerate(row):
            client.write_register(no + 1, int(value))

        # wait one second to overwrite values
        time.sleep(int(wait))


if __name__ == "__main__":
    publish_data()

