from shutil import which
import os

commands = {}


def installed(name: str):
    return which(name) is not None


def checkcmd(cmd: str):
    def wrapper_out(func):
        def wrapper(*args, **kwargs):
            if installed(cmd):
                func(*args, **kwargs)
            else:
                print("ERR: " + cmd + " 未安装")
                return True  # the os.system zero when succeed

        return wrapper

    return wrapper_out


class Mset:
    def new_command_map(self, cmd: list, func):
        global commands
        for k in cmd:
            commands[k] = func

    @checkcmd("pip")
    def pypi(self):
        return os.system(
            "pip config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple/"
        )

    @checkcmd("npm")
    def npm(self):
        return os.system(
            "npm config set registry https://mirrors.cloud.tencent.com/npm/"
        )

    @checkcmd("test")
    def test(self):
        return os.system("echo hello")


if __name__ == "__main__":
    print("MSet")
    m = Mset()
    failed = m.pypi()
    if failed:
        print("ooops")
