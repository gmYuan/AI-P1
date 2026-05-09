

//-------------------------------------------------------------------------------

function compose(...funcs) {
    function composed(...args) {
        let result = funcs[funcs.length - 1](...args)
        for (let i = funcs.length - 2; i >= 0; i--) {
            result = funcs[i](result)
        }
        return result
    }
    return composed
}

function add_one(x) {
    return x + 1
}


function multiply_by_two(x) {
    return x * 2
}


function square(x) {
    return x ** 2
}

const composed_func = compose(square, multiply_by_two, add_one)
const result = composed_func(3)
console.log(result)

