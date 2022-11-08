### Portfolio App
This is the culmination of work from the entire course.

To run this code:
```
python3 print-report.py portfolio.csv prices.csv txt
```
Note: 'txt' can be replaced with 'csv' or 'html'

To create a distribution:
```
python setup.py sdist
```
This will create a .tar.gz or .zip file.

To install your code:
```
python -m pip install porty-0.0.1.tar.gz
```

In the future, I would like to take parts of the code from here to write a data pipeline that takes in stock portfolio data from somewhere and stores it into a DB or in the cloud.