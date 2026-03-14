/**
class MyClass{
    constructor(){
        this._attrValue = "初始值"
    }
    get attr(){// __get__ get
        console.log(`Getting Value:${this._attrValue}`)
        return this._attrValue
    }
    set attr(value){// __set__ set
         console.log(`Setting Value to:${value}`)
        this._attrValue=value
    }
}
//在js中，属性访问器是实例级别的，每个实例都有自己的getter setter
//在Python中描述是类级别的，可以被 多个实例共享 
const obj = new MyClass()
console.log(obj.attr)
obj.attr="新值"
console.log(obj.attr)


class MyClass{
    constructor(){
        this._attrValue = "初始值"
    }
}
Object.defineProperty(MyClass.prototype,'attr',{
    get: function(){// __get__ get
        console.log(`Getting Value:${this._attrValue}`)
        return this._attrValue
    },
    set: function(value){// __set__ set
         console.log(`Setting Value to:${value}`)
        this._attrValue=value
    },
    configurable:true,
    enumerable:true
})
Object.defineProperty(MyClass.prototype,'nd',{
    get: function(){// __get__ get
        console.log(`Getting Value:${this._attrValue}`)
        return this._attrValue
    }
})
const obj = new MyClass()
console.log(obj.attr)
console.log(obj.nb)
obj.attr = '新值'
console.log(obj.attr) 

class Animal{

}
duck = new Animal()
duck.name = "鸭鸭"
function say_hi(){
 return `Hi! I am ${this.name}`
}
dog = new Animal()
dog.name = "旺旺"
duck.say_hi = say_hi.bind(dog)
console.log(duck.say_hi())

class Animal{
    constructor(name){
        this.name = name
    }
}
function meow(){
 return `${this.name} 喵喵...`
}
   
cat1 = new Animal('小白')
cat2 = new Animal('小黑')
//cat1.speak=meow
//cat2.speak=meow
//在JS里面，给类添加属性或方法，实例是访问不到的,要想说到需要给类的原型Animal.prototype加
//但是在Pyhton中，给类添加属性的方法，实例是可以访问的
Animal.speak=meow
Animal.prototype.speak=meow
console.log(cat1.speak());
console.log(cat2.speak());

const person = {
    name:"张三"
}
function intro(){
    console.log(`我叫${this.name}`)
}
person.method1 = intro.bind(person)
person.method2 = ()=>intro.call(person)
person.method1()
person.method2()
class MathUtils{
    static add(a, b){
        return a+b
    }
}
   

let arr = [1,2,3]
const oldPush = Array.prototype.push
Array.prototype.push = function(...args){
    //return [...this,...args,...args,...args]
    oldPush.call(this,...args,...args,...args)
}
arr.push(4)
console.log(arr)
Array.prototype.push=oldPush
arr.push(5)
console.log(arr)

class Student{
    school = "清华大学" 
    constructor(name){
        this.name = name
    }
    static getSchool(){
        return Student.school
    }
}
s1 = new Student("小明")
s2 = new Student("小红")

console.log(s1.school)
console.log(s2.school)
console.log(s1.name)  
console.log(s2.name)  


class Utils{
    static add(a,b){
        return a+b
    }
}
const util = new Utils()
console.log(util.add(1,2))


let obj = {}
class Person{
    constructor(name){
        this.name = name
    }
}
const person = new Person()
console.log(person instanceof Object) 
class Singleton{
    constructor(value){
        if (Singleton._instance){
            return Singleton._instance
        }
        this.value = value
        Singleton._instance=this
    }
}
const s1 = new Singleton(1)
console.log(s1.value)
const s2 = new Singleton(2)
console.log(s1.value, s2.value)
console.log(s1 === s2)


class Person{
    age = 25
}

const person1 = new Person()
const person2 = new Person()
console.log(person1.age)
console.log(person2.age)
person1.age=30
console.log(person1.age)
console.log(person2.age)

class Person{
    constructor(name,age){
        this._name= name
        this._age = age
    }
    get name(){
        return this._name
    }
    get age(){
        return this._age
    }
    set name(value){
        this._name=value
    }
    set age(value){
       this._age=value
    }

}
const person = new Person('张三',25);
console.log(person.name)
person.name='李四'
console.log(person.name)
class Animal{
    constructor(name){
        this.name = name
    }
    speak(){
        console.log(`${this.name} 发出叫声`)
    }
}
class Dog extends Animal{
    constructor(name,breed){
        super(name)
        this.breed = breed
    }
    speak(){
        super.speak()//super().speak()
        console.log(`${this.name}汪汪`)
    }
}
const dog = new Dog('','')
dog.speak()
console.log(dog instanceof Dog)
console.log(dog instanceof Animal)

const Person={}
Object.defineProperty(Person,'myage',{
    get: function(){// __get__ get
        console.log(`Getting Value:1`)
        return 1
    },
    set: function(value){// __set__ set
         console.log(`Setting Value to:2`)
    }
})
console.log(Person.myage)
Person.myage=2

*/


function decoratorName(func) {
    return function(...args) {
        // 在调用原始函数前可加入自定义操作
        console.log("开始执行");
        const result = func(...args);
        // 在调用原始函数后可加入自定义操作
        console.log("执行结束");
        return result;
    }
}

// 等效于 func = decoratorName(func)
function func() {
    console.log("这是原始函数内容");
}

const decoratedFunc = decoratorName(func);
decoratedFunc();