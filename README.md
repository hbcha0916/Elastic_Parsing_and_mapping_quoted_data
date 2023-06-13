# Elastic_Parsing_and_mapping_quoted_data.

# 제작목적

ElasticSearch에 Json 데이터를 넣어주려나, JsonData가 모두 따옴표(” “) 로 묶여 있어 자동 Mapping이 전부 text로 될 때 손수 하나하나 보고 맵핑하기 번거로워 제작

# 주의사항

- 해당 프로그램은 `long` , `float` , `text` 형태로만 Parsing하고 Mapping 합니다. `Keyword`, `date` 등의 형식은 파일 추출 후 직접 수정해 주셔야 합니다.
- 여러 단계로 중첩된 JSON 형태일 경우 데이터를 Merge작업 한 데이터를 기반으로 추출되기 때문에 중첩 JSON 데이터는 추출 후 다시 확인작업이 필요합니다.
- 단순반복노동을 돕는 프로그램이고, ElasticSearch의 Mapping 기능을 대신할 순 없습니다.
- 잘못된 매핑으로 인한 책임은 지지 않습니다.

# 사용방법

1. 해당 저장소를 clone 합니다.
2. 그 다음으로 clone 한 디렉토리 내에서 맵핑할 원본 데이터의 json 파일을 가져다 둡니다.
3. 아래 명령어에 따릅니다. 
    
    ```bash
    python Elamapping.py <맵핑 파일명>.json <맵핑 파일명1>.json <맵핑 파일명2>.json...
    ```
    
4. 매핑이 완료된 파일은 `<맵핑 파일명>_mapping.json` 으로 저장됩니다.

# 소통

