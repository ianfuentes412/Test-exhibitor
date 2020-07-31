#!/bin/bash
pip3  install -r requirements.txt
python3 -m pytest --alluredir=allure-results tests/tests.py -v -s
python3 -m pytest --alluredir=allure-results tests/tests2.py -v -s