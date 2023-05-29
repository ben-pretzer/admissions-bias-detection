import math
import pandas as pd


US_dict = {'name':'US','Gender':45,'Asian':6.59,'Black':11.1,'White':59.1,'Hispanic':13.06,'American Indian':.61,'Multiracial':2.85,'Non-resident':6.68}
en_Southeast = {'Name': 'en_Southeast', 'Total': 3287671611, 'Asian': 0.06798540835166156, 'Black or African American': 0.13416443008608014, 'Native Hawaiian or Other Pacific Islanders': 0.003333283641630715, 'Hispanic or Latino': 0.22854853370572845, 'Two or More Races': 0.040897789046243034, 'American Indian or Alaska Native': 0.006693024305218542, 'White': 0.5183775308634375}
en_Soutwest = {'Name': 'en_Soutwest', 'Total': 1227097367, 'Asian': 0.070929385345181, 'Black or African American': 0.13218624321276048, 'Native Hawaiian or Other Pacific Islanders': 0.003307235521107593, 'Hispanic or Latino': 0.23113095474517467, 'Two or More Races': 0.041112097015851556, 'American Indian or Alaska Native': 0.006586474078873971, 'White': 0.5147476100810507}
en_Northeast = {'Name': 'en_Northeast', 'Total': 2882487460, 'Asian': 0.06884760463103629, 'Black or African American': 0.13393577226525039, 'Native Hawaiian or Other Pacific Islanders': 0.0032497119692586627, 'Hispanic or Latino': 0.21761918922623866, 'Two or More Races': 0.04071057745382178, 'American Indian or Alaska Native': 0.006396325137872413, 'White': 0.5292408193165219}
en_Midwest = {'Name': 'en_Midwest', 'Total': 2962537766, 'Asian': 0.0667258984066568, 'Black or African American': 0.13410977256044876, 'Native Hawaiian or Other Pacific Islanders': 0.003321579934923942, 'Hispanic or Latino': 0.22412289612648267, 'Two or More Races': 0.0407030183324252, 'American Indian or Alaska Native': 0.0066834351370088155, 'White': 0.5243333995020538}
en_West = {'Name': 'en_West', 'Total': 2224983117, 'Asian': 0.06895399017987246, 'Black or African American': 0.13372092881368142, 'Native Hawaiian or Other Pacific Islanders': 0.0034181886333836844, 'Hispanic or Latino': 0.23686488898423402, 'Two or More Races': 0.040753805414155866, 'American Indian or Alaska Native': 0.006749585147526313, 'White': 0.5095386128271462}
grad_Southeast = {'Name': 'grad_Southeast', 'Total': 278420, 'Asian': 0.04027368723511242, 'Black or African American': 0.16767114431434524, 'Native Hawaiian or Other Pacific Islanders': 0.0, 'Hispanic or Latino': 0.1059622153580921, 'Two or More Races': 0.028097837799008693, 'American Indian or Alaska Native': 0.002535737375188564, 'White': 0.655459377918253}
grad_Southwest = {'Name': 'grad_Southwest', 'Total': 107235, 'Asian': 0.06728213736186879, 'Black or African American': 0.07729752412924884, 'Native Hawaiian or Other Pacific Islanders': 0.0, 'Hispanic or Latino': 0.30736233505851634, 'Two or More Races': 0.03890520818762531, 'American Indian or Alaska Native': 0.018389518347554437, 'White': 0.4907632769151863}
grad_Northeast = {'Name': 'grad_Northeast', 'Total': 240913, 'Asian': 0.09432865806328426, 'Black or African American': 0.08906534724153532, 'Native Hawaiian or Other Pacific Islanders': 0.0, 'Hispanic or Latino': 0.11735356747041463, 'Two or More Races': 0.029180658577992884, 'American Indian or Alaska Native': 0.002125248533703038, 'White': 0.6679465201130699}
grad_Midwest = {'Name': 'grad_Midwest', 'Total': 236423, 'Asian': 0.04562584858495155, 'Black or African American': 0.05172085626186961, 'Native Hawaiian or Other Pacific Islanders': 0.0, 'Hispanic or Latino': 0.06803060615929922, 'Two or More Races': 0.027222393760336347, 'American Indian or Alaska Native': 0.0011377911624503537, 'White': 0.8062625040710929}
grad_West = {'Name': 'grad_West', 'Total': 190184, 'Asian': 0.16121755773356328, 'Black or African American': 0.03126971774702393, 'Native Hawaiian or Other Pacific Islanders': 0.0, 'Hispanic or Latino': 0.2965864636352164, 'Two or More Races': 0.057097337315441886, 'American Indian or Alaska Native': 0.006278130652420813, 'White': 0.44755079291633365}
en_g_Southeast = {'Name': 'en_g_Southeast', 'Total': [444672, 620405], 'Asian': [0.0419747589234312, 0.0357024846672738], 'Black or African American': [0.15511658031088082, 0.21087193043254004], 'Native Hawaiian or Other Pacific Islanders': [0.0017136226252158894, 0.0015844488680781103], 'Hispanic or Latino': [0.12149404504893495, 0.12395128988322145], 'Two or More Races': [0.029759013385146804, 0.03224023017222621], 'American Indian or Alaska Native': [0.00459214881980426, 0.004619563027377278], 'White': [0.645349830886586, 0.5910300529492831]}
en_g_Southwest = {'Name': 'en_g_Southwest', 'Total': [201470, 301853], 'Asian': [0.06326996575172482, 0.05263157894736842], 'Black or African American': [0.09491239390479972, 0.12172150020042868], 'Native Hawaiian or Other Pacific Islanders': [0.00258102943366258, 0.0023190095841353242], 'Hispanic or Latino': [0.30498337221422545, 0.32268687076159586], 'Two or More Races': [0.03621382836154266, 0.03660722272099333], 'American Indian or Alaska Native': [0.016295230059065868, 0.018790603373165085], 'White': [0.4817441802749789, 0.4452432144123133]}
en_g_Northeast = {'Name': 'en_g_Northeast', 'Total': [283545, 423709], 'Asian': [0.09710275264949127, 0.08614638820511247], 'Black or African American': [0.1013454654464018, 0.1288030228293475], 'Native Hawaiian or Other Pacific Islanders': [0.0014530321465728545, 0.0014656285327901933], 'Hispanic or Latino': [0.12491844328060801, 0.14222969066033528], 'Two or More Races': [0.03030912200885221, 0.03179776686357854], 'American Indian or Alaska Native': [0.002426422613694475, 0.002808531326924847], 'White': [0.6424447618543794, 0.6067489715819112]}
en_g_Midwest = {'Name': 'en_g_Midwest', 'Total': [345402, 488320], 'Asian': [0.05100433697546627, 0.04463057011795544], 'Black or African American': [0.07230705091458649, 0.08652522935779816], 'Native Hawaiian or Other Pacific Islanders': [0.0011638612399464971, 0.0010812581913499345], 'Hispanic or Latino': [0.08219408109970411, 0.08449172673656619], 'Two or More Races': [0.03139819688363125, 0.033156536697247704], 'American Indian or Alaska Native': [0.004099570934736915, 0.004570773263433814], 'White': [0.7578329019519284, 0.7455439056356488]}
en_g_West = {'Name': 'en_g_West', 'Total': [361411, 530078], 'Asian': [0.1306656410568577, 0.11370213440286146], 'Black or African American': [0.04436776965836679, 0.050911375307030285], 'Native Hawaiian or Other Pacific Islanders': [0.005254405648970286, 0.004987945170333422], 'Hispanic or Latino': [0.28960656980556765, 0.3335490248604922], 'Two or More Races': [0.05326899291941861, 0.052684699232943076], 'American Indian or Alaska Native': [0.005318045106540753, 0.006427355974026464], 'White': [0.47151857580427825, 0.43773746505231304]}
grad_g_Southeast = {'Name': 'grad_g_Southeast', 'Total': [118511, 159909], 'Asian': [0.04380184117929981, 0.03765891850990251], 'Black or African American': [0.14615520922108496, 0.183616932130149], 'Native Hawaiian or Other Pacific Islanders': [0.0, 0.0], 'Hispanic or Latino': [0.10447975293432678, 0.10706089088168896], 'Two or More Races': [0.025997586721907672, 0.02965436592061735], 'American Indian or Alaska Native': [0.00257360076279839, 0.0025076762408619904], 'White': [0.6769920091805824, 0.6395012163167801]}
grad_g_Southwest = {'Name': 'grad_g_Southwest', 'Total': [45217, 62018], 'Asian': [0.0751487272486012, 0.061546647747428164], 'Black or African American': [0.0660371099365283, 0.08550743332580864], 'Native Hawaiian or Other Pacific Islanders': [0.0, 0.0], 'Hispanic or Latino': [0.2854015082822832, 0.3233738592021671], 'Two or More Races': [0.038834951456310676, 0.03895643200361185], 'American Indian or Alaska Native': [0.018355928080146848, 0.018414008836144344], 'White': [0.5162217749961298, 0.47220161888483986]}
grad_g_Northeast = {'Name': 'grad_g_Northeast', 'Total': [105277, 135636], 'Asian': [0.09198590385364325, 0.09614704060868796], 'Black or African American': [0.0779657475042032, 0.09768055678433454], 'Native Hawaiian or Other Pacific Islanders': [0.0, 0.0], 'Hispanic or Latino': [0.10751636159844981, 0.12498894098911793], 'Two or More Races': [0.02581760498494448, 0.0317909699489811], 'American Indian or Alaska Native': [0.0021657152084500887, 0.0020938393936712966], 'White': [0.6945486668503091, 0.6472986522752072]}
grad_g_Midwest = {'Name': 'grad_g_Midwest', 'Total': [106164, 130259], 'Asian': [0.04753023623827286, 0.04407373003017066], 'Black or African American': [0.04709694435025055, 0.05548944794601525], 'Native Hawaiian or Other Pacific Islanders': [0.0, 0.0], 'Hispanic or Latino': [0.06453223314871331, 0.07088185845123945], 'Two or More Races': [0.025074413172073397, 0.028973046008337236], 'American Indian or Alaska Native': [0.0006216796654233074, 0.001558433582324446], 'White': [0.8151444934252665, 0.7990234839819129]}
grad_g_West = {'Name': 'grad_g_West', 'Total': [78292, 111892], 'Asian': [0.17340213559495224, 0.15269188145711937], 'Black or African American': [0.02666939150871098, 0.034488614020662785], 'Native Hawaiian or Other Pacific Islanders': [0.0, 0.0], 'Hispanic or Latino': [0.27182853931436163, 0.31390984163300323], 'Two or More Races': [0.0559316405252133, 0.057912987523683554], 'American Indian or Alaska Native': [0.004815306800183927, 0.007301683766489114], 'White': [0.46735298625657795, 0.43369499159904196]}
en_g_USTotal = {'Name': 'en_g_USTotal', 'Total': [1636500, 2364365], 'Asian': [0.07564069660861594, 0.06623469726543914], 'Black or African American': [0.0964521845401772, 0.12323900920543147], 'Native Hawaiian or Other Pacific Islanders': [0.0024411854567674917, 0.002316055262195135], 'Hispanic or Latino': [0.17350870760769935, 0.1914399849431031], 'Two or More Races': [0.03618698441796517, 0.03749125029341916], 'American Indian or Alaska Native': [0.005714023831347388, 0.006499419505871556], 'White': [0.6100562175374274, 0.5727795835245404]}
grad_g_USTotal = {'Name': 'grad_g_USTotal', 'Total': [453461, 599714], 'Asian': [0.08136311612244493, 0.07621299486088369], 'Black or African American': [0.07851391850677346, 0.09838189537012643], 'Native Hawaiian or Other Pacific Islanders': [0.0, 0.0], 'Hispanic or Latino': [0.1427664121060025, 0.16421994484037392], 'Two or More Races': [0.03218799411636282, 0.036223933408257934], 'American Indian or Alaska Native': [0.003982701930265227, 0.004747262861964203], 'White': [0.661185857218151, 0.6202139686583938]}

