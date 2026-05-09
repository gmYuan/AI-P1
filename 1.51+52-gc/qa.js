

//-------------------------------------------------------------------------------

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


