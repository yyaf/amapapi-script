import requests
import time

def get_pois():
    keywords = '关键词'
    key = 'b71774895644a654648295448faf24'  # 注册高德开放平台获取key
    page = 1

    urls = []
    for i in range(20):
        url = 'https://restapi.amap.com/v5/place/around?keywords='+ keywords +'&region=郑州市&location=34.698556,113.944008&radius=5000&page_size=25&show_fields=business&page_num=' + str(page) + '&key=b717741fb1a5cd8a6df28295448faf24'
        page += 1
        urls.append(url)

    f=open(r''+keywords+'.csv','a',encoding='utf-8-sig')


    for url in urls:
        time.sleep(1) # 为了防止并发量报警，设置了一个休眠。认证后就不需要了
        html = requests.get(url) # 获取网页信息
        data = html.json()

        for item in data['pois']: 
            jname = item['name'] # 获取名称

            try:
                jtel = item['business']['tel'] # 获取电话
            except KeyError:
                jtel = ""
                print("没有电话信息")
            jcity = item['cityname']
            jad = item['adname']
            jadd = item['address'] # 获取详细地址
            print(item)
            j_str = jname + ',' + jtel + ',' + jcity + ',' + jad + ',' + jadd + '\n' # 以逗号格式，将数据存入一个字符串
            f.write(j_str) # 将数据以行的形式写入CSV文件中


    f.close()
    print ('*****************{}获取完成******************'.format(keywords))
get_pois()
