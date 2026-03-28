

// ------------------------------------------------------------------------

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log(numbers.slice(3,8).filter(x=> x % 2 == 0))

const words = ['hello', 'world', 'python', 'programming']
console.log(words.map(x=>x.slice(2)))




// ------------------------------------------------------------------------
const list = [1, 2, 3]
//const list2 = [item*2 for item in list if item > 1]
console.log(list.filter(item=>item>1).map(item=>item*2))
