import pandas as pd
import math
from utils.counting_utils import counting_utils
from constants.specific_region_data import region_enum

def female_enroll_report_statistics(file_enroll):
    df_en = pd.read_csv(file_enroll, sep=',')
    total, count = counting_utils.get_count_total_national_enrollment('Female', 'Asian')
    total_black, count_black = counting_utils.get_count_total_national_enrollment('Female', 'Black or African American')
    total_NH, count_NH = counting_utils.get_count_total_national_enrollment('Female', 'Native Hawaiian or Other Pacific Islanders')
    total_HL, count_HL = counting_utils.get_count_total_national_enrollment('Female', 'Hispanic or Latino')
    total_2OM, count_2OM = counting_utils.get_count_total_national_enrollment('Female', 'Two or More Races')
    total_AA, count_AA = counting_utils.get_count_total_national_enrollment('Female', 'American Indian or Alaska Native')
    total_W, count_W = counting_utils.get_count_total_national_enrollment('Female', 'White')
    # count = count + count_black +count_NH + count_HL + count_2OM + count_AA + count_W
    # national_ratio_enroll = count/total
    # print("National Ratio: ", national_ratio_enroll)
    print('Asian National Enrollment Ratio: ', count/total)
    print("Black National Enrollment Ratio: ", count_black/total_black)
    print('Native Hawaiian or Other Pacific Islanders National Enroll Ratio: ', count_NH/total_NH)
    print('Hispanic or Latino National Enroll ratio: ', count_HL/total_HL)
    print('Two or More Races National Enroll Ratio: ', count_2OM/total_2OM)
    print('American Indian or Alaska Native National Enroll Ratio: ', count_AA/total_AA)
    print('White National Enroll Ratio: ', count_W/total_W)

    #Stats for actual university
    total, count = counting_utils.get_count_total(df_en, 'Female', 'Asian')
    total_black, count_black = counting_utils.get_count_total(df_en, 'Female', 'Black or African American')
    total_NH, count_NH =  counting_utils.get_count_total(df_en, 'Female', 'Native Hawaiian or Other Pacific Islanders')
    total_HL, count_HL = counting_utils.get_count_total(df_en, 'Female', 'Hispanic or Latino')
    total_2OM, count_2OM = counting_utils.get_count_total(df_en, 'Female', 'Two or More Races')
    total_AA, count_AA = counting_utils.get_count_total(df_en, 'Female', 'American Indian or Alaskan Native')
    total_W, count_W = counting_utils.get_count_total(df_en, 'Female', 'White')
    count = count + count_black +count_NH + count_HL + count_2OM + count_AA + count_W
    university_enroll_ratio = count / total
    print('Asian Uni Enrollment Ratio: ', university_enroll_ratio)
    print("Black Uni Enrollment Ratio: ", count_black/total_black)
    print('Native Hawaiian or Other Pacific Islanders Uni Enroll Ratio: ', count_NH/total_NH)
    print('Hispanic or Latino Uni Enroll ratio: ', count_HL/total_HL)
    print('Two or More Races Uni Enroll Ratio: ', count_2OM/total_2OM)
    print('American Indian or Alaska Native Uni Enroll Ratio: ', count_AA/total_AA)
    print('White Uni Enroll Ratio: ', count_W/total_W)
    # print('Actual University Ratio: ', university_enroll_ratio)

    #Data for regional enrollment
    dict_en = region_enum.en_g_Southwest
    total, count = counting_utils.get_count_total_regional(dict_en, 'Female', 'Asian')
    total_black, count_black =  counting_utils.get_count_total_regional(dict_en, 'Female', 'Black or African American')
    total_NH, count_NH =  counting_utils.get_count_total_regional(dict_en, 'Female', 'Native Hawaiian or Other Pacific Islanders')
    total_HL, count_HL = counting_utils.get_count_total_regional(dict_en, 'Female', 'Hispanic or Latino')
    total_2OM, count_2OM = counting_utils.get_count_total_regional(dict_en, 'Female', 'Two or More Races')
    total_AA, count_AA = counting_utils.get_count_total_regional(dict_en, 'Female', 'American Indian or Alaska Native')
    total_W, count_W = counting_utils.get_count_total_regional(dict_en, 'Female', 'White')
    # count = count + count_black +count_NH + count_HL + count_2OM + count_AA + count_W
    regional_enroll_ratio = count / total
    print('Asian Regional Enrollment Ratio: ', regional_enroll_ratio)
    print("Black Regional Enrollment Ratio: ", count_black/total_black)
    print('Native Hawaiian or Other Pacific Islanders Regional Enroll Ratio: ', count_NH/total_NH)
    print('Hispanic or Latino Regional Enroll ratio: ', count_HL/total_HL)
    print('Two or More Races Regional Enroll Ratio: ', count_2OM/total_2OM)
    print('American Indian or Alaska Native Regional Enroll Ratio: ', count_AA/total_AA)
    print('White Regional Enroll Ratio: ', count_W/total_W)
    # print('Enrollment Regional Ratio: ', regional_enroll_ratio)

