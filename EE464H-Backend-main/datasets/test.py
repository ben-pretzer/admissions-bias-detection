import pandas as pd
import math
# from utils.counting_utils import counting_utils
# from constants.specific_region_data import region_enum

#en = enrolled
#g = gender specific(Breakdown of race and gender)
#grad = graduation rate
from fastapi.encoders import jsonable_encoder

#US_dict = {'name':'US','Gender':45,'Asian':6.59,'Black':11.1,'White':59.1,'Hispanic':13.06,'American Indian':.61,'Multiracial':2.85,'Non-resident':6.68}
en_Southeast = {'Name': 'en_Southeast', 'Total': 3287671611, 'Asian': 0.06798540835166156, 'Black or African American': 0.13416443008608014, 'Native Hawaiian or Other Pacific Islanders': 0.003333283641630715, 'Hispanic or Latino': 0.22854853370572845, 'Two or More Races': 0.040897789046243034, 'American Indian or Alaskan Native': 0.006693024305218542, 'White': 0.5183775308634375}
en_Soutwest = {'Name': 'en_Soutwest', 'Total': 1227097367, 'Asian': 0.070929385345181, 'Black or African American': 0.13218624321276048, 'Native Hawaiian or Other Pacific Islanders': 0.003307235521107593, 'Hispanic or Latino': 0.23113095474517467, 'Two or More Races': 0.041112097015851556, 'American Indian or Alaskan Native': 0.006586474078873971, 'White': 0.5147476100810507}
en_Northeast = {'Name': 'en_Northeast', 'Total': 2882487460, 'Asian': 0.06884760463103629, 'Black or African American': 0.13393577226525039, 'Native Hawaiian or Other Pacific Islanders': 0.0032497119692586627, 'Hispanic or Latino': 0.21761918922623866, 'Two or More Races': 0.04071057745382178, 'American Indian or Alaskan Native': 0.006396325137872413, 'White': 0.5292408193165219}
en_Midwest = {'Name': 'en_Midwest', 'Total': 2962537766, 'Asian': 0.0667258984066568, 'Black or African American': 0.13410977256044876, 'Native Hawaiian or Other Pacific Islanders': 0.003321579934923942, 'Hispanic or Latino': 0.22412289612648267, 'Two or More Races': 0.0407030183324252, 'American Indian or Alaskan Native': 0.0066834351370088155, 'White': 0.5243333995020538}
en_West = {'Name': 'en_West', 'Total': 2224983117, 'Asian': 0.06895399017987246, 'Black or African American': 0.13372092881368142, 'Native Hawaiian or Other Pacific Islanders': 0.0034181886333836844, 'Hispanic or Latino': 0.23686488898423402, 'Two or More Races': 0.040753805414155866, 'American Indian or Alaskan Native': 0.006749585147526313, 'White': 0.5095386128271462}
grad_Southeast = {'Name': 'grad_Southeast', 'Total': 278420, 'Asian': 0.04027368723511242, 'Black or African American': 0.16767114431434524, 'Native Hawaiian or Other Pacific Islanders': 0.0, 'Hispanic or Latino': 0.1059622153580921, 'Two or More Races': 0.028097837799008693, 'American Indian or Alaskan Native': 0.002535737375188564, 'White': 0.655459377918253}
grad_Southwest = {'Name': 'grad_Southwest', 'Total': 107235, 'Asian': 0.06728213736186879, 'Black or African American': 0.07729752412924884, 'Native Hawaiian or Other Pacific Islanders': 0.0, 'Hispanic or Latino': 0.30736233505851634, 'Two or More Races': 0.03890520818762531, 'American Indian or Alaskan Native': 0.018389518347554437, 'White': 0.4907632769151863}
grad_Northeast = {'Name': 'grad_Northeast', 'Total': 240913, 'Asian': 0.09432865806328426, 'Black or African American': 0.08906534724153532, 'Native Hawaiian or Other Pacific Islanders': 0.0, 'Hispanic or Latino': 0.11735356747041463, 'Two or More Races': 0.029180658577992884, 'American Indian or Alaskan Native': 0.002125248533703038, 'White': 0.6679465201130699}
grad_Midwest = {'Name': 'grad_Midwest', 'Total': 236423, 'Asian': 0.04562584858495155, 'Black or African American': 0.05172085626186961, 'Native Hawaiian or Other Pacific Islanders': 0.0, 'Hispanic or Latino': 0.06803060615929922, 'Two or More Races': 0.027222393760336347, 'American Indian or Alaskan Native': 0.0011377911624503537, 'White': 0.8062625040710929}
grad_West = {'Name': 'grad_West', 'Total': 190184, 'Asian': 0.16121755773356328, 'Black or African American': 0.03126971774702393, 'Native Hawaiian or Other Pacific Islanders': 0.0, 'Hispanic or Latino': 0.2965864636352164, 'Two or More Races': 0.057097337315441886, 'American Indian or Alaskan Native': 0.006278130652420813, 'White': 0.44755079291633365}
en_g_Southeast = {'Name': 'en_g_Southeast', 'Total': [444672, 620405], 'Asian': [0.0419747589234312, 0.0357024846672738], 'Black or African American': [0.15511658031088082, 0.21087193043254004], 'Native Hawaiian or Other Pacific Islanders': [0.0017136226252158894, 0.0015844488680781103], 'Hispanic or Latino': [0.12149404504893495, 0.12395128988322145], 'Two or More Races': [0.029759013385146804, 0.03224023017222621], 'American Indian or Alaskan Native': [0.00459214881980426, 0.004619563027377278], 'White': [0.645349830886586, 0.5910300529492831]}
en_g_Southwest = {'Name': 'en_g_Southwest', 'Total': [201470, 301853], 'Asian': [0.06326996575172482, 0.05263157894736842], 'Black or African American': [0.09491239390479972, 0.12172150020042868], 'Native Hawaiian or Other Pacific Islanders': [0.00258102943366258, 0.0023190095841353242], 'Hispanic or Latino': [0.30498337221422545, 0.32268687076159586], 'Two or More Races': [0.03621382836154266, 0.03660722272099333], 'American Indian or Alaskan Native': [0.016295230059065868, 0.018790603373165085], 'White': [0.4817441802749789, 0.4452432144123133]}
en_g_Northeast = {'Name': 'en_g_Northeast', 'Total': [283545, 423709], 'Asian': [0.09710275264949127, 0.08614638820511247], 'Black or African American': [0.1013454654464018, 0.1288030228293475], 'Native Hawaiian or Other Pacific Islanders': [0.0014530321465728545, 0.0014656285327901933], 'Hispanic or Latino': [0.12491844328060801, 0.14222969066033528], 'Two or More Races': [0.03030912200885221, 0.03179776686357854], 'American Indian or Alaskan Native': [0.002426422613694475, 0.002808531326924847], 'White': [0.6424447618543794, 0.6067489715819112]}
en_g_Midwest = {'Name': 'en_g_Midwest', 'Total': [345402, 488320], 'Asian': [0.05100433697546627, 0.04463057011795544], 'Black or African American': [0.07230705091458649, 0.08652522935779816], 'Native Hawaiian or Other Pacific Islanders': [0.0011638612399464971, 0.0010812581913499345], 'Hispanic or Latino': [0.08219408109970411, 0.08449172673656619], 'Two or More Races': [0.03139819688363125, 0.033156536697247704], 'American Indian or Alaskan Native': [0.004099570934736915, 0.004570773263433814], 'White': [0.7578329019519284, 0.7455439056356488]}
en_g_West = {'Name': 'en_g_West', 'Total': [361411, 530078], 'Asian': [0.1306656410568577, 0.11370213440286146], 'Black or African American': [0.04436776965836679, 0.050911375307030285], 'Native Hawaiian or Other Pacific Islanders': [0.005254405648970286, 0.004987945170333422], 'Hispanic or Latino': [0.28960656980556765, 0.3335490248604922], 'Two or More Races': [0.05326899291941861, 0.052684699232943076], 'American Indian or Alaskan Native': [0.005318045106540753, 0.006427355974026464], 'White': [0.47151857580427825, 0.43773746505231304]}
grad_g_Southeast = {'Name': 'grad_g_Southeast', 'Total': [118511, 159909], 'Asian': [0.04380184117929981, 0.03765891850990251], 'Black or African American': [0.14615520922108496, 0.183616932130149], 'Native Hawaiian or Other Pacific Islanders': [0.0, 0.0], 'Hispanic or Latino': [0.10447975293432678, 0.10706089088168896], 'Two or More Races': [0.025997586721907672, 0.02965436592061735], 'American Indian or Alaskan Native': [0.00257360076279839, 0.0025076762408619904], 'White': [0.6769920091805824, 0.6395012163167801]}
grad_g_Southwest = {'Name': 'grad_g_Southwest', 'Total': [45217, 62018], 'Asian': [0.0751487272486012, 0.061546647747428164], 'Black or African American': [0.0660371099365283, 0.08550743332580864], 'Native Hawaiian or Other Pacific Islanders': [0.0, 0.0], 'Hispanic or Latino': [0.2854015082822832, 0.3233738592021671], 'Two or More Races': [0.038834951456310676, 0.03895643200361185], 'American Indian or Alaskan Native': [0.018355928080146848, 0.018414008836144344], 'White': [0.5162217749961298, 0.47220161888483986]}
grad_g_Northeast = {'Name': 'grad_g_Northeast', 'Total': [105277, 135636], 'Asian': [0.09198590385364325, 0.09614704060868796], 'Black or African American': [0.0779657475042032, 0.09768055678433454], 'Native Hawaiian or Other Pacific Islanders': [0.0, 0.0], 'Hispanic or Latino': [0.10751636159844981, 0.12498894098911793], 'Two or More Races': [0.02581760498494448, 0.0317909699489811], 'American Indian or Alaskan Native': [0.0021657152084500887, 0.0020938393936712966], 'White': [0.6945486668503091, 0.6472986522752072]}
grad_g_Midwest = {'Name': 'grad_g_Midwest', 'Total': [106164, 130259], 'Asian': [0.04753023623827286, 0.04407373003017066], 'Black or African American': [0.04709694435025055, 0.05548944794601525], 'Native Hawaiian or Other Pacific Islanders': [0.0, 0.0], 'Hispanic or Latino': [0.06453223314871331, 0.07088185845123945], 'Two or More Races': [0.025074413172073397, 0.028973046008337236], 'American Indian or Alaskan Native': [0.0006216796654233074, 0.001558433582324446], 'White': [0.8151444934252665, 0.7990234839819129]}
grad_g_West = {'Name': 'grad_g_West', 'Total': [78292, 111892], 'Asian': [0.17340213559495224, 0.15269188145711937], 'Black or African American': [0.02666939150871098, 0.034488614020662785], 'Native Hawaiian or Other Pacific Islanders': [0.0, 0.0], 'Hispanic or Latino': [0.27182853931436163, 0.31390984163300323], 'Two or More Races': [0.0559316405252133, 0.057912987523683554], 'American Indian or Alaskan Native': [0.004815306800183927, 0.007301683766489114], 'White': [0.46735298625657795, 0.43369499159904196]}
en_g_USTotal = {'Name': 'en_g_USTotal', 'Total': [1636500, 2364365], 'Asian': [0.07564069660861594, 0.06623469726543914], 'Black or African American': [0.0964521845401772, 0.12323900920543147], 'Native Hawaiian or Other Pacific Islanders': [0.0024411854567674917, 0.002316055262195135], 'Hispanic or Latino': [0.17350870760769935, 0.1914399849431031], 'Two or More Races': [0.03618698441796517, 0.03749125029341916], 'American Indian or Alaskan Native': [0.005714023831347388, 0.006499419505871556], 'White': [0.6100562175374274, 0.5727795835245404]}
grad_g_USTotal = {'Name': 'grad_g_USTotal', 'Total': [453461, 599714], 'Asian': [0.08136311612244493, 0.07621299486088369], 'Black or African American': [0.07851391850677346, 0.09838189537012643], 'Native Hawaiian or Other Pacific Islanders': [0.0, 0.0], 'Hispanic or Latino': [0.1427664121060025, 0.16421994484037392], 'Two or More Races': [0.03218799411636282, 0.036223933408257934], 'American Indian or Alaskan Native': [0.003982701930265227, 0.004747262861964203], 'White': [0.661185857218151, 0.6202139686583938]}
Texas_Schools_enroll = {'Total': [41.757362857949374, 58.242637142050626], 'Asian': [3.7810118244832673, 4.339303076874824], 'Black or African American': [3.2242888059467427, 5.876956371734153], 'Native Hawaiian or Other Pacific Islanders': [0.05645641878116865, 0.08154816046168804], 'Hispanic or Latino': [13.508766427249633, 20.177680895775175], 'Two or More Races': [1.2890882288366843, 1.8019006994322992], 'American Indian or Alaskan Native': [0.1231063576200483, 0.16623278863344104], 'White': [19.774644795031833, 25.799015149139038]}
Texas_Schools_grad = {'Total': [43.279128339903636, 56.720871660096364], 'Asian': [4.886662286465177, 5.2973061760841], 'Black or African American': [2.4200613228208496, 4.177617170389838], 'Native Hawaiian or Other Pacific Islanders': [0.0, 0.0], 'Hispanic or Latino': [13.400678931230836, 19.026500219010074], 'Two or More Races': [1.459154621112571, 2.0997590889180904], 'American Indian or Alaskan Native': [0.11224266316250547, 0.14235654840122647], 'White': [21.000328515111697, 25.977332457293034]}

