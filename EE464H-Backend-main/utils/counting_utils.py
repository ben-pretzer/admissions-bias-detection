from constants.specific_region_data import region_enum


class counting_utils():
    @staticmethod
    def get_count_total(df, gender, race):
        df_gender = df['Gender'].tolist()
        df_race = df['Race'].tolist()
        total = 0
        count = 0
        for i in range(0,len(df_gender)):
            total += 1
            if df_gender[i] == gender and df_race[i] == race:
                count += 1
        return total, count

    @staticmethod
    def get_count_total_regional(dict, gender, race):
        total = 0
        count = 0
        total = dict['Total'][0] + dict['Total'][1]
        if gender == 'Male':
            count = dict[race][0] * dict['Total'][0]
        else:
            count = dict[race][1] * dict['Total'][1]
        return total, count


    @staticmethod
    def get_count_total_national_enrollment(gender, race):
        total = region_enum.en_g_Southeast['Total'][0] + region_enum.en_g_Southeast['Total'][1] + \
                region_enum.en_g_Southwest['Total'][0] + region_enum.en_g_Southwest['Total'][1] + \
                region_enum.en_g_Northeast['Total'][0] + region_enum.en_g_Northeast['Total'][1] + \
                region_enum.en_g_Midwest['Total'][0] + region_enum.en_g_Midwest['Total'][1] + \
                region_enum.en_g_West['Total'][0] + region_enum.en_g_West['Total'][1]
        
        if gender == 'Male':
            count = (region_enum.en_g_Southeast[race][0] * region_enum.en_g_Southeast['Total'][0]) + (
                        region_enum.en_g_Southwest[race][0] * region_enum.en_g_Southwest['Total'][0]) + (
                                region_enum.en_g_Northeast[race][0] * region_enum.en_g_Northeast['Total'][0]) + (
                                region_enum.en_g_Midwest[race][0] * region_enum.en_g_Midwest['Total'][0]) + (
                                region_enum.en_g_West[race][0] * region_enum.en_g_West['Total'][0])
        else:
            count = (region_enum.en_g_Southeast[race][1] * region_enum.en_g_Southeast['Total'][1]) + (
                        region_enum.en_g_Southwest[race][1] * region_enum.en_g_Southwest['Total'][1]) + (
                                region_enum.en_g_Northeast[race][1] * region_enum.en_g_Northeast['Total'][1]) + (
                                region_enum.en_g_Midwest[race][1] * region_enum.en_g_Midwest['Total'][1]) + (
                                region_enum.en_g_West[race][1] * region_enum.en_g_West['Total'][1])
        
        return total, count
        


    @staticmethod
    def get_count_total_national_graduation(gender, race):
        total = region_enum.grad_g_Southeast['Total'][0] + region_enum.grad_g_Southeast['Total'][1] + \
                region_enum.grad_g_Southwest['Total'][0] + region_enum.grad_g_Southwest['Total'][1] + \
                region_enum.grad_g_Northeast['Total'][0] + region_enum.grad_g_Northeast['Total'][1] + \
                region_enum.grad_g_Midwest['Total'][0] + region_enum.grad_g_Midwest['Total'][1] + \
                region_enum.grad_g_West['Total'][0] + region_enum.grad_g_West['Total'][1]
        
        if gender == 'Male':
            count = (region_enum.grad_g_Southeast[race][0] * region_enum.grad_g_Southeast['Total'][0]) + (
                        region_enum.grad_g_Southwest[race][0] * region_enum.grad_g_Southwest['Total'][0]) + (
                                region_enum.grad_g_Northeast[race][0] * region_enum.grad_g_Northeast['Total'][0]) + (
                                region_enum.grad_g_Midwest[race][0] * region_enum.grad_g_Midwest['Total'][0]) + (
                                region_enum.grad_g_West[race][0] * region_enum.grad_g_West['Total'][0])
        else:
            count = (region_enum.grad_g_Southeast[race][1] * region_enum.grad_g_Southeast['Total'][1]) + (
                        region_enum.grad_g_Southwest[race][1] * region_enum.grad_g_Southwest['Total'][1]) + (
                                region_enum.grad_g_Northeast[race][1] * region_enum.grad_g_Northeast['Total'][1]) + (
                                region_enum.grad_g_Midwest[race][1] * region_enum.grad_g_Midwest['Total'][1]) + (
                                region_enum.grad_g_West[race][1] * region_enum.grad_g_West['Total'][1])
        
        return total, count