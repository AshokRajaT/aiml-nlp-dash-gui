from dash_core_components.Markdown import Markdown
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

objectives = html.Div(

    [
        dcc.Markdown('''
            ## Objective
            The aim of this project is to classify the IT tickets generated from end user into their respective assignment groups. Currently many companies
            are manually assigning these tickets to the respective team/groups through their immediate support staff which is time consuming, and prone
            to mistakes. The role of the IT task force is to provide quick turnaround solutions, which defeats the purpose in this case. By using machine
            learning and deep learning techniques mainly in the context of Natural Language Processing framework, we want to develop a sophisticated AI
            or ML technique that can automate this process of assigning correct tickets to the right functional groups within the organisation.

            ## Approach
            The approach and design to counter this issue would be on the guidelines/framework of machine learning flowchart i.e. **Data Loading → Data
            Cleaning →Data Pre-processing →EDA →Model Selection → Model Building-Validation → Model Performance Comparison → Model
            Deployment.**

            ## Text Classification
            The initial data exploration revealed that lot of data cleaning and pre-processing needs to be done to prepare the dataset for model building
            purposes. Thereafter, traditional machine learning models namely Multinomial Naïve Bayes, Linear SVC and Random Forest were built to check
            the benchmark accuracy of these models, as in the context of NLP these were found to be suitable models. Later, simple deep learning model
            such as Dense Neural Network is also explored, which showed a better accuracy than these machine learning models. In the initial stage a
            benchmark accuracy of 70% is achieved with F1 score of 66% with dense neural network. In terms of other models that have been explored
            include LSTM, Bi-directional LSTM models with Glove embeddings, however these models did not surpass the benchmark readings. As a result
            transformers models such as BERT, Roberta, XLnet were used to further develop on the benchmark accuracy & F1 score attained. The transformer
            models showed promising results. These models were also later integrated with GUI to classify the incoming tickets in real-time.

            '''),
    ])

home_content = dbc.Container([objectives], className='inner-box')
