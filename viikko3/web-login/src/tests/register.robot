*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Register  kalle2  kalle123  kalle123
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Register  ka  kalle123  kalle123
    Page Should Contain  Username should have at least 3 characters

Register With Valid Username And Too Short Password
    Register  kalle2  kal  kal
    Page Should Contain  Password should have at least 8 characters

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
# esim. vain isoja kirjaimia
    Register  kalle2  KALLEKALLE  KALLEKALLE
    Page Should Contain  Password should have at least one number

Register With Nonmatching Password And Password Confirmation
    Register  kalle2  kalle123  kalle1234
    Page Should Contain  Password and password confirmation do not match

Register With Username That Is Already In Use
    Register  kalle  kalle321  kalle321
    Page Should Contain  Username is already in use

Login After Successful Registration
    Register  kalle2  kalle123  kalle123
    Welcome Page Should Be Open
    Click Link  Continue to main page
    Click Link  Logout
    Login Page Should Be Open
    Input Text  id=username  kalle2
    Input Text  id=password  kalle123
    Click Button  Login
    Welcome Page Should Be Open

Login After Failed Registration
    Register  kalle2  kala  kala
    Click Link  Login
    Login Page Should Be Open
    Input Text  id=username  kalle2
    Input Text  id=password  kala
    Click Button  Login
    Page Should Contain  Invalid username or password

*** Keywords ***

Register
    [Arguments]  ${username}  ${password}  ${password_confirmation}
    Input Text  id=username  ${username}
    Input Text  id=password  ${password}
    Input Text  id=password_confirmation  ${password_confirmation}
    Click Button  Register

Welcome Page Should Be Open
    Page Should Contain  Welcome to Ohtu Application!

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
