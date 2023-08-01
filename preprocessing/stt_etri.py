import urllib3
import json
import base64
import csv
import os


openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
accessKey = ""
audioFilePath = "/split"
languageCode = "korean"

file_list = os.listdir(audioFilePath)
f = open('.csv','a', newline='')
for file in file_list:
    file = open(audioFilePath+'/'+file, "rb")
    audioContents = base64.b64encode(file.read()).decode("utf8")
    file.close()

    requestJson = {    
        "argument": {
            "language_code": languageCode,
            "audio": audioContents
        }
    }

    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        openApiURL,
        headers={"Content-Type": "application/json; charset=UTF-8","Authorization": accessKey},
        body=json.dumps(requestJson)
    )
    try:
        print("[responseCode] " + str(response.status))
        print("[responBody]")
        print("===== 결과 확인 ====")
        data = json.loads(response.data.decode("utf-8", errors='ignore'))    
        print(data['return_object']['recognized'])

        wr = csv.writer(f)
        wr.writerow([file,data['return_object']['recognized'], 0])
    except:
        continue
f.close()