def female_grad_report_statistics(file_grad):
    df_en = pd.read_csv(file_grad, sep=',')
    total, count = counting_utils.get_count_total_national_graduation('Female', 'Asian')
    total_black, count_black = counting_utils.get_count_total_national_graduation('Female', 'Black or African American')
    total_NH, count_NH = counting_utils.get_count_total_national_graduation('Female', 'Native Hawaiian or Other Pacific Islanders')
    total_HL, count_HL = counting_utils.get_count_total_national_graduation('Female', 'Hispanic or Latino')
    total_2OM, count_2OM = counting_utils.get_count_total_national_graduation('Female', 'Two or More Races')
    total_AA, count_AA = counting_utils.get_count_total_national_graduation('Female', 'American Indian or Alaska Native')
    total_W, count_W = counting_utils.get_count_total_national_graduation('Female', 'White')
    # count = count + count_black +count_NH + count_HL + count_2OM + count_AA + count_W
    # national_ratio_grad = count/total
    # print("National Ratio: ", national_ratio_grad)
    print('Asian National Grad Ratio: ', count/total)
    print("Black National Grad Ratio: ", count_black/total_black)
    print('Native Hawaiian or Other Pacific Islanders National Grad Ratio: ', count_NH/total_NH)
    print('Hispanic or Latino National Grad ratio: ', count_HL/total_HL)
    print('Two or More Races National Grad Ratio: ', count_2OM/total_2OM)
    print('American Indian or Alaska Native National Grad Ratio: ', count_AA/total_AA)
    print('White National Grad Ratio: ', count_W/total_W)

    total, count = counting_utils.get_count_total(df_en, 'Female', 'Asian')
    total_black, count_black = counting_utils.get_count_total(df_en, 'Female', 'Black or African American')
    total_NH, count_NH =  counting_utils.get_count_total(df_en, 'Female', 'Native Hawaiian or Other Pacific Islanders')
    total_HL, count_HL = counting_utils.get_count_total(df_en, 'Female', 'Hispanic or Latino')
    total_2OM, count_2OM = counting_utils.get_count_total(df_en, 'Female', 'Two or More Races')
    total_AA, count_AA = counting_utils.get_count_total(df_en, 'Female', 'American Indian or Alaskan Native')
    total_W, count_W = counting_utils.get_count_total(df_en, 'Female', 'White')
    count = count + count_black +count_NH + count_HL + count_2OM + count_AA + count_W
    university_grad_ratio = count / total
    print('Asian Uni Grad Ratio: ', university_grad_ratio)
    print("Black Uni Grad Ratio: ", count_black/total_black)
    print('Native Hawaiian or Other Pacific Islanders Uni Grad Ratio: ', count_NH/total_NH)
    print('Hispanic or Latino Uni Grad ratio: ', count_HL/total_HL)
    print('Two or More Races Uni Grad Ratio: ', count_2OM/total_2OM)
    print('American Indian or Alaska Native Uni Grad Ratio: ', count_AA/total_AA)
    print('White Uni Grad Ratio: ', count_W/total_W)
    # print('Actual University Ratio: ', university_grad_ratio)

    #Data for regional graduation
    dict_grad = region_enum.grad_g_Southwest
    total, count = counting_utils.get_count_total_regional(dict_grad, 'Female', 'Asian')
    total_black, count_black =  counting_utils.get_count_total_regional(dict_grad, 'Female', 'Black or African American')
    total_NH, count_NH =  counting_utils.get_count_total_regional(dict_grad, 'Female', 'Native Hawaiian or Other Pacific Islanders')
    total_HL, count_HL = counting_utils.get_count_total_regional(dict_grad, 'Female', 'Hispanic or Latino')
    total_2OM, count_2OM = counting_utils.get_count_total_regional(dict_grad, 'Female', 'Two or More Races')
    total_AA, count_AA = counting_utils.get_count_total_regional(dict_grad, 'Female', 'American Indian or Alaska Native')
    total_W, count_W = counting_utils.get_count_total_regional(dict_grad, 'Female', 'White')
    count = count + count_black +count_NH + count_HL + count_2OM + count_AA + count_W
    regional_grad_ratio = count / total
    print('Asian Regional Grad Ratio: ', regional_grad_ratio)
    print("Black Regional Grad Ratio: ", count_black/total_black)
    print('Native Hawaiian or Other Pacific Islanders Regional Grad Ratio: ', count_NH/total_NH)
    print('Hispanic or Latino Regional Grad ratio: ', count_HL/total_HL)
    print('Two or More Races Regional Grad Ratio: ', count_2OM/total_2OM)
    print('American Indian or Alaska Native Regional Grad Ratio: ', count_AA/total_AA)
    print('White Regional Grad Ratio: ', count_W/total_W)
    # print('Regional Grad Ratio: ', regional_grad_ratio)

