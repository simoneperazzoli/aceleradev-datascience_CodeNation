# Probability functions

In this challenge we will practice our skills in probability and statistics, which are fundamentals for any data scientist.

## Goal

The here is to explore the main functions about probability distributions such as PDF, CDF and quantiles and the relationships between the normal and the binomial distributions.

Here  _data set_ [Pulsar Star](https://archive.ics.uci.edu/ml/datasets/HTRU2) (Dr. Robert Lyon from Manchester University) will be our case.

 _data set_ contains 16,259 spurious examples caused by RFI/noise, and 1,639 real pulsar examples. 
It contains 8 continuous variables, and a single class variable. The first four are simple statistics obtained from the integrated pulse profile (folded profile). This is an array of continuous variables that describe a longitude-resolved version of the signal that has been averaged in both time and frequency (see [3] for more details). The remaining four variables are similarly obtained from the DM-SNR curve (again see [3] for more details). These are summarised below:

1. Mean of the integrated profile.
2. Standard deviation of the integrated profile.
3. Excess kurtosis of the integrated profile.
4. Skewness of the integrated profile.
5. Mean of the DM-SNR curve.
6. Standard deviation of the DM-SNR curve.
7. Excess kurtosis of the DM-SNR curve.
8. Skewness of the DM-SNR curve.
9. Class 
 

## Topics

* Probability
* Estatistics
* NumPy
* SciPy
* StatsModels

## Requirements

Python 3 and pip. It is highly recommended to use virtual environments with `virtualenv` and the `requirements.txt` file to install the dependency packages for this challenge:

```bash
$ pip3 install virtualenv
$ virtualenv venv -p python3
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Windows

```
bash
> pip3 install virtualenv
> virtualenv ..\venv -p python3
> ..\venv\Scripts\activate
> pip install -r requirements.txt

When you finish your task, you can deactivate your `venv` with: 

```
bash
$ deactivate
```
