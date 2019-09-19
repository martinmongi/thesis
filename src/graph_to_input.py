from random import sample, choice, uniform, shuffle
from utils import haversine_dist
from pprint import pprint
from optparse import OptionParser


def generate_students(n, stops, max_w):
    max_w_deg = max_w / 78710
    students = []
    for _ in range(n):
        st = choice(stops[1:])
        while True:
            std = (uniform(st[0] - max_w_deg, st[0] + max_w_deg),
                   uniform(st[1] - max_w_deg, st[1] + max_w_deg))
            if haversine_dist(std, st) <= max_w:
                break
        students.append(std)
    return students


parser = OptionParser()
parser.add_option("--if", dest="in_file")
# parser.add_option("--of", dest="out_file")
parser.add_option("--N", "--stops", dest="N")
parser.add_option("--S", "--students", dest="S")
parser.add_option("--MAXW", "--max_walking_distance", dest="MAXW")
parser.add_option("--K", "--depots", dest="K")
parser.add_option("--C", "--capacity", dest="CAPACITY")
parser.add_option("--hardcode", dest="HARDCODE")

(options, args) = parser.parse_args()

N = int(options.N)
S = int(options.S)
MAXW = float(options.MAXW)
K = int(options.K)
CAPACITY = int(options.CAPACITY)

with open(options.in_file, 'r') as f:
    g = eval(f.readline())

vset = sample(list(g), k=N)

