/**
const str = ' \t\nhello world \t\n'
console.log(str.trim())
console.log(str.trimStart())
console.log(str.trimEnd())

def gen():
    yield 1
    yield 2
    yield 3


it = gen()

for item in it:
    print(item)


function *gen(){
    yield 1
    yield 2
    yield 3
}
it =gen()
console.log(it.next().value)
console.log(it.next().value)
console.log(it.next().value)
console.log(it.next())

let obj = {
    a: 1,
    b: 2,
    c: 3
}
console.log("a" in obj)
console.log(Object.keys(obj))//[ 'a', 'b', 'c' ]
console.log(Object.values(obj))//[ 1, 2, 3 ]
console.log(Object.entries(obj))//[ [ 'a', 1 ], [ 'b', 2 ], [ 'c', 3 ] ]


class MyClass {
    // 类的初始化方法，接收一个数据列表
    constructor( data) {
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


const is_admin = true
const is_active = false
console.log(is_admin && is_active)// and
console.log(is_admin || is_active)// or

const original_value = true
const double_negation = !!original_value
console.log(original_value , double_negation)



class Parent{
    __contains__(item){
        console.log("Parent __contains__")
        return true
    }
}

class Child extends Parent{}
    
const child = new Child()
child.__contains__()

a=2
console.log(1<a && a<3)
console.log(1<a<3)


console.log(!!null)  // 输出: False
console.log(!!undefined)  // 输出: False
console.log(!!false)  // 输出: False
console.log(!!0)  // False
console.log(!!0.0) // 输出: False
console.log(!!'')  // 输出: False

console.log(!![])  // 输出: true
console.log(!!{})  // 输出: true
console.log(!!(new Set()))  // 输出: true

console.log(parseInt(true))
let arr = []
console.log(arr&& arr.length===0)



let a = 5
console.log(1<a<3)//true
console.log(true<0.9)
console.log(true<1.1)
console.log(true==1)
console.log(1<a && a<3)//false

let obj = {}
console.log(Object.keys(obj).length)


const result_and = false && (1 / 0)
console.log(result_and)
const result_or = false || (1 / 0)
console.log(result_or)
Code Runner

//这跟js不一样啊，js返回的不是具体值，就是true或者false
//或返回第一个真值 或返首真  全假返回最后一个假
const res = 'a' || 'b'||'c'
console.log(res)
//与返回第一个假值 与返首假  全真返回最后一个真
const res2 = 'a' && 'b'&&'c'&& 0&&'d'
console.log(res2)

const res3 = 'a' && 'b'&&'c'&&'d'
console.log(res3)
const res4 = 0 || ''||[]
console.log(res4)

console.log(1>"1")

let x = 5
x += 5
console.log(x)

let arr  = [1, 2, 3]
arr += [4, 5]
console.log(arr)
arr *= 2
console.log(arr)

let a = 10
let b = 3
console.log(Math.floor(a/b))
console.log(a%b)
console.log(a**b)

console.log(7+56+64*3)
console.log(15+15*16)



console.log(parseInt("11111111",2))
console.log(parseInt("377",8))
console.log(parseInt("FF",16))

const x = -1;
const result = x > 0 ? "正数" : x == 0 ? "零" : "非零";
console.log(result)

const day = 'day1'
switch (day) {
    case 'day1':
        console.log('星期一')
        break;
    case 'day2':
        console.log('星期二')
        break;
    default:
        console.log('未知')
}
const a=5
const b=3
//2个|表示逻辑运算符的或,也就是python的or
console.log(a||b)
//在js中，一个|对应的也是位运行中的或
console.log(a|b)


let numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log(numbers.slice(2,8));


//是pop和push吧
const arr =[1,2,3,4,5]
const item1 = arr.pop()
arr.unshift(item1)
const item2 = arr.pop()
arr.unshift(item2)
const item3 = arr.pop()
arr.unshift(item3)
console.log(arr)

const l1 = [1, 2]
const l2 = [3, 4]
//const l3 = l1 + l2
const l3 = l1.toString()+l2.toString()
console.log(l3)

const arr6 = ['a','b','c']
console.log(arr6[2])
console.log(arr6.at(1))
console.log(arr6.at(-1))
console.log(arr6[arr6.length-1])

// I 忽略 大小写 M 多行匹配 Gg 全局匹配
const str = `a A a
a A a
`
const regexp = /a/gim
while ((match=regexp.exec(str))!==null){
    console.log(match[0])
}




 function replace_color(match){
    console.log(match)
    return color_map[match]||match
}
const pattern_colors = new RegExp(
    Object.keys(color_map)
    .map(key=>key.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'))
    .join('|'),'g'
) 
//const new_text_colors = text_colors.replace(pattern_colors,replace_color)
//console.log(new_text_colors)
const text_colors = "这些颜色有 red、blue 和 green。"

const color_map = {"red": "red2", "blue": "blue2", "green": "green2"}

const new_text_colors  = text_colors.replace(
    new RegExp(
    Object.keys(color_map)
    .map(key=>key.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'))
    .join('|'),'g'),match=>color_map[match]||match
)
console.log(new_text_colors)
console.log(RegExp.escape)

const text_colors = "这些颜色有 red、blue 和 green。"

const color_map = {"red": "red2", "blue": "blue2", "green": "green2"}

const new_text_colors  = text_colors.replace(
    new RegExp(
    Object.keys(color_map)
    .map(RegExp.escape)
    .join('|'),'g'),match=>color_map[match]||match
)
console.log(new_text_colors)


let my_list = [1, 2, 3]
my_list.push(4)
my_list.push("hello")
my_list.push([5, 6])
console.log(my_list)

//array.splice(start,deleteCount,item1,item2)
const array = ['a','b','c','d']
array.splice(2,2,'e','f')
console.log(array)


const my_list = [1, 2, 3]
const new_list = [4,5,6]
//my_list.push(...new_list)
const result = my_list.concat(new_list)
console.log(my_list)
console.log(result)


const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log(numbers.slice(3,8).filter(x=> x % 2 == 0))



const words = ['hello', 'world', 'python', 'programming']
console.log(words.map(x=>x.slice(2)))



const list = [1, 2, 3]
//const list2 = [item*2 for item in list if item > 1]
console.log(list.filter(item=>item>1).map(item=>item*2))
*/


//let my_list_original = [1, 2, 3, 4, 2, 5]
//const index = my_list_original.indexOf(2)
//my_list_original.splice(index,1)
//console.log(my_list_original)

//del my_list_del[2]
//my_list_original.splice(2,1)
//del my_list_del[2:4]
//my_list_original.splice(2,2)
//console.log(my_list_original)
//var my_list_original = [1, 2, 3, 4, 2, 5]
//delete my_list_original;
//console.log(my_list_original)

let my_list_original = [1, 2, 3, 4, 2, 5]
const index = my_list_original.findIndex(item=>item==2)
console.log(index)
