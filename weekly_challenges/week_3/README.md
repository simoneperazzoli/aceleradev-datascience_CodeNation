# Knowing our consumers: which state has the customers with the best credit scores?

## Goal

We want to know our customers better by their local. For this, we started by analyzing the credit score data.
To perform it, we need some get values: mean, median, mode, and standard deviation for credit score.

## Topics

With this challenge, you will learn:

- Mean;
- Median;
- Mode;
- Standard deviation.

## Requirements:

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

## Observations

The answer must contain the values of the mean, median, mode and standard deviation of the credit score for each local state in the dataset.
The file for submission must be in json format, according to the example file "submission.json".


Data info:
'id': customer ID
'sobrenome': customer surname
'pontuacao_credito': customer score (as higher, better)
'estado_residencia': local (state) of client residence
'genero': customer genre
'nivel_estabilidade': customer economic stability
'saldo_conta': customer account balance available
'numero_produtos': products consumed by customer
'possui_cartao_de_credito': credit card register
'membro_ativo': customer activity

Obs: The data are fictitious, but try to represent the reality of a customer base for a SaaS product. 




