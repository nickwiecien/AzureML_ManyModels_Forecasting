# Import required packages
from azureml.core import Run, Workspace, Datastore, Dataset
from azureml.data.datapath import DataPath
import pandas as pd
import os
import argparse
from sklearn import preprocessing
import numpy as np

#Parse input arguments
parser = argparse.ArgumentParser("Get tabular data from attached datastore, split into separate files, and register as file dataset in AML workspace")
parser.add_argument('--train_dataset', dest='train_dataset', required=True)
parser.add_argument('--forecast_dataset', dest='forecast_dataset', required=True)
parser.add_argument('--source_dataset_name', type=str, required=True)
parser.add_argument('--group_column_names', type=str, required=True)
parser.add_argument('--timestamp_column', type=str, required=True)
parser.add_argument('--cutoff_date', type=str, required=True)

args, _ = parser.parse_known_args()
train_dataset = args.train_dataset
forecast_dataset = args.forecast_dataset
source_dataset_name = args.source_dataset_name
group_column_names = args.group_column_names.split(';')
timestamp_column = args.timestamp_column
cutoff_date = args.cutoff_date

#Get current run
current_run = Run.get_context()

#Get associated AML workspace
ws = current_run.experiment.workspace

#Connect to default Blob Store
ds = ws.get_default_datastore()

#Read dataset from AML Datastore
source_dataset = Dataset.get_by_name(ws, name=source_dataset_name)
source_df = source_dataset.to_pandas_dataframe()

grouped_dfs = source_df.groupby(group_column_names)

# Make directory on mounted storage for output dataset
os.makedirs(train_dataset, exist_ok=True)
os.makedirs(forecast_dataset, exist_ok=True)

for idx, new_df in grouped_dfs:
    train_filename = "_".join([str(x) for x in list(idx)]) + "_train.csv"
    forecast_filename = "_".join([str(x) for x in list(idx)]) + "_forecast.csv"
    before_split_date = new_df[timestamp_column] < cutoff_date
    train_df, forecast_df = new_df[before_split_date], new_df[~before_split_date]
    
    train_df.to_csv(os.path.join(train_dataset, train_filename), index=False)
    forecast_df.to_csv(os.path.join(forecast_dataset, forecast_filename), index=False)