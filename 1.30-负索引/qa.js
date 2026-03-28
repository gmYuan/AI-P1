

// ----------------------------------------------------------------------------
// 1.30-2 正负索引切片
let numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log(numbers.slice(2,8));


// ----------------------------------------------------------------------------
//1.30-4.2 循环在 算法应用 2- 数组旋转

//是pop和push吧
const arr =[1,2,3,4,5]
const item1 = arr.pop()
arr.unshift(item1)
const item2 = arr.pop()
arr.unshift(item2)
const item3 = arr.pop()
arr.unshift(item3)
console.log(arr)


const l1 = [1, 2]
const l2 = [3, 4]
//const l3 = l1 + l2
const l3 = l1.toString()+l2.toString()
console.log(l3)



// ----------------------------------------------------------------------------
// 1.30-5.3 实际应用2- 日志文件内容

const arr6 = ['a','b','c']
console.log(arr6[2])
console.log(arr6.at(1))
console.log(arr6.at(-1))
console.log(arr6[arr6.length-1])