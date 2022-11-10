# Forward to the Past
A simple Sales POS program that takes:
As input, a cart in the form of text, separated by line breaks which contain the name of the films purchased
As output, a number representing the total price (taking into consideration current discounts).

- dvd of 1 part of the saga costs 15€
- for the purchase of 2 DIFFERENT parts of the saga, a 10% reduction is applied to all "Back to the Future" DVDs purchased
- for the purchase of 3 DIFFERENT parts of the saga, a 20% reduction is applied to all "Back to the Future" DVDs purchased
- The DVD shop also sells other films which cost 20€ each.

## Installation
To run this locally, you need Python 3.6 or greater installed. It is advisable to create a separate environment before running the following commands
```sh
$ git clone [url]
$ cd /discount-calculator
```
Create and activate a virtual environment for the project with virtualenv or pipenv or other. Then run ..
```sh
$ pip install -r requirements.txt
$ streamlit run "./app/app.py"
```

## Running Tests
```sh
pytest -v
```