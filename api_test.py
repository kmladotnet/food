import requests
import json
import datetime

def get_food():
  food = dict()
  now = datetime.datetime.now()

  URI = "https://open.neis.go.kr/hub/mealServiceDietInfo"

  with open("./급식 정보/config.json") as f:
    config = json.load(f)
    KEY = config["FOOD_KEY"]

  TYPE = "json"
  
  ATPT_OFCDC_SC_CODE = "K10"
  SD_SCHUL_CODE = "7801132"
  MLSV_FROM_YMD = str(now.year) + "0101"
  MLSV_TO_YMD = str(now.year) + "1231"
  pIndex = 40
  pSize = 3

  params = {
    "KEY": KEY,
    "Type": TYPE,
    "ATPT_OFCDC_SC_CODE": ATPT_OFCDC_SC_CODE,
    "SD_SCHUL_CODE": SD_SCHUL_CODE,
    "MLSV_FROM_YMD": MLSV_FROM_YMD,
    "MLSV_TO_YMD": MLSV_TO_YMD,
    "pIndex": pIndex,
    "pSize": pSize
  }

  response = requests.get(URI, params=params)
  json_data = json.dumps(response.json(), ensure_ascii=False, indent=4, separators=(',', ': '))
  print(json_data)

get_food()