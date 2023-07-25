import urllib3
import json
import base64
openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
accessKey = "03cdc1ef-505b-42f4-8566-8f477092e098"
audioFilePath = "C:/Users/pc/Desktop/h/test/preprocessing_data/0_2.wav"
languageCode = "korean"

file = open(audioFilePath, "rb")
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

print("[responseCode] " + str(response.status))
print("[responBody]")
print(str(response.data,"utf-8"))
                                      