

/**
// ---------------------------------------------------------------------------
// 1.7-3.1 变量交换

let a = 10;
let b = 20;
console.log(a,b);
//a, b = b, a;
[a,b]=[b,a];
console.log(a,b);

*/









/**
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