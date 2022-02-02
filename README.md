# Azure ML - Many Models Time-Series Forecasting

This repo contains a sample notebook for constructing an Azure ML many models pipeline to...
* Retrieve data from an AML-registered Datastore and split into multiple  hierarchical time-series
* Train a forecasting model for each unique time-series using AutoML
* Generate forecasts for each unique time-series using its best performing model
* Register forecasted data as an AML dataset in the default datastore.

This sample repo is adapted from [Microsoft's Many Models Solution Accelerator developed and supported by the AML product team](https://github.com/microsoft/solution-accelerator-many-models).