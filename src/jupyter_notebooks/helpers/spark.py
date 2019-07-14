from pyspark import SparkContext
from pyspark.sql import Row
from pyspark.sql import SparkSession

def spark_session(app_name):
    return SparkSession \
        .builder \
        .appName(app_name) \
        .getOrCreate()

def convert_to_df(values, attr_names=None):
    """
    Converts either a list of dict or a list of tuples to a Spark DataFrame.

    Acceptable types for values are (mapped to the spark types in pyspark.sql.types):

    - bool
    - int, long
    - float, decimal.Decimal
    - str, unicode
    - bytearray
    - datetime.date, datetime.datetime
    - list, tuple, array
    - dict

    Parameters:
    -----------
    values : list of dict or list of tuple
        A list of dict to be converted as list of pyspark.sql.Row. The dict must
        contain str as keys (will be the Data frame attribute name) and simple types
        as values (the accepted types are listed above).
        Every dict must contain the exact same keys and value types.

        A list of tuple to be converted as list of pyspark.sql.Row. attr_names is required in this case.
        The tuple content must contain simple types as values (the accepted types are listed above).
        Every tuple must contain the exact value types and size must be the same as attr_names.

    attr_names : list of str
        If values is a list of tuple, attr_names contains the corresponding attribute names.

    Returns:
    --------
        pyspark.sql.dataframe.DataFrame

    Examples:
    --------
    To convert a list of dict:

    ```
    convert_to_df([{'Person': 'Eric', 'Age': 31}, {'Person': 'Laura', 'Age': 29}])
    ```

    To convert a list of tuples:

    ```
    convert_to_df([('Eric', 31), ('Laura', 29)], attr_names=['Person', 'Age'])
    ```
    """
    if attr_names is not None:
        SparkRow = Row(*attr_names)
        def _convert_to_row(d):
            return SparkRow(*d)
    else:
        def _convert_to_row(d):
            return Row(**d)
    sc = SparkContext.getOrCreate()
    return sc.parallelize(values).map(_convert_to_row).toDF()

