# encoding:utf-8

import requests
import base64

def getAccessToken():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format('', '')
    response = requests.get(host)
    return response.json()['access_token']

def doOcr(filePath):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token={}".format(getAccessToken())
    f = open(filePath, 'rb')
    img = base64.b64encode(f.read())
    params = {"image":img}
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        result = response.json()
        if result and result['words_result_num'] > 0:
            return result['words_result'][0]['words']
    return ''

if __name__ == '__main__':
    for i in range(10):
        word = doOcr('result/image/{}.jpg'.format(i + 1))
        print(word)