import os
import subprocess
from time import sleep, time

# Popen 생성자가 프로세스를 시작한다.
proc = subprocess.Popen(
    ['echo', 'Hello from the child'],
    stdout=subprocess.PIPE)

# communicate 메서드는 자식 프로세스의 출력을 읽어오고 자식 프로세스가 종료할 때까지 대기한다.
out, err = proc.communicate()
print(out.decode('utf-8'))

proc = subprocess.Popen(['sleep', '0.3'])
while proc.poll() is None:
    print('working')
    # 시간이 걸리는 작업 몇 개를 수행함
    sleep(0.2)

print('Exit status', proc.poll())


def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc


start = time()
procs = []
for _ in range(10):
    proc = run_sleep(0.1)
    procs.append(proc)

for proc in procs:
    proc.communicate()
end = time()
print('finished in %.3f seconds' % (end - start))


def run_openssl(data):
    env = os.environ.copy()
    env['password'] = '\xe24U\n\xd0Ql3S\x11'
    print(env)
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
    proc.stdin.write(data)
    proc.stdin.flush()  # 자식 프로세스가 입력을 반드시 받게 함
    return proc


procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    procs.append(proc)

for proc in procs:
    out, err = proc.communicate()
    print(out[-10:])


def run_md5(input_stdin):
    proc = subprocess.Popen(
        ['md5'],
        stdin=input_stdin,
        stdout=subprocess.PIPE)
    return proc


input_procs = []
hash_procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    input_procs.append(proc)
    hash_proc = run_md5(proc.stdout)
    hash_procs.append(hash_proc)

for proc in input_procs:
    proc.communicate()

for proc in hash_procs:
    out.err = proc.communicate(timeout=0.1)
    print(out.strip())

