from subprocess import Popen, PIPE


def switch():
    x = int(input("Выберите номер проблемы: "))
    s = "python \"./Problems/Problem %d.py\"" % x
    proc = Popen(
        s,
        shell=True,
        stdout=PIPE
    )
    proc.wait()
    res = proc.communicate()[0]
    print(res.decode('utf-8'), end='')


if __name__ == "__main__":
    switch()
