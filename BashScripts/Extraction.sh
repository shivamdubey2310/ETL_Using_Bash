#!/bin/bash

curl -X GET "https://randomuser.me/api/?format=csv&results=5000" -o data/raw_data.csv