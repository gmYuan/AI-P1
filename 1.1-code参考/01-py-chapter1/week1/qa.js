
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

const p = {"a": 1, "b": 2}
//if p.a  else 

let obj1 = {a:1}
let obj2 = {b:2}
let obj3 = {
    ...obj1,
    ...obj2
}
console.log(obj3)


let arr1 = [1,2]
let arr2 = [3,4]
//展开
let arr3 = [...arr1,...arr2]
console.log(arr3)


let arr4 = [1,2,3]
let arr5 = [...arr4.map(item=>item*item)]
console.log(arr5)

console.log(arr5.join(', '));


//能不能像js那样 grade_counts||100
let grade_counts = 10
let grade = grade_counts||100
console.log(grade)

//print(", ".join([f"{grade}:{count}人" for grade, count in grade_counts.items()]))l
let arr8 = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
let result = arr8.map(item=>item.a+item.b)
// item=>item.a+item.b  lambda x: x["b"]
console.log(result)

let a = 10;
let b = 20;
console.log(a,b);
//a, b = b, a;
[a,b]=[b,a];
console.log(a,b);


const arr1 = []
const arr2 = new Array()

const obj1 = {}
const obj2 = new Object()

const my_list = [1, 2, 2, 3, 3, 4]
const unique_set = new Set(my_list)
unique_set.add(5)
console.log(unique_set.size)
console.log("a".repeat(10));


class Person{

}
p = new Person()
console.log(p instanceof Person)
//  == ===
//# == is 

class Student{
    toString(){
        return "stu"
    }
}
const s = new Student()
console.log(s)
console.log(s+"$");
console.log(String(s));
console.log(s.toString());

const book = {
    name:'red',
    toString(){
        return "bookred"
    }
}

console.log(book);
console.log(book+"$");
console.log(String(book));
console.log(book.toString());
 


const str = "a,b,c"
const arr = str.split(',')
console.log(arr)
const str2 = arr.join(',')
console.log(str2)
*/
const arr = [1,2,3]
console.log("a,b,c".split(',').join(','))