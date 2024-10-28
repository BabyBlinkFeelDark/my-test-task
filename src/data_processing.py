from .database import get_data

def process_data():
    """
    Обрабатывает данные о слябах и извлекает информацию о временных точках и параметрах.

    Использует CTE (Common Table Expression) для вычисления временных точек и группировки данных
    по идентификатору сляба.
    :return: Список словарей, где каждый словарь представляет собой строку результата запроса
    """
    query = """
    WITH TimePoints AS (
        SELECT 
            id,
            coord,
            time,
            mold_level,
            cooling,
            pyr_temperature,
            CASE WHEN coord = 10 THEN time END AS ten_point_time,
            CASE WHEN coord = 22 THEN time END AS tt_point_time,
            SUM(CASE WHEN coord = 22 THEN 1 ELSE 0 END) OVER (PARTITION BY id ORDER BY time) AS group_num
        FROM 
            Caster
        WHERE 
            coord BETWEEN 1 AND 22
    )
    SELECT 
        id,
        coord,
        MIN(time) AS zero_point_time,
        MAX(ten_point_time) AS ten_point_time,
        MAX(tt_point_time) AS tt_point_time,
        MAX(mold_level) AS mold_level,
        MAX(cooling) AS cooling,
        MAX(pyr_temperature) AS pyr_temperature
    FROM 
        TimePoints
    GROUP BY 
        id, coord, group_num
    ORDER BY 
        id, zero_point_time;
    """
    return get_data(query)
