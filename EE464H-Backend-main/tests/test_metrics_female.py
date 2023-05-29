from constants.specific_region_data import region_enum
from metrics import metrics
import pandas as pd
import pytest
import unittest

class test_metrics(unittest.TestCase):
    #makes it so that it runs before any test runs
    @pytest.fixture(autouse=True)
    def pytest_configure(self):
        self.df_en = pd.read_csv("../datasets/biased_enrollment.csv", sep=',')
        self.df_grad = pd.read_csv("../datasets/biased_graduation.csv", sep=',')
        self.dict_en = region_enum.en_g_West
        self.dict_grad = region_enum.grad_g_West
        self.gender = "Female"
        self.race = "White"

    def test_DPL(self):
        #Act
        metric_configuration = metrics(self.df_en, self.df_grad, self.dict_en, self.dict_grad, self.gender, self.race)
        uni_ratio, regional_ratio, US_ratio = metric_configuration.DPL()
        #Assert
        assert US_ratio == 0.202
        assert regional_ratio == 0.004042473453271078
        assert uni_ratio == 0.04743438513385345

    def test_KS(self):
        #Act
        metric_configuration = metrics(self.df_en, self.df_grad, self.dict_en, self.dict_grad, self.gender, self.race)
        uni_ratio, regional_ratio, US_ratio = metric_configuration.KS()
        #Assert
        assert uni_ratio == 0.236
        assert regional_ratio == 0.010239733216576008
        assert US_ratio == 0.029358648517014307

    def test_ClassImbalance(self):
        #Act
        metric_configuration = metrics(self.df_en, self.df_grad, self.dict_en, self.dict_grad, self.gender, self.race)
        uni_ratio, regional_ratio, US_ratio = metric_configuration.class_imbalance()
        #Assert
        assert uni_ratio == 0.5841584158415841
        assert regional_ratio == 0.010565928619076534
        assert US_ratio == 0.04760804172678346

    def test_KL(self):
        #Act
        metric_configuration = metrics(self.df_en, self.df_grad, self.dict_en, self.dict_grad, self.gender, self.race)
        uni_ratio, regional_ratio, US_ratio = metric_configuration.KL()
        #Assert
        assert uni_ratio == 0.4280013430241468
        assert regional_ratio == 0.010131917976105383
        assert US_ratio == 0.03077962462183963

    def test_TVD(self):
        #Act
        metric_configuration = metrics(self.df_en, self.df_grad, self.dict_en, self.dict_grad, self.gender, self.race)
        uni_ratio, regional_ratio, US_ratio = metric_configuration.TVD()
        #Assert
        assert uni_ratio == 0.916
        assert regional_ratio == 0.5205560584594986
        assert US_ratio == 0.7063422508130177
