#nand computation
with open('inverter_leakages.txt', 'r') as pmos_file:
    lines = pmos_file.readlines()
with open('nand_leakages.txt', 'r') as pmos_file:
    lines1 = pmos_file.readlines()
with open('nor_leakage.txt', 'r') as pmos_file:
    lines2 = pmos_file.readlines()

inverter = []
And = []
Or = []
for i in range(2):
    line = lines[i]
    values = line.split()
    inverter.append(float(values[0]))

for i in range(4):
    line = lines1[i]
    values = line.split()
    value = float(values[0])
    And.append(value)

for i in range(4):
    line = lines2[i]
    values = line.split()
    value = float(values[0])
    Or.append(value)

for i in range(4):
    if(i == 3):
        And[i] = And[i] + inverter[0]
    else:
        And[i] = And[i] + inverter[1]

for i in range(4):
    if(i == 0):
        Or[i] = Or[i] + inverter[1]
    else:
        Or[i] = Or[i] + inverter[0]

print(inverter)
print(And)
print(Or)

arr = [0.035983259573583996, 0.03716964276512912, 0.0578508709326493, 0.11756622828261959, 0.06381535863389952, 0.05193545724780738, 0.08287476298200837, 0.13033927432634548, 0.07702972164948199, 0.07732785193342699, 0.09324060628473478, 0.147654199723491, 0.16045520538558197, 0.14698335610097812, 0.2099236539225037, 0.19287908498617715, 0.09008590559870747, 0.07760868179279089, 0.10699878936929366, 0.15570585356190061, 0.07680269548507972, 0.06533041351253516, 0.09408354992892311, 0.1397353893503305, 0.12315796925754122, 0.11136478361285942, 0.13603976341909801, 0.18014263218716556, 0.1682555733820555, 0.1552507206999041, 0.21528739573907946, 0.19911706384915076, 0.09639465438787283, 0.09634637008545782, 0.1110493236839707, 0.16588418310719005, 0.11916852931733136, 0.10781329982515206, 0.13224962820643602, 0.17576516105707005, 0.12587925281150544, 0.12479429509732144, 0.1377222312510699, 0.18933339236525656, 0.20224806203270837, 0.18949524342491336, 0.24669182031801742, 0.2317952852323479, 0.17687411480607126, 0.1634562400976746, 0.18621153628795512, 0.23561540917893067, 0.16082324198208384, 0.14843527230037765, 0.1709143424230872, 0.21733028314551553, 0.2367488993009551, 0.22274112450562555, 0.2554437940990895, 0.2679054286924431, 0.21717755651423548, 0.2038619050058716, 0.23656658328282706, 0.2209117312506393, 0.11732876701121908, 0.10396765212290213, 0.13230854587188204, 0.1834633157618199, 0.10259150860965958, 0.09021292482697577, 0.11803680569641174, 0.16588621172702298, 0.1473673722818568, 0.1351864792628132, 0.15884631209221317, 0.20519345126824295, 0.19415937611017234, 0.18037507185554535, 0.24171264324781747, 0.22553627742408888, 0.1011490139816349, 0.08910479286712478, 0.11634775580555624, 0.16304541868429606, 0.08817823798660226, 0.07695264113246568, 0.10377683250119829, 0.14758010289907636, 0.13134551871314093, 0.12014710788338602, 0.1426519580905017, 0.18574401317288594, 0.17434260622943262, 0.16186090994376817, 0.21894808301376312, 0.20363450041404763, 0.1661271754535608, 0.15363361923776014, 0.17583676007545238, 0.22249641974401999, 0.15122998681178415, 0.13955988123757135, 0.1618570386869134, 0.20553587270342416, 0.1880495933148483, 0.1768031779465988, 0.19648055263805655, 0.2404180175759284, 0.23089044832747696, 0.21832959291032059, 0.2739856957659714, 0.25976072950007917, 0.18261680558757826, 0.16986330488707665, 0.19081578483085812, 0.23826313579790992, 0.16711690360642048, 0.15520441953574465, 0.1766965134416605, 0.22075532444057736, 0.23926778361776785, 0.225985867482896, 0.25700654217797486, 0.26889594692829455, 0.2206156645804575, 0.20786722420818657, 0.23909085237518046, 0.224338215485686, 0.09975341315128097, 0.09963653072650688, 0.11538907838096163, 0.17488003415381234, 0.12443404572804373, 0.11194007069827663, 0.1377893404212088, 0.18533015353495408, 0.130540128952116, 0.12991727443831927, 0.1424285804664172, 0.19658373500866197, 0.21225355052717113, 0.19847966631687816, 0.25825340453593615, 0.24271139312112439, 0.1488886891593421, 0.1358765989940272, 0.1603730731816046, 0.20910230846612737, 0.1338528960452097, 0.12174013672616925, 0.14593839122350635, 0.19171029954074364, 0.17296539411451528, 0.16102867723069791, 0.18210667692258456, 0.22639615513212924, 0.21724833177327232, 0.2039854643105672, 0.26113310916484067, 0.2462191268364465, 0.13407334133839335, 0.1333619026081529, 0.14592387546331453, 0.20222699794728655, 0.1558854409645388, 0.14378105492730664, 0.1662949144404907, 0.21119327331368581, 0.14583857571392805, 0.14498646799133721, 0.14263207977819767, 0.18488679367633906, 0.21300105790076357, 0.19980847905048896, 0.23202642107556687, 0.21660640048212446, 0.20205116752294283, 0.18834522788066904, 0.20928373636740788, 0.25902696136717807, 0.1848848815133273, 0.17242312506486557, 0.1933088383840185, 0.24006792996943402, 0.23540703410356595, 0.22130123041038197, 0.22762524692801842, 0.23963443805817736, 0.21567614287911688, 0.20216895095793047, 0.20765079655783095, 0.19143358594937815, 0.1718661131667035, 0.15764870286571744, 0.18220100602402964, 0.23473993615516697, 0.1549841930689421, 0.14180750614895857, 0.16613797320989004, 0.2153040756287495, 0.19423145066853534, 0.18132269096951922, 0.20230198791875492, 0.24976496007960933, 0.2413154355306587, 0.22692306361626566, 0.2870387589847587, 0.2717750042463691, 0.1523176112922891, 0.13962055397183554, 0.1634182486131543, 0.21126810089140544, 0.1374459317037015, 0.12561250453507355, 0.1491401492066739, 0.1941403306321051, 0.17561728568382773, 0.16366312331505742, 0.18480259502586818, 0.22798910104636633, 0.21900213812719843, 0.20606566295214737, 0.26199714139731795, 0.24749300842952215, 0.1997166216450168, 0.18562302481829057, 0.2073438967881763, 0.2585717776955126, 0.1823274811935348, 0.16933449770850173, 0.19098613491290384, 0.23905174043878824, 0.20639003891540073, 0.19287082762572968, 0.19982426924602978, 0.23794485250040212, 0.21386619327344783, 0.19998029612650178, 0.23390954984368506, 0.21768389210731162, 0.17620316574332642, 0.16324158314028506, 0.18536854181823761, 0.23349433372831127, 0.1602661551248202, 0.14838266024360383, 0.17045237746754646, 0.21573622533231526, 0.1822124091043717, 0.16921851954462797, 0.17493936360926404, 0.18528223382166153, 0.16314246602953983, 0.15061844125705504, 0.15356728481984439, 0.13655547431398676, 0.03300889482260459, 0.03032403981585115, 0.004814533702300729, 0.05253424639086255, 0.002819031378952852, 0.01341451730301254, 0.022387990595072817, 0.06732484853469839, 0.01835959294701645, 0.019744094176193123, 0.03896605495374679, 0.09167688365045185, 0.1001563080637644, 0.08782631436878763, 0.15166085859956227, 0.13350879133065652, 0.024420986372430103, 0.01318346410347143, 0.04732739373481102, 0.09372426613308865, 0.0141408541553142, 0.0036894916657386184, 0.036693838040804096, 0.080314903977097, 0.06714900302325304, 0.05645112975007854, 0.0840740634782664, 0.12676586003955387, 0.11115854054285712, 0.09907064149160971, 0.16002894410114654, 0.14286014011783357, 0.038658784797267615, 0.03966315455060314, 0.05801323542477816, 0.11114399225977752, 0.06331892891921635, 0.05275191931621389, 0.08043276001012563, 0.12256051213779016, 0.074972472518867, 0.07547269548389787, 0.08971479997799735, 0.13987854178989537, 0.15030540946011525, 0.13830241263123857, 0.19602033216037934, 0.18037577651837722, 0.1189864550851112, 0.10662137532571367, 0.13297164285385488, 0.18064108973187726, 0.10527442923272162, 0.0936523664849756, 0.11956136240127556, 0.16434715290128382, 0.18344152676542783, 0.1703198845754851, 0.2038916059645541, 0.21517802929326588, 0.16420457602293503, 0.15156167871291307, 0.1833362234917118, 0.16685394354653038, 0.05126817749091234, 0.039152739516446974, 0.07232348364648888, 0.12117947414647809, 0.03944327460959501, 0.028207881726095563, 0.060460977714413125, 0.10617705963733008, 0.09109239796239071, 0.0797035471480344, 0.10665911950153405, 0.15130624413280175, 0.13681447585376288, 0.12405967231990932, 0.186254232242846, 0.16906017887408314, 0.039580088730789297, 0.028739098477362533, 0.06008973573234653, 0.1046375395663603, 0.02915050227655716, 0.019038567143466703, 0.049544770950331864, 0.09144513651094006, 0.07825685948575771, 0.06786081841749111, 0.09387473737864883, 0.13475835721698315, 0.12038511682938226, 0.10882622569446734, 0.16674912390672575, 0.1504327925210941, 0.11074734039466243, 0.09901291582045087, 0.12462908298307898, 0.169781823338011, 0.09789922221922144, 0.08693397343456727, 0.11211226679090999, 0.1546620153187195, 0.139025689111595, 0.12817173840793897, 0.1509973910414314, 0.1926186214655474, 0.18118406208218313, 0.16891101668318662, 0.22547394419722666, 0.21055937555323287, 0.1280648607536536, 0.11604076846843851, 0.1406025364372833, 0.18632157114306486, 0.11454884605888993, 0.10331489541745463, 0.12761415240291302, 0.17059574543268297, 0.1888200059840359, 0.17613571553584972, 0.20803705738038097, 0.21887344791783786, 0.17036794202602354, 0.15821841992935606, 0.18860804604407208, 0.17301332052574203, 0.05736586299703359, 0.05805652044209074, 0.07595173685503091, 0.13241903474466418, 0.08254594989512865, 0.07123233950353232, 0.09899053566024937, 0.1437840584700349, 0.09303285972401801, 0.09304367832834827, 0.10741995333622284, 0.15879588714234597, 0.17139764968312518, 0.15874098546629622, 0.2173772989400953, 0.20151101819520711, 0.10681104517233804, 0.09498680772253687, 0.12141253444446942, 0.16737788318327326, 0.09383248937854442, 0.08280212307593059, 0.10875192069578635, 0.15200982984942615, 0.13579826419424168, 0.12441261136140404, 0.14739551422417382, 0.18919648559190264, 0.17817518067665233, 0.16593909503975016, 0.22194481326409934, 0.20693625314721223, 0.11123490389715178, 0.11093782261501703, 0.12468288587044853, 0.17710479434682275, 0.132727202495422, 0.12154388315139261, 0.14364996786729872, 0.1862733449576276, 0.1385722265859777, 0.1382486580970705, 0.13509752319776738, 0.1752095958140352, 0.2131531767195073, 0.20063288151533815, 0.23117696902913792, 0.21657062159090743, 0.18816372445671062, 0.17528760103577215, 0.1962589860889861, 0.24372424859864106, 0.17212005333349145, 0.16039416257859362, 0.18107197052992732, 0.22597988295503618, 0.24683010308875797, 0.23322724439376044, 0.2394096619522017, 0.2511050048261186, 0.2279427365333759, 0.21478910396666256, 0.22061575116363055, 0.20517168835760066, 0.1409216048559513, 0.12746109675033906, 0.15367333874231678, 0.20426042264089056, 0.12554926700990424, 0.11305831737248664, 0.1387922941156825, 0.18628433663444677, 0.16716379210930474, 0.15483584970838912, 0.17734464987867604, 0.22287275009994886, 0.21312371199888486, 0.19936065051507912, 0.25901624892146224, 0.243515389695811, 0.12359906444083936, 0.11144564321575935, 0.13679304434128778, 0.18305153286221695, 0.110032252765012, 0.09868990318785367, 0.12364019808993283, 0.16718415468111772, 0.15066193369795397, 0.13892108568190853, 0.16013192781458516, 0.20298169855787457, 0.1926694782291303, 0.18018278518447575, 0.23581189147172757, 0.2211009405595597, 0.19847907416465216, 0.1848585445181529, 0.20612738683705797, 0.2560613648605652, 0.18165762720689688, 0.16897606294026477, 0.19017518928692864, 0.23709693840590676, 0.23192159214679947, 0.2182765577035543, 0.2244215083660964, 0.26244483006467983, 0.2392967726225059, 0.22540341891164928, 0.2588790571530286, 0.24352180537891752, 0.17567247883041517, 0.16291609313366365, 0.18467480375938744, 0.23154806923355534, 0.16011964760258537, 0.14849976627928152, 0.1696216743378402, 0.21426385077438415, 0.20864457188042926, 0.19548710723517587, 0.20142048142217234, 0.21217001387137435, 0.1898317760484349, 0.17732665058410238, 0.18134493686920958, 0.16535972810592306]
average = sum(arr) / len(arr)

# Find minimum value and its index
min_value = min(arr)
min_index = arr.index(min_value)

# Find maximum value and its index
max_value = max(arr)
max_index = arr.index(max_value)

# Print results
print("Average:", average)
print("Minimum value:", min_value,"at index",min_index)
print("Maximum value:", max_value,"at index",max_index)