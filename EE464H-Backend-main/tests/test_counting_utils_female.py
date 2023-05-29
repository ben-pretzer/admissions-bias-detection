from utils.counting_utils import counting_utils
from constants.specific_region_data import region_enum
import pandas as pd
import pytest
import unittest

class test_unit_counting(unittest.TestCase):
    #makes it so that it runs before any test runs
    @pytest.fixture(autouse=True)
    def pytest_configure(self):
        self.df_en = pd.read_csv("../datasets/biased_enrollment.csv", sep=',')
        self.df_grad = pd.read_csv("../datasets/biased_graduation.csv", sep=',')
        self.dict_en = region_enum.en_g_West
        self.dict_grad = region_enum.grad_g_West
        self.gender = "Female"
        self.race = "White"

    def test_get_count_total(self):
        #Act 
        actual_total_enrollment, actual_count_enrollment = \
            counting_utils.get_count_total(self.df_en, self.gender, self.race)
        actual_total_graduation, actual_count_graduation = \
            counting_utils.get_count_total(self.df_grad, self.gender, self.race)
        #Assert
        assert actual_count_enrollment == 170
        assert actual_count_graduation == 271
        assert actual_total_enrollment == 500
        assert actual_total_graduation == 500

    def test_get_count_total_regional(self):
        actual_total_regional_enrollment, actual_count_regional_enrollment = \
            counting_utils.get_count_total_regional(self.dict_en, self.gender, self.race)
        actual_total_regional_graduation, actual_count_regional_graduation = \
            counting_utils.get_count_total_regional(self.dict_grad, self.gender, self.race)
        
        assert actual_count_regional_enrollment == 232035
        assert actual_count_regional_graduation == 48527
        assert actual_total_regional_enrollment == 891489
        assert actual_total_regional_graduation == 190184

    def test_get_count_total_national_enrollment(self):
        actual_total_national, actual_count_national = \
            counting_utils.get_count_total_national_enrollment(self.gender, self.race)
        
        assert actual_total_national == 4000865
        assert actual_count_national == 1354260

    def test_get_count_total_national_graduation(self):
        actual_total_national, actual_count_national = \
        counting_utils.get_count_total_national_graduation(self.gender, self.race)
        
        assert actual_total_national == 1053175
        assert actual_count_national == 371951
