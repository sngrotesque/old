# 作者：SN-Grotesque（Author: SN-Grotesque）

import requests
import time
#import ssl

nowtime = time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime())
print("此刻的时间是: "+nowtime)
print("正在帮你查询上海米哈游科技股份有限公司的“游戏客服”岗位信息...\n")

url = "https://jobs.mihoyo.com/api/outer/ats-jc-apply/website/job"

headers = {
    "Host": "jobs.mihoyo.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Referer": "https://jobs.mihoyo.com/apply/mihoyo/7524/",
    "Content-Type": "application/json",
    "Origin": "https://jobs.mihoyo.com",
    #"Cookie": "请您使用自己的Cookie（Please use your own Cookie）"
}

data = {
    "jobId": "612ec466-7d0e-42dc-b489-f460ff282a38",
    "orgId": "mihoyo",
    "siteId": "7524"
}

r = requests.post(url, json=data, headers=headers,verify=True).json()
mihoyo_jobs = str(r)

print("上海米哈游科技股份有限公司的“游戏客服”岗位信息如下\n")
print("岗位类型: %s" % mihoyo_jobs[160:162])
print("岗位职责: ")
print("%s" % mihoyo_jobs[370:454])
print("%s" % mihoyo_jobs[461:501])
print("%s" % mihoyo_jobs[508:554])
print("%s" % mihoyo_jobs[561:583])
print("%s" % mihoyo_jobs[590:623])
print("\n岗位要求: ")
print("%s" % mihoyo_jobs[652:678])
print("%s" % mihoyo_jobs[685:707])
print("%s" % mihoyo_jobs[714:738])
print("%s" % mihoyo_jobs[745:769])
print("\n以下有加分: ")
print("%s" % mihoyo_jobs[800:839])
print("%s" % mihoyo_jobs[846:871])
print("\n公司地址: 上海市徐汇区宜山路700号普天信息产业园C4\n")


print("请问是否投递简历?（y / n）")
queren1 = input()

if queren1 == 'y':
    url_tdjl = "https://jobs.mihoyo.com/api/apply/mihoyo/612ec466-7d0e-42dc-b489-f460ff282a38"  # 投递网址
    h = {"Host": "jobs.mihoyo.com",
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}  # 请求头部
    print("个人网站 - 没有就写 无")
    website = input()  # 个人网站 - 没有就写 无
    print("姓名")
    name = input()  # 姓名
    print("性别")
    gender = input()  # 性别
    print("手机号 - 不需要+86")
    phone = input()  # 手机号 - 不需要+86
    print("电子邮箱")
    email = input()  # 电子邮箱
    print("出生日期 - 格式 1970-01-01")
    birthdate = input()  # 出生日期 - 格式 1970-01-01
    print("所在地")
    location = input()  # 所在地
    print("学历")
    academicDegree = input()  # 学历
    print("毕业到开始找工作的时间  - 只写年月")
    graduateDate = input()  # 毕业到开始找工作的时间  - 只写年月
    print("到岗时间 - 不是几月几日，如“随时到岗”")
    startFrom = input()  # 到岗时间 - 不是几月几日，如“随时到岗”
    print("当前薪资")
    salary = input()  # 当前薪资
    print("期望薪资")
    aimSalary = input()  # 期望薪资
    print("开始工作的时间  - 只写年月")
    startDate = input()  # 开始工作的时间  - 只写年月
    print("结束工作的时间  - 只写年月 - 未离职填 至今")
    endDate = input()  # 结束工作的时间  - 只写年月 - 未离职填 至今
    print("公司名称")
    company = input()  # 公司名称
    print("职位名称")
    title = input()  # 职位名称
    print("公司地址")
    location_gs = input()  # 公司地址
    print("所在行业")
    industry = input()  # 所在行业
    print("工作职责")
    summary = input()  # 工作职责
    print("入学时间  - 只写年月")
    startDate_school = input()  # 入学时间  - 只写年月
    print("毕业时间  - 只写年月")
    endDate_school = input()  # 毕业时间  - 只写年月
    print("学校名称")
    school = input()  # 学校名称
    print("就读专业")
    speciality = input()  # 就读专业
    print("学历")
    academicDegree = input()  # 学历
    data = {
    "1822": [{}],
    "1823": [{}],
    "1824": [{}],
    "1825": [{}],
    "applyInfo": {
        "campusSiteId": "null",
        "aimWorkCity": "上海市"
    },
    "uploadInfo": {
        "resumeKey": "",
        "portrait": "null",
        "attachments": []
    },
    "basicInfo": {
        "23329": website,
        "name": name,
        "gender": gender,
        "countryCallingCode": "",
        "phone": phone,
        "fullPhone": phone,
        "email": email,
        "birthDate": birthdate,
        "location": location,
        "academicDegree": academicDegree,
        "graduateDate": {"startDate": graduateDate},
        "startFrom": startFrom
    },
    "jobIntention": {"salary": salary, "aimSalary": aimSalary},
    "experienceInfo": [{
        "startDate": startDate,
        "endDate": endDate,
        "company": company,
        "title": title,
        "location": location_gs,
        "industry": industry,
        "summary": summary
    }],
    "educationInfo": [{
        "startDate": startDate_school,
        "endDate": endDate_school,
        "school": school,
        "speciality": speciality,
        "academicDegree": academicDegree
    }],
    "practiceInfo": [{}],
    "projectInfo": [{}],
    "languageInfo": [{}],
    "selfDescription": {},
    "awardInfo": [{}],
    "device": "pc",
    "recommender": {},
    "recommendInfo": {"recommendReason": ""},
    "siteId": "7524",
    "acquisitionMode": 9
    }
    print("是否确认提交？（y / n）")
    queren = input()

    if queren == 'y':
        rr = requests.post(url_tdjl, json=data, headers=h).json()
        print("%s" % rr)
    else:
        print("好的，再见。")
        exit()
else:
    print("好的，再见！")
    exit()

