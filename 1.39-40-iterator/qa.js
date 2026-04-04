

//------------------------------------------------------------------------------------------

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


function delay(ms, value) {
    return new Promise(resolve => setTimeout(() => resolve(value), ms))
}

async function* asyncGenerator() {
    yield await delay(1000, '第1个异步值')
    yield await delay(2000, '第2个异步值')
    yield await delay(3000, '第3个异步值')
    return '完成'
}


async function processAsyncGenerator(){
    for await (const value of asyncGenerator()){
        console.log(`收到${value}`)
    }
}
processAsyncGenerator()



async function processAsyncGeneratorV2(){
     const asyncGen = asyncGenerator()
     let result = await asyncGen.next()
     while(!result.done){
        console.log(`${result.value}`)
        result = await asyncGen.next()
     }
     console.log(`${result.value}`)
}

processAsyncGeneratorV2()


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



//不是把 '正常' 赋值给result
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
// console.log(throwGen.throw(new Error('从外部抛出异常')))  // 捕获错误, done: false
// console.log(throwGen.next())   // undefined, done: true

//console.log(throwGen.return())   // undefined, done: true

console.log(throwGen.next('张三'))
console.log(throwGen.next())

