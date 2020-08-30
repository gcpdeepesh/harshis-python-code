# How to connect to github internet public

…or create a new repository on the command line
echo "# harshis-python-code" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/gcpdeepesh/harshis-python-code.git
git push -u origin master

…or push an existing repository from the command line
git remote add origin https://github.com/gcpdeepesh/harshis-python-code.git
git branch -M master
git push -u origin master




# How to upload in GitLab Office SDC

FIRST connect to Forticlient Ubuntu. At 40% load, it will ask for certificate , click Yes there.

1. Go to your Python folder, on your PC
2. Right click there, and in opened menu select "Git Bash here"
3. In opened window, run following commands:
git add -A
git commit -m "Added Star.py and Rosette and Polygon 2.py"
---- In above command, write your changes within double quotes and then only run
git push


