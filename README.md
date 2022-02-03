# Azure ML - Many Models Time-Series Forecasting

## Overview

This repo contains a sample notebook for constructing an Azure ML many models pipeline to:
* Retrieve data from an AML-registered Datastore and split into multiple  hierarchical time-series
* Train a forecasting model for each unique time-series using AutoML
* Generate forecasts for each unique time-series using its best performing model
* Register forecasted data as an AML dataset in the default datastore.

The data used in this sample was taken from the [OJ Sales Simulated Dataset](https://docs.microsoft.com/en-us/azure/open-datasets/dataset-oj-sales-simulated?tabs=azureml-opendatasets) made available as part of [Azure's Open Datasets](https://docs.microsoft.com/en-us/azure/open-datasets/overview-what-are-open-datasets).

This sample repo is adapted from [Microsoft's Many Models Solution Accelerator developed and supported by the AML product team](https://github.com/microsoft/solution-accelerator-many-models).

## Prerequisites

To run the code included in this repo you must have access to an [Azure Machine Learning](https://azure.microsoft.com/en-us/services/machine-learning/) workspace. Details on provisioning an AML workspace can be found [here](https://docs.microsoft.com/en-us/azure/machine-learning/quickstart-create-resources).

## Getting Started

To begin, clone this repository to your local machine, sign into the Azure portal, and then navigate to your Azure Machine Learning workspace.

![AML Workspace](img/01.png?raw=true "AML Workspace")

Once inside your AML workspace, click the <i>Datasets</i> button along the left rail.

![Datasets](img/02.png?raw=true "Datasets")

From the Datasets tab click the <i>+ Create dataset</i> dropdown and select <i>From local files</i>.

![Create Dataset](img/03.png?raw=true "Create Dataset")

When prompted, name your dataset `OJ-Sales-Data` and leave the Dataset type selection set to Tabular. Then click <i>Next</i>.

![Specify Dataset Name](img/04.png?raw=true "Specify Dataset Name")

In the next tab, leave workspaceblobstore selected as the default datastore and then browse to and select the `./sample_data/OJ_SalesData_10Stores.csv` file located on your local machine. Leave 'Skip data validation' unchecked and click <i>Next</i>.

![Upload Local Data](img/05.png?raw=true "Upload Local Data")

Leave all default values set under the Settings and preview tab. Your window should look similar to what is shown below. Click <i>Next</i>.

![Settings and Preview](img/06.png?raw=true "Settings and Preview")

Leave all default settings under the Schema panel and click <i>Next</i>.

![Schema](img/07.png?raw=true "Schema")

Finally click <i>Create</i>.

![Create Dataset](img/08.png?raw=true "Create Dataset")

From the left rail, click into the Compute panel and under Compute instances click <i>+ New</i>.

![Create Compute Instance](img/09.png?raw=true "Create Compute Instance")

From the Create compute instance window, leave the default settings selected and click <i>Create</i>.

![Create Compute Instance](img/10.png?raw=true "Create Compute Instance")

After your compute instance is created click on the <i>JupyterLab</i> hyperlink - this will open a new instance of JuptyerLab in a separate browser tab.

![Launch JupyterLab](img/11.png?raw=true "Launch JupyterLab")

Inside JupyterLab click the <i>Terminal</i> icon from the launcher panel to open a new terminal.

![Open Terminal](img/12.png?raw=true "Open Terminal")

Execute the following lines in your terminal:
```
cd Users/<YOUR-USERNAME>/
git clone https://github.com/nickwiecien/AzureML_ManyModels_Forecasting
```
This will clone the contents of this repository including AML pipeline creation notebooks into your compute instance.

![Clone Repo](img/13.png?raw=true "Clone Repo")

Open the notebook located at `Users/<YOUR-USERNAME>/AzureML_ManyModels_Forecasting/AML_ManyModelsPipeline.ipynb`. 

![Open Pipeline Creation Notebook](img/14.png?raw=true "Open Pipeline Creation Notebook")

Execute the cells in the notebook one-by-one by clicking into the cell and entering `Ctrl+Enter` or by navigating the <i>Run</i> menubar item and selecting <i>Run All cells</i>.

![Run Notebook Cells](img/15.png?raw=true "Run Notebook Cells")