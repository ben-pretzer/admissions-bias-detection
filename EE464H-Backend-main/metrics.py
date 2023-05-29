import math
from utils.counting_utils import counting_utils
from constants.specific_region_data import region_enum


class metrics():
    
    def __init__(self, df_en, df_grad, dict_en, dict_grad, gender, race):
        self.df_en = df_en
        self.df_grad = df_grad
        self.gender = gender
        self.race = race
        self.dict_en = dict_en
        self.dict_grad = dict_grad

    def KL(self):
        # enrollment
        total, count = counting_utils.get_count_total(self.df_en, self.gender, self.race)
        uni_kl_enrollment = (max(count - (total - count), (total - count) - count)) / total
        # graduation
        total, count = counting_utils.get_count_total(self.df_grad, self.gender, self.race)
        uni_kl_grad = (max(count - (total - count), (total - count) - count)) / total
        # regional enrollment
        total, count = counting_utils.get_count_total_regional(self.dict_en, self.gender, self.race)
        regional_kl_enrollment = (max(count - (total - count), (total - count) - count)) / total
        # regional graduation
        total, count = counting_utils.get_count_total_regional(self.dict_grad, self.gender, self.race)
        regional_kl_grad = (max(count - (total - count), (total - count) - count)) / total
        # national enrollment
        total, count = counting_utils.get_count_total_national_enrollment(self.gender, self.race)
        national_kl_enrollment = (max(count - (total - count), (total - count) - count)) / total
        # national graduation
        total, count = counting_utils.get_count_total_national_graduation(self.gender, self.race)
        national_kl_grad = (max(count - (total - count), (total - count) - count)) / total

        return abs(uni_kl_enrollment*math.log(uni_kl_enrollment/uni_kl_grad)), \
        abs(regional_kl_enrollment*math.log(regional_kl_enrollment/regional_kl_grad)), \
        abs(national_kl_enrollment*math.log(national_kl_enrollment/national_kl_grad))
    

    def KS(self):
        #enrollment
        total, count = counting_utils.get_count_total(self.df_en, self.gender, self.race)
        uni_ks_enrollment = max((count/total) - ((total - count)/total), ((total - count)/total) - (count/total))
        #graduation
        total, count = counting_utils.get_count_total(self.df_grad, self.gender, self.race)
        uni_ks_grad = max((count/total) - ((total - count)/total), ((total - count)/total) - (count/total))
        #regional enrollment
        total, count = counting_utils.get_count_total_regional(self.dict_en, self.gender, self.race)
        regional_ks_enrollment = max((count/total) - ((total - count)/total), ((total - count)/total) - (count/total))
        #regional graduation
        total, count = counting_utils.get_count_total_regional(self.dict_grad, self.gender, self.race)
        regional_ks_grad = max((count/total) - ((total - count)/total), ((total - count)/total) - (count/total))
        #national enrollment
        total, count = counting_utils.get_count_total_national_enrollment(self.gender, self.race)
        national_ks_enrollment = max((count/total) - ((total - count)/total), ((total - count)/total) - (count/total))
        #national graduation 
        total, count = counting_utils.get_count_total_national_graduation(self.gender, self.race)
        national_ks_grad = max((count/total) - ((total - count)/total), ((total - count)/total) - (count/total))

        return max(uni_ks_enrollment - uni_ks_grad, uni_ks_grad - uni_ks_enrollment), \
        max(regional_ks_enrollment - regional_ks_grad, regional_ks_grad - regional_ks_enrollment), \
        max(national_ks_enrollment - national_ks_grad, national_ks_grad - national_ks_enrollment)
    
    def class_imbalance(self):
        total, count = counting_utils.get_count_total(self.df_en, self.gender, self.race)
        uni_cb_enrollment = (max(count - (total - count), (total - count) - count)) / total
        #graduation
        total, count = counting_utils.get_count_total(self.df_grad, self.gender, self.race)
        uni_cb_grad = (max(count - (total - count), (total - count) - count)) / total
        #regional enrollment
        total, count = counting_utils.get_count_total_regional(self.dict_en, self.gender, self.race)
        regional_cb_enrollment = (max(count - (total - count), (total - count) - count)) / total
        #regional graduation
        total, count = counting_utils.get_count_total_regional(self.dict_grad, self.gender, self.race)
        regional_cb_grad = (max(count - (total - count), (total - count) - count)) / total
        #national enrollment
        total, count = counting_utils.get_count_total_national_enrollment(self.gender, self.race)
        national_cb_enrollment = (max(count - (total - count), (total - count) - count)) / total
        #national graduation 
        total, count = counting_utils.get_count_total_national_graduation(self.gender, self.race)
        national_cb_grad = (max(count - (total - count), (total - count) - count)) / total

        return (max(uni_cb_enrollment - uni_cb_grad, uni_cb_grad - uni_cb_enrollment)) / (uni_cb_grad + uni_cb_enrollment),\
        (max(regional_cb_enrollment - regional_cb_grad, regional_cb_grad - regional_cb_enrollment)) / (regional_cb_grad + regional_cb_enrollment),\
        (max(national_cb_enrollment - national_cb_grad, national_cb_grad - national_cb_enrollment)) / (national_cb_grad + national_cb_enrollment)
    

    def DPL(self):
        gender_dict = {'Male':0, 'Female':1}
        total, count = counting_utils.get_count_total(self.df_grad, self.gender, self.race)
        local = count / total
        
        total, count = counting_utils.get_count_total(self.df_en, self.gender, self.race)
        local -= (count / total)
        local = abs(local)

        US_metric = region_enum.en_g_USTotal[self.race][gender_dict[self.gender]] - region_enum.grad_g_USTotal[self.race][gender_dict[self.gender]]
        regional_metric = self.dict_en[self.race][gender_dict[self.gender]] - self.dict_grad[self.race][gender_dict[self.gender]]
        return abs(US_metric), abs(regional_metric), local

    def TVD(self):
        # enrollment
        total, count = counting_utils.get_count_total(self.df_en, self.gender, self.race)
        uni_tvd_enrollment = (max(count - (total - count), (total - count) - count)) / total
        # graduation
        total, count = counting_utils.get_count_total(self.df_grad, self.gender, self.race)
        uni_tvd_grad = (max(count - (total - count), (total - count) - count)) / total
        # regional enrollment
        total, count = counting_utils.get_count_total_regional(self.dict_en, self.gender, self.race)
        regional_tvd_enrollment = (max(count - (total - count), (total - count) - count)) / total
        # regional graduation
        total, count = counting_utils.get_count_total_regional(self.dict_grad, self.gender, self.race)
        regional_tvd_grad = (max(count - (total - count), (total - count) - count)) / total
        # national enrollment
        total, count = counting_utils.get_count_total_national_enrollment(self.gender, self.race)
        national_tvd_enrollment = (max(count - (total - count), (total - count) - count)) / total
        # national graduation
        total, count = counting_utils.get_count_total_national_graduation(self.gender, self.race)
        national_tvd_grad = (max(count - (total - count), (total - count) - count)) / total

        return 0.5 * (abs(uni_tvd_enrollment - uni_tvd_grad) + abs((1 - uni_tvd_enrollment) + (1 - uni_tvd_grad))), 0.5 * (abs(regional_tvd_enrollment - regional_tvd_grad) + abs((1 - regional_tvd_enrollment) + (1 - regional_tvd_grad))), 0.5 * (abs(national_tvd_enrollment - national_tvd_grad) + abs((1 - national_tvd_enrollment) + (1 - national_tvd_grad)))



