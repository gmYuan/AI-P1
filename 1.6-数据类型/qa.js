
/**
 * desc
 * args
 * return

const Variable = 1
const variable = 2
console.log(Variable)
console.log(variable)

class Person{
    //也类似于一个魔术方法，你只要写好了，运行的时候会默认调用
    constructor(){
        console.log("Person")
    }
}
const p1 = new Person()

*/




/**------------------------------------------------
// 1.6-3  属性存在判断
const p = {"a": 1, "b": 2}
 if p.a  else


/**------------------------------------------------
// 1.6-6 展开运算符/ 解包

let obj1 = {a:1}
let obj2 = {b:2}
let obj3 = {
    ...obj1,
    ...obj2
}
console.log(obj3)

let arr1 = [1,2]
let arr2 = [3,4]

// 展开运算符
let arr3 = [...arr1,...arr2]
console.log(arr3)

*/



/**------------------------------------------------------------------------
// 1.6-7 列表生成式

let arr4 = [1,2,3]
let arr5 = [...arr4.map(item=>item*item)]
console.log(arr5)
console.log(arr5.join(', '));

*/



/**------------------------------------------------------------------------
// 1.6-10 变量的 后备值

// 能不能像js那样 grade_counts||100
let grade_counts = 10
let grade = grade_counts  || 100
console.log(grade)
*/



/**------------------------------------------------------------------------
// 1.6-9 grade_counts.items + join使用
//1.6-9.2 类似于 JS 的 map效果

// print(", ".join([f"{grade}:{count}人" for grade, count in grade_counts.items()]))

let arr8 = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
let result = arr8.map(item=>item.a+item.b)
console.log(result)

// 箭头函数 VS lambda匿名函数
// item=>item.a+item.b    lambda x: x["b"]
*/
