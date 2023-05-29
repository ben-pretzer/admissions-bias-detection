from api_handler import api_handler
import pandas as pd
import io
from fastapi.encoders import jsonable_encoder

def test_returns_correct_values():
    #Arrange
    enrollment_csv = pd.read_csv("../datasets/biased_enrollment.csv", sep=',').to_csv()
    file_enrollment_bytes = io.BytesIO(enrollment_csv.encode('utf-8')).read()
    graduation_csv = pd.read_csv("../datasets/biased_graduation.csv", sep=',').to_csv()
    file_graduation_bytes = io.BytesIO(graduation_csv.encode('utf-8')).read()
    expected_output = jsonable_encoder({'cb_uni_ratio': 0.5841584158415841, 'cb_regional_ratio': 0.010565928619076534, 'cb_national_ratio': 0.04760804172678346, 'bias_cb_regional': True, 'bias_cb_national': True, 'ks_uni_ratio': 0.236, 'ks_regional_ratio': 0.010239733216576008, 'ks_national_ratio': 0.029358648517014307, 'bias_ks_regional': True, 'bias_ks_national': True, 'dpl_uni_ratio': 0.04743438513385345, 'dpl_regional_ratio': 0.004042473453271078, 'dpl_national_ratio': 0.202, 'bias_dpl_regional': False, 'bias_dpl_national': True, 'kl_uni_ratio': 0.4280013430241468, 'kl_regional_ratio': 0.010131917976105383, 'kl_national_ratio': 0.03077962462183963, 'bias_kl_regional': True, 'bias_kl_national': True, 'tvd_uni_ratio': 0.916, 'tvd_regional_ratio': 0.5205560584594986, 'tvd_national_ratio': 0.7063422508130177, 'bias_tvd_regional': True, 'bias_tvd_national': True})
    #Act
    actual_output = api_handler()\
        .return_all_metrics(file_enrollment_bytes, file_graduation_bytes, "West", "Female", "White")
    #print(actual_output)
    #Assert
    assert actual_output == expected_output

test_returns_correct_values()