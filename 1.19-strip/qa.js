

// ----------------------------------------------------------------------------
// 1.19-1  trim()

const str = ' \t\nhello world \t\n'
console.log(str.trim())
console.log(str.trimStart())
console.log(str.trimEnd())



// ----------------------------------------------------------------------------
// 1.19-4.2 py 里迭代器的本质： 生成器会返回一个迭代器

/* py 写法
def gen():
    yield 1
    yield 2
    yield 3

it = gen()

for item in it:
    print(item)
*/

// 等价于
function *gen(){
    yield 1
    yield 2
    yield 3
}
it =gen()
console.log(it.next().value)
console.log(it.next().value)
console.log(it.next().value)
console.log(it.next())