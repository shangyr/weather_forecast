# -*- coding: utf-8 -*-
import redis
import json
#角色Master 主要是负责发布url任务
class WeatherMaster():
    def __init__(self):
        #加载redis配置文件
        with open("config.json","r",encoding='utf8') as f:
            config = json.load(f)
        self.machine_count = config['machine_count']
        self.red = redis.Redis(host=config['redis_address'], port=config['redis_port'], db=config['redis_db'])
        self.timer = redis.Redis(host=config['redis_address'], port=config['redis_port'], db=11)

    def publish_task(self,city_list):
        """
        #发布县城名称任务 任务详情： 加载全国各县城名单，按机器数量平均分city
        #任务是数组格式，表示一台机器接收到的任务量，worker收到任务后开启多线程任务
        #任务名称，machineId  machineId是机器id，需要指定，手动创建或者通过web端注册，这里使用的是手动创建
        #在Master 目录下新建machineIds.json 内容为所有需要工作Worker的machineId
        :param city_list:
        :return:
        """
        #加载所有机器id
        with open('machineIds.json','r',encoding='utf8') as f:
            machineIds = json.load(f)
        i = 0
        for list in city_list:
            #发布任务
            self.red.lpush(machineIds[i], json.dumps(list))
            i += 1

    #加载全国县城名称
    def load_city(self):
        with open("city.txt", "r", encoding='utf8') as f:
            city = f.readlines()
        city_list = city[0].replace('\xa0', " ").split(' ')
        return city_list
    #将城市按照Worker机器数量平均分，返回数组
    def average_group(self,lst):
        """
        将列表均匀分组
        :param lst: 待分配的列表
        :param group_size: 每组的大小
        :return: 分组后的列表
        """
        return [lst[i::int(self.machine_count)] for i in range(int(self.machine_count))]

    def main(self):
        #清空计时器
        self.timer.flushall()
        city_list = self.load_city()
        print(city_list)
        list = self.average_group(city_list)
        print(city_list)
        #发布任务
        l = ['荔湾区', '越秀区', '海珠区', '天河区', '白云区', '黄埔区', '番禺区', '花都区', '南沙区', '萝岗区', '武江区', '浈江区', '曲江区', '始兴县', '仁化县', '翁源县', '乳源瑶族自治县', '新丰县', '乐昌市', '南雄市', '罗湖区', '福田区', '南山区', '宝安区', '龙岗区', '盐田区', '香洲区', '斗门区', '金湾区', '汕头市', '金平区', '濠江区', '潮阳区', '潮南区', '澄海区', '南澳县', '禅城区', '南海区', '南海区', '南海区', '高明区', '蓬江区', '江海区', '新会区', '台山市', '开平市', '鹤山市', '恩平市', '赤坎区', '霞山区', '坡头区', '麻章区', '遂溪县', '遂溪县', '廉江市', '雷州市', '吴川市', '茂南区', '茂港区', '电白县', '高州市', '化州市', '信宜市', '端州区', '鼎湖区', '广宁县', '怀集县', '封开县', '德庆县', '高要市', '四会市', '惠城区', '惠阳区', '博罗县', '惠东县', '龙门县', '梅江区', '梅县', '大埔县', '丰顺县', '五华县', '平远县', '蕉岭县', '兴宁市', '海丰县', '陆河县', '陆丰市', '源城区', '紫金县', '龙川县', '连平县', '和平县', '东源县', '江城区', '阳西县', '阳东县', '阳春市', '清城区', '佛冈县', '阳山县', '连山壮族瑶族自治县', '连南瑶族自治县', '清新县', '连州市', '英德市', '东城街道办事处', '南城街道办事处', '万江街道办事处', '莞城街道办事处', '石碣镇', '石龙镇', '茶山镇', '石排镇', '企石镇', '横沥镇', '石岐区街道办事处', '东区街道办事处', '火炬开发区街道办事处', '西区街道办事处', '南区街道办事处', '五桂山街道办事处', '小榄镇', '黄圃镇', '民众镇', '东凤镇', '湘桥区', '潮安县', '饶平县', '榕城区', '揭东县', '揭西县', '惠来县', '普宁市', '云城区', '新兴县', '郁南县', '云安县', '罗定市', '黄浦区', '卢湾区', '徐汇区', '长宁区', '静安区', '普陀区', '闸北区', '虹口区', '杨浦区', '闵行区', '崇明县', '玄武区', '白下区', '秦淮区', '建邺区', '鼓楼区', '下关区', '浦口区', '栖霞区', '雨花台区', '江宁区', '崇安区', '南长区', '北塘区', '锡山区', '惠山区', '滨湖区', '江阴市', '宜兴市', '鼓楼区', '云龙区', '九里区', '贾汪区', '泉山区', '丰县', '沛县', '铜山县', '睢宁县', '新沂市', '天宁区', '钟楼区', '戚墅堰区', '新北区', '武进区', '溧阳市', '金坛市', '沧浪区', '平江区', '金阊区', '虎丘区', '吴中区', '相城区', '常熟市', '张家港市', '昆山市', '吴江市', '崇川区', '港闸区', '通州区', '海安县', '如东县', '启东市', '如皋市', '海门市', '连云区', '新浦区', '海州区', '赣榆县', '东海县', '灌云县', '灌南县', '博乐市', '精河县', '温泉县', '东昌府区', '阳谷县', '莘县', '茌平县', '东阿县', '冠县', '高唐县', '临清市']
        self.publish_task(list)
        print("任务发布成功")

if __name__ == '__main__':
    wm = WeatherMaster()
    wm.main()