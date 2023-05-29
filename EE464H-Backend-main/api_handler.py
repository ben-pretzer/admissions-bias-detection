import pandas as pd
from constants.specific_region_data import region_enum
from fastapi.encoders import jsonable_encoder
from metrics import metrics
from utils.counting_utils import counting_utils
import io
import math


class api_handler():

    def __init__(self):
        self.mean_regional = 0
        self.mean_national = 0
        self.std_regional = 0
        self.std_national = 0

    def get_current_data(self, file_bytes,region,gender,race,info_type):
        df = self.convertBytesToDf(file_bytes)
        uni_total, uni_count = counting_utils.get_count_total(df, gender, race)
        regional_total = 0
        regional_count = 0
        national_total = 0
        national_count = 0
        if info_type == 'Enrollment':
            if region == 'Southeast':
                dict_en = region_enum.en_g_Southeast
                regional_total, regional_count = counting_utils.get_count_total_regional(dict_en,gender,race)
            elif region == 'Southwest':
                dict_en = region_enum.en_g_Southwest
                regional_total, regional_count = counting_utils.get_count_total_regional(dict_en, gender, race)
            elif region == 'Northeast':
                dict_en = region_enum.en_g_Northeast
                regional_total, regional_count = counting_utils.get_count_total_regional(dict_en, gender, race)
            elif region == 'Midwest':
                dict_en = region_enum.en_g_Midwest
                regional_total, regional_count = counting_utils.get_count_total_regional(dict_en, gender, race)
            else:
                dict_en = region_enum.en_g_West
                regional_total, regional_count = counting_utils.get_count_total_regional(dict_en, gender, race)
            national_total, national_count = counting_utils.get_count_total_national_enrollment(gender,race)
        else:
            if region == 'Southeast':
                dict_grad = region_enum.grad_g_Southeast
                regional_total, regional_count = counting_utils.get_count_total_regional(dict_grad,gender,race)
            elif region == 'Southwest':
                dict_grad = region_enum.grad_g_Southwest
                regional_total, regional_count = counting_utils.get_count_total_regional(dict_grad, gender, race)
            elif region == 'Northeast':
                dict_grad = region_enum.grad_g_Northeast
                regional_total, regional_count = counting_utils.get_count_total_regional(dict_grad, gender, race)
            elif region == 'Midwest':
                dict_grad = region_enum.grad_g_Midwest
                regional_total, regional_count = counting_utils.get_count_total_regional(dict_grad, gender, race)
            else:
                dict_grad = region_enum.grad_g_West
                regional_total, regional_count = counting_utils.get_count_total_regional(dict_grad, gender, race)
            national_total, national_count = counting_utils.get_count_total_national_graduation(gender, race)

        university_percentage = (uni_count/uni_total) * 100
        regional_percentage = (regional_count/regional_total) * 100
        national_percentage = (national_count / national_total) * 100
        return jsonable_encoder({'national': national_percentage, 'regional': regional_percentage, 'university': university_percentage})

    def get_data_over_time(self,region,gender,race,info_type):
        gender_1 = 0
        if gender == 'Female':
            gender_1 = 1
        dict_region = None
        dict_national = None
        if info_type == 'Enrollment':
            dict_national = region_enum.dict1_national_enroll
            if region == 'Southeast':
                dict_region = region_enum.dict1_southeast_enroll
            elif region == 'Southwest':
                dict_region = region_enum.dict1_southwest_enroll
            elif region == 'Northeast':
                dict_region = region_enum.dict1_northeast_enroll
            elif region == 'Midwest':
                dict_region = region_enum.dict1_midwest_enroll
            else:
                dict_region = region_enum.dict1_west_enroll
        else:
            dict_national = region_enum.dict1_national_grad
            if region == 'Southeast':
                dict_region = region_enum.dict1_southeast_grad
            elif region == 'Southwest':
                dict_region = region_enum.dict1_southwest_grad
            elif region == 'Northeast':
                dict_region = region_enum.dict1_northeast_grad
            elif region == 'Midwest':
                dict_region = region_enum.dict1_midwest_grad
            else:
                dict_region = region_enum.dict1_west_grad

        list_region = dict_region[race][gender_1]
        list_national = dict_national[race][gender_1]
        over_time_array = []
        for year in range(2012,2021):
            if year != 2019:
                region_nat_year_dict = {}
                index = year - 2012
                region_nat_year_dict["year"] = year
                region_nat_year_dict["regional"] = list_region[index]
                region_nat_year_dict["national"] = list_national[index]
                over_time_array.append(region_nat_year_dict)
        return jsonable_encoder(over_time_array)
        
    def convertBytesToDf(self, bytes): 
        df = pd.read_csv(io.BytesIO(bytes))
        return df

    def setRatiosMean(self,list1_regional, list2_national):
        total_regional = sum(list1_regional)
        self.mean_regional = total_regional / len(list1_regional)

        total_national = sum(list2_national)
        self.mean_national = total_national / len(list2_national)


    def setRatiosStdDev(self, list1_regional, list2_national):
        def traverse_list_std_dev(mean, list1):
            variance = 0
            for num in list1:
                variance += (num - mean) ** 2
            return math.sqrt(variance / len(list1))

        self.std_regional = traverse_list_std_dev(self.mean_regional, list1_regional)
        self.std_national = traverse_list_std_dev(self.mean_national, list2_national)


    def IsItBias(self, uni_ratio, regional_ratio, national_ratio):
        bias_regional = False
        bias_national = False

        if round((uni_ratio - self.mean_regional) / self.std_regional) != round((regional_ratio - self.mean_regional) / self.std_regional):
            bias_regional = True
        if round((uni_ratio - self.mean_national) / self.std_national) != round((national_ratio - self.mean_national) / self.std_national):
            bias_national = True

        return bias_regional, bias_national
    
    # def isItBias(self,uni_ratio, regional_ratio, national_ratio):
    #     if max(uni_ratio, regional_ratio, national_ratio) - min(uni_ratio, regional_ratio, national_ratio) > .1:
    #         return True
    #     return False

    def return_all_metrics(self, file_enrollment, file_graduation, region, gender, race):
        df_en = self.convertBytesToDf(file_enrollment)
        df_grad = self.convertBytesToDf(file_graduation)
        dict_en = None
        dict_grad = None

        if region == 'Southeast':
            dict_en = region_enum.en_g_Southeast
            dict_grad = region_enum.grad_g_Southeast
        elif region == 'Southwest':
            dict_en = region_enum.en_g_Southwest
            dict_grad = region_enum.grad_g_Southwest
        elif region == 'Northeast':
            dict_en = region_enum.en_g_Northeast
            dict_grad = region_enum.grad_g_Northeast
        elif region == 'Midwest':
            dict_en = region_enum.en_g_Midwest
            dict_grad = region_enum.grad_g_Midwest
        else:
            dict_en = region_enum.en_g_West
            dict_grad = region_enum.grad_g_West


        metrics_calculation = metrics(df_en, df_grad, dict_en, dict_grad, gender, race)
        list1_regional = []
        list2_national = []

        uni_ratio_1, regional_ratio_1, national_ratio_1 = metrics_calculation.class_imbalance()
        list1_regional.extend([uni_ratio_1, regional_ratio_1])
        list2_national.extend([uni_ratio_1, national_ratio_1])

        uni_ratio_2, regional_ratio_2, national_ratio_2 = metrics_calculation.KS()
        list1_regional.extend([uni_ratio_2, regional_ratio_2])
        list2_national.extend([uni_ratio_2, national_ratio_2])

        uni_ratio_3, regional_ratio_3, national_ratio_3 = metrics_calculation.DPL()
        list1_regional.extend([uni_ratio_3, regional_ratio_3])
        list2_national.extend([uni_ratio_3, national_ratio_3])

        uni_ratio_4, regional_ratio_4, national_ratio_4 = metrics_calculation.KL()
        list1_regional.extend([uni_ratio_4, regional_ratio_4])
        list2_national.extend([uni_ratio_4, national_ratio_4])

        uni_ratio_5, regional_ratio_5, national_ratio_5 = metrics_calculation.TVD()
        list1_regional.extend([uni_ratio_5, regional_ratio_5])
        list2_national.extend([uni_ratio_5, national_ratio_5])

        self.setRatiosMean(list1_regional, list2_national)
        self.setRatiosStdDev(list1_regional, list2_national)

        bias_cb_regional, bias_cb_national = self.IsItBias(uni_ratio_1, regional_ratio_1, national_ratio_1)
        bias_ks_regional, bias_ks_national = self.IsItBias(uni_ratio_2, regional_ratio_2, national_ratio_2)
        bias_dpl_regional, bias_dpl_national = self.IsItBias(uni_ratio_3, regional_ratio_3, national_ratio_3)
        bias_kl_regional, bias_kl_national = self.IsItBias(uni_ratio_4, regional_ratio_4, national_ratio_4)
        bias_tvd_regional, bias_tvd_national = self.IsItBias(uni_ratio_5, regional_ratio_5, national_ratio_5)

        return jsonable_encoder({"cb_uni_ratio": uni_ratio_1, "cb_regional_ratio": regional_ratio_1,
                 "cb_national_ratio": national_ratio_1,
                 "bias_cb_regional": bias_cb_regional, "bias_cb_national": bias_cb_national,
                 "ks_uni_ratio": uni_ratio_2, "ks_regional_ratio": regional_ratio_2,
                 "ks_national_ratio": national_ratio_2, "bias_ks_regional": bias_ks_regional,
                 "bias_ks_national": bias_ks_national, "dpl_uni_ratio": uni_ratio_3,
                 "dpl_regional_ratio": regional_ratio_3,
                 "dpl_national_ratio": national_ratio_3, "bias_dpl_regional": bias_dpl_regional,
                 "bias_dpl_national": bias_dpl_national, "kl_uni_ratio": uni_ratio_4,
                 "kl_regional_ratio": regional_ratio_4,
                 "kl_national_ratio": national_ratio_4, "bias_kl_regional": bias_kl_regional,
                 "bias_kl_national": bias_kl_national, "tvd_uni_ratio": uni_ratio_5,
                 "tvd_regional_ratio": regional_ratio_5,
                 "tvd_national_ratio": national_ratio_5, "bias_tvd_regional": bias_tvd_regional,
                 "bias_tvd_national": bias_tvd_national})
