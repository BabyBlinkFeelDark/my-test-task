class Caster:
    """
    Класс, представляющий таблицу слябов.

    Attributes:
        id (int): Уникальный идентификатор сляба.
        coord (tuple): Координаты сляба (например, (x, y)).
        zero_point_time (float): Время в нулевой точке.
        ten_point_time (float): Время в десятой точке.
        tt_point_time (float): Время в двадцать второй точке.
        mold_level (int): Ширина металла.
        cooling (float): Расход охлаждения в точке 10.
        pyr_temperature (float): Температура металла.
    """
    def __init__(self, id, coord, zero_point_time, ten_point_time, tt_point_time, mold_level, cooling, pyr_temperature):
        """
        Инициализация объекта Caster.

        :param id: Уникальный идентификатор сляба
        :param coord: Координаты сляба (например, (x, y)).
        :param zero_point_time: Время в нулевой точке.
        :param ten_point_time: Время в десятой точке.
        :param tt_point_time: Время в двадцать второй точке.
        :param mold_level: Ширина металла.
        :param cooling: Расход охлаждения в точке 10.
        :param pyr_temperature: Температура металла.
        """
        self.id = id
        self.coord = coord
        self.zero_point_time = zero_point_time
        self.ten_point_time = ten_point_time
        self.tt_point_time = tt_point_time
        self.mold_level = mold_level
        self.cooling = cooling
        self.pyr_temperature = pyr_temperature

    def __repr__(self):
        """
        Возвращает строковое представление объекта Caster.

        :return: Строковое представление объекта с его идентификатором и координатами.
        """
        return f"Caster(id={self.id}, coord={self.coord})"

