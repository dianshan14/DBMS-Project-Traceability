# DBMS-Project-Traceability

A simple web site that simulate the management system of product traceability.

## Table of Contents

[TOC]

## Environment

* Operating system : `Ubuntu 16.04`
* Programming language : `Python 3.5.2`
* GUI : web
* Python web framework : `flask`

## Entity-Relationshop diagram

## Relation Schema with third normalization

## Build

1. clone the repository
    `$ git clone https://github.com/e652424342007/DBMS-Project-Traceability.git`
2. create and activate virtual environment
    `$ virtualenv dbms_venv`
    `$ source dbms_venv/bin/activate`
3. install required Python package with pip
    `$ pip install -r requirements.txt`
4. set flask environment
    `$ cd DBMS-Project-Traceability`
    `$ export FLASK_APP=dbms`
    `$ export FLASK_ENV=development`
5. initialize the **sqlite** database
    `$ flask init-schema`
    `$ flask init-data`
    Note: You can use `$ flask` to see what command can be used (at `DBMS-Project-Traceability` directory)
6. lanuch
    `$ flask run`
7. usage
    open your browser and enter URL `127.0.0.1:5000` in your browser's URL bar


## Directory tree
```
.
 ├── dbms
 │   ├── button.py
 │   ├── db.py
 │   ├── default_data
 │   │   ├── Commodity.csv
 │   │   ├── dbms.sqlite
 │   │   ├── Distribute.csv
 │   │   ├── init.py
 │   │   ├── Jobber.csv
 │   │   ├── Manufacturer.csv
 │   │   ├── Market.csv
 │   │   ├── Retailer.csv
 │   │   ├── schema.sql
 │   │   └── Sell.csv
 │   ├── favicon.ico
 │   ├── __init__.py
 │   ├── __pycache__
 │   │   ├── button.cpython-35.pyc
 │   │   ├── db.cpython-35.pyc
 │   │   └── __init__.cpython-35.pyc
 │   ├── schema.sql
 │   ├── static
 │   │   ├── image
 │   │   │   ├── background.png
 │   │   │   ├── background.svg
 │   │   │   ├── background_v.png
 │   │   │   └── SQL-icon-transparent.png
 │   │   └── my.css
 │   └── templates
 │       ├── backup.html
 │       ├── base.html
 │       ├── delete.html
 │       ├── enter.html
 │       ├── insert.html
 │       ├── select.html
 │       ├── sql.html
 │       └── update.html
 ├── Design
 │   ├── Design.png
 │   ├── ERD.xml
 │   └── tree.txt
 ├── instance
 │   └── dbms.sqlite
 ├── README.md
 ├── requirements.txt
 └── tree.txt

```