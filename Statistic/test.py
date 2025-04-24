""" Тест чтения файлов и некоторых методов """
import pandas as pd
import random
import math
import numpy as np
from scipy import ndimage, stats
from typing import List

file = pd.read_csv(
    filepath_or_buffer='./Files/Температура, осадки по регионам.csv',
    # dtype={'фактическая температура январь': 'float'},
    decimal=',',
    keep_default_na=False
)
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
    ja = file['fact_temp_ja']
    ju = file['fact_temp_ju']
    means = {
        'jan_mean': ja.mean(),
        'jul_mean': ju.mean(),
        'jan_median': ndimage.median(ja),
        'jul_median': ndimage.median(ju),
        'jan_trim_mean': stats.trim_mean(ja, 0.1),  # среднее усеченное
        'jul_trim_mean': stats.trim_mean(ju, 0.1),  # отбрасываем по 10% данных с каждого конца выборки
    }
    return [print(f'{metric}: {value}') for metric, value in means.items()]


def _create_list(rand=False, start=0, stop=35, n=31, is_neg=False) -> List[int]:
    """
    Возвращаем список заданной длинны
    :param rand: сгенерировать случайные числа
    :param start: от
    :param stop: до
    :param n: сколько
    :return:
    """
    if rand:
        coef = -1 if is_neg else 1
        return [coef * random.randint(start, stop) for _ in range(n)]

    return [-15, -13, -29, -17, -21, -12, -20, -32, -32, -11, -21, -18, -31, -23, -11, -25, -20, -28, -27, -13, -31,
            -23, -31, -31, -12, -13, -17, -26, -20, -18, -20]


def _mean_val(lst: List[int]) -> float:
    """ Расчет среднего """
    # return float(np.mean(lst))
    return sum(lst) / len(lst)


def mean_abs_deviations():
    """ Среднее абсолютное отклонение """
    jan_temp = _create_list()

    mean_jan_temp = _mean_val(jan_temp)
    mean_abs_dev = sum(map(lambda x: abs(x - mean_jan_temp), jan_temp)) / len(jan_temp)
    print(mean_jan_temp, mean_abs_dev)

    # NumPy Absolute mean deviation
    print('NumPy: ', np.mean(np.absolute(jan_temp - np.mean(jan_temp))))


def get_variance():
    """ Расчет дисперсии """
    jun_temp = _create_list(True, 10, 28, 30)
    mean_jun_temp = _mean_val(jun_temp)
    var = sum(map(lambda x: ((x - mean_jun_temp) ** 2), jun_temp)) / (len(jun_temp) - 1)
    print(mean_jun_temp, var)
    np_var = np.var(jun_temp)
    print('NumPy: ', np_var)
    return var, np_var


def get_standart_deviation():
    """ Расчет стандартного отклонения """
    var, np_var = get_variance()
    print('math: ', math.sqrt(var), 'NumPy: ', np.sqrt(np_var))


# df = renames_colums_df(file)
# means_median_temp(df)
mean_abs_deviations()
get_variance()
get_standart_deviation()
