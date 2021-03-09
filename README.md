
# Employee Retention Model Pipeline
This project is the creation of a pipeline and accompanying API for a model designed to assess the retention level of new employees, based on experience and demographic characteristics of said employee.

## Dataset
This dataset is from the Kaggle [HR Analytics: Job Change of Data Scientists](https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists). It consists if records on employees demographics & experience, as well as their company retention.

### Task
The dataset will be used to build a ML pipeline and accompanying API for assessing new employees and their likely retention levels.

### Access
The dataset was uploaded to Azure's dataset repository, and is accessed through that.

## Automated ML
An AutoML run was conducted for this model, consisting of a classification, metriced against a weighted AUC.

### Results
The resulting model consisted of a voting classifier, with an L2 penalty and 100 max iterations.

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
HyperDrive was used on a logistic regression model, tuning the L1, L2, and max iteration inputs, and targeting accuracy.

### Results
The resulting model consisted of

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
