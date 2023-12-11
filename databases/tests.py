import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

import pandas as pd

from elements_appear_more_than_25percent import elements_appear_more_than_25percent
from pyspark.sql import SparkSession

def test_elements_appear_more_than_25percent():
    cases = [
        [1],
        [1, 1, 1],
        [1, 2, 3, 2],
        [1, 2, 3, 4, 4]
    ]
    cases_output =  [
        1,
        1,
        2,
        4
    ]

    for case, out in zip(cases, cases_output):
        assert elements_appear_more_than_25percent(case) == out
    

def test_can_send_sql_to_spark():
    spark = SparkSession.builder.appName("utsql").getOrCreate()
    df = spark.sql("SELECT 1").toPandas()
    spark.stop()
    del spark
    
    assert df.shape == (1, 1)
    assert df.iloc[0, 0] == 1

def test_can_create_table():
    spark = SparkSession.builder.appName("utsql").getOrCreate()
    data = [
        {'personId': 0, 'lastName': 'sarajpoor', 'firstName': 'nima'},
    ]
    df = spark.createDataFrame(data)
    df.createOrReplaceTempView('Person')
    df = spark.sql("SELECT * FROM Person").toPandas()
    print(df)
    assert True


"""def test_combine_two_tables():
    spark = SparkSession.builder.appName("utsql").getOrCreate()
   
    data = [
        {'personId': 0, 'lastName': 'sarajpoor', 'firstName': 'nima'},
        {'personId': 1, 'lastName': 'belbasi', 'firstName': 'simin'},
        {'personId': 2, 'lastName': 'life', 'firstName': 'manu'}
    ]
    df = spark.createDataFrame(data)
    df.createOrReplaceTempView("Person")
    df_Person = spark.sql("SELECT * FROM Person").toPandas()

    data = [
        {'addressId':10, 'personId':0 , 'city': 'Calgary', 'state':'Alberta'},
        {'addressId':20, 'personId':2 , 'city': 'Toronto', 'state':'Ontario'}
    ]

    df = spark.createDataFrame(data)
    df.createOrReplaceTempView("Address")
    df_Address = spark.sql("SELECT * FROM Address").toPandas()

    df_ref = df_Person.merge(df_Address, how='left', on='personId')
    df_ref = df_ref[['lastName','firstName', 'city','state']]
    df_ref.reset_index(drop=True, inplace=True)

    with open("./combine_two_tables.sql") as f:
        query = f.read()
        df_comp = spark.sql(query).toPandas()
        df_comp.reset_index(drop=True, inplace=True)
    
    spark.stop()
    del spark
    
    assert len(df_ref.compare(df_comp)) == 0"""

    
