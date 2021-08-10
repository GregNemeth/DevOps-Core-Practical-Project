#!/bin/bash

python3 -m venv venv

source venv/bin/activate
pip3 install -r requirements.txt

for i in service_{1,2,3}; do
    cd ${i}
    python3 -m pytest --cov=app --cov-report xml -v
    cd ..
done

cd service_4

python3 -m pytest --cov=application --cov-report xml -v