📋Blog : [https://hbcha0916.tistory.com/](https://hbcha0916.tistory.com/)

📧E-Mail : [hbcha0916@naver.com](mailto:hbcha0916@naver.com)

# 사용예시

### 맵핑할 파일
! Scouter의 가짜 데이터입니다.

```json
{
   "bucket_date" : "20230522",
   "memory" : 0,
   "error" : 0,
   "bucket_time_number" : 1684716440310,
   "elapsed" : 6,
   "sqlCount" : 2,
   "queuingTime" : 0,
   "ipaddr" : "192.168.0.0",
   "queuing2ndTime" : 0,
   "group" : "/rest",
   "apicallCount" : 0,
   "sqlTime" : 6,
   "objHash" : 12345678,
   "bucket_time" : "12345678",
   "txid" : "-12345678",
   "cpu" : 0,
   "userAgent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
   "objName" : "/localhost.localdomain/TEST",
   "txid_string" : "z33b9c91lfj5k3",
   "end_time_number" : 1684716440316,
   "threadName" : "http-bio-8080-exec-18",
   "referrer" : "http://192.168.0.99:8080/Test/rest/Search",
   "caller" : "0",
   "apicallTime" : 0,
   "objHashCode" : "x1olli9s",
   "service" : "/rest/Search<GET>",
   "endTime" : "20230522094720",
   "gxid" : "0",
   "result" : [ {
     "mainValue" : "[driving thread] http-bio-8080-exec-18",
     "step" : {
       "parent" : "-1",
       "start_time" : "0",
       "start_cpu" : "0",
       "stepTypeName" : "HASHED_MESSAGE",
       "stepType" : "9",
       "index" : "0",
       "time" : "-1",
       "value" : "0",
       "hash" : "-1815871479",
       "order" : "0"
     }
   }, {
     "mainValue" : "param: framework..rest.vo.Name=<null>,ClassName=<null>,mnlContents=<null>,confirmGb=<null>,mnlContentsNew=<null>,newGb=<null>,UseYn=<null>,RegistId=<null>,RegistDate=<null>,EditId=<null>,EditDate=<null>,tokenStr=<null>,description=<null>,rnum=0,searchCondition=,searchKeyword=,searchUseYn=,pageIndex=1,pageUnit=10,pageSize=10,firstIndex=1,lastIndex=1,recordCountPerPage=10]",
     "step" : {
       "parent" : "-1",
       "start_time" : "0",
       "start_cpu" : "0",
       "stepTypeName" : "MESSAGE",
       "stepType" : "3",
       "index" : "1",
       "message" : "param: framework..rest.vo.Name=<null>,ClassName=<null>,mnlContents=<null>,confirmGb=<null>,mnlContentsNew=<null>,newGb=<null>,UseYn=<null>,RegistId=<null>,RegistDate=<null>,EditId=<null>,EditDate=<null>,tokenStr=<null>,description=<null>,rnum=0,searchCondition=,searchKeyword=,searchUseYn=,pageIndex=1,pageUnit=10,pageSize=10,firstIndex=1,lastIndex=1,recordCountPerPage=10]",
       "order" : "1"
     }
   }, {
     "mainValue" : "param: {manualVO=framework.e.rest.vo.ManPropertyBindingResult: 0 errors}",
     "step" : {
       "parent" : "-1",
       "start_time" : "0",
       "start_cpu" : "0",
       "stepTypeName" : "MESSAGE",
       "stepType" : "3",
       "index" : "2",
       "message" : "param: {manualVO=framework.e.rest.vo.ManPropertyBindingResult: 0 errors}",
       "order" : "2"
     }
   }, {
     "mainValue" : "param: org.379d",
     "step" : {
       "parent" : "-1",
       "start_time" : "0",
       "start_cpu" : "0",
       "stepTypeName" : "MESSAGE",
       "stepType" : "3",
       "index" : "3",
       "message" : "param: org.379d",
       "order" : "3"
     }
   }, {
     "mainValue" : "param: org.apache.catalina.connect",
     "step" : {
       "parent" : "-1",
       "start_time" : "0",
       "start_cpu" : "0",
       "stepTypeName" : "MESSAGE",
       "stepType" : "3",
       "index" : "4",
       "message" : "param: org.apache.catalina.connect",
       "order" : "4"
     }
   }, {
     "mainValue" : "param: org.apache.catalina.session",
     "step" : {
       "parent" : "-1",
       "start_time" : "0",
       "start_cpu" : "0",
       "stepTypeName" : "MESSAGE",
       "stepType" : "3",
       "index" : "5",
       "message" : "param: org.apache.catalina.session",
       "order" : "5"
     }
   }, {
     "mainValue" : "select @{1} from dual",
     "step" : {
       "parent" : "6",
       "xtypePrefix" : "STM> ",
       "xtype" : "48",
       "stepType" : "16",
       "index" : "7",
       "error" : "0",
       "elapsed" : "1",
       "start_time" : "0",
       "start_cpu" : "0",
       "stepTypeName" : "SQL3",
       "param" : "1",
       "cputime" : "0",
       "updated" : "-1",
       "hash" : "-1008304795",
       "order" : "7"
     }
   }, {
     "mainValue" : "RESULT-SET-FETCH",
     "step" : {
       "parent" : "6",
       "start_time" : "1",
       "start_cpu" : "0",
       "stepTypeName" : "HASHED_MESSAGE",
       "stepType" : "9",
       "index" : "8",
       "time" : "0",
       "value" : "1",
       "hash" : "-1479939665",
       "order" : "8"
     }
   }, {
     "mainValue" : "#getConnection",
     "step" : {
       "elapsed" : "1",
       "parent" : "-1",
       "start_time" : "0",
       "start_cpu" : "0",
       "stepTypeName" : "METHOD",
       "stepType" : "1",
       "index" : "6",
       "cputime" : "0",
       "hash" : "1559472428",
       "order" : "6"
     }
   }, {
     "mainValue" : "SELECT NO\n\t\t     , SCOUTER\n\t\t     , FAKE\n\t\t     , X\n\t\t     , LOG\n\t\t     , HELLO\n\t\t\t , WORLD\n\t\t  FROM FAKELOG\n\t\t WHERE HI = '@{1}'\n\t  \t   AND PPPOOODDD \t= ?\n\t  \t   AND WJNBWEB \t\t= ?\n\t  \t   AND EBFBVBD = ?\n\t  \t   AND ASDF \t\t= ?\n\t  \t   AND CONFIRM_GB IN ('@{2}','@{3}','@{4}')",
     "step" : {
       "parent" : "-1",
       "xtypePrefix" : "PRE> ",
       "xtype" : "17",
       "stepType" : "16",
       "index" : "9",
       "error" : "0",
       "elapsed" : "5",
       "start_time" : "1",
       "start_cpu" : "0",
       "stepTypeName" : "SQL3",
       "param" : "'Y','1','2','3','04','01','00','11'",
       "cputime" : "0",
       "updated" : "-1",
       "hash" : "2109344007",
       "order" : "9"
     }
   }, {
     "mainValue" : "RESULT_CH",
     "step" : {
       "parent" : "-1",
       "start_time" : "6",
       "start_cpu" : "0",
       "stepTypeName" : "HASHED_MESSAGE",
       "stepType" : "9",
       "index" : "10",
       "time" : "0",
       "value" : "1",
       "hash" : "-1479939665",
       "order" : "10"
     }
   }, {
     "mainValue" : "CLOSE",
     "step" : {
       "elapsed" : "0",
       "parent" : "-1",
       "start_time" : "6",
       "start_cpu" : "0",
       "stepTypeName" : "METHOD",
       "stepType" : "1",
       "index" : "11",
       "cputime" : "0",
       "hash" : "-464174220",
       "order" : "11"
     }
   } ],
   "requestId" : "#m102",
   "resultCode" : "0",
   "message" : "success",
   "status" : "200"
 }
```

### 맵핑후 파일

```json
{
   "properties": {
      "apicallCount": {
         "type": "long"
      },
      "apicallTime": {
         "type": "long"
      },
      "bucket_date": {
         "type": "long"
      },
      "bucket_time": {
         "type": "long"
      },
      "bucket_time_number": {
         "type": "long"
      },
      "caller": {
         "type": "long"
      },
      "cpu": {
         "type": "long"
      },
      "elapsed": {
         "type": "long"
      },
      "endTime": {
         "type": "long"
      },
      "end_time_number": {
         "type": "long"
      },
      "error": {
         "type": "long"
      },
      "group": {
         "type": "text"
      },
      "gxid": {
         "type": "long"
      },
      "ipaddr": {
         "type": "text"
      },
      "memory": {
         "type": "long"
      },
      "message": {
         "type": "text"
      },
      "objHash": {
         "type": "long"
      },
      "objHashCode": {
         "type": "text"
      },
      "objName": {
         "type": "text"
      },
      "queuing2ndTime": {
         "type": "long"
      },
      "queuingTime": {
         "type": "long"
      },
      "referrer": {
         "type": "text"
      },
      "requestId": {
         "type": "text"
      },
      "result": {
         "properties": {
            "mainValue": {
               "type": "text"
            },
            "step": {
               "properties": {
                  "hash": {
                     "type": "long"
                  },
                  "index": {
                     "type": "long"
                  },
                  "order": {
                     "type": "long"
                  },
                  "parent": {
                     "type": "long"
                  },
                  "start_cpu": {
                     "type": "long"
                  },
                  "start_time": {
                     "type": "long"
                  },
                  "stepType": {
                     "type": "long"
                  },
                  "stepTypeName": {
                     "type": "text"
                  },
                  "time": {
                     "type": "long"
                  },
                  "value": {
                     "type": "long"
                  },
                  "message": {
                     "type": "text"
                  },
                  "cputime": {
                     "type": "long"
                  },
                  "elapsed": {
                     "type": "long"
                  },
                  "error": {
                     "type": "long"
                  },
                  "param": {
                     "type": "long"
                  },
                  "updated": {
                     "type": "long"
                  },
                  "xtype": {
                     "type": "long"
                  },
                  "xtypePrefix": {
                     "type": "text"
                  }
               }
            }
         }
      },
      "resultCode": {
         "type": "long"
      },
      "service": {
         "type": "text"
      },
      "sqlCount": {
         "type": "long"
      },
      "sqlTime": {
         "type": "long"
      },
      "status": {
         "type": "long"
      },
      "threadName": {
         "type": "text"
      },
      "txid": {
         "type": "long"
      },
      "txid_string": {
         "type": "text"
      },
      "userAgent": {
         "type": "text"
      }
   }
}
```