if options.HARDCODE:
    if options.HARDCODE == "barracas":
        vset = [(-58.3995315759582, -34.6509575272884), (-58.3765807795484, -34.6278938507396), (-58.3927225510848, -34.6526506123645), (-58.3722073983387, -34.6394033918234), (-58.375070367351, -34.6543667340355), (-58.3828573843635, -34.6491425780634), (-58.3952117995134, -34.6541936574633), (-58.382309550051, -34.6473774843598), (-58.388452216846, -34.6581894377734), (-58.3833201541685, -34.6566290577465), (-58.3743527909516, -34.6333206240939), (-58.3945294293527, -34.6620507137364), (-58.3949642750481, -34.6572602278624), (-58.3954672824905, -34.6509589192549), (-58.3819900948889, -34.654961759612), (-58.370393517092, -34.6483769530691), (-58.371587034402, -34.6310313702691), (-58.3714045843483, -34.6382567232486), (-58.4027479535339, -34.6558710235517), (-58.3912545398064, -34.6434344044505), (-58.3726963889906, -34.6368964804596), (-58.3766736094788, -34.6501946169259), (-58.3812539632874, -34.63306855776), (-58.3963097603206, -34.646902102113), (-58.3955405564987, -34.65003155916), (-58.3716307213807, -34.651258754282), (-58.3688266546662, -34.6429199334654), (-58.385490400789, -34.6548381272459), (-58.3835210114978, -34.6330191664044), (-58.3736806799315, -34.6296768016422), (-58.3885544445181, -34.6569064649303), (-58.383395047952, -34.632219055392), (-58.3878831927972, -34.6350193345977), (-58.3902896907866, -34.6557127204528), (-58.3932422189751, -34.6519349213586), (-58.3994091957013, -34.6565862450091), (-58.3712942928419, -34.6328125053323), (-58.3788865550052, -34.6531642872198), (-58.376162995612, -34.6321914268215), (-58.3783896144486, -34.6410724443939), (-58.3886565836548, -34.6556236325195), (-58.3873815823568, -34.6508589413313), (-58.3790480340741, -34.6293320164902), (-58.3772882597299, -34.636827239812), (-58.3888734154848, -34.6352795932223), (-58.3917850044695, -34.6570840373656), (-58.3966429624402, -34.6501011421136), (-58.3867956262902, -34.6581005921934), (-58.3751403804105, -34.6444205884615), (-58.3865232510815, -34.6331398060705), (-58.3724127993083, -34.6277899128932), (-58.3706451988712, -34.6539325610314), (-58.3798720949896, -34.6413572023196), (-58.3805634320805, -34.6453355925657), (-58.3817639087834, -34.6369532320773), (-58.3747328233305, -34.637846153805), (-58.3800957868889, -34.6326306562322), (-58.3838623285038, -34.6325762729133), (-58.3956516256515, -34.6486271741421), (-58.3801544321494, -34.6468592695951), (-58.3767221041974, -34.6308385720793), (-58.3799507252063, -34.6422245872111), (-58.3827249752355, -34.6528263888975), (-58.3812842293049, -34.6323551204258), (-58.3744115377445, -34.63966783738), (-58.3885154714457, -34.6467822887239), (-58.3711898291118, -34.6392964294407), (-58.3719860558317, -34.6294334140507), (-58.3922434515895, -34.6513537057125), (-58.3722907862872, -34.6338903759743), (-58.3730932514203, -34.6466631929347), (-58.3915500039948, -34.6498125143287), (-58.4029723455468, -34.6552115384895), (-58.3735492098838, -34.6377381748987), (-58.3734402805678, -34.6558180509907), (-58.4035830333166, -34.6532686723723), (-58.3728849212892, -34.6359731612653), (-58.4010754802931, -34.6560405423195), (-58.3730883609427, -34.6349697814926), (-58.3740458184954, -34.6415939245218), (-58.4003872001938, -34.652453126678), (-58.3873248037294, -34.635844277484), (-58.3771335313962, -34.6489481735296), (-58.3885751102688, -34.6394792377043), (-58.3742439954501, -34.6405716665012), (-58.4008117906562, -34.6568992942388), (-58.4020113775962, -34.6576131307626), (-58.3954285713505, -34.6515096057129), (-58.3812296264986, -34.6336436878016), (-58.3796096250689, -34.649446380411), (-58.3726428572431, -34.6423219801485), (-58.3923598549407, -34.649857002549), (-58.3948419463306, -34.6514962495268), (-58.3979329639788, -34.656244082456), (-58.3738780116651, -34.6517054259529), (-58.3864331509551, -34.6466718381937), (-58.3924641616724, -34.6484510671861), (-58.3869715577316, -34.6561168176781), (-58.3714893085614, -34.6485875732295), (-58.3738911692415, -34.642386212099)]
    elif options.HARDCODE == "telmo":
        vset = [(-58.3694619003706, -34.6165735363312), (-58.3691455669587, -34.6157917336099), (-58.3698017083908, -34.6171645791492), (-58.3658853661917, -34.6233090521743), (-58.3675724015812, -34.6156840995449), (-58.3699775161048, -34.6206728543066), (-58.3665965504383, -34.6168777812925), (-58.3759800252477, -34.6162190756999), (-58.3672880731436, -34.618195315339), (-58.3702746686521, -34.6166043000222), (-58.367433149312, -34.616927878814), (-58.3726735113255, -34.6243226750345), (-58.3711924174847, -34.6242358604893), (-58.3729419473916, -34.6196032425012), (-58.3772321449433, -34.6208831204657), (-58.3716913502741, -34.61665790793), (-58.369302103368, -34.618383787489), (-58.372626678311, -34.6254779346272), (-58.3756035278333, -34.6272638257197), (-58.3744426813242, -34.6172519220776), (-58.3731316007411, -34.6160287618583), (-58.3750610000132, -34.6256407075492), (-58.3691583824399, -34.6183731641986), (-58.3716039078395, -34.6184813151805), (-58.3697563806587, -34.624159062634), (-58.3743059447007, -34.6196640346354), (-58.3758537381649, -34.6185395770953), (-58.3706970769011, -34.6291879327158), (-58.3772023870658, -34.6220650145937), (-58.3667749961952, -34.6226993996497), (-58.3701009906641, -34.6165977589327), (-58.3679754217283, -34.6251940332981), (-58.3728541869498, -34.6207212188066), (-58.3666204596284, -34.6240266160659), (-58.3694485902849, -34.6283216878452), (-58.3697516521946, -34.6222847650841), (-58.3773618429219, -34.6174511285039), (-58.3762283962606, -34.6262681729681), (-58.3683153242606, -34.6216863014297), (-58.3755547534025, -34.6233867429502), (-58.3701110780232, -34.6193856173068), (-58.3706622348626, -34.6294922755746), (-58.3717181969878, -34.6160242582574), (-58.3688159147727, -34.6157713901692), (-58.3684370188151, -34.6205961722389), (-58.3713367362319, -34.6218348155014), (-58.3716396874903, -34.6178590810202), (-58.3686864248866, -34.6170051551036), (-58.3757393169234, -34.6208294518232), (-58.3774292231301, -34.6162922883787), (-58.3740328449421, -34.6244350870638), (-58.3709677445767, -34.6266457168852), (-58.3741124796329, -34.6232571743912), (-58.366194624662, -34.6204208846995), (-58.3714220122462, -34.620671838114), (-58.3702099649562, -34.6177943356596), (-58.3739697954207, -34.6255566025354), (-58.3758047401344, -34.6196926543715), (-58.3717211434901, -34.6159784148278), (-58.3687726577932, -34.6183356313338), (-58.3759152922577, -34.6173524940719), (-58.3716705626346, -34.617203532834), (-58.3687028498966, -34.6192970329386), (-58.3754759078946, -34.6245625444242), (-58.3684859045207, -34.6194108956435), (-58.3745835005697, -34.6267595229402), (-58.3741672134637, -34.6219422698392), (-58.3667388080788, -34.6156239348096), (-58.3745373662307, -34.6160871174382), (-58.3721011920138, -34.620288258754), (-58.36972716474, -34.6252938414385), (-58.3657901681724, -34.6239859547338), (-58.3685944818262, -34.6183154172759), (-58.3707976910143, -34.6281137725779), (-58.36949853916, -34.6158134968029), (-58.3671612298644, -34.6193081864964), (-58.3698784554967, -34.6171663985306), (-58.3660713718019, -34.6215074892502), (-58.3664557513913, -34.6181188818719), (-58.3728018080479, -34.6218887991295), (-58.3705689102024, -34.6158931067625), (-58.3670272395031, -34.6204845031196), (-58.3743652650842, -34.6185161768286), (-58.3697528562599, -34.6217579764862), (-58.368964365, -34.6191996633131), (-58.3772718462442, -34.6197228530878), (-58.3689891343949, -34.6170326844563), (-58.3701565330508, -34.6184243024939), (-58.3659405413778, -34.6226607079026), (-58.3702513077412, -34.6158599067762), (-58.3695442246466, -34.6177510788319), (-58.3680635139605, -34.62407085032), (-58.3720866080029, -34.6206933934435), (-58.3742278532319, -34.6207588497011), (-58.3669021100186, -34.6215825860317), (-58.3714554244209, -34.6202676331861), (-58.3770866814318, -34.623486075823), (-58.3664921721112, -34.6251939215099), (-58.3767543753931, -34.6251128304597), (-58.371097541784, -34.6253682660577)]
    elif options.HARDCODE == "boca":
        vset = [(-58.3588553027156, -34.6383642285023), (-58.3666238816315, -34.6370137206122), (-58.3591741937097, -34.6336727137174), (-58.3677652384505, -34.6389591441337), (-58.3662473101925, -34.6341782921097), (-58.3615772085469, -34.6397479768565), (-58.3648754868704, -34.6482979757264), (-58.3633059657973, -34.6399633245393), (-58.357911923133, -34.6369517849023), (-58.3580654409307, -34.6425639363932), (-58.3537239126408, -34.6355700536467), (-58.3596829038519, -34.6282788529857), (-58.3594363198079, -34.6314507877897), (-58.359773929909, -34.6338273939431), (-58.3681770138557, -34.6473319972994), (-58.3631997038792, -34.63706462073), (-58.3624754158645, -34.6425409013009), (-58.3701099624575, -34.6345563411218), (-58.358554069907, -34.6450349395404), (-58.359182262912, -34.6442008936872), (-58.3670740611889, -34.6436791325768), (-58.3561850146713, -34.6372373956479), (-58.3642837936003, -34.631351297169), (-58.3688266546662, -34.6429199334654), (-58.3665980938655, -34.6325107004971), (-58.3678997569328, -34.6380831150465), (-58.3695745928668, -34.638016666571), (-58.3632365420686, -34.6390964292545), (-58.3694485902849, -34.6283216878452), (-58.3639797554917, -34.6343294588437), (-58.3581754029806, -34.630914138909), (-58.3581076166813, -34.6350075701171), (-58.3621451754794, -34.6266575225375), (-58.3650146642202, -34.630872446938), (-58.3631826675481, -34.6289768533629), (-58.3589855991325, -34.6322913268004), (-58.3651623247058, -34.6395402514005), (-58.353799821718, -34.6312297289466), (-58.3623584631026, -34.6310459131743), (-58.3654655138877, -34.6444486333709), (-58.3647651035483, -34.6402566273078), (-58.3673738927429, -34.6276366160336), (-58.361780671964, -34.6364921046729), (-58.3623453147086, -34.6416172651018), (-58.3653358445512, -34.6453007188746), (-58.3651785471585, -34.6322766067591), (-58.3685865541726, -34.6334610727682), (-58.3680994760834, -34.6315188437331), (-58.3625197918216, -34.6417101566431), (-58.36818143073, -34.636299938853), (-58.3616460233197, -34.6286240295025), (-58.3659211645728, -34.6414323543523), (-58.3618865085019, -34.645368463068), (-58.3624535037358, -34.6294583702662), (-58.3573973787852, -34.6377617688471), (-58.3620849877014, -34.6290776386215), (-58.3656389429849, -34.6386840069268), (-58.3598429508694, -34.6284415961465), (-58.3662400671689, -34.6300673197342), (-58.3605449031952, -34.6448509276522), (-58.3633066739477, -34.631989520364), (-58.3659072077953, -34.6317959184738), (-58.3606835443091, -34.6276215934995), (-58.3630699267052, -34.6250089973263), (-58.3706622348626, -34.6294922755746), (-58.3657616913534, -34.6424947003208), (-58.3660674308447, -34.6405125338608), (-58.3602624649089, -34.6418609476384), (-58.3580172879184, -34.6339415668096), (-58.3692497299385, -34.6401141106394), (-58.3631330922163, -34.6450585051048), (-58.3602184049033, -34.6258884365212), (-58.3674886789186, -34.6407990836226), (-58.3558943167301, -34.6320710360755), (-58.361303591695, -34.6392515864508), (-58.3608192980119, -34.6320221040221), (-58.3703633010244, -34.6326878546327), (-58.3646422109009, -34.6385516542672), (-58.3588891946032, -34.6353199347046), (-58.3679754217283, -34.6251940332981), (-58.3608152960719, -34.638116241215), (-58.370251843187, -34.6336203138301), (-58.3640578131068, -34.6265902901172), (-58.3684762675575, -34.6343940945015), (-58.3570508513823, -34.6279434866627), (-58.359463516931, -34.6263749845397), (-58.3646969486337, -34.6366487239997), (-58.359515064252, -34.6338945620444), (-58.3611471260427, -34.6466939120902), (-58.3656031633923, -34.6435467648774), (-58.3686958672915, -34.6438135011211), (-58.353349525782, -34.6331268068404), (-58.3634839484296, -34.6351368080631), (-58.3679493413402, -34.6271409352361), (-58.364084189989, -34.6299097825757), (-58.3626285281195, -34.6436040643544), (-58.365562920073, -34.6368859020328), (-58.3696743223826, -34.6373732163441), (-58.3655776237262, -34.6289250626971), (-58.3665047894914, -34.6476287821622)]
    print(len(vset), "PARADAS HARDCODEADAS, VOY A USAR", N)
else:
    vset = sample(list(g), k=N)

if N > len(vset):
    raise ValueError

vset = vset[:N]

students = generate_students(S, vset, MAXW)

depots = vset[1:K+1]

path = options.in_file.split("\\")
fn = path[-1].split(".")[0]
# print(path)
rfn = "_".join(["\\".join(path[:-1] + [fn]), str(N), str(S),
                str(K) + "x" + str(CAPACITY), str(round(MAXW)) + ".in"])
# print(rfn)

with open(rfn, 'w') as f:
    f.write(str(g) + '\n')
    f.write(str(vset) + '\n')
    f.write(str(students) + '\n')
    f.write(str(MAXW) + '\n')
    f.write(str(depots) + '\n')
    f.write(str(CAPACITY) + '\n')
