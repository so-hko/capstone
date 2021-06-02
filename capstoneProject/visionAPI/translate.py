from google.cloud import translate_v2 as translate
#import google.cloud 
#import translate_v2 as translate
#import translate as translate
import os
#import getDbInfo
#import getDrugInfo


info = ["게보린정",
        "아세트아미노펜,이소프로필안티피린,카페인무수물",
        "두통, 치통, 발치(이를 뽑음)후 동통(통증), 인후(목구멍)통, 귀의 통증, 관절통, 신경통, 요(허리)통, 근육통, 견통(어깨통증), 타박통, 골절통, 염좌통(삔 통증), 월경통(생리통), 외상(상처)통의 진통과 오한(춥고 떨리는 증상), 발열시의 해열에 사용",
        "성인은 1회 1정 1일 3회까지 공복시를 피해 복용 복용간격은 4시간 이상",
        "과민증 환자, 다른 해열진통제(비스테로이드성 소염제), 감기약 복용시 천식발작 유발 또는 그 경험자, 글루코스-6-인산 탈수소효소결핍증, 급성 간헐성(시간 간격을 두고 되풀이하여) 포르피린증, 과립백혈구감소증, 중증 간장애, 중증 신장애, 출혈 소인, 15세 미만의 소아, 소화성궤양, 심한 혈액 이상, 심한 심장기능저하, 바르비탈계 약물, 삼환계 항우울제, 알코올을 복용한 환자는 이 약을 복용하지 마십시오"]

os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS', '/home/ec2-user/capstone/capstoneProject/visionAPI/My_First_Project-51cda441fdd3.json')
client = translate.Client()

def translation(info,code): 
    print(info)
    result = client.translate(info, target_language= code)
    print(result['translatedText'])
    return result['translatedText']


for i in info:
    translation(i,"vi")
"""
translation(info,"vi")
"""