def KS(df_en,df_grad,dict_en,dict_grad,gender,race):

    uni_ks_enrollment = 0
    uni_ks_grad = 0
    regional_ks_enrollment = 0
    regional_ks_grad = 0
    national_ks_enrollment = 0
    national_ks_grad = 0

    #enrollment
    df_en_gender = df_en['Gender'].tolist()
    df_en_race = df_en['Race'].tolist()

    total = 0
    count = 0
    for i in range(0,len(df_en_gender)):
        total += 1
        if df_en_gender[i] == gender and df_en_race[i] == race:
            count += 1
    print("actual enrollment", count)
    print("actual total enrollment", total)
    uni_ks_enrollment = max((count/total) - ((total - count)/total), ((total - count)/total) - (count/total))

    #graduation
    df_grad_gender = df_grad['Gender'].tolist()
    df_grad_race = df_grad['Race'].tolist()

    total = 0
    count = 0
    for i in range(0, len(df_grad_gender)):
        total += 1
        if df_grad_gender[i] == gender and df_grad_race[i] == race:
            count += 1
    print("actual count grad", count)
    print("actual total grad", total)
    uni_ks_grad = max((count/total) - ((total - count)/total), ((total - count)/total) - (count/total))

    #regional enrollment

    total = dict_en['Total'][0] + dict_en['Total'][1]
    count = 0
    if gender == 'Male':
        count = dict_en[race][0] * dict_en['Total'][0]
    else:
        count = dict_en[race][1] * dict_en['Total'][1]
    print("regional_enrollment", count)
    print("total_regional_enroll", total)
    regional_ks_enrollment = max((count/total) - ((total - count)/total), ((total - count)/total) - (count/total))

    #regional graduation

    total = dict_grad['Total'][0] + dict_grad['Total'][1]
    count = 0
    if gender == 'Male':
        count = dict_grad[race][0] * dict_grad['Total'][0]
    else:
        count = dict_grad[race][1] * dict_grad['Total'][1]
    print("regional_grad count", count)
    print("regional_grad total", total)
    regional_ks_grad = max((count/total) - ((total - count)/total), ((total - count)/total) - (count/total))

    #national enrollment

    total = en_g_Southeast['Total'][0] + en_g_Southeast['Total'][1] + en_g_Southwest['Total'][0] + en_g_Southwest['Total'][1] + en_g_Northeast['Total'][0] + en_g_Northeast['Total'][1] + en_g_Midwest['Total'][0] + en_g_Midwest['Total'][1] + en_g_West['Total'][0] + en_g_West['Total'][1]
    count = 0
    if gender == 'Male':
        count = (en_g_Southeast[race][0] * en_g_Southeast['Total'][0]) + (en_g_Southwest[race][0] * en_g_Southwest['Total'][0]) + (en_g_Northeast[race][0] * en_g_Northeast['Total'][0]) + (en_g_Midwest[race][0] * en_g_Midwest['Total'][0]) + (en_g_West[race][0] * en_g_West['Total'][0])
    else:
        count = (en_g_Southeast[race][1] * en_g_Southeast['Total'][1]) + (en_g_Southwest[race][1] * en_g_Southwest['Total'][1]) + (en_g_Northeast[race][1] * en_g_Northeast['Total'][1]) + (en_g_Midwest[race][1] * en_g_Midwest['Total'][1]) + (en_g_West[race][1] * en_g_West['Total'][1])
    print("national enroll count", count)
    print("national enroll total", total)
    national_ks_enrollment = max((count/total) - ((total - count)/total), ((total - count)/total) - (count/total))


    #national graduation
    total = grad_g_Southeast['Total'][0] + grad_g_Southeast['Total'][1] + grad_g_Southwest['Total'][0] + grad_g_Southwest['Total'][1] + grad_g_Northeast['Total'][0] + grad_g_Northeast['Total'][1] + \
            grad_g_Midwest['Total'][0] + grad_g_Midwest['Total'][1] + grad_g_West['Total'][0] + grad_g_West['Total'][1]
    count = 0
    if gender == 'Male':
        count = (grad_g_Southeast[race][0] * grad_g_Southeast['Total'][0]) + (
                    grad_g_Southwest[race][0] * grad_g_Southwest['Total'][0]) + (
                            grad_g_Northeast[race][0] * grad_g_Northeast['Total'][0]) + (
                            grad_g_Midwest[race][0] * grad_g_Midwest['Total'][0]) + (
                            grad_g_West[race][0] * grad_g_West['Total'][0])
    else:
        count = (grad_g_Southeast[race][1] * grad_g_Southeast['Total'][1]) + (
                    grad_g_Southwest[race][1] * grad_g_Southwest['Total'][1]) + (
                            grad_g_Northeast[race][1] * grad_g_Northeast['Total'][1]) + (
                            grad_g_Midwest[race][1] * grad_g_Midwest['Total'][1]) + (
                            grad_g_West[race][1] * grad_g_West['Total'][1])

    print("national grad count", count)
    print("national grad total", total)
    national_ks_grad = max((count/total) - ((total - count)/total), ((total - count)/total) - (count/total))
    return max(uni_ks_enrollment - uni_ks_grad, uni_ks_grad - uni_ks_enrollment), max(regional_ks_enrollment - regional_ks_grad, regional_ks_grad - regional_ks_enrollment), max(national_ks_enrollment - national_ks_grad, national_ks_grad - national_ks_enrollment)




