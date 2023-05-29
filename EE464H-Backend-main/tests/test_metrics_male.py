from constants.specific_region_data import region_enum
from metrics import metrics
import pandas as pd
import pytest
import unittest
from datasets.test import testResults

class test_metrics(unittest.TestCase):
    #makes it so that it runs before any test runs
    @pytest.fixture(autouse=True)
    def pytest_configure(self):
        self.df_en = pd.read_csv("../datasets/biased_enrollment.csv", sep=',')
        self.df_grad = pd.read_csv("../datasets/biased_graduation.csv", sep=',')
        self.dict_en = region_enum.en_g_West
        self.dict_grad = region_enum.grad_g_West
        self.gender = "Male"
        self.race = "White"

    def test_DPL(self):
        #Act
        metric_configuration = metrics(self.df_en, self.df_grad, self.dict_en, self.dict_grad, self.gender, self.race)
        uni_ratio, regional_ratio, US_ratio = metric_configuration.DPL()
        #Assert
        assert US_ratio == 0.134
        assert regional_ratio == 0.004165589547700299
        assert uni_ratio == 0.05112963968072359

    def test_KS(self):
        #Act
        metric_configuration = metrics(self.df_en, self.df_grad, self.dict_en, self.dict_grad, self.gender, self.race)
        uni_ratio, regional_ratio, US_ratio = metric_configuration.KS()
        #Assert
        assert uni_ratio == 0.268
        assert regional_ratio == 0.0024765613236852335
        assert US_ratio == 0.07029728785234984

    def test_ClassImbalance(self):
        #Act
        metric_configuration = metrics(self.df_en, self.df_grad, self.dict_en, self.dict_grad, self.gender, self.race)
        uni_ratio, regional_ratio, US_ratio = metric_configuration.class_imbalance()
        #Assert
        assert uni_ratio == 0.3621621621621622
        assert regional_ratio == 0.002008718623355674
        assert US_ratio == 0.07546177392655426

    def test_KL(self):
        #Act
        metric_configuration = metrics(self.df_en, self.df_grad, self.dict_en, self.dict_grad, self.gender, self.race)
        uni_ratio, regional_ratio, US_ratio = metric_configuration.KL()
        #Assert
        assert uni_ratio == 0.17906369327879904
        assert regional_ratio == 0.002481539376171241
        assert US_ratio == 0.07574604297246784

    def test_TVD(self):
        #Act
        metric_configuration = metrics(self.df_en, self.df_grad, self.dict_en, self.dict_grad, self.gender, self.race)
        uni_ratio, regional_ratio, US_ratio = metric_configuration.TVD()
        #Assert
        assert uni_ratio == 0.764
        assert regional_ratio == 0.3847852605897447
        assert US_ratio == 0.5693678638402926

