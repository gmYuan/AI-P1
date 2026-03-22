

// ----------------------------------------------------------------------------
// 1.29-1.1 switch语法

const day = 'day1'
switch (day) {
    case 'day1':
        console.log('星期一')
        break;
    case 'day2':
        console.log('星期二')
        break;
    default:
        console.log('未知')
}



// ----------------------------------------------------------------------------
// 1.29-1.1  在Python中重载操作符 |

const a=5
const b=3
//2个|表示逻辑运算符的或,也就是python的or
console.log(a||b)
//在js中，一个|对应的也是位运行中的或
console.log(a|b)