def class_imbalance(df_en,df_grad,dict_en,dict_grad,gender,race):
    uni_cb_enrollment = 0
    uni_cb_grad = 0
    regional_cb_enrollment = 0
    regional_cb_grad = 0
    national_cb_enrollment = 0
    national_cb_grad = 0

    # enrollment
    df_en_gender = df_en['Gender'].tolist()
    df_en_race = df_en['Race'].tolist()

    total = 0
    count = 0
    for i in range(0, len(df_en_gender)):
        total += 1
        if df_en_gender[i] == gender and df_en_race[i] == race:
            count += 1
    uni_cb_enrollment = (max(count - (total - count), (total - count) - count)) / total

    # graduation
    df_grad_gender = df_grad['Gender'].tolist()
    df_grad_race = df_grad['Race'].tolist()

    total = 0
    count = 0
    for i in range(0, len(df_grad_gender)):
        total += 1
        if df_grad_gender[i] == gender and df_grad_race[i] == race:
            count += 1
    uni_cb_grad = (max(count - (total - count), (total - count) - count)) / total

    # regional enrollment

    total = dict_en['Total'][0] + dict_en['Total'][1]
    count = 0
    if gender == 'Male':
        count = dict_en[race][0] * dict_en['Total'][0]
    else:
        count = dict_en[race][1] * dict_en['Total'][1]

    regional_cb_enrollment = (max(count - (total - count), (total - count) - count)) / total

    # regional graduation

    total = dict_grad['Total'][0] + dict_grad['Total'][1]
    count = 0
    if gender == 'Male':
        count = dict_grad[race][0] * dict_grad['Total'][0]
    else:
        count = dict_grad[race][1] * dict_grad['Total'][1]

    regional_cb_grad = (max(count - (total - count), (total - count) - count)) / total

    # national enrollment

    total = en_g_Southeast['Total'][0] + en_g_Southeast['Total'][1] + en_g_Southwest['Total'][0] + \
            en_g_Southwest['Total'][1] + en_g_Northeast['Total'][0] + en_g_Northeast['Total'][1] + \
            en_g_Midwest['Total'][0] + en_g_Midwest['Total'][1] + en_g_West['Total'][0] + en_g_West['Total'][1]
    count = 0
    if gender == 'Male':
        count = (en_g_Southeast[race][0] * en_g_Southeast['Total'][0]) + (
                    en_g_Southwest[race][0] * en_g_Southwest['Total'][0]) + (
                            en_g_Northeast[race][0] * en_g_Northeast['Total'][0]) + (
                            en_g_Midwest[race][0] * en_g_Midwest['Total'][0]) + (
                            en_g_West[race][0] * en_g_West['Total'][0])
    else:
        count = (en_g_Southeast[race][1] * en_g_Southeast['Total'][1]) + (
                    en_g_Southwest[race][1] * en_g_Southwest['Total'][1]) + (
                            en_g_Northeast[race][1] * en_g_Northeast['Total'][1]) + (
                            en_g_Midwest[race][1] * en_g_Midwest['Total'][1]) + (
                            en_g_West[race][1] * en_g_West['Total'][1])
    print("CI Total_enroll", count)
    national_cb_enrollment = (max(count - (total - count), (total - count) - count)) / total

    # national graduation
    total = grad_g_Southeast['Total'][0] + grad_g_Southeast['Total'][1] + grad_g_Southwest['Total'][0] + \
            grad_g_Southwest['Total'][1] + grad_g_Northeast['Total'][0] + grad_g_Northeast['Total'][1] + \
            grad_g_Midwest['Total'][0] + grad_g_Midwest['Total'][1] + grad_g_West['Total'][0] + grad_g_West['Total'][1]
    count = 0
    if gender == 'Male':
        count = (grad_g_Southeast[race][0] * grad_g_Southeast['Total'][0]) + (
                grad_g_Southwest[race][0] * grad_g_Southwest['Total'][0]) + (
                        grad_g_Northeast[race][0] * grad_g_Northeast['Total'][0]) + (
                        grad_g_Midwest[race][0] * grad_g_Midwest['Total'][0]) + (
                        grad_g_West[race][0] * grad_g_West['Total'][0])
    else:
        count = (grad_g_Southeast[race][1] * grad_g_Southeast['Total'][1]) + (
                grad_g_Southwest[race][1] * grad_g_Southwest['Total'][1]) + (
                        grad_g_Northeast[race][1] * grad_g_Northeast['Total'][1]) + (
                        grad_g_Midwest[race][1] * grad_g_Midwest['Total'][1]) + (
                        grad_g_West[race][1] * grad_g_West['Total'][1])

    national_cb_grad = (max(count - (total - count), (total - count) - count)) / total

    return (max(uni_cb_enrollment - uni_cb_grad, uni_cb_grad - uni_cb_enrollment)) / (uni_cb_grad + uni_cb_enrollment), (max(regional_cb_enrollment - regional_cb_grad, regional_cb_grad - regional_cb_enrollment)) / (regional_cb_grad + regional_cb_enrollment), (max(national_cb_enrollment - national_cb_grad, national_cb_grad - national_cb_enrollment)) / (national_cb_grad + national_cb_enrollment)