'''The data for all race enrollment'''
def allRaces_report_statistics(file_en):
    df_en = pd.read_csv(file_en, sep=',')
    total, count = counting_utils.get_count_total_national_enrollment('Female', 'Asian')
    total_black, count_black = counting_utils.get_count_total_national_enrollment('Female', 'Black or African American')
    total_NH, count_NH = counting_utils.get_count_total_national_enrollment('Female', 'Native Hawaiian or Other Pacific Islanders')
    total_HL, count_HL = counting_utils.get_count_total_national_enrollment('Female', 'Hispanic or Latino')
    total_2OM, count_2OM = counting_utils.get_count_total_national_enrollment('Female', 'Two or More Races')
    total_AA, count_AA = counting_utils.get_count_total_national_enrollment('Female', 'American Indian or Alaska Native')
    total_W, count_W = counting_utils.get_count_total_national_enrollment('Female', 'White')
    # count = count + count_black +count_NH + count_HL + count_2OM + count_AA + count_W
    # national_ratio_enroll = count/total
    # print("National Ratio: ", national_ratio_enroll)
    print('Asian National Enrollment Ratio: ', count/total)
    print("Black National Enrollment Ratio: ", count_black/total_black)
    print('Native Hawaiian or Other Pacific Islanders National Enroll Ratio: ', count_NH/total_NH)
    print('Hispanic or Latino National Enroll ratio: ', count_HL/total_HL)
    print('Two or More Races National Enroll Ratio: ', count_2OM/total_2OM)
    print('American Indian or Alaska Native National Enroll Ratio: ', count_AA/total_AA)
    print('White National Enroll Ratio: ', count_W/total_W)

    #Stats for actual university
    total, count = counting_utils.get_count_total(df_en, 'Female', 'Asian')
    total_black, count_black = counting_utils.get_count_total(df_en, 'Female', 'Black or African American')
    total_NH, count_NH =  counting_utils.get_count_total(df_en, 'Female', 'Native Hawaiian or Other Pacific Islanders')
    total_HL, count_HL = counting_utils.get_count_total(df_en, 'Female', 'Hispanic or Latino')
    total_2OM, count_2OM = counting_utils.get_count_total(df_en, 'Female', 'Two or More Races')
    total_AA, count_AA = counting_utils.get_count_total(df_en, 'Female', 'American Indian or Alaskan Native')
    total_W, count_W = counting_utils.get_count_total(df_en, 'Female', 'White')
    count = count + count_black +count_NH + count_HL + count_2OM + count_AA + count_W
    university_enroll_ratio = count / total
    print('Asian Uni Enrollment Ratio: ', university_enroll_ratio)
    print("Black Uni Enrollment Ratio: ", count_black/total_black)
    print('Native Hawaiian or Other Pacific Islanders Uni Enroll Ratio: ', count_NH/total_NH)
    print('Hispanic or Latino Uni Enroll ratio: ', count_HL/total_HL)
    print('Two or More Races Uni Enroll Ratio: ', count_2OM/total_2OM)
    print('American Indian or Alaska Native Uni Enroll Ratio: ', count_AA/total_AA)
    print('White Uni Enroll Ratio: ', count_W/total_W)
    # print('Actual University Ratio: ', university_enroll_ratio)

    #Data for regional enrollment
    dict_en = region_enum.en_g_Southwest
    total, count = counting_utils.get_count_total_regional(dict_en, 'Female', 'Asian')
    total_black, count_black =  counting_utils.get_count_total_regional(dict_en, 'Female', 'Black or African American')
    total_NH, count_NH =  counting_utils.get_count_total_regional(dict_en, 'Female', 'Native Hawaiian or Other Pacific Islanders')
    total_HL, count_HL = counting_utils.get_count_total_regional(dict_en, 'Female', 'Hispanic or Latino')
    total_2OM, count_2OM = counting_utils.get_count_total_regional(dict_en, 'Female', 'Two or More Races')
    total_AA, count_AA = counting_utils.get_count_total_regional(dict_en, 'Female', 'American Indian or Alaska Native')
    total_W, count_W = counting_utils.get_count_total_regional(dict_en, 'Female', 'White')
    # count = count + count_black +count_NH + count_HL + count_2OM + count_AA + count_W
    regional_enroll_ratio = count / total
    print('Asian Regional Enrollment Ratio: ', regional_enroll_ratio)
    print("Black Regional Enrollment Ratio: ", count_black/total_black)
    print('Native Hawaiian or Other Pacific Islanders Regional Enroll Ratio: ', count_NH/total_NH)
    print('Hispanic or Latino Regional Enroll ratio: ', count_HL/total_HL)
    print('Two or More Races Regional Enroll Ratio: ', count_2OM/total_2OM)
    print('American Indian or Alaska Native Regional Enroll Ratio: ', count_AA/total_AA)
    print('White Regional Enroll Ratio: ', count_W/total_W)
    # print('Enrollment Regional Ratio: ', regional_enroll_ratio)

female_enroll_report_statistics('datasets/UT_enrollment.csv')
female_grad_report_statistics('datasets/UT_grad.csv')