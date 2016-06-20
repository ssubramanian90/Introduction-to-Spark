# Check loading data with sqlContext.read.text
import os.path
baseDir = os.path.join('databricks-datasets', 'cs100')
inputPath = os.path.join('lab1', 'data-001', 'shakespeare.txt')
fileName = os.path.join(baseDir, inputPath)

dataDF = sqlContext.read.text(fileName)
shakespeareCount = dataDF.count()

print shakespeareCount

# If the text file didn't load properly an AssertionError will be raised
assert shakespeareCount == 122395

#122395