def KL(df_en,df_grad,dict_en,dict_grad,gender,race):
    uni_kl_enrollment = 0
    uni_kl_grad = 0
    regional_kl_enrollment = 0
    regional_kl_grad = 0
    national_kl_enrollment = 0
    national_kl_grad = 0

    # enrollment
    df_en_gender = df_en['Gender'].tolist()
    df_en_race = df_en['Race'].tolist()

    total = 0
    count = 0
    for i in range(0, len(df_en_gender)):
        total += 1
        if df_en_gender[i] == gender and df_en_race[i] == race:
            count += 1
    uni_kl_enrollment = (max(count - (total - count), (total - count) - count)) / total

    # graduation
    df_grad_gender = df_grad['Gender'].tolist()
    df_grad_race = df_grad['Race'].tolist()

    total = 0
    count = 0
    for i in range(0, len(df_grad_gender)):
        total += 1
        if df_grad_gender[i] == gender and df_grad_race[i] == race:
            count += 1
    uni_kl_grad = (max(count - (total - count), (total - count) - count)) / total

    # regional enrollment

    total = dict_en['Total'][0] + dict_en['Total'][1]
    count = 0
    if gender == 'Male':
        count = dict_en[race][0] * dict_en['Total'][0]
    else:
        count = dict_en[race][1] * dict_en['Total'][1]

    regional_kl_enrollment = (max(count - (total - count), (total - count) - count)) / total

    # regional graduation

    total = dict_grad['Total'][0] + dict_grad['Total'][1]
    count = 0
    if gender == 'Male':
        count = dict_grad[race][0] * dict_grad['Total'][0]
    else:
        count = dict_grad[race][1] * dict_grad['Total'][1]

    regional_kl_grad = (max(count - (total - count), (total - count) - count)) / total

    # national enrollment

    total = en_g_Southeast['Total'][0] + en_g_Southeast['Total'][1] + en_g_Southwest['Total'][0] + \
            en_g_Southwest['Total'][1] + en_g_Northeast['Total'][0] + en_g_Northeast['Total'][1] + \
            en_g_Midwest['Total'][0] + en_g_Midwest['Total'][1] + en_g_West['Total'][0] + en_g_West['Total'][1]
    count = 0
    if gender == 'Male':
        count = (en_g_Southeast[race][0] * en_g_Southeast['Total'][0]) + (
                    en_g_Southwest[race][0] * en_g_Southwest['Total'][0]) + (
                            en_g_Northeast[race][0] * en_g_Northeast['Total'][0]) + (
                            en_g_Midwest[race][0] * en_g_Midwest['Total'][0]) + (
                            en_g_West[race][0] * en_g_West['Total'][0])
    else:
        count = (en_g_Southeast[race][1] * en_g_Southeast['Total'][1]) + (
                    en_g_Southwest[race][1] * en_g_Southwest['Total'][1]) + (
                            en_g_Northeast[race][1] * en_g_Northeast['Total'][1]) + (
                            en_g_Midwest[race][1] * en_g_Midwest['Total'][1]) + (
                            en_g_West[race][1] * en_g_West['Total'][1])
    national_kl_enrollment = (max(count - (total - count), (total - count) - count)) / total

    # national graduation
    total = grad_g_Southeast['Total'][0] + grad_g_Southeast['Total'][1] + grad_g_Southwest['Total'][0] + \
            grad_g_Southwest['Total'][1] + grad_g_Northeast['Total'][0] + grad_g_Northeast['Total'][1] + \
            grad_g_Midwest['Total'][0] + grad_g_Midwest['Total'][1] + grad_g_West['Total'][0] + grad_g_West['Total'][1]
    count = 0
    if gender == 'Male':
        count = (grad_g_Southeast[race][0] * grad_g_Southeast['Total'][0]) + (
                grad_g_Southwest[race][0] * grad_g_Southwest['Total'][0]) + (
                        grad_g_Northeast[race][0] * grad_g_Northeast['Total'][0]) + (
                        grad_g_Midwest[race][0] * grad_g_Midwest['Total'][0]) + (
                        grad_g_West[race][0] * grad_g_West['Total'][0])
    else:
        count = (grad_g_Southeast[race][1] * grad_g_Southeast['Total'][1]) + (
                grad_g_Southwest[race][1] * grad_g_Southwest['Total'][1]) + (
                        grad_g_Northeast[race][1] * grad_g_Northeast['Total'][1]) + (
                        grad_g_Midwest[race][1] * grad_g_Midwest['Total'][1]) + (
                        grad_g_West[race][1] * grad_g_West['Total'][1])

    national_kl_grad = (max(count - (total - count), (total - count) - count)) / total

    return abs(uni_kl_enrollment*math.log(uni_kl_enrollment/uni_kl_grad)), abs(regional_kl_enrollment*math.log(regional_kl_enrollment/regional_kl_grad)), abs(national_kl_enrollment*math.log(national_kl_enrollment/national_kl_grad))

