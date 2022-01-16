[![PyPi downloads](https://img.shields.io/pypi/dm/robotframework-soaplibrary.svg)](https://pypi.org/project/robotframework-soaplibrary)
[![Total downloads](https://static.pepy.tech/personalized-badge/robotframework-soaplibrary?period=total&units=international_system&left_color=lightgrey&right_color=yellow&left_text=Total)](https://pypi.org/project/robotframework-soaplibrary)
[![Latest Version](https://img.shields.io/pypi/v/robotframework-soaplibrary.svg)](https://pypi.org/project/robotframework-soaplibrary)
[![SOAP-Library](https://github.com/SanthoshS20/Robot-Framework-SOAP-Library/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/SanthoshS20/Robot-Framework-SOAP-Library/actions/workflows/python-app.yml)


# Robot-Framework-SOAP-Library
SOAP Library for Robot Framework

## Compatibility
- _Python 2.7_
- _Python 3.7_
- _Zeep 3.1.0_ (or higher)

## Introduction
The SoapLibrary was created for those who want to use the Robot Framework as if they were using SoapUI, just send the request XML and get the response XML.

![alt text](https://github.com/Altran-PT-GDC/Robot-Framework-SOAP-Library/blob/master/Doc/img_SoapUI.png)

![alt text](https://github.com/Altran-PT-GDC/Robot-Framework-SOAP-Library/blob/master/Doc/img2_SoapLibrary.png)

## Instalation
`pip install robotframework-soaplibrary`

## Example

    *** Settings ***
    Library           SoapLibrary
    Library           OperatingSystem

    *** Test Cases ***
    Example
        Create Soap Client    http://endpoint.com/example.asmx?wsdl
        ${response}    Call SOAP Method With XML    ${CURDIR}/request.xml
        ${text}    Get Data From XML By Tag    ${response}    tag_name
        Log    ${text}
        Save XML To File    ${response}    ${CURDIR}    response_test
        
## Keyword Documentation

You can find the keywords documentation [here](https://raw.githack.com/Altran-PT-GDC/Robot-Framework-SOAP-Library/master/Doc/SoapLibrary.html)

## Development setup

Start off by forking this repository and pulling the source code from GitHub.

Depending on your preferences, you can create a virtual environment to
keep system and project dependencies separate.

`python -m venv .venv`

To activate the virtual environment,
run `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (MacOS & Linux).

Install main and development dependencies by running `python -m pip install -r requirements-dev.txt`

This project is using [invoke](https://www.pyinvoke.org/) as task runner. Before pushing your code, make sure python and robot code is formatted by running `inv lint`.

To run acceptance tests, run `inv test`.

## Authors
   - **Altran -** [Altran Web Site](https://www.altran.com/us/en/)
   - **Samuel Cabral**
   - **Joao Gomes**
   
## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/Altran-PT-GDC/Robot-Framework-SOAP-Library/blob/master/LICENSE.md) file for details.   
