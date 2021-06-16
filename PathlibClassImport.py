from pathlib import Path

# Absolute path  -> from root of Harddisk
# /usr/local/bin

# Relative path  -> from current directory to path

path = Path("ecommerce")
print(path.exists())  # -> checking if our Directory/PACKAGE EXISTS?


path = Path("email")
# -> make directory(will create new directory/pkg inside of our current Path)
print(path.mkdir())
print(path.rmdir())  # -> remove the directory(delete created direct/pkg)
