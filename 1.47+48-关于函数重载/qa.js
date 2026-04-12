

//-------------------------------------------------------------------------------

function add_item(item, target_list=[]){
    target_list.push(item)
    return target_list
}

list1 = add_item("apple")
console.log(list1)
list2 = add_item("banana")
console.log(list2)




/**



function calculate_sum(...args){

}

 

function decorator(){

}
//@decorator()
class Person{

}


function wrapper() {
}

function register() {
    console.log("register")
}
wrapper.register = register
wrapper.register()
// py 实现单例是不是 也有静态属性



function compose(...funcs) {
    function composed(...args) {
        let result = funcs[funcs.length - 1](...args)
        for (let i = funcs.length - 2; i >= 0; i--) {
            result = funcs[i](result)
        }
        return result
    }
    return composed
}

function add_one(x) {
    return x + 1
}


function multiply_by_two(x) {
    return x * 2
}


function square(x) {
    return x ** 2
}


const composed_func = compose(square, multiply_by_two, add_one)
const result = composed_func(3)
console.log(result)
*/
//弱引用就是不阻止垃圾回收的引用，如果一个对象只有弱引用指向它，那么垃圾回收器可以回收这个对象
let obj = {
    data:'important'
}

let obj1 = {id:1}//引用计数1
let obj2 = {id:2}//引用计数为1

let set = new Set()
set.add(obj1)//obj1引用计数变成2
set.add(obj2)//obj2引用计数变成2
console.log(set.has(obj1))//True
obj1 = null//obj1引用计数变成1
obj2 = null//obj2引用计数变成1



let weakSet = new WeakSet()
weakSet.add(obj1)//obj1引用计数变成1
weakSet.add(obj2)//obj2引用计数变成1
console.log(weakSet.has(obj1))
obj1 = null//obj1引用计数变成0
obj2 = null//obj2引用计数变成0


