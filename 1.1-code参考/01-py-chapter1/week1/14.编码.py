# 测试数据：用于字符编码分析的字符串列表
test_texts = ["Hello World", "Hello 世界 🌍", "Python编程😊🎉"]


def analyze_text_encoding(text0):
    if not isinstance(text, str):  # p instanceof Person
        raise TypeError("输入的必须是字符串")
    # 字符总数
    total_chars = len(text)
    ascii_chars = 0
    unicode_chars = 0
    character_details = []
    for char in text:
        # 获取字符对应的unicode码点 就是此字符在unicode中的编号
        char_unicode = ord(char)
        char_utf8_bytes = char.encode("utf-8")
        # 获取此字符对应的字节数
        char_utf8_bytes_len = len(char_utf8_bytes)
        # 判断此字符的码点是否小于128
        if char_unicode < 128:
            ascii_chars += 1
        else:
            unicode_chars += 1
        character_details.append(
            {
                "char": char,
                "unicode": f"U+{char_unicode:04X}",
                "char_utf8_bytes": char_utf8_bytes_len,
                "is_ascii": char_unicode < 128,
            }
        )
    utf8_bytes = len(text.encode("utf-8"))
    # 返回分析结果字典
    return {
        "total_chars": total_chars,
        "ascii_chars": ascii_chars,
        "unicode_chars": unicode_chars,
        "utf8_bytes": utf8_bytes,
        "character_details": character_details,
    }


"""
# 遍历测试文本并展示分析结果
for text in test_texts:
    # 分析当前文本
    result = analyze_text_encoding(text)
    # 打印当前文本内容
    print(f'\n文本: "{text}"')
    # 打印文本总字符数
    print(f"总字符数: {result['total_chars']}")
    # 打印ASCII字符数目
    print(f"ASCII字符数: {result['ascii_chars']}")
    # 打印非ASCII的Unicode字符数目
    print(f"Unicode字符数: {result['unicode_chars']}")
    # 打印UTF-8编码字节数
    print(f"UTF-8字节数: {result['utf8_bytes']}")

    # 显示前3个字符的详细编码信息
    print("字符详情 (前3个):")
    for detail in result["character_details"][:3]:
        # 打印每个字符的详细编码信息
        print(f"  {detail}")



def convert_encoding(text, target_encoding="utf-8"):
    if not isinstance(text, str):  # p instanceof Person
        raise TypeError("输入的必须是字符串")
    try:
        return text.encode(target_encoding)
    except UnicodeEncodeError:
        if target_encoding.lower() == "ascii":
            # 使用errors="replace"表示把不能转换的编码的字符替换为?
            ascii_text = text.encode("ascii", errors="replace")
            return ascii_text
        else:
            try:
                return text.encode(target_encoding, errors="replace")
            except (LookupError, UnicodeEncodeError):
                utf8_bytes = text.encode("utf-8", errors="replace")
                return utf8_bytes
"""


def detect_and_fix_encoding(data_bytes, possible_encodings=["utf-8", "gbk", "ascii"]):
    if not isinstance(data_bytes, bytes):
        raise TypeError("输入必须是字节类型")
    best_result = {
        "detected_encoding": None,
        "decoded_text": "",
        "success": False,
        "error_info": "",
    }
    for encoding in possible_encodings:
        try:
            # 用当前的编码尝试解码
            decoded_text = data_bytes.decode(encoding)
            error_chars = decoded_text.count("?")
            error_ratio = error_chars / len(decoded_text) if decoded_text else 1
            # 如果问号的出现的比率小于30%,认为解码成功
            if error_ratio < 0.3:
                best_result = {
                    "detected_encoding": encoding,
                    "decoded_text": decoded_text,
                    "success": True,
                    "error_info": "",
                }
                break

        except (UnicodeDecodeError, LookupError) as e:
            continue
    # 如果所有的正常解码都失败了，则尝试采用errors='replace'来进行替换
    if not best_result["success"]:
        for encoding in possible_encodings:
            try:
                decoded_text = data_bytes.decode(encoding, errors="replace")
                best_result = {
                    "detected_encoding": encoding,
                    "decoded_text": decoded_text,
                    "success": False,
                    "error_info": f"使用{encoding}解码从早到晚 包含替换字符",
                }
                break
            except LookupError:
                continue
    return best_result


# 定义乱码检测测试用例列表，包含要转换的文本和采用的编码
test_cases = [("Hello 世界", "utf-8"), ("Python编程", "utf-8")]

# 遍历每个测试用例进行编码检测和修复
for text, encoding in test_cases:
    # 将文本用指定编码转为字节数据
    encoded_bytes = text.encode(encoding)
    # 自动检测并修复编码
    result = detect_and_fix_encoding(encoded_bytes)

    # 打印原始文本及其编码类型
    print(f'\n原始文本: "{text}" (使用{encoding}编码)')
    # 打印检测到的编码类型
    print(f"检测到编码: {result['detected_encoding']}")
    # 打印是否解码成功
    print(f"解码成功: {result['success']}")
    # 打印实际解码得到的文本
    print(f"解码结果: {result['decoded_text']}")
    # 如果有错误信息则打印
    if result["error_info"]:
        print(f"错误信息: {result['error_info']}")
