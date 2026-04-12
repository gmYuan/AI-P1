

//-------------------------------------------------------------------------------
let str = '1+2+3'
let result = eval(str)
console.log(result)


//const keyValueParies = ["a", 1, "b", 2, "c", 3]
const keyValueParies =[
    ["name","张三"],
    ["age",25],
    ["city","北京"]
]
// properties.reduce((accumulator,currentValue,currentIndex,array)=>{
//    return accumulator
//},initialValue)

const obj = keyValueParies.reduce((acc,[key,value])=>{
    acc[key]=value
    return acc
},{})

console.log(obj)
