import subprocess
def getImage():
    url = "\"https://www.tylenol.co.kr/sites/tylenol_kr/files/styles/product_image/public/tairenol_500mg_yaggugyong_ceugmyeontylenol_500mg.jpg\""
    subprocess.call("curl " + url + " > drug_image.jpg", shell=True)

def getLanguage():
    return 0


