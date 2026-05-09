
//---------------------------------------------------------------------

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



//---------------------------------------------------------------------

class Utils{
    static add(a,b){
        return a+b
    }
}
const util = new Utils()
console.log(util.add(1,2))



//---------------------------------------------------------------------
let obj = {}
class Person{
    constructor(name){
        this.name = name
    }
}
const person = new Person()
console.log(person instanceof Object)



//---------------------------------------------------------------------

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



//---------------------------------------------------------------------

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



//---------------------------------------------------------------------

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



//---------------------------------------------------------------------

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



//---------------------------------------------------------------------

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