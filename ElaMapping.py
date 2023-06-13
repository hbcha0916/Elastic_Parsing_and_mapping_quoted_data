# EalsticSearch Mapping Program . py
# 단순 text, long 형으로만 매핑한다.
# 날짜형 포맷, keyword는 따로 수정 필요
# Logic
# 1. 샘플 데이터 입력 (Elastic에 들어갈 데이터 입력)
# 2. 샘플 데이터 를 int형으로 변환
# 3. 만약 int형으로 변환 중 오류가 발생한 경우 해당 데이터는 float로 매핑하는데 이마저도 오류가 날 경우 text로 매핑
# 4. 오류가 안날경우 long으로 매핑하나 ElasticSearch의 최대 숫자와 최소 숫자의 범위를 벗어날 경우 text로 매핑
# 5. 맵핑 데이터가 <파일명>_mapping.json 으로 저장됨
# 6. Kibana에 맵핑 구문 작성

# 사용방법
# 1. 해당 내용을 복사 후 컴퓨터 작업 디렉토리에 mapping.py(예) 를 만들고 붙여놓기
# 2. (윈도우 기준)터미널로 python .\mapping.py <샘플데이터 디렉토리 파일명1.json> <샘플데이터 디렉토리 파일명2.json> <샘플데이터 디렉토리 파일명3... .json> (개수 상관없음) 실행

import sys
import json
import os

def merge_dicts(dict1, dict2):
    # 두 딕셔너리를 병합하는 함수
    for key in dict2:
        if key in dict1 and isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            # 두 값이 모두 딕셔너리인 경우, 재귀적으로 합침
            merge_dicts(dict1[key], dict2[key])
        else:
            # 두 값 중 하나가 딕셔너리가 아닌 경우, 값을 덮어씀
            dict1[key] = dict2[key]
    return dict1


def merge_nested_dicts(*dicts):
    # 중첩된 딕셔너리를 합치는 함수
    merged_dict = {}
    for dictionary in dicts:
        merged_dict = merge_dicts(merged_dict, dictionary)
    return merged_dict

def processing_List_String(data):
    new_data = {"properties": {}}
    for i in range(0,len(data)):
        if type(data[i])==dict:
            if i==0:
                tmp = merge_nested_dicts(processing_Dict_String(data[i]), processing_Dict_String(data[i+1]))
            else:
                try:
                    tmp = merge_nested_dicts(tmp,processing_Dict_String(data[i+1]))
                except IndexError:
                    new_data['properties'].update(tmp['properties'])
    return new_data

def processing_Dict_String(data):
    new_data = {"properties": {}}
    setText = {"type": "text"}
    setNum = {"type": "long"}
    setFloat = {"type": "float"}

    sort_data = sorted(data.items())
    dic_sort_data = dict(sort_data)
    dic_sort_data_keys = list(dic_sort_data.keys())

    for i in dic_sort_data_keys:
        if type(dic_sort_data[i]) == list:
            try:
                tmp = new_data["properties"][i]
            except:
                new_data["properties"][i] = processing_List_String(dic_sort_data[i])
            else:
                new_data["properties"][i].update(processing_List_String(dic_sort_data[i]))
        elif type(dic_sort_data[i]) == dict:
            try:
                tmp = new_data["properties"][i]
            except:
                new_data["properties"][i] = processing_Dict_String(dic_sort_data[i])
            else:
                new_data["properties"][i].update(processing_Dict_String(dic_sort_data[i]))

        else:
            try:
                if new_data["properties"][i]["type"] == "text":
                    new_data["properties"][i] = setText
            except:
                try:
                    tmp = int(dic_sort_data[i])
                except:
                    try:
                        tmp = float(dic_sort_data[i])
                    except:
                        new_data["properties"][i] = setText
                    else:
                        new_data["properties"][i] = setFloat
                else:
                    try:
                        if new_data["properties"][i]["type"] == "float":
                            new_data["properties"][i] = setFloat
                    except:
                        if str(int(dic_sort_data[i])) != str(dic_sort_data[i]):
                            new_data["properties"][i] = setFloat
                        elif int(dic_sort_data[i]) < 9223372036854775807 and int(
                                dic_sort_data[i]) > -9223372036854775808:
                            new_data["properties"][i] = setNum
                        else:
                            print("숫자형이지만 숫자가 너무 작거나 큰 Data (text형식으로 변환된 MappingData)=> ", i)
                            new_data["properties"][i] = setText

            finally:
                pass
    return new_data

for i in range(1,len(sys.argv)):

    dir = os.path.abspath(sys.argv[i])
    print("=============== | ",dir," | ===============")
    print(i," / ",len(sys.argv)-1," Data")

    filename = os.path.basename(sys.argv[i]).split(".")
    with open(dir,"r") as file:
        dict_data = json.load(file,strict=False)

    new_data = processing_Dict_String(dict_data)



    with open(filename[0]+"_mapping.json", "w") as file:
        file.write(json.dumps(new_data,indent=3))
        print("=== | ",filename[0]+"_mapping.json 생성 완료 | ===")

    print()

print("=============== | 매핑이 완료됨 | ===============")