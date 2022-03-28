# Introduction
This is a pet-project of API-REST-Testing automation framework with Python, requests, Pytest, Allure, Gitlab CI.

Testing website: https://automationexercise.com/

# Files

**/utils**
- assertions.py — contains assertion functions
- print_helper.py — contains custom print function 
- request_helper.py — contains class that wrap requests methods

**/tests**
- conftest.py — contains the fixture that is used by tests
- test_account_actions.py — contains API tests for account actions
- test_products_actions.py — contains API tests for products actions

**/testdata**
- testdata.py — contains data that is used while tests execution

**/allure-results** — default Allure directory. Can be changed via --alluredir="dir_name" command
- categories.json — file that fills the "categories" section in Allure report

**pytest.ini** — configuration file. Contains pytest launch options

**requirements.txt** — requirements file

**.gitlab-ci.yml** — yaml file that contains instructions for gitlab-runner

# Prerequisites

1. Install all requirements:

```bash
pip install -r requirements.txt
```

2. To generate Allure reports install Allure:

https://docs.qameta.io/allure/#_installing_a_commandline

# How to run

Quickrun all the tests in the directory:

    pytest

Specify launch options in **pytest.ini** file and/or using command line.

Pytest documentation can be found at https://docs.pytest.org/

# Make an Allure report

If tests were run with --alluredir="allure-results" option, it is possible to generate an Allure report:

    allure serve allure-results

Allure documentation can be found at https://docs.qameta.io/allure/

# Gitlab CI

A pipline contains 4 jobs:
- Testing in a Docker container
- Coping history from the last pipline
- Making an allure report
- Pushing an allure report at Gitlab Pages

Allure report available at Gitlab Pages: 
https://kozlovartemq.gitlab.io/API-REST-Testing/# 

# List of test APIs
1. _Get All Products List_
   - **API URL**: https://automationexercise.com/api/productsList
   - **Request Method**: GET
   - **Response Code**: 200
   - **Response JSON**: All products list
2. _POST To All Products List_
   - **API URL**: https://automationexercise.com/api/productsList
   - **Request Method**: POST
   - **Response Code**: 405
   - **Response Message**: This request method is not supported.
3. _Get All Brands List_
   - **API URL**: https://automationexercise.com/api/brandsList
   - **Request Method**: GET
   - **Response Code**: 200
   - **Response JSON**: All brands list
4. _PUT To All Brands List_
   - **API URL**: https://automationexercise.com/api/brandsList
   - **Request Method**: PUT
   - **Response Code**: 405
   - **Response Message**: This request method is not supported.
5. _POST To Search Product_
   - **API URL**: https://automationexercise.com/api/searchProduct
   - **Request Method**: POST
   - **Request Parameter**: search_product (For example: top, tshirt, jean)
   - **Response Code**: 200
   - **Response JSON**: Searched products list
6. _POST To Search Product without search_product parameter_
   - **API URL**: https://automationexercise.com/api/searchProduct
   - **Request Method**: POST
   - **Response Code**: 400
   - **Response Message**: Bad request, search_product parameter is missing in POST request.
7. _POST To Verify Login with valid details_
   - **API URL**: https://automationexercise.com/api/verifyLogin
   - **Request Method**: POST
   - **Request Parameters**: email, password
   - **Response Code**: 200
   - **Response Message**: User exists!
8. _POST To Verify Login without email parameter_
   - **API URL**: https://automationexercise.com/api/verifyLogin
   - **Request Method**: POST
   - **Request Parameter**: password
   - **Response Code**: 400
   - **Response Message**: Bad request, email or password parameter is missing in POST request.
9. _DELETE To Verify Login_
   - **API URL**: https://automationexercise.com/api/verifyLogin
   - **Request Method**: DELETE
   - **Response Code**: 405
   - **Response Message**: This request method is not supported.
10. _POST To Verify Login with invalid details_
    - **API URL**: https://automationexercise.com/api/verifyLogin
    - **Request Method**: POST
    - **Request Parameters**: email, password (invalid values)
    - **Response Code**: 404
    - **Response Message**: User not found!
11. _POST To Create/Register User Account_
    - **API URL**: https://automationexercise.com/api/createAccount
    - **Request Method**: POST
    - **Request Parameters**: name, email, password, title (for example: Mr, Mrs, Miss), birth_date, birth_month, birth_year, firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number
    - **Response Code**: 201
    - **Response Message**: User created!
12. _DELETE METHOD To Delete User Account_
    - **API URL**: https://automationexercise.com/api/deleteAccount
    - **Request Method**: DELETE
    - **Request Parameters**: email, password
    - **Response Code**: 200
    - **Response Message**: Account deleted!
13. _PUT METHOD To Update User Account_
    - **API URL**: https://automationexercise.com/api/updateAccount
    - **Request Method**: PUT
    - **Request Parameters**: name, email, password, title (for example: Mr, Mrs, Miss), birth_date, birth_month, birth_year, firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number
    - **Response Code**: 200
    - **Response Message**: User updated!
14. _GET user account detail by email_
    - **API URL**: https://automationexercise.com/api/getUserDetailByEmail
    - **Request Method**: GET
    - **Request Parameters**: email
    - **Response Code**: 200
    - **Response JSON**: User Detail
15. _GET user account detail by invalid email_
    - **API URL**: https://automationexercise.com/api/getUserDetailByEmail
    - **Request Method**: GET
    - **Request Parameters**: email (invalid value)
    - **Response Code**: 404
    - **Response Message**: Account not found with this email, try another email!
