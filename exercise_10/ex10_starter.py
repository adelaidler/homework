import glob, os

# Get the directory name
if os.name == 'nt':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,"c:/",'*')
files = glob.glob(pattern)
for file in files:
    # if os.path.getsize(file) > 0:
    print(file)
    print(os.path.getsize(file))