def first_metric(df,threshold,category_name):
    for (columnName, columnData) in df.iteritems():
        if columnName == category_name:
            temp_dict1 = {}
            for values in columnData:
                if values in temp_dict1:
                    temp_dict1[values] += 1
                else:
                    temp_dict1[values] = 1
            majority_group = max(temp_dict1.values())
            minority_group = min(temp_dict1.values())
            # class imbalance formula, Ratio closer to 1 is bad while closer to 0 is good
            ratio_value = ((majority_group - minority_group) / (majority_group + minority_group))
            if ratio_value > threshold + .10 or ratio_value < threshold - .10:
                return ratio_value,1
            else:
                return 0,0
    return 0,0
#FUnction for website data cumulative data
# def DPL(grad_df, en_df, gender_category, race_category, region):
#     year = grad_df['Year'].max()
#     gender = {'Men':0, 'Women':1}
#     race_enrollment = {'Southeast':en_g_Southeast, 'Northeast':en_g_Northeast, 'Midwest':en_g_Midwest,'Southwest':en_g_Southwest}
#     race_grad = {'Southeast':grad_g_Southeast, 'Northeast':grad_g_Northeast, 'Midwest':grad_g_Midwest,'Southwest':grad_g_Southwest}

#     grad_df = grad_df.loc[grad_df['Year'] == year]
#     grad_df = grad_df.loc[grad_df['Sex'] == gender_category]
#     print(grad_df)
#     en_df = en_df.loc[en_df['Year'] == year]
#     print(en_df)
#     US_metric = en_g_USTotal[race_category][gender[gender_category]] - grad_g_USTotal[race_category][gender[gender_category]]
#     regional_metric = race_enrollment[region][race_category][gender[gender_category]] - race_grad[region][race_category][gender[gender_category]]
#     local = 0

