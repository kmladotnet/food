# Food

* 이 디렉토리에 담긴 파일들은 kmlaonline.net에서 급식을 보여주는 역할을 담당하고 있습니다.
* 급식 정보가 최종적으로 담기는 파일은 이 디렉토리 안에 있는 data.json이며, 이외 파일들은 이 json 파일을 만들기 위해 사용됩니다.

## 작동 방식

~~1. 급식 정보는 외부 java api를 사용해서 가져오며, 이 데이터를 총 2번 가공해 json 파일을 생성합니다.
2. 첫 번째 가공은 Food.class 파일에서 이루어집니다. API를 이용해 올해의 급식 데이터를 가져오고, 정해진 형식으로 출력을 합니다 (Food.java 파일 참조). 
3. 이 출력값을 makeJSON.py에서 입력값으로 받아 한 번 더 파싱합니다. 급식 뒤에 있는 숫자와 &(ampersand) 기호를 없앤 뒤, json 파일을 생성해냅니다.~~

모든 급식 정보 api 및 데이터 가공은 GetFood.py 내에서 이루어집니다.

급식 정보는 나이스 api를 사용합니다.
[나이스 링크](https://open.neis.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=OPEN17320190722180924242823&infSeq=1)
api 인증키가 만료될 일은 없지만, 만약 변경해야 한다면 위 사이트에서 새로 발급받아 config.json 파일에 "FOOD_KEY" : "[인증키]" 형식으로 저장하시면 됩니다.

* 위의 작업은 /scripts/food/update.sh 라는 shell script를 이용해 자동화 합니다.

```bash
cd /scripts/food
python3 ./GetFood.py
```

## Cron (주기적 실행)

* cron 이라는 프로그램을 이용해 매일 자정에 실행합니다. 
* 정기적으로 실행되어 업데이트가 되는 것이기 때문에 수동적으로 업데이트를 할 필요는 없다. 
* 혹시 급식이 보이지 않는 날이 있다면 update.sh를 직접 실행해 업데이트를 해보시기를 바랍니다.

## Notes
* 이 디렉터리 속 파일들은 모두 한 곳에 있어야 합니다. 각각 다른 곳에 두기를 희망하신다면 소스 코드를 잘 숙지하신 이후 경로 값을 적절히 변형해 정상적인 작동에 지장이 없도록 해주세요.

* data.json의 경로가 바뀐다면! lib.php에서 바뀐 경로로 소스 코드를 업데이트해야 합니다. 

* cron에서는 update.sh를 정기적으로 실행하고 있기 때문에 경로 정보가 명확해야 합니다. 따라서 update.sh의 경로가 바뀐다면! cron을 실행해 그 경로 정보를 바뀐 것으로 업데이트해야 합니다.
