import sys
sys.path.append("Python")
sys.path.append("Python/Entities")
import common_functions
import user

ur = user.User()
ur.setUserName('Karthik-Yana')

cf = common_functions.Common_functions()
cf.insertIntoCsv('user.csv',ur)

