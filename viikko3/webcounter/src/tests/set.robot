
*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
When counter has a nonzero value and it is reset the value becomes zero
    Go To  ${HOME_URL}
    Input Text  name=setValue  10
    Click Button  Aseta
    Page Should Contain  nappia painettu 10 kertaa