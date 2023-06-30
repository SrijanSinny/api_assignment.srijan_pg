# #Config parser Reading part
#
#
# mongo_details ={}
#
#
#
#
# return mongo_details
import configparser
parser = configparser.RawConfigParser()
parser.read(r'C:\Users\srijan.tirunagari\PycharmProjects\project structure\configuration\application.conf')
# config = configparser.RawConfigParser()
# client = config.read(r"C:\Users\srijan.tirunagari\PycharmProjects\project structure\configuration\application.conf")
# path1 = config.get('MongoDB', 'client')
# path2 = config.get('MongoDB', 'db')
# path3 = config.get('MongoDB', 'collection')
# path4 = config.get('MongoDB', 'double_share')
# path5 = config.get('MongoDB', 'triple_share')
