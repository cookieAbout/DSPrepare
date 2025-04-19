""" Тест чтения файлов и некоторых методов """
import pandas as pd
import scipy.stats

file = pd.read_csv('./Files/Температура, осадки по регионам.csv')
rename_head = {
    'Название региона': 'region_name',
    'Код региона': 'region_code',
    'фактическая температура январь': 'fact_temp_ja',
    'отклонение от нормы 1991-2020 январь': 'norm_dev_ja',
    'фактическая температура июль': 'fact_temp_ju',
    'отклонение от нормы 1991-2020 июль': 'norm_dev_ju',
    'сумма осадков, мм январь': 'total_prec_ja',
    'отношение к норме 1991-2020, %, январь': 'norm_ratio_ja',
    'сумма осадков, мм, июль': 'total_prec_ju',
    'отношение к норме 1991-2020, %, июль': 'norm_ratio_ju',
}


def renames_colums_df(file: pd.DataFrame) -> pd.DataFrame:
    """"""
    return file.rename(columns=rename_head)


def means_median_temp(file: pd.DataFrame):
    """"""

    # return file.describe()
    # return file.head()
    return type(file['fact_temp_ja'][0])  #, file['fact_temp_ju']


df = renames_colums_df(file)
print(means_median_temp(df))
