import os

print __file__
path, filename = os.path.split(__file__)
print "__file__ path:%s" % path
print "__file__ filename %s" % filename
path = os.path.abspath(os.path.split(__file__)[0])
print "abspath:%s" % path 
print os.path.join(path, filename)
input();