a = 0.017310619354248047
b = 0.009784698486328125
# print(a+b)
import redis
# mmnm = ['行唐县', '平山县', '元氏县', '无极县', '正定县', '玉田县', '乐亭县', '昌黎县', '磁县', '魏县', '大名县', '临漳县', '广平县', '鸡泽县威县', '巨鹿县', '临西县', '隆尧县', '内丘县', '平乡县', '雄县', '唐县', '博野县', '安新县', '阜平县', '涞水县', '顺平县', '容城县', '赤城县', '怀安县', '康保县', '张北县', '阳原县', '兴隆县', '滦平县沧县', '献县', '海兴县', '吴桥县', '南皮县', '固安县', '大城县', '安平县', '故城县', '武邑县', '饶阳县', '阳曲县', '清徐县', '阳高县', '浑源县', '灵丘县', '平定县', '壶关县', '襄垣县', '黎城县', '陵川县', '泽州县', '应县', '山阴县', '灵石县榆社县', '', '昔阳县', '寿阳县', '夏县', '临猗县', '万荣县', '垣曲县', '闻喜县', '代县', '定襄县', '河曲县', '偏关县', '静乐县', '五寨县', '古县', '吉县', '襄汾县', '安泽县', '浮山县', '乡宁县', '永和县', '岚县', '临县', '文水县', '交口县', '中阳县', '武川县', '清水河县', '固阳县', '宁城县', '五原县', '卓资县', '兴和县', '突泉县', '辽宁省', '康平县', '台安县', '黑山县', '彰武县', '盘山县', '昌图县', '朝阳县', '绥中县', '农安县', '梨树县', '东辽县', '辉南县', '抚松县', '镇赉县', '乾安县', '汪清县', '宾县', '方正县', '通河县', '木兰县', '富裕县', '克山县', '甘南县', '依安县', '桦川县', '汤原县', '肇州县', '嘉荫县', '汤旺县', '大箐山县', '萝北县', '集贤县', '友谊县', '勃利县', '兰西县', '绥棱县', '孙吴县', '呼玛县', '丰县', '睢宁县', '灌云县', '东海县', '金湖县', '响水县', '阜宁县', '宝应县', '泗洪县', '桐庐县', '象山县', '苍南县', '平阳县', '文成县', '德清县', '长兴县', '嘉善县', '武义县', '常山县', '龙游县', '三门县', '缙云县', '遂昌县', '庆元县', '岱山县', '安徽省', '肥东县', '庐江县', '五河县', '怀远县', '寿县', '和县', '濉溪县枞阳县', '岳西县', '宿松县', '歙县', '黟县', '颍上县', '阜南县', '砀山县', '泗县', '来安县', '凤阳县', '霍山县', '舒城县', '泾县', '旌德县', '石台县', '蒙城县', '利辛县', '连江县', '闽清县', '平潭县', '沙县', '宁化县', '尤溪县', '建宁县', '泰宁县', '安溪县', '德化县', '云霄县', '诏安县', '东山县', '平和县', '浦城县', '松溪县', '长汀县', '武平县', '霞浦县', '屏南县', '周宁县', '江西省', '安义县', '永修县', '都昌县', '彭泽县', '武宁县', '玉山县', '横峰县', '万年县', '鄱阳县', '黎川县', '崇仁县', '广昌县', '金溪县', '奉新县', '上高县', '靖安县', '吉安县', '新干县', '泰和县', '遂川县万安县', '永新县', '大余县', '全南县', '寻乌县', '宁都县', '会昌县', '石城县', '莲花县', '芦溪县', '分宜县', '商河县', '高青县', '广饶县', '临朐县', '嘉祥县', '梁山县', '鱼台县', '泗水县', '东平县', '莒县', '阳信县', '博兴县', '平原县', '武城县', '宁津县', '阳谷县', '高唐县', '莘县', '郯城县', '沂水县', '平邑县', '临沭县', '曹县', '巨野县', '郓城县', '东明县', '兰考县', '通许县', '嵩县', '洛宁县', '孟津县', '汝阳县', '宝丰县', '郏县', '汤阴县', '滑县', '淇县', '获嘉县', '延津县', '修武县', '武陟县', '清丰县', '南乐县', '范县', '襄城县', '临颍县', '卢氏县', '宁陵县', '虞城县', '民权县', '西华县', '沈丘县', '太康县', '西平县', '新蔡县', '泌阳县', '确山县', '平舆县', '西峡县', '镇平县', '桐柏县', '社旗县', '新野县', '息县', '固始县', '罗山县', '光山县', '郧西县', '竹溪县', '公安县', '远安县', '秭归县', '谷城县', '沙洋县', '红安县', '英山县', '蕲春县', '孝昌县', '云梦县', '通城县', '通山县', '巴东县', '宣恩县', '鹤峰县', '湖南省（61个）', '攸县', '茶陵县', '祁东县', '衡南县', '衡山县', '新宁县', '邵阳县', '洞口县', '岳阳县', '湘阴县', '安乡县', '石门县', '桃源县', '慈利县', '安化县', '新化县', '桂东县', '桂阳县', '宜章县', '汝城县', '道县', '祁阳县', '双牌县', '蓝山县', '会同县', '沅陵县', '溆浦县', '泸溪县', '花垣县', '古丈县', '新丰县', '仁化县', '东源县', '和平县', '龙川县', '五华县', '蕉岭县', '龙门县', '惠东县', '遂溪县', '郁南县', '阳山县', '海丰县', '南澳县', '广宁县', '怀集县', '揭西县', '隆安县', '上林县', '横县', '鹿寨县', '阳朔县', '全州县', '兴安县', '永福县', '苍梧县', '藤县', '上思县', '浦北县', '容县', '博白县', '西林县', '德保县', '凌云县', '田林县', '钟山县', '天峨县', '东兰县', '武宣县', '扶绥县', '龙州县', '天等县', '屯昌县', '临高县', '丰都县', '忠县', '奉节县', '巫溪县', '大邑县', '梓潼县', '平武县', '荣县', '米易县', '泸县', '古蔺县', '中江县', '剑阁县', '青川县', '蓬溪县', '威远县', '夹江县', '井研县', '乐至县', '长宁县', '珙县', '屏山县', '西充县', '蓬安县', '仪陇县', '大竹县', '开江县', '武胜县', '平昌县', '南江县', '青神县', '洪雅县', '汉源县', '天全县', '宝兴县', '汶川县', '红原县', '松潘县', '茂县', '九寨沟县', '小金县', '甘孜县', '白玉县', '炉霍县', '稻城县', '理塘县', '巴塘县', '石渠县', '泸定县', '德昌县', '喜德县', '会东县', '美姑县', '会理县', '布拖县', '盐源县', '雷波县', '息烽县', '桐梓县', '余庆县', '凤冈县', '绥阳县', '大方县', '金沙县', '黔西县', '江口县', '思南县', '望谟县', '晴隆县', '册亨县', '镇远县', '施秉县', '天柱县', '剑河县', '锦屏县', '雷山县', '从江县', '黎平县', '贵定县', '平塘县', '龙里县', '罗甸县', '富民县', '嵩明县', '富源县', '师宗县', '通海县', '易门县', '盐津县', '绥江县', '威信县', '彝良县', '施甸县', '昌宁县', '华坪县', '云县', '镇康县', '盈江县', '福贡县', '祥云县', '弥渡县', '永平县', '洱源县', '双柏县', '南华县', '武定县', '姚安县', '牟定县', '石屏县', '元阳县', '绿春县', '广南县', '马关县', '西畴县', '勐海县', '林周县', '尼木县', '曲水县', '左贡县', '洛隆县', '江达县', '丁青县', '类乌齐县', '江孜县', '萨迦县', '昂仁县', '仲巴县', '聂拉木县', '仁布县', '萨嘎县', '定结县', '米林县', '察隅县', '朗县', '扎囊县', '洛扎县', '加查县', '错那县', '措美县', '贡嘎县', '班戈县', '巴青县', '比如县', '嘉黎县', '尼玛县', '普兰县', '日土县', '改则县', '蓝田县', '宜君县', '陇县', '凤翔县', '扶风县', '千阳县', '三原县', '乾县', '永寿县', '长武县', '淳化县', '大荔县', '澄城县', '白水县', '延长县', '', '志丹县', '甘泉县', '洛川县', '黄龙县', '洋县', '西乡县', '略阳县', '留坝县', '府谷县', '定边县', '米脂县', '吴堡县', '子洲县', '石泉县', '紫阳县', '镇坪县', '旬阳县', '洛南县', '柞水县', '山阳县', '榆中县', '永登县', '会宁县', '景泰县', '秦安县', '武山县', '金塔县', '民乐县', '高台县', '民勤县', '陇西县', '渭源县', '临洮县', '两当县', '西和县', '康县', '徽县', '灵台县', '静宁县', '正宁县', '合水县', '庆城县', '环县', '康乐县', '永靖县', '夏河县', '舟曲县', '迭部县', '卓尼县', '海晏县', '刚察县', '泽库县', '同德县', '兴海县', '玛沁县', '甘德县', '久治县', '杂多县', '治多县', '曲麻莱县', '都兰县', '永宁县', '平罗县', '盐池县', '隆德县', '彭阳县', '海原县', '鄯善县', '伊吾县', '伊宁县', '巩留县', '昭苏县', '额敏县', '托里县', '布尔津县', '福海县', '青河县', '呼图壁县', '奇台县', '精河县', '轮台县', '若羌县', '和静县', '博湖县', '沙雅县', '拜城县', '阿瓦提县', '阿克陶县', '乌恰县', '疏勒县', '泽普县', '叶城县', '岳普湖县', '巴楚县', '墨玉县', '洛浦县', '于田县', '苗栗县', '南投县', '新竹县', '屏东县', '花莲县', '澎湖县', '大厂回族自治县', '宽城满族自治县', '围场满族蒙古族自治县', '桓仁满族自治县', '新宾满族自治县', '宽甸满族自治县', '喀喇沁左翼蒙古族自治县', '长白朝鲜族自治县', '杜尔伯特蒙古族自治县', '长阳土家族自治县', '靖州苗族侗族自治县', '芷江侗族自治县', '麻阳苗族自治县', '江华瑶族自治县', '连南瑶族自治县', '环江毛南族自治县', '巴马瑶族自治县', '大化瑶族自治县', '三江侗族自治县', '龙胜各族自治县', '富川瑶族自治县', '昌江黎族自治县', '乐东黎族自治县', '保亭黎族苗族自治县', '石柱土家族自治县', '酉阳土家族苗族自治县', '马边彝族自治县', '北川羌族自治县', '威宁彝族回族苗族自治县', '务川仡佬族苗族自治县', '镇宁布依族苗族自治县', '印江土家族苗族自治县', '松桃苗族自治县', '三都水族自治县', '玉龙纳西族自治县', '禄劝彝族苗族自治县', '峨山彝族自治县', '元江哈尼族彝族傣族自治县', '耿马傣族佤族自治县', '景东彝族自治县', '澜沧拉祜族自治县', '景谷傣族彝族自治县', '江城哈尼族彝族自治县', '孟连傣族拉祜族佤族自治县', '维西傈僳族自治县', '贡山独龙族怒族自治县', '南涧彝族自治县', '河口瑶族自治县', '金平苗族瑶族傣族自治县', '肃南裕固族自治县', '阿克塞哈萨克族自治县', '东乡族自治县', '大通回族土族自治县', '循化撒拉族自治县', '化隆回族自治县', '河南蒙古族自治县', '和布克赛尔蒙古自治县', '察布查尔锡伯自治县', '焉耆回族自治县']


# 连接到本地Redis实例
r = redis.Redis(host='192.168.1.30', port=6379, db=11)

# 要存储的float对象
float_value = 3.14159

# # 将float对象转换为字符串并存储
r.set('float_key', str(float_value))
# print(r.get('machine2req'))
# print(r.get('machine2parse'))
# print(r.get('machine2req'))
# 从Redis中检索字符串并转换回float对象
retrieved_value = float(r.get('float_key'))
for i in range(10):
    print(i)
print(retrieved_value)  # 输出: 3.14159