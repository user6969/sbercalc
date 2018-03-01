## Sberbank online currency converter - testing exercise

Sample approach to testing http://sberbank.ru/ru/quotes/converter using WebDriver, Pytest, and test parametrization via CSV file.

#### Test scenarios:
1. Calculator testing - test whether calculator returns correct values
2. UI testing - test whether buttons/links etc work as as expected
3. semi-API testing - test whether JSON response returns expected result

##### Parametrization 
https://github.com/user6969/sbercalc/blob/master/test_artifacts/currency.csv

##### Possible improvements:
1. Wrap utils.py functions in try/catch for error handling
2. Implement logging
