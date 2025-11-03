def format_file_size(size_bytes):
    if size_bytes < 0:
        raise ValueError("文件大小不能为负数")
    units = ["B", "KiB", "Mib", "GiB", "Tib"]
    size = float(size_bytes)
    unit_index = 0
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024.0
        unit_index += 1
    return f"{size:.2f} {units[unit_index]}"


size_tests = [500, 1536, 1048576, 3221225472]
# 遍历文件大小测试用例，格式化并输出结果
for size in size_tests:
    result = format_file_size(size)
    print(f"{size:,} 字节 -> {result}")


def calculate_download_time(file_size_mb, bandwidth_mbps):
    """
    计算特定带宽下下载所需的时间
    参数:
        file_size_mb:文件大小MB  B=bytes字节
        bandwidth_mbps:网络带宽Mbps  b=bit 位     1B=8b 1字节=8位
    返回:
        下载时间字符串
    """
    if file_size_mb <= 0 or bandwidth_mbps <= 0:
        raise ValueError("文件大小和带宽必须大于0")
    # 文件大小从M字节转为M比特Mb
    file_size_mb_bits = file_size_mb * 8
    time_seconds = file_size_mb_bits / bandwidth_mbps
    if time_seconds < 60:
        return f"{time_seconds:.1f}秒"
    elif time_seconds < 3600:
        time_seconds = time_seconds / 60
        return f"{time_seconds:.1f}分钟"
    else:
        time_seconds = time_seconds / 3600
        return f"{time_seconds:.1f}小时"


# 下载时间计算测试用例
download_tests = [
    (100, 50, "16.0 秒"),
    (2048, 100, "2.7 分钟"),
    (10240, 10, "2.3 小时"),
]

# 遍历下载时间测试用例，调用计算函数并输出结果
for file_size, bandwidth, expected in download_tests:
    result = calculate_download_time(file_size, bandwidth)
    print(f"{file_size} MB, {bandwidth} Mbps -> {result} [期望: {expected}]")
