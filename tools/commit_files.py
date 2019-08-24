import constants as const
from git import Repo
from datetime import datetime
from pathlib import Path
from subprocess import call
from os import stat

repo = Repo(path=const.REPO_PATH)

now = datetime.now().strftime("%Y%m%d_%H%M%S")

Path(const.LOG_PATH).mkdir(exist_ok=True)
# create log file to keep stdout from subprocess.call
log_file = open("{}/{}.log".format(const.LOG_PATH, now), "a")


def commit_files(files):
    count = 0

    for f in files:
        solution_abbr = None

        with open(Path(const.REPO_PATH).joinpath(f)) as target:
            solution_abbr = target.readline().strip("#").split()[0]
            if solution_abbr == 'PVT':
                continue

        count += 1
        commit_emoji = None
        commit_msg = None

        call(["git", "add", f], stdout=log_file, cwd=const.REPO_PATH)

        if solution_abbr == 'AC':
            commit_emoji = const.EMOJI_AC
            commit_msg = const.MSG_AC
        elif solution_abbr == 'WA':
            commit_emoji = const.EMOJI_WA
            commit_msg = const.MSG_WA
        elif solution_abbr == 'TLE':
            commit_emoji = const.EMOJI_TLE
            commit_msg = const.MSG_TLE
        else:
            commit_emoji = const.EMOJI_INC
            commit_msg = const.MSG_INC

        call(["git", "commit", "-m", f"{commit_emoji} {commit_msg}"],
             stdout=log_file,
             cwd=const.REPO_PATH)

    return count

# list containing modified files
modified_files = [item.a_path for item in repo.index.diff(None)]
# list containing untracked files
untracked_files = repo.untracked_files

print("Modified Files:", commit_files(modified_files))
print("Untracked Files:", commit_files(untracked_files))

# check if log file is empty
if stat("{}/{}.log".format(const.LOG_PATH, now)).st_size == 0:
    log_file.write("Everything up-to-date")
log_file.close()