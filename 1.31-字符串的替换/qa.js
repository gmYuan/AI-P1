

// I 忽略 大小写 M 多行匹配 Gg 全局匹配
const str = `a A a
a A a
`
const regexp = /a/gim
while ((match=regexp.exec(str))!==null){
    console.log(match[0])
}



// ------------------------------------------------------------------------
const text_colors = "这些颜色有 red、blue 和 green。"

const color_map = {"red": "red2", "blue": "blue2", "green": "green2"}

function replace_color(match){
    console.log(match)   // red; blue; green
    return color_map[match]||match
}

const pattern_colors = new RegExp(
    Object.keys(color_map)
    // 转义正则里 有特殊含义的字符
    .map(key=>key.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'))
    .join('|'),'g'
)
const new_text_colors = text_colors.replace(pattern_colors,replace_color)
// "这些颜色有 red2、blue2 和 green2。"
console.log(new_text_colors)


// 简洁写法1：
const new_text_colors  = text_colors.replace(
    new RegExp(
    Object.keys(color_map)
    // 转义正则里 有特殊含义的字符
    .map(key=>key.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'))
    .join('|'),'g'), match=>color_map[match]||match
)
console.log(new_text_colors)
console.log(RegExp.escape)


// 简洁写法2：
const new_text_colors  = text_colors.replace(
    new RegExp(
    Object.keys(color_map)
    .map(RegExp.escape)
    .join('|'),'g'),match=>color_map[match]||match
)
console.log(new_text_colors)



// ------------------------------------------------------------------------
let my_list = [1, 2, 3]
my_list.push(4)
my_list.push("hello")
my_list.push([5, 6])
console.log(my_list)



// ------------------------------------------------------------------------
//array.splice(start, deleteCount, item1, item2)
const array = ['a','b','c','d']
array.splice(2, 2, 'e', 'f')
console.log(array)           //  ['a','b','e','f']




// ------------------------------------------------------------------------
const my_list = [1, 2, 3]
const new_list = [4,5,6]
//my_list.push(...new_list)
const result = my_list.concat(new_list)
console.log(my_list)
console.log(result)