def DPL(grad_df, en_df, dict_en, dict_grad, gender_category, race_category):
    #race_enrollment = {'Southeast':en_g_Southeast, 'Northeast':en_g_Northeast, 'Midwest':en_g_Midwest,'Southwest':en_g_Southwest, 'West':en_g_West}
    #race_grad = {'Southeast':grad_g_Southeast, 'Northeast':grad_g_Northeast, 'Midwest':grad_g_Midwest,'Southwest':grad_g_Southwest, 'West':grad_g_West} 
    gender = {'Male':0, 'Female':1}
    total = 0
    local = 0
    demographic_count = 0
    grad_df_gender = grad_df['Gender'].tolist()
    grad_df_race = grad_df['Race'].tolist()
    for i in range(len(grad_df_gender)):
        total += 1
        if grad_df_gender[i] == gender_category and grad_df_race[i] == race_category:
            demographic_count += 1
    local = (demographic_count / total)
    total = 0
    demographic_count = 0
    en_df_gender = en_df['Gender'].tolist()
    en_df_race = en_df['Race'].tolist()
    for i in range(len(en_df_gender)):
        total += 1
        if en_df_gender[i] == gender_category and en_df_race[i] == race_category:
            demographic_count += 1
    local -= (demographic_count / total)
    local = abs(local)


    US_metric = en_g_USTotal[race_category][gender[gender_category]] - grad_g_USTotal[race_category][gender[gender_category]]
    regional_metric = dict_en[race_category][gender[gender_category]] - dict_grad[race_category][gender[gender_category]]
    return abs(US_metric), abs(regional_metric), local


