from pprint import pprint


def process_student_data(student_info):
    try:
        # 1.验证完整性
        required_fields = ["name", "age", "score", "is_passed"]
        for field in required_fields:
            if field not in student_info:
                return None
        # 2.去空格
        name = str(student_info["name"]).strip()
        if not name:
            return None

        age = int(student_info["age"])
        if not (1 <= age <= 120):
            return None

        score = float(student_info["score"])
        if not (0.0 <= score <= 100.0):
            return None
        is_passed_str = student_info["is_passed"].lower()
        if is_passed_str == "true":
            is_passed = True
        elif is_passed_str == "false":
            is_passed = False
        else:
            return None

        return {"name": name, "age": age, "score": score, "is_passed": is_passed}

    except Exception:
        return None


def calculate_and_format_grades(students):
    if not students:
        return None

    students_with_grades = []

    def get_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    for student in students:
        garde = get_grade(student["score"])
        students_with_grades.append({**student, "grade": garde})

    scores = [s["score"] for s in students_with_grades]
    # 平均分
    average_score = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)
    # 统计每个等级的人数
    grade_counts = {}
    for student in students_with_grades:
        grade = student["grade"]
        grade_counts[grade] = grade_counts.get(grade, 0) + 1
    result = "成绩报告"
    result += "=" * 42 + "\n"
    result += f"{'学生姓名':<10} {'分数':<8} {'等级':<4}\n"
    result += "=" * 42 + "\n"

    for student in students_with_grades:
        result += f"{student['name']:<10} {student['score']:<8} {student['grade']:<4}\n"

    result += "=" * 42 + "\n"
    result += f"平均分:{average_score}\n"
    result += f"最高分:{max_score}\n"
    result += f"最低分:{min_score}\n"

    grade_dist = ", ".join(
        [f"{grade}:{count}人" for grade, count in sorted(grade_counts.items())]
    )
    result += f"等级分布:{grade_dist}\n"
    return result


def analyze_student_performance(students, filter=None):
    if not students:
        return {
            "total_count": 0,
            "filtered_count": 0,
            "average_score": 0.0,
            "grade_distribution": {},
            "top_performers": [],
            "pass_rate": 0.0,
        }
    # 总人数
    total_count = len(students)
    # 对学生列表进行浅拷贝
    filtered_students = students.copy()

    def get_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    if filter:
        if "min_score" in filter:
            filtered_students = [
                s for s in filtered_students if s["score"] >= filter["min_score"]
            ]
        if "max_score" in filter:
            filtered_students = [
                s for s in filtered_students if s["score"] <= filter["max_score"]
            ]

        if "grade" in filter:
            target_grade = filter["grade"]
            filtered_students = [
                s for s in filtered_students if get_grade(s["score"]) == target_grade
            ]
        filtered_count = len(filtered_students)
        if filtered_students:
            average_score = (
                sum([s["score"] for s in filtered_students]) / filtered_count
            )
        else:
            average_score = 0
        sorted_students = sorted(
            filtered_students, key=lambda x: x["score"], reverse=True
        )
        top_performers = sorted_students[:3]
        passed_count = sum([1 for s in filtered_students if s["score"] >= 60])
        pass_rate = (passed_count / filtered_count * 100) if filtered_count > 0 else 0.0
    return {
        "total_count": total_count,
        "filtered_count": filtered_count,
        "average_score": average_score,
        "top_performers": [item["name"] for item in top_performers],
        "pass_rate": pass_rate,
    }


print("学生成绩管理系统")
# 定义测试用的学生数据列表
test_students = [
    {"name": " 张三 ", "age": "20", "score": "85.5", "is_passed": "true"},
    {"name": "李四", "age": "19", "score": "92.0", "is_passed": "true"},
    {"name": "王五", "age": "21", "score": "78.3", "is_passed": "false"},
    {"name": "赵六", "age": "22", "score": "65.7", "is_passed": "true"},
    {"name": "钱七", "age": "20", "score": "45.2", "is_passed": "false"},
]
# 1.数据类型转换
processed_students = []
for i, student in enumerate(test_students):
    processed = process_student_data(student)
    if processed:
        processed_students.append(processed)
    else:
        print(f"学生{i}无效")
pprint(processed_students)

# 2.成绩计算与格式化
if processed_students:
    grade_report = calculate_and_format_grades(processed_students)
    print(grade_report)

# 3.数据筛选与统计
# 筛选条件测试
test_filters = [{"min_score": 80, "max_score": 95}, {"grade": "A"}, {"min_score": 60}]
for i, filter_condition in enumerate(test_filters, 1):
    result = analyze_student_performance(processed_students, filter_condition)
    pprint(result)