#     return US_metric, regional_metric, local

def DPL(grad_df, en_df, gender_category, race_category, region):
    race_enrollment = {'Southeast':en_g_Southeast, 'Northeast':en_g_Northeast, 'Midwest':en_g_Midwest,'Southwest':en_g_Southwest, 'West':en_g_West}
    race_grad = {'Southeast':grad_g_Southeast, 'Northeast':grad_g_Northeast, 'Midwest':grad_g_Midwest,'Southwest':grad_g_Southwest, 'West':grad_g_West}
    gender = {'Male':0, 'Female':1}
    total = 0
    local = 0
    demographic_count = 0
    grad_df_gender = grad_df['Gender'].tolist()
    grad_df_race = grad_df['Race'].tolist()
    for i in range(len(grad_df_gender)):
        total += 1
        if grad_df_gender[i] == gender_category and grad_df_race[i] == 'Black':
            demographic_count += 1
    local = (demographic_count / total)
    total = 0
    demographic_count = 0
    en_df_gender = en_df['Gender'].tolist()
    en_df_race = en_df['Race'].tolist()
    print(local)
    for i in range(len(en_df_gender)):
        total += 1
        if en_df_gender[i] == gender_category and en_df_race[i] == 'Black':
            demographic_count += 1
    print(demographic_count / total)
    local -= (demographic_count / total)
    local = abs(local)


    US_metric = en_g_USTotal[race_category][gender[gender_category]] - grad_g_USTotal[race_category][gender[gender_category]]
    regional_metric = race_enrollment[region][race_category][gender[gender_category]] - race_grad[region][race_category][gender[gender_category]]
    return abs(US_metric), abs(regional_metric), local