def TVD(df_en,df_grad,dict_en,dict_grad,gender,race):
    uni_tvd_enrollment = 0
    uni_tvd_grad = 0
    regional_tvd_enrollment = 0
    regional_tvd_grad = 0
    national_tvd_enrollment = 0
    national_tvd_grad = 0

    # enrollment
    df_en_gender = df_en['Gender'].tolist()
    df_en_race = df_en['Race'].tolist()

    total = 0
    count = 0
    for i in range(0, len(df_en_gender)):
        total += 1
        if df_en_gender[i] == gender and df_en_race[i] == race:
            count += 1
    uni_tvd_enrollment = (max(count - (total - count), (total - count) - count)) / total

    # graduation
    df_grad_gender = df_grad['Gender'].tolist()
    df_grad_race = df_grad['Race'].tolist()

    total = 0
    count = 0
    for i in range(0, len(df_grad_gender)):
        total += 1
        if df_grad_gender[i] == gender and df_grad_race[i] == race:
            count += 1
    uni_tvd_grad = (max(count - (total - count), (total - count) - count)) / total

    # regional enrollment

    total = dict_en['Total'][0] + dict_en['Total'][1]
    count = 0
    if gender == 'Male':
        count = dict_en[race][0] * dict_en['Total'][0]
    else:
        count = dict_en[race][1] * dict_en['Total'][1]

    regional_tvd_enrollment = (max(count - (total - count), (total - count) - count)) / total

    # regional graduation

    total = dict_grad['Total'][0] + dict_grad['Total'][1]
    count = 0
    if gender == 'Male':
        count = dict_grad[race][0] * dict_grad['Total'][0]
    else:
        count = dict_grad[race][1] * dict_grad['Total'][1]

    regional_tvd_grad = (max(count - (total - count), (total - count) - count)) / total

    # national enrollment

    total = en_g_Southeast['Total'][0] + en_g_Southeast['Total'][1] + en_g_Southwest['Total'][0] + \
            en_g_Southwest['Total'][1] + en_g_Northeast['Total'][0] + en_g_Northeast['Total'][1] + \
            en_g_Midwest['Total'][0] + en_g_Midwest['Total'][1] + en_g_West['Total'][0] + en_g_West['Total'][1]
    count = 0
    if gender == 'Male':
        count = (en_g_Southeast[race][0] * en_g_Southeast['Total'][0]) + (
                    en_g_Southwest[race][0] * en_g_Southwest['Total'][0]) + (
                            en_g_Northeast[race][0] * en_g_Northeast['Total'][0]) + (
                            en_g_Midwest[race][0] * en_g_Midwest['Total'][0]) + (
                            en_g_West[race][0] * en_g_West['Total'][0])
    else:
        count = (en_g_Southeast[race][1] * en_g_Southeast['Total'][1]) + (
                    en_g_Southwest[race][1] * en_g_Southwest['Total'][1]) + (
                            en_g_Northeast[race][1] * en_g_Northeast['Total'][1]) + (
                            en_g_Midwest[race][1] * en_g_Midwest['Total'][1]) + (
                            en_g_West[race][1] * en_g_West['Total'][1])
    national_tvd_enrollment = (max(count - (total - count), (total - count) - count)) / total

    # national graduation
    total = grad_g_Southeast['Total'][0] + grad_g_Southeast['Total'][1] + grad_g_Southwest['Total'][0] + \
            grad_g_Southwest['Total'][1] + grad_g_Northeast['Total'][0] + grad_g_Northeast['Total'][1] + \
            grad_g_Midwest['Total'][0] + grad_g_Midwest['Total'][1] + grad_g_West['Total'][0] + grad_g_West['Total'][1]
    count = 0
    if gender == 'Male':
        count = (grad_g_Southeast[race][0] * grad_g_Southeast['Total'][0]) + (
                grad_g_Southwest[race][0] * grad_g_Southwest['Total'][0]) + (
                        grad_g_Northeast[race][0] * grad_g_Northeast['Total'][0]) + (
                        grad_g_Midwest[race][0] * grad_g_Midwest['Total'][0]) + (
                        grad_g_West[race][0] * grad_g_West['Total'][0])
    else:
        count = (grad_g_Southeast[race][1] * grad_g_Southeast['Total'][1]) + (
                grad_g_Southwest[race][1] * grad_g_Southwest['Total'][1]) + (
                        grad_g_Northeast[race][1] * grad_g_Northeast['Total'][1]) + (
                        grad_g_Midwest[race][1] * grad_g_Midwest['Total'][1]) + (
                        grad_g_West[race][1] * grad_g_West['Total'][1])

    national_tvd_grad = (max(count - (total - count), (total - count) - count)) / total

    return 0.5 * (abs(uni_tvd_enrollment - uni_tvd_grad) + abs((1 - uni_tvd_enrollment)+(1 - uni_tvd_grad))), 0.5 * (abs(regional_tvd_enrollment - regional_tvd_grad) + abs((1 - regional_tvd_enrollment)+(1 - regional_tvd_grad))), 0.5 * (abs(national_tvd_enrollment - national_tvd_grad) + abs((1 - national_tvd_enrollment)+(1 - national_tvd_grad)))

def std_Dev(results):
    total = 0
    for item in results.values():
        total += item
    num = len(results.values())
    mean = total / num
    variance = 0
    for item in results.values():
        variance += (item - mean)**2
    dev = math.sqrt(variance/num)
    return dev, mean

