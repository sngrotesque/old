import requests

x=0
while x<10000:
    url_tdjl = "https://jobs.mihoyo.com/api/apply/mihoyo/612ec466-7d0e-42dc-b489-f460ff282a38"
    h = {"Host": "jobs.mihoyo.com","User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
    
    data = {
    "1822": [{}],"1823": [{}],"1824": [{}],"1825": [{}],
    "applyInfo": {
        "campusSiteId": "null","aimWorkCity": "上海市"
    },
    "uploadInfo": {
        "resumeKey": "","portrait": "null","attachments": []
    },
    "basicInfo": {
        "23329": x,"name": x,"gender": x,"countryCallingCode": "","phone": x,"fullPhone": x,"email": x,"birthDate": x,"location": x,"academicDegree": x,"graduateDate": {"startDate": x},"startFrom": x
    },
    "jobIntention": {"salary": x, "aimSalary": x},
    "experienceInfo": [{
        "startDate": x,"endDate": x,"company": x,"title": x,"location": x,"industry": x,"summary": x
    }],
    "educationInfo": [{
        "startDate": x,"endDate": x,"school": x,"speciality": x,"academicDegree": x
    }],
    "practiceInfo": [{}],"projectInfo": [{}],"languageInfo": [{}],"selfDescription": {},"awardInfo": [{}],"device": "pc","recommender": {},"recommendInfo": {"recommendReason": ""},
    "siteId": "7524",
    "acquisitionMode": 9
    }
    rr = requests.post(url_tdjl, json=data, headers=h).json()
    print("%s" % rr)
    
    x=x+1

exit()
