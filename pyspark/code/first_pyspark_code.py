from pyspark.sql import SparkSession
import random

spark = SparkSession.builder \
    .appName("YourAppName") \
    .getOrCreate()

def check(i):
    #print(i)
    return [i+1,i+4]

def check_flat_map(i):
    #print(i)
    return i+1,i+4

def for_partition_check(i):
    s = 0
    for a in i:
        s = a+s
        print(s)
    yield s


print(spark.sparkContext.defaultParallelism)
random_list = random.sample(range(100,299),5)
rdd1 = spark.sparkContext.parallelize(random_list,3)
'''
glom partitions show krta h
'''
print(rdd1.glom().collect())

'''
map single single elment me operate karega phr jitna bada input utna he bada output dega
'''
rdd_mapp = rdd1.map(check)
print(rdd_mapp.glom().collect())

'''
flatmap single single elment me operate karega lekin input ka multiple out de skta h jo map se alg h
'''
rdd_mapp = rdd1.flatMap(check_flat_map)
print(rdd_mapp.glom().collect())

'''
mapPartitions single single elment me operate karega lekin partition level pe
'''
rdd_mapp = rdd1.mapPartitions(for_partition_check)
print(rdd_mapp.glom().collect())
