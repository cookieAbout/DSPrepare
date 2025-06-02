from abc import ABC, abstractmethod


# Банкомат.
# Умеет выдавать купюры для заданной суммы, либо отвечать отказом.
# Допустимые номиналы: 50₽, 100₽, 500₽, 1000₽, 5000₽.
class ATM:
    nominals = {
        1: 50,
        2: 100,
        3: 500,
        4: 1000,
        5: 5000,
    }

    def nominals_cnt(self):
        sdk = SDK()
        d = {}
        for cassette_id in self.nominals.keys():
            d.update({cassette_id: sdk.count_banknotes(cassette_id)})
        return d

    def client_requst(self, summ):
        if summ < 50:
            raise "Минимальная сумма выдачи 50Р"
        if summ % 50 != 0:
            raise "Сумма должна быть кратна 50"
        # если сумма равна одному из номиналов, просто берем нужную касету, одну купюру
        res = {}
        d = self.nominals_cnt()
        for key, val in sorted(self.nominals.items(), key=lambda item: item[1]):
            if summ >= val:
                cnt = summ // val
                if d.get(key) >= cnt:
                    res.update({key: cnt})
                    summ = summ % val
                    d[key] -= cnt
                else:
                    res.update({key: d.get(key) - cnt})
                    # summ =

        # Иначе находим наибольший близкий номинал, делим, распределяем остаток


# API для взаимодействия с аппаратурой банкомата.
# Краткий ликбез по устройству банкомата:
# - деньги расположены в кассетах, кассеты устанавливаются инкассацией;
# - в каждой кассете лежит свой номинал банкнот, количество известно инкассатору при установке;
# - банкомат может подсчитать оставшиеся в кассетах банкноты, но эта операция занимает около 10 секунд, и шумная, её стоит вызывать как можно реже.
class SDK(ABC):
    @abstractmethod
    def count_banknotes(self, cassette_id: int) -> int:
        pass

    @abstractmethod
    def move_banknote_to_dispenser(self, cassette_id: int, count: int) -> None:
        pass

    @abstractmethod
    def open_dispenser(self) -> None:
        pass
