# Facebook Dataset Python (Elasticsearch)

This project is mainly to put the csv dataset in elasticsearch

### Requirements 

Python version = 3.9.0

## Installation

 * Make sure that python is installed in your server or PC, you can follow the instructions in [Python official website](https://www.python.org/downloads/)

 * You need to copy the **constant.example.py** and rename it to **constants.py**

 * You need to set your configuration in **constants.py** file

 * Please make sure to install those libraries

```bash
pip install requests
```

### Objectif

 * Mapping the index that we need
 * Get the the data from the CSV file
 * Index the list in elasticsearch

### **Mapping**

You need to start by mapping the elastic index, this command should run only one time.

#### For Windows

```bash
py -3 mapping.py
```

#### For Ubuntu

```bash
python3 mapping.py
```

### **Indexation**

 * You can run this script manually or put it in a cron that runs each few hours depending on the need.

#### For Windows

```bash
py -3 indexing.py
```

#### For Ubuntu

```bash
python3 indexing.py
```