import constants as const

csf_cmd = 'python3 {}/tools/create_solution_file.py'.format(const.REPO_PATH)
psf_cmd = 'python3 {}/tools/commit_files.py'.format(const.REPO_PATH)
rmlf_cmd = 'python3 {}/tools/remove_log_files.py'.format(const.REPO_PATH)

print(f'alias csf="{csf_cmd}"')
print(f'alias psf="{psf_cmd}"')
print(f'alias rmlf="{rmlf_cmd}"')