def test_std_dev(results):
    dev, mean = std_Dev(results)
    print(dev)
    print(mean)
    for i in results.values():
        val = (i - mean) / dev
        print('Pairs:')
        print(i)
        print(val)
    


def getRatiosMean(list1_regional,list2_national):
    total_regional = sum(list1_regional)
    mean_regional = total_regional/len(list1_regional)

    total_national = sum(list2_national)
    mean_national = total_national/len(list2_national)
    return mean_regional,mean_national

def getRatiosStdDev(mean_regional, mean_national, list1_regional, list2_national):
    def traverse_list_std_dev(mean, list1):
        variance = 0
        for num in list1:
            variance += (num - mean) ** 2
        return math.sqrt(variance/len(list1))
    std_regional = traverse_list_std_dev(mean_regional, list1_regional)
    std_national = traverse_list_std_dev(mean_national, list2_national)
    return std_regional, std_national

def IsItBias(mean_regional, mean_national, std_regional, std_national, uni_ratio, regional_ratio, national_ratio):
    bias_regional = False
    bias_national = False

    if round((uni_ratio - mean_regional)/std_regional) != round((regional_ratio - mean_regional)/std_regional):
        bias_regional = True
    if round((uni_ratio - mean_national)/std_national) != round((national_ratio - mean_national)/std_national):
        bias_national = True

    return bias_regional, bias_national


# def female_enroll_report_statistics(file_enroll):
#     df_en = pd.read_csv(file_enroll, sep=',')
#     total, count = counting_utils.get_count_total_national_enrollment('Female', 'Asian')
#     total_black, count_black = counting_utils.get_count_total_national_enrollment('Female', 'Black or African American')
#     total_NH, count_NH = counting_utils.get_count_total_national_enrollment('Female', 'Native Hawaiian or Other Pacific Islanders')
#     total_HL, count_HL = counting_utils.get_count_total_national_enrollment('Female', 'Hispanic or Latino')
#     total_2OM, count_2OM = counting_utils.get_count_total_national_enrollment('Female', 'Two or More Races')
#     total_AA, count_AA = counting_utils.get_count_total_national_enrollment('Female', 'American Indian or Alaska Native')
#     total_W, count_W = counting_utils.get_count_total_national_enrollment('Female', 'White')
#     total = total + total_black + total_NH + total_HL + total_2OM + total_AA + total_W
#     count = count + count_black +count_NH + count_HL + count_2OM + count_AA + count_W
#     national_ratio_enroll = count/total
#     print("National Ratio: ", national_ratio_enroll)
#
#     total, count = counting_utils.get_count_total(df_en, 'Female', 'Asian')
#     total_black, count_black = counting_utils.get_count_total(df_en, 'Female', 'Black or African American')
#     total_NH, count_NH =  counting_utils.get_count_total(df_en, 'Female', 'Native Hawaiian or Other Pacific Islanders')
#     total_HL, count_HL = counting_utils.get_count_total(df_en, 'Female', 'Hispanic or Latino')
#     total_2OM, count_2OM = counting_utils.get_count_total(df_en, 'Female', 'Two or More Races')
#     total_AA, count_AA = counting_utils.get_count_total(df_en, 'Female', 'American Indian or Alaska Native')
#     total_W, count_W = counting_utils.get_count_total(df_en, 'Female', 'White')
#     total = total + total_black + total_NH + total_HL + total_2OM + total_AA + total_W
#     count = count + count_black +count_NH + count_HL + count_2OM + count_AA + count_W
#     university_enroll_ratio = count / total
#     print('Actual University Ratio: ', university_enroll_ratio)
#
#     #Data for regional enrollment
#     dict_en = region_enum.en_g_Southwest
#     total, count = counting_utils.get_count_total_regional(dict_en, 'Female', 'Asian')
#     total_black, count_black =  counting_utils.get_count_total_regional(dict_en, 'Female', 'Black or African American')
#     total_NH, count_NH =  counting_utils.get_count_total_regional(dict_en, 'Female', 'Native Hawaiian or Other Pacific Islanders')
#     total_HL, count_HL = counting_utils.get_count_total_regional(dict_en, 'Female', 'Hispanic or Latino')
#     total_2OM, count_2OM = counting_utils.get_count_total_regional(dict_en, 'Female', 'Two or More Races')
#     total_AA, count_AA = counting_utils.get_count_total_regional(dict_en, 'Female', 'American Indian or Alaska Native')
#     total_W, count_W = counting_utils.get_count_total_regional(dict_en, 'Female', 'White')
#     total = total + total_black + total_NH + total_HL + total_2OM + total_AA + total_W
#     count = count + count_black +count_NH + count_HL + count_2OM + count_AA + count_W
#     regional_enroll_ratio = count / total
#     print('University Ratio: ', regional_enroll_ratio)



    

