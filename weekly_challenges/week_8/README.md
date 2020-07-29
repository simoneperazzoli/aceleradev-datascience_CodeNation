# Discover the best math scores of the ENEM 2016

You will create a model to predict the score of the math test for those who participated of the ENEM 2016. For this, you will use Python, Pandas, Sklearn and Regression.


## Topics

- Python
- Pandas
- Sklearn
- Regression

## Requirements

Python 3 and pip. It is highly recommended to use virtual environments with `virtualenv` and the `requirements.txt` file to install the dependency packages for this challenge:

```bash
$ pip3 install virtualenv
$ virtualenv venv -p python3
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Windows

```bash
> pip3 install virtualenv
> virtualenv ..\venv -p python3
> ..\venv\Scripts\activate
> pip install -r requirements.txt
```
When you finish your task, you can deactivate your `venv` with: 

```bash
$ deactivate
```

## Context

This dataset was downloaded from INEP, a department from the Brazilian Education Ministry. It contains data from the applicants for the 2016 National High School Exam. Inside this dataset there are not only the exam results, but the social and economic context of the applicants.
Check here data for description: [Enem 2016 Microdata](https://s3-us-west-1.amazonaws.com/acceleration-assets-highway/data-science/dicionario-de-dados.zip).

You will have two datasets - train.csv e test.csv - for using to predict math scores (`NU_NOTA_MT`). But the train file is a good amount of data from ENEM 2016 and contains most of the columns for those who would like to do some EDA.

Your answer should be stored in a .csv file 'answer.csv' containing two columns: `NU_INSCRICAO` and `NU_NOTA_MT`.

