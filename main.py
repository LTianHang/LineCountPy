import os
import argparse
import sys


def Count_lines_suffix(path, suffix="*"):
    cnt = 0
    for name in os.listdir(path):
        fpath = os.path.join(path, name)
        if os.path.isfile(fpath) and fpath.endswith(suffix):
            with open(fpath, 'rb') as f:
                fcnt = len(f.readlines())
                cnt += fcnt
                # print(fpath, fcnt, cnt)
                print(fpath, "共" + str(fcnt) + "行")
        elif os.path.isdir(fpath):
            cnt += Count_lines_suffix(fpath, suffix)
    return cnt


def Count_lines(path):
    cnt = 0
    for name in os.listdir(path):
        fpath = os.path.join(path, name)
        if os.path.isfile(fpath):
            with open(fpath, 'rb') as f:
                fcnt = len(f.readlines())
                cnt += fcnt
                # print(fpath, fcnt, cnt)
                print(fpath, "共" + str(fcnt) + "行")
        elif os.path.isdir(fpath):
            cnt += Count_lines(fpath)
    return cnt


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    if (len(sys.argv)) < 2:
        print('useage : ./Count_lines.exe -h')
    else:
        parser = argparse.ArgumentParser()
        parser.description = 'Count lines Tool by keleth'
        parser.add_argument('-p', help="Path -> Your Source Directory", type=str, dest='check_path')
        parser.add_argument('-e', help="Suffix -> File Suffixes You Want To Count", type=str, dest='check_suffix')
        args = parser.parse_args()
        if os.path.exists(args.check_path):
            if args.check_path and args.check_suffix:
                print("此目录下文件后缀为" + args.check_suffix + "的文件行数共为: ",
                      Count_lines_suffix(args.check_path, args.check_suffix))
            elif args.check_path:
                print("此目录下文件行数共为: ", Count_lines(args.check_path))
            else:
                print('useage : ./Count_lines.exe -h')
        else:
            print("您输入的路径有误, 请输入文件夹名称! ")
            print('useage : ./Count_lines.exe -h')
