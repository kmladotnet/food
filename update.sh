#!/bin/bash
cd /scripts/food
java -cp .:./foodAPI.jar Food | python3 ./makeJSON.py
