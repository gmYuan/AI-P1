/**
function add(a,b){
    return [a,b,a+b]
}
console.log(add(1,2))

const result = '3' + 4


class Person{

}
class Dog{

}
const p = new Person()
console.log(p instanceof Person || p instanceof Dog)
console.log(add instanceof Function)



function * simpleGenerator(){
    yield "1"
    yield "2"
    yield "3"
    return "完成"
}
const gen = simpleGenerator()
console.log(gen.next())
console.log(gen.next())
console.log(gen.next())
console.log(gen.next())

 */

function delay(ms, value) {
    return new Promise(resolve => setTimeout(() => resolve(value), ms))
}

async function* asyncGenerator() {
    yield await delay(1000, '第1个异步值')
    yield await delay(2000, '第2个异步值')
    yield await delay(3000, '第3个异步值')
    return '完成'
}
/**
async function processAsyncGenerator(){
    for await (const value of asyncGenerator()){
        console.log(`收到${value}`)
    }
}
processAsyncGenerator()

async function processAsyncGenerator(){
     const asyncGen = asyncGenerator()
     let result = await asyncGen.next()
     while(!result.done){
        console.log(`${result.value}`)
        result = await asyncGen.next()
     }
     console.log(`${result.value}`)

}
processAsyncGenerator()

function * errorHandlerGenerator(){
    try{
        yield '1'
        throw new Error('模拟错误')
        yield '2'
    }catch(error){
        yield "捕获错误"
    }
}
const erorGen = errorHandlerGenerator()
console.log(erorGen.next())
console.log(erorGen.next())

//不是把正常'赋值给result
function * throwIntoGenerator(){
     try{
       const result = yield '正常'
       return "结果"+result
    }catch(error){
        yield "捕获错误"
    }
}
const throwGen = throwIntoGenerator()
console.log(throwGen.next())
//console.log(throwGen.throw(new Error('从外部抛出异常')))
//console.log(throwGen.return())
console.log(throwGen.next('张三'))
console.log(throwGen.next())




class Person{

}

const p = new Person()
p.age = 30
p.home='bj'
console.log(p)
console.log(Object.getPrototypeOf(p).constructor)
const type = Object.getPrototypeOf(p).constructor
//result = cls.__new__(cls)
const newP = new type()

for (const key in p){
    newP[key]=p[key]
}
console.log(newP)
// class -> cls
//1 去掉元音字母 重复字母保留一个

//在jS经常会看到这样的定法
//创建一个完全 空白的对象
const pureObject = Object.create(null)


//obj.__class__
console.log(Object.getPrototypeOf(p).constructor)


//(lambda x: x > 5)(num)

const result = (function(x){
    return x>5
})(1)
console.log(result)


let str = '1+2+3'
let result = eval(str)
console.log(result)

//const keyValueParies = ["a", 1, "b", 2, "c", 3]
const keyValueParies =[
    ["name","张三"],
    ["age",25],
    ["city","北京"]
]
 properties.reduce((accumulator,currentValue,currentIndex,array)=>{
    return accumulator
},initialValue) 
const obj = keyValueParies.reduce((acc,[key,value])=>{
    acc[key]=value
    return acc
},{})
console.log(obj)

const list = [0,2,4]
//js中的some对应python中的any
function mySome(array,predicate){
    for(let i=0;i<array.length;i++){
        if(predicate?predicate(array[i],i,array):array[i]){
            return true;
        }
    }
    return false
}
console.log(mySome(list,x=>x%2==0))
//js 中的every对应python中的all
function myEvery(array,predicate){
    for(let i=0;i<array.length;i++){
        if(!(predicate?predicate(array[i],i,array):array[i])){
            return false;
        }
    }
    return true
}
console.log(myEvery(list,x=>x%2==0))

console.log(list.every(x=>x%2==0))
console.log(list.some(x=>x%2==0))


function add_item(item, target_list=[]){
    target_list.push(item)
    return target_list
}
    
list1 = add_item("apple")
console.log(list1)
list2 = add_item("banana")
console.log(list2)


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