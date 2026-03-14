

// ----------------------------------------------------------------------------
// 1.20-1.2  in 在字典里的使用

let obj = {
    a: 1,
    b: 2,
    c: 3
}
console.log("a" in obj)

console.log(Object.keys(obj))//[ 'a', 'b', 'c' ]
console.log(Object.values(obj))//[ 1, 2, 3 ]
console.log(Object.entries(obj))//[ [ 'a', 1 ], [ 'b', 2 ], [ 'c', 3 ] ]



// ----------------------------------------------------------------------------
// 1.20-3.2  in + not in 在自定义对象 里的使用

class MyClass {
    // 类的初始化方法，接收一个数据列表
    constructor(data) {
        // 将传入的数据存储为实例属性
        this.data = data
    }

    // 定义 __contains__ 方法，使其支持 in 和 not in 运算符
    __contains__(item) {
        // 检查 item 是否存在于实例的 data 属性中
        return item in this.data
    }
    // 定义字符串表示方法
    __repr__() {
        return `MyClass(${this.data})`
    }
}

obj = new MyClass([1, 2, 3])
console.log("2" in obj)
console.log(obj.__contains__(2))
console.log(!obj.__contains__(2))