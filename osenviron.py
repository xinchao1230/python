import os
string = ""
for k, v in os.environ.items():
    string += ('%-30s %s\n' % (k, v))
with open("osEnviron.txt", "w") as f:
    f.write(string);
