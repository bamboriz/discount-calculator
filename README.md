# Forward to the Past
A simple Sales POS program that takes:
As input, a cart in the form of text, separated by line breaks which contain the name of the films purchased
As output, a number representing the total price (taking into consideration current discounts).

- dvd of 1 part of the saga costs 15€
- for the purchase of 2 DIFFERENT parts of the saga, a 10% reduction is applied to all "Back to the Future" DVDs purchased
- for the purchase of 3 DIFFERENT parts of the saga, a 20% reduction is applied to all "Back to the Future" DVDs purchased
- The DVD shop also sells other films which cost 20€ each.

# Environment setup

Ideal OS: **Ubuntu 20.04**   
Ideal Python version: **Python 3.8**


## Installation

Create and activate a virtual environment for the project with virtualenv or pipenv or other

## With conda [Anaconda]
- Create a new virtual environment  
    ```sh $
    conda create -n <env_name> python=3.8
    ```
- Activate the conda environment  
    ```sh $
    conda activate <env_name>
    ```


## With Virtualenv
- Create a new virtual environment  
    ```sh $
    python3 -m venv <env_name>
    ```
- Activate the virtual environment  
    ```sh $
    source <env_name_absolute_path>/bin/activate
    ```


To run this locally, you need Python 3.6 or greater installed. It is advisable to create a separate environment before running the following commands
```sh
$ git clone https://github.com/bamboriz/discount-calculator.git
$ cd /discount-calculator
```
```sh
$ pip install -r requirements.txt
$ streamlit run "app.py"
```

Navigate to the url that is displayed on your terminal

## Running Tests
```sh
pytest -v
```
<img src="/assets/tests.png">