# TEST Compare with hash (2a)
# Check our testing library/package
# This should print '1 test passed.' on two lines

from databricks_test_helper import Test

twelve = 12
Test.assertEquals(twelve, 12, 'twelve should equal 12')
Test.assertEqualsHashed(twelve, '7b52009b64fd0a2a49e6d8a939753077792b0554',
                        'twelve, once hashed, should equal the hashed value of 12')
