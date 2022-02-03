import pandas as pd
import os
import datetime
import argparse

# Parse input arguments
parser = argparse.ArgumentParser("parallel run step results directory")
parser.add_argument("--result_dataset", dest='result_dataset', required=True)
parser.add_argument("--forecast_output_dir", type=str, required=True)


args, _ = parser.parse_known_args()
result_dataset = args.result_dataset
forecast_output_dir = args.forecast_output_dir

automl_result_file = os.path.join(forecast_output_dir, 'parallel_run_step.txt')

# Load results from AutoML inferencing step into a Pandas dataframe
df_results = pd.read_csv(automl_result_file, delimiter=" ")

# Create output directory
os.makedirs(args.result_dataset, exist_ok=True)

# Save final dataframe to ./outputs dir
df_results.to_csv(os.path.join(result_dataset, 'forecasting_results.csv'), index=False)