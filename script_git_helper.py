import os
from pathlib import Path

home = os.path.expanduser('~')


def do_git_operation(path, git_branch):
    os.chdir(path)
    print(f"模块：{path.name}")
    os.system("git reset --hard")
    os.system(f"git checkout {git_branch}")
    os.system("git fetch --all")
    if git_branch.startswith("origin"):
        os.system(f"git reset --hard {git_branch}")
    else:
        os.system(f"git reset --hard origin/{git_branch}")
    print("\n")


def get_input_root():
    last_root = None
    path = f"{home}/script_git_helper_input_root"
    if os.path.exists(path):
        last_root = open(path, 'r').read()

    hint = "输入项目目录："
    if last_root is not None:
        hint = f"输入项目目录（上一次输入为 {last_root}，按回车使用上一次的结果）："

    return_input_root = input(hint)
    if len(return_input_root) == 0:
        return_input_root = last_root
        if len(return_input_root) == 0:
            raise IOError("项目目录为空")
    with open(path, 'w+') as f:
        f.write(return_input_root)

    return return_input_root


def get_branch():
    last_branch = None
    path = f"{home}/script_git_helper_branch"
    if os.path.exists(path):
        last_branch = open(path, 'r').read()

    hint = "输入分支："
    if last_branch is not None:
        hint = f"输入分支（上一次输入为 {last_branch}，按回车使用上一次的结果）："

    return_branch = input(hint)
    if len(return_branch) == 0:
        return_branch = last_branch
        if len(return_branch) == 0:
            raise IOError("项目目录为空")
    with open(path, 'w+') as f:
        f.write(return_branch)

    return return_branch


if __name__ == '__main__':
    input_root = get_input_root()
    branch = get_branch()

    root_path = Path(input_root)
    if root_path.is_dir():
        for path1 in root_path.iterdir():
            if path1.name == '.git' and path1.is_dir():
                # 根目录的 git 操作
                do_git_operation(root_path, branch)
            if path1.is_dir():
                for path2 in path1.iterdir():
                    if path2.name == '.git' and path2.is_dir():
                        # 子目录的 git 操作
                        do_git_operation(path1, branch)
