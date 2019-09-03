#!/bin/bash
java -cp ./foodAPI.jar Food.java
java -cp .:./foodAPI.jar Food | python3 ./makeJSON.py