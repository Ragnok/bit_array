'''Goal:  Learn a fundamental data analysis skill:  how to group
data using collections.defaultdict().

The core idea is compute a feature for every element in a dataset and
then use a dictionary to group the elements based on the common features.

In the dictionary, the key is the feature and the value is a collection
of elements with that feature.  

The collection is typically a list (which allows duplicates and preserves
order) or a set (which eliminates duplicates), but it can also be a deque,
dict, array, Counter, or even another defaultdict.

'''

from collections import defaultdict
from pprint import pprint

names = '''
    raymond rachel matthew susan rodney david sue mark art
    martin shelly davin dave bill bob dolly hank adam drew
    bill mary betty able henry raymond david adam bill hal
    miriam beatrice deb henrietta bridget matt adrianna
'''.split()
