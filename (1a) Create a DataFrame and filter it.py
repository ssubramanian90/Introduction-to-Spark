# Check that Spark is working
from pyspark.sql import Row
data = [('Alice', 1), ('Bob', 2), ('Bill', 4)]
df = sqlContext.createDataFrame(data, ['name', 'age'])
fil = df.filter(df.age > 3).collect()
print fil

# If the Spark job doesn't work properly this will raise an AssertionError
assert fil == [Row(u'Bill', 4)]

#[Row(name=u'Bill', age=4)]
