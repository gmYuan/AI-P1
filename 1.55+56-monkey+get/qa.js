

//---------------------------------------------------------------------

class MyClass {
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



//---------------------------------------------------------------------


class MyClass2 {
    constructor(){
        this._attrValue = "初始值"
    }
}

Object.defineProperty(MyClass2.prototype,'attr',{
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

Object.defineProperty(MyClass2.prototype,'nd',{
    get: function(){// __get__ get
        console.log(`Getting Value:${this._attrValue}`)
        return this._attrValue
    }
})

const obj = new MyClass2()
console.log(obj.attr)
console.log(obj.nb)
obj.attr = '新值'
console.log(obj.attr)



//---------------------------------------------------------------------

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



//---------------------------------------------------------------------

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



//---------------------------------------------------------------------

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



//---------------------------------------------------------------------

class MathUtils{
    static add(a, b){
        return a+b
    }
}




//---------------------------------------------------------------------

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