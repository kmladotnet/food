#!/bin/bash
java -cp /scripts/food/foodAPI.jar Food.java
java -cp /scripts/food:/scripts/food/foodAPI.jar Food | python3 /scripts/food/makeJSON.py