def test(file_enroll,file_grad,region,gender,race):
    df_en = pd.read_csv(file_enroll, sep=',')
    df_grad = pd.read_csv(file_grad, sep=',')
    dict_en = None
    dict_grad = None
    if region == 'Southeast':
        dict_en = en_g_Southeast
        dict_grad = grad_g_Southeast
    elif region == 'Southwest':
        dict_en = en_g_Southwest
        dict_grad = grad_g_Southwest
        # dict_en = Texas_Schools_enroll
        # dict_grad = Texas_Schools_grad
    elif region == 'Northeast':
        dict_en = en_g_Northeast
        dict_grad = grad_g_Northeast
        pass
    elif region == 'Midwest':
        dict_en = en_g_Midwest
        dict_grad = grad_g_Midwest
        pass
    else:
        dict_en = en_g_West
        dict_grad = grad_g_West
        pass

    list1_regional = []
    list2_national = []

    uni_ratio_1, regional_ratio_1, national_ratio_1 = class_imbalance(df_en, df_grad, dict_en, dict_grad,
                                                                      gender, race)
    list1_regional.extend([uni_ratio_1, regional_ratio_1])
    list2_national.extend([uni_ratio_1,national_ratio_1])


    uni_ratio_2, regional_ratio_2, national_ratio_2 = KS(df_en, df_grad, dict_en, dict_grad, gender, race)
    list1_regional.extend([uni_ratio_2, regional_ratio_2])
    list2_national.extend([uni_ratio_2, national_ratio_2])


    uni_ratio_3, regional_ratio_3, national_ratio_3 = DPL(df_grad, df_en, dict_en, dict_grad, gender, race)
    list1_regional.extend([uni_ratio_3, regional_ratio_3])
    list2_national.extend([uni_ratio_3, national_ratio_3])


    uni_ratio_4, regional_ratio_4, national_ratio_4 = KL(df_en, df_grad, dict_en, dict_grad, gender, race)
    list1_regional.extend([uni_ratio_4, regional_ratio_4])
    list2_national.extend([uni_ratio_4, national_ratio_4])


    uni_ratio_5, regional_ratio_5, national_ratio_5 = TVD(df_en, df_grad, dict_en, dict_grad, gender, race)
    list1_regional.extend([uni_ratio_5, regional_ratio_5])
    list2_national.extend([uni_ratio_5, national_ratio_5])


    mean_regional, mean_national = getRatiosMean(list1_regional, list2_national)
    print(mean_regional)
    print(mean_national)
    std_regional, std_national = getRatiosStdDev(mean_regional, mean_national, list1_regional, list2_national)
    print(std_regional)
    print(std_national)

    bias_cb_regional, bias_cb_national = IsItBias(mean_regional, mean_national, std_regional, std_national, uni_ratio_1, regional_ratio_1, national_ratio_1)
    bias_ks_regional, bias_ks_national = IsItBias(mean_regional, mean_national, std_regional, std_national, uni_ratio_2, regional_ratio_2, national_ratio_2)
    bias_dpl_regional, bias_dpl_national = IsItBias(mean_regional, mean_national, std_regional, std_national, uni_ratio_3, regional_ratio_3, national_ratio_3)
    bias_kl_regional, bias_kl_national = IsItBias(mean_regional, mean_national, std_regional, std_national, uni_ratio_4, regional_ratio_4, national_ratio_4)
    bias_tvd_regional, bias_tvd_national = IsItBias(mean_regional, mean_national, std_regional, std_national, uni_ratio_5, regional_ratio_5, national_ratio_5)

    dict1 = {"cb_uni_ratio": uni_ratio_1, "cb_regional_ratio": regional_ratio_1, "cb_national_ratio": national_ratio_1,
         "bias_cb_regional": bias_cb_regional, "bias_cb_national": bias_cb_national, "ks_uni_ratio": uni_ratio_2, "ks_regional_ratio": regional_ratio_2,
         "ks_national_ratio": national_ratio_2, "bias_ks_regional": bias_ks_regional, "bias_ks_national": bias_ks_national, "dpl_uni_ratio": uni_ratio_3, "dpl_regional_ratio": regional_ratio_3,
         "dpl_national_ratio": national_ratio_3, "bias_dpl_regional": bias_dpl_regional, "bias_dpl_national": bias_dpl_national, "kl_uni_ratio": uni_ratio_4, "kl_regional_ratio": regional_ratio_4,
         "kl_national_ratio": national_ratio_4, "bias_kl_regional": bias_kl_regional, "bias_kl_national": bias_kl_national, "tvd_uni_ratio": uni_ratio_5, "tvd_regional_ratio": regional_ratio_5,
         "tvd_national_ratio": national_ratio_5, "bias_tvd_regional": bias_tvd_regional, "bias_tvd_national": bias_tvd_national}
    # dict2 = {"cb_ut_ratio": uni_ratio_1, "cb_texas_ratio": regional_ratio_1, "bias_cb": bias_cb_regional, "ks_ut_ratio": uni_ratio_2, "ks_texas_ratio": regional_ratio_2, "bias_ks": bias_ks_regional,"dpl_ut_ratio": uni_ratio_3, "dpl_texas_ratio": regional_ratio_3,
    #           "bias_dpl": bias_dpl_regional,"kl_ut_ratio": uni_ratio_4, "kl_texas_ratio": regional_ratio_4,
    #           "bias_kl": bias_kl_regional,
    #          "tvd_utratio": uni_ratio_5, "tvd_texas_ratio": regional_ratio_5,
    #           "bias_tvd": bias_tvd_regional}

    print(dict1)

    # return jsonable_encoder(
    #     {"cb_uni_ratio": uni_ratio_1, "cb_regional_ratio": regional_ratio_1, "cb_national_ratio": national_ratio_1,
    #      "bias_cb": bias_cb, "ks_uni_ratio": uni_ratio_2, "ks_regional_ratio": regional_ratio_2,
    #      "ks_national_ratio": national_ratio_2, "bias_ks": bias_ks, "dpl_uni_ratio": uni_ratio_3, "dpl_regional_ratio": regional_ratio_3,
    #      "dpl_national_ratio": national_ratio_3, "bias_dpl": bias_dpl})

results = {'cb_uni_ratio': 0.5841584158415841, 'cb_regional_ratio': 0.010565928619076534,
        'cb_national_ratio': 0.04760804172678346, 'ks_uni_ratio': 0.236, 
        'ks_regional_ratio': 0.010239733216576008, 'ks_national_ratio': 0.029358648517014307, 
        'dpl_uni_ratio': 0.04743438513385345, 'dpl_regional_ratio': 0.004042473453271078, 
        'dpl_national_ratio': 0.202, 'kl_uni_ratio': 0.4280013430241468, 
        'kl_regional_ratio': 0.010131917976105383, 'kl_national_ratio': 0.03077962462183963, 
        'tvd_uni_ratio': 0.916, 'tvd_regional_ratio': 0.5205560584594986, 'tvd_national_ratio': 0.7063422508130177}
#test_std_dev(results)
#female_enroll_report_statistics("datasets/UT_enrollment.csv")
#test("datasets/UT_enrollment.csv","datasets/UT_grad.csv","Southwest","Male","Black or African American")

#test_std_dev()

test("biased_enrollment.csv","biased_graduation.csv","West","Female","White")

