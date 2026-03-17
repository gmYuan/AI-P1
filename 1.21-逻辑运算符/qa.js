

// ----------------------------------------------------------------------------
// 1.21-1.1～1.3 逻辑与 + 逻辑或 + 逻辑取反
const is_admin = true
const is_active = false
console.log(is_admin && is_active)// and
console.log(is_admin || is_active)// or

const original_value = true
const double_negation = !!original_value
console.log(original_value , double_negation)



// ----------------------------------------------------------------------------
// 1.21-2.1 成员运算符是否会 继承查找

class Parent{
    __contains__(item){
        console.log("Parent __contains__")
        return true
    }
}

class Child extends Parent{}

const child = new Child()
child.__contains__()        // 打印出 Parent __contains__



//---------------------------------------------------------------------------
// 1.21-3.1 常见真假值测试

console.log(!!null)  // 输出: False
console.log(!!undefined)  // 输出: False
console.log(!!false)  // 输出: False
console.log(!!0)  // False
console.log(!!0.0) // 输出: False
console.log(!!'')  // 输出: False

// 和 py 不一样的 真假值类型
console.log(!![])  // 输出: true
console.log(!!{})  // 输出: true
console.log(!!(new Set()))  // 输出: true



//---------------------------------------------------------------------------
//1.21-3.2 连续比较 + 判断空对象

let b =2
console.log(1< b && a<3)   // true
console.log(1< b <3)       // true

// 在 js 里这 2 种写法是不等价的，但是在 py 里是等价的 🌟🌟
let a = 5
console.log(1<a<3)         // true，见下相当于转化为 true(即 1)
console.log(1<a && a<3)    // false

console.log(true<0.9)      // false
console.log(true<1.1)
console.log(true==1)       // true

console.log(parseInt(true))   // 转化的结果是 NaN，而 py 里是 1  🌟🌟

let arr = []
console.log(arr&& arr.length===0)

let obj = {}
console.log(Object.keys(obj).length)



//---------------------------------------------------------------------------
// 1.21-5.1 短路计算

const result_and = false && (1 / 0)
console.log(result_and)
const result_or = false || (1 / 0)
console.log(result_or)



//---------------------------------------------------------------------------
// 1.21-6.1 逻辑运算符的返回值

//Q: 这跟js不一样啊，js返回的不是具体值，就是true或者false

//A: 和 py是一样的： 或返首真；与返首假

//或返回第一个真值(或返首真); 全假返回最后一个假
const res = 'a' || 'b'||'c'
console.log(res)

//与返回第一个假值(与返首假); 全真返回最后一个真
const res2 = 'a' && 'b'&&'c'&& 0&&'d'
console.log(res2)

const res3 = 'a' && 'b'&&'c'&&'d'
console.log(res3)

const res4 = 0 || ''||[]
console.log(res4)