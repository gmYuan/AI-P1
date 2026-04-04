

//---------------------------------------------------------

class Person{}

const p = new Person()
p.age = 30
p.home='bj'

console.log(p)
console.log(Object.getPrototypeOf(p).constructor)
const type = Object.getPrototypeOf(p).constructor

// class -> cls
//1 去掉元音字母 重复字母保留一个
//result = cls.__new__(cls)
const newP = new type()

for (const key in p){
    newP[key]=p[key]
}
console.log(newP)



//---------------------------------------------------------

//在jS经常会看到这样的定法
//创建一个完全 空白的对象
const pureObject = Object.create(null)


//obj.__class__
console.log(Object.getPrototypeOf(p).constructor)

