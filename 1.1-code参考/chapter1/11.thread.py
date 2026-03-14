import threading
import time

"""
def task(name):
    print(f"{name} 线程开始执行")
    time.sleep(1)
    print(f"{name} 线程执行完毕")


# 创建两个线程，分别指定不同的参数
t1 = threading.Thread(target=task, args=("线程1",))
t2 = threading.Thread(target=task, args=("线程2",))
# 启动线程
t1.start()
t2.start()
# 主线程等待子线程运行结束 Promise.all()
t1.join()
t2.join()
print("所有的线程都已经执行完毕")
class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"{self.name}线程开始执行")
        time.sleep(1)
        print(f"{self.name} 线程执行完毕")


thread1 = MyThread("自定义线程A")
thread2 = MyThread("自定义线程B")

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("所有的线程都已经执行完毕")


# 导入threading模块，用于多线程编程
import threading

# 导入multiprocessing模块，用于多进程编程
from multiprocessing import Process

# 导入time模块，用于时间控制
import time


# 定义一个CPU密集型任务函数，参数n为循环次数
def cpu_intensive_task(n):
    # 初始化结果变量result为0
    result = 0
    # 使用循环执行n次，每次将i的平方累加到result中
    for i in range(n):
        result += i * i
    # 返回最终结果
    return result


# 定义一个I/O密集型任务函数，参数duration表示等待的秒数
def io_bound_task(duration):
    # 打印I/O任务开始并告知持续的秒数
    print(f"开始I/O任务，持续{duration}秒")
    # 模拟I/O操作，阻塞duration秒
    time.sleep(duration)
    # I/O操作结束，打印完成信息
    print(f"I/O任务完成")


# 使用 if __name__ == '__main__': 保护主代码，避免在 Windows 上使用 multiprocessing 时出错
if __name__ == "__main__":
    # 打印关于CPU密集型任务多线程效果有限的信息
    print("1. CPU密集型任务 - 多线程效果有限:")

    # 记录CPU密集型任务多线程执行的开始时间
    start_time = time.time()

    # 创建一个空列表用于保存线程对象
    threads = []
    # 创建4个线程，每个线程执行cpu_intensive_task，参数为1000000
    for i in range(4):
        thread = threading.Thread(target=cpu_intensive_task, args=(10000000,))
        threads.append(thread)
        thread.start()  # 启动线程

    # 等待所有线程结束
    for thread in threads:
        thread.join()

    # 计算CPU密集型任务多线程执行的耗时
    cpu_thread_time = time.time() - start_time
    # 打印CPU密集型任务多线程执行的总时间
    print(f"CPU密集型多线程执行时间: {cpu_thread_time:.2f}秒")

    # 打印I/O密集型任务多线程效果显著信息
    print("\n2. I/O密集型任务 - 多线程效果明显:")

    # 记录I/O密集型任务多线程执行的开始时间
    start_time = time.time()

    # 创建存储I/O线程对象的空列表
    io_threads = []
    # 创建4个线程，每个线程执行io_bound_task，参数为2
    for i in range(4):
        thread = threading.Thread(target=io_bound_task, args=(2,))
        io_threads.append(thread)
        thread.start()  # 启动线程

    # 等待所有I/O线程完成
    for thread in io_threads:
        thread.join()

    # 计算I/O密集型任务多线程执行的耗时
    io_thread_time = time.time() - start_time
    # 打印I/O密集型任务多线程用时
    print(f"I/O密集型多线程执行时间: {io_thread_time:.2f}秒")

    # 打印单线程执行I/O密集型任务的对比信息
    print("\n3. 对比单线程执行时间:")

    # 记录单线程执行I/O密集型任务的开始时间
    start_time = time.time()
    # 用单线程依次执行4次I/O密集型任务，每次2秒
    for i in range(4):
        io_bound_task(2)
    # 计算单线程共耗时
    single_thread_time = time.time() - start_time
    # 打印单线程执行总时间
    print(f"   单线程执行时间: {single_thread_time:.2f}秒")
    # 打印多线程与单线程耗时比值，得到加速比
    print(f"   多线程加速比: {single_thread_time / io_thread_time:.2f}倍")

    # 打印多进程CPU密集型任务执行提示
    print("\n4. 多进程CPU密集型任务:")

    # 记录多进程任务开始时间
    start_time = time.time()

    # 创建用于存储进程对象的空列表
    processes = []
    # 创建4个进程，每个进程执行cpu_intensive_task，参数为1000000
    for i in range(4):
        process = Process(target=cpu_intensive_task, args=(10000000,))
        processes.append(process)
        process.start()  # 启动进程

    # 等待所有子进程结束
    for process in processes:
        process.join()

    # 计算多进程CPU密集型任务执行总时间
    multiprocessing_time = time.time() - start_time
    # 打印多进程CPU密集型任务的耗时
    print(f"CPU密集型任务多进程执行时间: {multiprocessing_time:.2f}秒")

    # 打印性能对比提示
    print(f"\n5. 性能对比:")
    # 打印多进程比多线程的加速比
    print(f"   多进程比多线程快: {cpu_thread_time / multiprocessing_time:.2f}倍")

import threading
import time

shared_count = 0
lock = threading.Lock()


def increment_counter():
    global shared_count
    for _ in range(5):
        with lock:
            current_value = shared_count
            time.sleep(0.1)
            shared_count = current_value + 1
            print(f"线程{threading.current_thread().name}:计数器={shared_count}")


threads = []
for i in range(3):
    thread = threading.Thread(target=increment_counter, name=f"Thread-{i+1}")
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print(f"最终计数器的结果:{shared_count}")


from multiprocessing import Process
import os
import time


def cpu_bound_task(name):
    print(f"进程{name}：进程 ID{os.getpid()} 开始执行CPU密集型任务")
    start_time = time.time()
    count = 0
    for i in range(10**6):
        count += i * i
    end_time = time.time()
    print(f"进程{name}CPU任务完成，最终计数为{count},耗时{end_time-start_time:.2f}秒")


if __name__ == "__main__":
    print(f"主进程开始")
    process1 = Process(target=cpu_bound_task, args=("Process-1",))
    process2 = Process(target=cpu_bound_task, args=("Process-2",))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    print(f"所有的进程全部执行完毕")

from multiprocessing import Process, Queue
import time


def producer(queue, name):
    for i in range(5):
        message = f"消息{i}来自{name}"
        queue.put(message)
        print(f"生产者{name}, 发送{message}")
        time.sleep(0.5)


def consumer(queue, name):
    while True:
        try:
            # 从队列中获取 消息，超时时间为3秒
            message = queue.get(timeout=3)
            print(f"消费者{name}:接收{message}")
            time.sleep(0.3)
        except:
            print(f"消费者{name}超时，退出")
            break


if __name__ == "__main__":
    print(f"主进程开始")
    # 创建用于进程间通信的队列
    comm_queue = Queue()
    producer_process = Process(
        target=producer,
        args=(comm_queue, "producer"),
    )
    consumer_process = Process(
        target=consumer,
        args=(comm_queue, "consumer"),
    )
    consumer_process.start()
    producer_process.start()
    consumer_process.join()
    producer_process.join()
    print(f"所有的进程全部执行完毕")

from concurrent.futures import ThreadPoolExecutor
import time
import threading


def worker_task(task_id, duration):
    print(f"任务{task_id}开始执行(线程:{threading.current_thread().name})")
    time.sleep(duration)
    result = f"任务{task_id}完成"
    print(f"任务{task_id}执行完成 线程 {threading.current_thread().name}")
    return result


with ThreadPoolExecutor(max_workers=3) as executor:
    print(f"1.线程池初始化完成，创建了3个工作线程")
    futures = []
    for i in range(5):
        # 向线程池提交一个新的任务，任务ID为i+1,,持续时间为2秒
        future = executor.submit(worker_task, i + 1, 2)
        futures.append(future)
        print(f"任务{i+1}已经提交到线程池")
    results = []
    for i, future in enumerate(futures, 1):
        # 调用result方法等待任务完成并获取返回值
        result = future.result()
        results.append(result)
        print(f"4.任务{i}结果 ：{result}")
print(f"线程池关闭，所有的线程被回收")


# 定义一个用于下载文件的函数
from concurrent.futures import ThreadPoolExecutor
import time
import requests


def download_file(url, filename):
    # 尝试执行以下操作进行容错
    try:
        # 输出开始下载的提示信息
        print(f"开始下载: {filename}")
        # 发送HTTP GET请求，5秒超时
        response = requests.get(url, timeout=5)
        # 以写二进制的方式打开文件
        with open(filename, "wb") as f:
            # 将下载的内容写入文件
            f.write(response.content)
        # 输出下载完成的提示信息
        print(f"下载完成: {filename}")
        # 返回True表示下载成功
        return True
    # 捕获所有异常
    except Exception as e:
        # 输出下载失败及错误信息
        print(f"下载失败: {filename}, 错误: {e}")
        # 返回False表示下载失败
        return False


# 输出I/O密集型任务 - 网络请求的标题
print("1. I/O密集型任务 - 网络请求:")

# 定义下载任务的列表（每个任务是(url, 文件名)元组）
download_tasks = [
    ("https://httpbin.org/delay/1", "file1.txt"),
    ("https://httpbin.org/delay/1", "file2.txt"),
    ("https://httpbin.org/delay/1", "file3.txt"),
    ("https://httpbin.org/delay/1", "file4.txt"),
    ("https://httpbin.org/delay/1", "file5.txt"),
]

# 获取当前时间，作为下载起始时间
start_time = time.time()

# 创建一个最大线程数为3的线程池，启动下载任务
with ThreadPoolExecutor(max_workers=3) as executor:
    # 利用线程池提交所有下载任务，返回Future对象列表
    futures = [
        executor.submit(download_file, url, filename)
        for url, filename in download_tasks
    ]
    # 等待所有线程任务完成，并收集结果
    results = [future.result() for future in futures]

# 计算并输出所有下载完成所用的时间
download_time = time.time() - start_time
print(f"   下载任务完成，耗时: {download_time:.2f}秒")


from concurrent.futures import ThreadPoolExecutor
import time
import os

# 输出I/O密集型任务 - 文件操作的标题
print("\n2. I/O密集型任务 - 文件操作:")


# 定义一个用于读取文件的函数
def read_file(filename):
    # 尝试执行以下操作进行容错
    try:
        # 输出开始读取文件的提示信息
        print(f"开始读取文件: {filename}")
        # 以只读和utf-8编码方式打开文件
        with open(filename, "r", encoding="utf-8") as f:
            # 读取文件内容
            content = f.read()
        # 输出文件读取完成的提示信息
        print(f"文件读取完成: {filename}")
        # 返回读取内容的长度
        return len(content)
    # 捕获所有异常
    except Exception as e:
        # 输出文件读取失败及错误信息
        print(f"文件读取失败: {filename}, 错误: {e}")
        # 返回0表示读取失败
        return 0


# 创建一个用于存储测试文件名的列表
test_files = []
# 创建3个测试文件，每个文件中写入100行内容
for i in range(3):
    # 定义测试文件名
    filename = f"test_file_{i+1}.txt"
    # 以写模式和utf-8编码打开文件
    with open(filename, "w", encoding="utf-8") as f:
        # 向文件写入100行内容
        f.write(f"这是测试文件 {i+1} 的内容\n" * 100)
    # 将文件名加入测试文件列表
    test_files.append(filename)

# 获取当前时间，作为文件读取起始时间
start_time = time.time()

# 创建一个最大线程数为2的线程池，启动读取任务
with ThreadPoolExecutor(max_workers=2) as executor:
    # 利用线程池提交所有文件读取任务，返回Future对象列表
    futures = [executor.submit(read_file, filename) for filename in test_files]
    # 等待所有线程任务完成，并收集结果
    results = [future.result() for future in futures]

# 计算并输出所有文件读取完成所用的时间
file_read_time = time.time() - start_time
print(f"   文件读取任务完成，耗时: {file_read_time:.2f}秒")

# 输出控制并发数量的说明性内容
print("\n3. 控制并发数量:")
print("   - 线程池可以限制同时执行的线程数量")
print("   - 避免创建过多线程导致系统资源耗尽")
print("   - 在服务器环境中特别有用")

# 清理刚刚创建的测试文件
for filename in test_files:
    # 尝试删除文件
    try:
        os.remove(filename)
    # 如果发生异常则忽略
    except:
        pass
"""
