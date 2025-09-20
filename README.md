
```
* Tools Required:

  1. Visual Studio Code.
  2. Python
```

```
* Necessary Basic Libraries:

  1. Pandas
  2. Numpy
```
```     
* File handling Libraries

  3. OS module
  4. Pickle
```

```
* Machine Learning Libraries 

  5. Scikit-learn
  6. ML algorithms: DecisionTree Regressor,RandomForest Regressor, XGBRegressor,Linear Regression.
```
```
* Front-End Module for Web application

  7. Streamlit
```

```
Process:

* Load the dataset from the Problem statement(csv files) into the Visual studio code Environment using pandas and os modules.

* Understand the dataset and its features by using df.head and df.info as it has been converted to a dataframe.

* Perform the pre-processing steps on the dataset like Conversion of data types, handlind missing values, dropping the duplicate count, transformation on certain features as per the need.

* Perform feature Engineering to extract relaevant features and create any additional features that may enhance prediction accuracy.

* Perform Exploratory Data analysis using Barplots, scatter plots to understand the relation b/w target feature and remaining features.

* Segregate features into numerical and categorical and further identify outliers using box plots, find the skewness of continuous features and perform encoding.

* Generate a heatmap using corelation matrix and understand the relation among the numerical features.

* Choose an appropriate machine learning model for regression (e.g., linear regression, decision trees, or random forests). Train the model on the historical data, using a portion of the dataset for training.

* Evaluate the model's predictive performance using regression metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), or Root Mean Squared Error (RMSE) and R2 Score.

* Develop a user-friendly web application using Streamlit that allows users to input details of a flat (town, flat type, storey range, etc.). Utilize the trained machine learning model to predict the resale price based on user inputs.

* Deploy the Streamlit application on the Render platform to make it accessible to users over the internet.
  
```


```
Note:

* The pickled files related to encoding, scaler and trained model are available for refernce in the project folder.

* The ipynb-notebook file and py file are uploaded in the Github

* The py file consists of code related to web application and the ipynb file consists of raw data, processed data set in a suitable format and ml models of regression.

* The ML algos predict the Resale prices of flats in Singapore based on the User Inputs like floor_area, remaining_lease(in years),location and flat type.  
