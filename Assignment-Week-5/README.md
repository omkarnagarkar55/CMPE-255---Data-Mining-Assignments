# Data Preparation and Processing Assignment

Welcome to the Week 5 assignments for the CMPE-255 Data Mining course. This week, we delve into various data types and their analysis. Below are the notebooks detailing each type:

### Medium Article 
<a target="_blank" href="https://medium.com/@omkarnagarkar53/leveraging-gpt-4-for-rapid-data-science-analysis-a-comprehensive-dive-across-diverse-datasets-c95a71c5cfc6">
    <img src="https://cdn.iconscout.com/icon/free/png-512/medium-47-569287.png" alt="Medium Article">
</a>


## Notebooks:

1. **Tabular Diverse Set Analysis** - [Tabular_Diverse_Set.ipynb](a.Tabular_Diverse_Set.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/omkarnagarkar55/CMPE-255---Data-Mining-Assignments/blob/main/Assignment-Week-5/a.Tabular_Diverse_Set.ipynb)
   - Description: Dive into the analysis of diverse tabular datasets and understand their characteristics.

2. **Time Series Analysis** - [Timeseries.ipynb](b.Timeseries.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/omkarnagarkar55/CMPE-255---Data-Mining-Assignments/blob/main/Assignment-Week-5/b.Timeseries.ipynb)
   - Description: Explore the intricacies of time series data and its patterns.

3. **Spatio-Temporal Data Analysis** - [Spatio_Temporal.ipynb](c.Spatio_Temporal.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/omkarnagarkar55/CMPE-255---Data-Mining-Assignments/blob/main/Assignment-Week-5/c.Spatio_Temporal.ipynb)
   - Description: Analyze spatio-temporal datasets and uncover hidden insights.

4. **CIFAR10 Image Analysis** - [CIFAR10_Image_Analysis.ipynb](d.CIFAR10_Image_Analysis.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/omkarnagarkar55/CMPE-255---Data-Mining-Assignments/blob/main/Assignment-Week-5/d.CIFAR10_Image_Analysis.ipynb)
   - Description: Dive deep into the CIFAR10 image dataset and understand image data mining techniques.

5. **Audio Classification** - [Audio_Classification.ipynb](e.Audio_Classification.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/omkarnagarkar55/CMPE-255---Data-Mining-Assignments/blob/main/Assignment-Week-5/e.Audio_Classification.ipynb)
   - Description: Explore the world of audio data and techniques to classify different sounds.

6. **Video Classification** - [Video_Classification.ipynb](f.Video_Classification.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/omkarnagarkar55/CMPE-255---Data-Mining-Assignments/blob/main/Assignment-Week-5/f.Video_Classification.ipynb)
   - Description: Understand the nuances of video data and methods to classify various video clips.

7. **Graph Data Set Analysis** - [Graph_Data_Set.ipynb](g.Graph_Data_Set.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/omkarnagarkar55/CMPE-255---Data-Mining-Assignments/blob/main/Assignment-Week-5/g.Graph_Data_Set.ipynb)
   - Description: Delve into graph datasets and understand their unique properties.

## Getting Started:

To get started with the notebooks, ensure you have Jupyter Notebook installed. Clone the repository and navigate to the "Assignment-Week-5" directory. Open the desired notebook and run the cells sequentially.

## Dependencies:

The following are the required dependencies for the notebooks in this repository:

1. **Python 3.9** - Ensure you have Python 3.9 installed. If not, download and install it from the official Python website.
2. **Pycaret** - Installation: pip install pycaret.
3. **Sweetviz** - Installation: pip install sweetviz
4. **Tensorflow and Keras** - Installation for Tensorflow: pip install tensorflow . Installation for Keras: pip install keras
5. **h2o** - Installation: pip install h2o

To install all the dependencies at once, you can use the following command:
```
pip install pycaret sweetviz tensorflow keras h2o
```

## Steps followed For Each Dataset :

1. **Exploratory Data Analysis (EDA)**:
    For each dataset:
    
    a) Load the data.
    b) Check for missing values.
    c) Visualize distributions of key features.
    d) Check for correlations between features.
    e) Use auto EDA tools like pandas-profiling or sweetviz for detailed reports.

2. **Data Preprocessing**:
    a) Cleaning:
    
        * Handle missing values (imputation or removal).
        * Remove duplicates.
        * Handle outliers (using IQR, Z-score, etc.).
    
    b) Feature Engineering:
        * Create new features based on domain knowledge.
        * Convert categorical variables to numerical (one-hot encoding, label encoding).
        * Normalize/standardize numerical features.
    
    c) Feature Selection:
        * Use techniques like Recursive Feature Elimination (RFE), feature importance from tree-based models, or correlation analysis.
        
    d) Clustering and Anomaly Detection:
        * Use algorithms like KMeans, DBSCAN for clustering.
        * Use Isolation Forest, One-Class SVM for anomaly detection.
    
3. **Model Building**:
    a) Split data into training and test sets.
    b) Use AutoML platforms like Azure ML, AWS Sagemaker, or tools like TPOT to automatically select the best model.
    c) Build ensemble models like Random Forest, Gradient Boosting, or stacking of different models.
