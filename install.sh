# Nikhil Anand <https://github.com/muj-programmer/cp_solutions>
#
# script to check for required packages,
# setup the template git repository and
# perform through clean after the setup

# ==== Helper Methods ==== #
# constants
tick="\xE2\x9C\x93"
cross="\xe2\x9c\x97"
error="\033[0;31m"
success="\033[0;32m"
reset="\033[0m"
origin=$1

# check if package is available
is_available() {

    # if prev command exit code != 0
    #    exit with code = 1

    if [ $? -ne 0 ]; then
        echo "$error[$cross]$reset $1 not found"
        exit 1
    fi
}

# check if package is compatible
is_compatible() {

    # version 1 => $1
    # version 2 => $2
    # command name => $3
    #
    # if version 1 < version 2
    #    exit with code = 2
    # else
    #    echo compatible version

    x1=$(echo $1 | tr "." " " | cut -d " " -f 1)
    y1=$(echo $1 | tr "." " " | cut -d " " -f 2)

    x2=$(echo $2 | tr "." " " | cut -d " " -f 1)
    y2=$(echo $2 | tr "." " " | cut -d " " -f 2)

    if (($x1 <= $x2 && $y1 < $y2)); then
        echo "$error[$cross]$reset $3 version not supported"
        exit 2
    else
        echo "$success[$tick]$reset $3 v$1 found"
    fi
}

# ==== Check Dependencies ==== #
# check for git requirements
git_cmd=$(git --version 2>/dev/null)

is_available "git"

git_version=$(echo $git_cmd | cut -d " " -f 3)

is_compatible $git_version "1.17.0" "git"

# check for python3 requirements
python_cmd=$(python3 --version 2>/dev/null)

is_available "python3"

python_version=$(echo $python_cmd | cut -d " " -f 2)

is_compatible $python_version "3.4.0" "python"

# ==== Housekeeping ==== #
# remove .git
rm -rf .git

echo "$success[$tick]$reset initialized new git repo"
git init &> /dev/null

# add origin to remote
git remote add origin $origin

# create a initial commit
git add -A &> /dev/null
git commit -m "initial commit from install script" &> /dev/null

echo "$success[$tick]$reset created a initial commit"

# push to the remote
git push origin master &> /dev/null

echo "$success[$tick]$reset pushed to the remote"

echo "\n Setup is complete 🔥"
echo "\n Would love it if you 🌟  the repo << https://github.com/muj-programmer/cp_solutions >>"
echo " Have a nice day! 🤗"