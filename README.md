# Promo codes generator

## Description 

This is the test task app that described in the [python-mid-tz.md](python-mid-tz.md) file (in Russian)
This app generate random codes and write them in JSON-file. 

## Installation

open terminal and run the following commands:

```shell script
git clone https://github.com/smokevadim/promo_gen.git
cd promo_gen
pip install -r requirements.txt
```

## Usage

Example 1 (create codes)

```shell script
python manage.py gen --amount="10" --group="Test group"
python manage.py gen -a="1" -g="Test group 2"
```
Return "Codes generates successful" when done.

Example 2 (check code)

```shell script
python manage.py chk --code="soNVuFJ"
python manage.py chk -c="soNVuFJ"
```
 Return "True" and name of group.

 
## Tests

```
python manage.py test
```

## Tech stack 

* Python 3.8: https://www.python.org/
* Django: https://docs.djangoproject.com/en/3.1/
* Django management commands: https://habr.com/ru/post/415049/ 

