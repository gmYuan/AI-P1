

// ----------------------------------------------------------------------------
// 1.30-2 正负索引切片
let numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log(numbers.slice(2,8));






/**







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

const arr6 = ['a','b','c']
console.log(arr6[2])
console.log(arr6.at(1))
console.log(arr6.at(-1))
console.log(arr6[arr6.length-1])

// I 忽略 大小写 M 多行匹配 Gg 全局匹配
const str = `a A a
a A a
`
const regexp = /a/gim
while ((match=regexp.exec(str))!==null){
    console.log(match[0])
}




 function replace_color(match){
    console.log(match)
    return color_map[match]||match
}
const pattern_colors = new RegExp(
    Object.keys(color_map)
    .map(key=>key.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'))
    .join('|'),'g'
) 
//const new_text_colors = text_colors.replace(pattern_colors,replace_color)
//console.log(new_text_colors)
const text_colors = "这些颜色有 red、blue 和 green。"

const color_map = {"red": "red2", "blue": "blue2", "green": "green2"}

const new_text_colors  = text_colors.replace(
    new RegExp(
    Object.keys(color_map)
    .map(key=>key.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'))
    .join('|'),'g'),match=>color_map[match]||match
)
console.log(new_text_colors)
console.log(RegExp.escape)

const text_colors = "这些颜色有 red、blue 和 green。"

const color_map = {"red": "red2", "blue": "blue2", "green": "green2"}

const new_text_colors  = text_colors.replace(
    new RegExp(
    Object.keys(color_map)
    .map(RegExp.escape)
    .join('|'),'g'),match=>color_map[match]||match
)
console.log(new_text_colors)


let my_list = [1, 2, 3]
my_list.push(4)
my_list.push("hello")
my_list.push([5, 6])
console.log(my_list)

//array.splice(start,deleteCount,item1,item2)
const array = ['a','b','c','d']
array.splice(2,2,'e','f')
console.log(array)


const my_list = [1, 2, 3]
const new_list = [4,5,6]
//my_list.push(...new_list)
const result = my_list.concat(new_list)
console.log(my_list)
console.log(result)


const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log(numbers.slice(3,8).filter(x=> x % 2 == 0))



const words = ['hello', 'world', 'python', 'programming']
console.log(words.map(x=>x.slice(2)))



const list = [1, 2, 3]
//const list2 = [item*2 for item in list if item > 1]
console.log(list.filter(item=>item>1).map(item=>item*2))
*/


//let my_list_original = [1, 2, 3, 4, 2, 5]
//const index = my_list_original.indexOf(2)
//my_list_original.splice(index,1)
//console.log(my_list_original)

//del my_list_del[2]
//my_list_original.splice(2,1)
//del my_list_del[2:4]
//my_list_original.splice(2,2)
//console.log(my_list_original)
//var my_list_original = [1, 2, 3, 4, 2, 5]
//delete my_list_original;
//console.log(my_list_original)

let my_list_original = [1, 2, 3, 4, 2, 5]
const index = my_list_original.findIndex(item=>item==2)
console.log(index)
