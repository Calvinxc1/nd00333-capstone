
# Employee Retention Model Pipeline
This project is the creation of a pipeline and accompanying API for a model designed to assess the retention level of new employees, based on experience and demographic characteristics of said employee. This will involve building models through the Azure Automl process, as well as building a logistic regression model with tuned Hyperparameters via Azure HyperDrive. A final model will be selected from these options and deployed to Azure, with a REST API endpoint for model consumption.

## Dataset
This dataset is from the Kaggle [HR Analytics: Job Change of Data Scientists](https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists). It consists if records on employees demographics (gender, education, etc.) & prior experience, as well as their company retention. In total there are 13 features (plus an ID column) for each employee.

### Task
The dataset will be used to build a ML pipeline and accompanying API for assessing new employees and their likely retention levels. As such a classification model is constructed.

### Access
The dataset was uploaded to Azure's dataset repository, and is accessed through that for the AutoML process. It is accessed through this Github repo for the HyperDrive process.

## Automated ML
The AutoML process was specified for a classification task on the dataset as uploaded to Azure ML. Early stoping was enabled, with automatic featurization, for convenience. Maximum concurrent iterations was set to 5, one less than the maximum nodes of the compute cluster that the AutoML model was run on, and accuracy was set as the primary metric.

AutoML Run:
![automl run](./images/AutomlRunStatus.jpg)

### Results
Best AutoML result:
![automl best](/.images/AutomlBestModel.jpg)
The best model was the Voting Ensemble model, with an accuracy of 0.799. Interestingly enough this seems to often be the best model type to use.

## Hyperparameter Tuning
HyperDrive was used on a logistic regression model, tuning the L2, and max iteration inputs, and targeting accuracy.

HyperDrive Run:
![hyperdrive run](./images/HyperdriveRunStatus.jpg)

L2 was randomly sampled using a uniform distribution across the 0.1 to 1.0 range, with the value being the inverse of the true regularization parameter. Maximum iterations was randomly sampled from a choice of four values: 10, 25, 35, and 50.

### Results
HyperDrive Best result:
![hyperdrive best](./images/HyperdriveBestModel.jpg)
The resulting models from the Hyperparameter tuning ended up with identical accuracy values. As unusual as this is, I believe it can be explained with a regularization value that is too high. Increasing the `C` parameter should help this (since it is inverse of the regularization parameter). I decided against this however, as AutoML produced a superior model.

## Model Deployment
The model is deployed with a REST endpoint, needing proper authentication, and can be called with the 'ExperimentName' parameter in a `POST` request set to `ds_header_retention`.

Deployed Model:
[!endpoint](./images/EndpointSuccess.jpg)

## Screen Recording
Screencast video: [https://www.youtube.com/watch?v=OdYLE9z6RGg](https://www.youtube.com/watch?v=OdYLE9z6RGg).

# Future Improvements
The dataset was not processed very rigorously. Engineering across some of the existing features would likely yield effective results. This would be supported by an effective exploratory analysis.

Additionally, the seperate use of AutoML and HyperDrive is inefficent. A more optimal way of identifying the best model would be to use AutoML to identify a model, then to take the resulting model and run its Hyperparameter through HyperDrive.