#Potentially do US - local and US - regional and see if that falls within one standard deviation of the mean?
def std_Dev(US, regional, local):
    mean = (US + regional + local) / 3
    dev = math.sqrt((((US - mean)**2) + ((regional - mean) ** 2) + ((local - mean)**2)) / 3)
    return dev, mean

def test(file_name1, file_name2):
    df1 = pd.read_csv(file_name1, sep=',')
    df2 = pd.read_csv(file_name2, sep=',')
    US_metric, region_metric, local_metric = DPL(df1, df2, 'Female', 'Black or African American', 'Southeast')
    print(US_metric)
    print(region_metric)
    print(local_metric)
    st_dev, mean = std_Dev(US_metric, region_metric, local_metric)
    print(st_dev)
    print(mean)
    # Most people = White  #Least People = Asian for this example
    #DPL(df1, df2, 'Male')
    # race_threshold = (59.1-6.59)/(59.1+6.59)
    # print('US Race Threshold: ',race_threshold)
    # gender_threshold = (55-45)/(55+45)
    # print('US Gender Threshold: ',gender_threshold)
    # category_list = ['Gender', 'Race']
    # threshold_list = [gender_threshold,race_threshold]
    # bias_dict = {}
    # for i in range(0,len(category_list)):
    #     ratio_value,bias = first_metric(df,threshold_list[i],category_list[i])
    #     if bias == 1:
    #         bias_dict[category_list[i]] = ratio_value
    # print(bias_dict)


test('biased_data.csv', 'unbiased_data_1.csv')







