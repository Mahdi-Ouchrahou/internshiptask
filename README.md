# internshiptask

The file "alphavantage.py" contains the primary code, it prints the data on the standard otput as a pandas dataframe, it creates both a csv file containing the data and also an "output.parquet" file.

Errors are handled in the code.

#Set up a virtual env (Ubuntu)

0) python3 and pip should be installed
1) Install virtual env: pip install virtualenv
2) Create virtual env: virtualenv name_of_virtenv (once in the local dir of your choice)
3) Actuvate virtualenv: source name_of_virtualenv/bin/activate

#Save your API key as environment variable:
export ALPHAVANTAGE_API_KEY='XXXXXXXXX'
#check API key:
$echo ALPHAVANTAGE_API_KEY



