import requests


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.9101 SLBChan/115 SLBVPV/64-bit",
    "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "PSTM": "1732620482",
    "BIDUPSID": "52CA11C77AC2D50D55F4826C4D0239E3",
    "BAIDUID": "73D3E8FCBF2FF9EBF5F64FF62A9AA908:FG=1",
    "H_WISE_SIDS_BFESS": "60271_61027_60851_61354_61365_61435_61469",
    "BDORZ": "FFFB88E999055A3F8A630C64834BD6D0",
    "H_PS_PSSID": "60271_61027_61354_61365_61435_61469_60853_61491_61430",
    "BDSFRCVID": "m-DOJeC62GTWIM6JDzsoEHtYogph7P7TH6aoVFK2pE2yClQPlD5oEG0Plx8g0K4-S2abogKKWeOTHxvfdm02nfb3D8B8rSbEO3hLtf8g0x5",
    "H_BDCLCKID_SF": "tRAOoCPytDvbeJrc5DTD-tFO5eT22-usa4jR2hcH0KLKsUb5yfF-yx0hKUn4Bn3kaKvjBI3xJMb1MRjv3xjvDR8kDlrm2poTagPtWh5TtUJSJKnTDM4MqqJX-f5yKMniQKT9-pnybJQfDDt4h4jDDU3bLG7HQ-j4Bb732PbDfn02JKKu-n5jHjJyjH8D3e",
    "H_WISE_SIDS": "60271_61027_61354_61365_61435_61469_60853_61491_61430",
    "BAIDUID_BFESS": "73D3E8FCBF2FF9EBF5F64FF62A9AA908:FG=1",
    "BDSFRCVID_BFESS": "m-DOJeC62GTWIM6JDzsoEHtYogph7P7TH6aoVFK2pE2yClQPlD5oEG0Plx8g0K4-S2abogKKWeOTHxvfdm02nfb3D8B8rSbEO3hLtf8g0x5",
    "H_BDCLCKID_SF_BFESS": "tRAOoCPytDvbeJrc5DTD-tFO5eT22-usa4jR2hcH0KLKsUb5yfF-yx0hKUn4Bn3kaKvjBI3xJMb1MRjv3xjvDR8kDlrm2poTagPtWh5TtUJSJKnTDM4MqqJX-f5yKMniQKT9-pnybJQfDDt4h4jDDU3bLG7HQ-j4Bb732PbDfn02JKKu-n5jHjJyjH8D3e",
    "delPer": "0",
    "PSINO": "7",
    "BA_HECTOR": "0h05250l0ha4al8k8401a080b1gbom1jm7v841u",
    "ZFY": "e:A2gz41RfAiJ1FmC6rSEThpLDJwsS4qJETCZcbj:AJR0:C",
    "Hm_lvt_3535ee208b02ecdf4b2576fd444e8473": "1734243022,1734297403,1734607153",
    "Hm_lpvt_3535ee208b02ecdf4b2576fd444e8473": "1734607153",
    "HMACCOUNT": "ECA2B798F954DB7F"
}
url = "https://weathernew.pae.baidu.com/weathernew/pc"
params = {
    "query": "遵义仁怀天气",
    "srcid": "4982",
    "forecast": "long_day_forecast"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
data = response.text + "qwertyuioplkjhgfdsazxcvbnm" + "仁怀"
city = data.split("qwertyuioplkjhgfdsazxcvbnm")[1]
print(city)