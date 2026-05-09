
//---------------------------------------------------------------------

function decoratorName(func) {
    return function(...args) {
        // 在调用原始函数前可加入自定义操作
        console.log("开始执行");
        const result = func(...args);
        // 在调用原始函数后可加入自定义操作
        console.log("执行结束");
        return result;
    }
}

// 等效于 func = decoratorName(func)
function func() {
    console.log("这是原始函数内容");
}

const decoratedFunc = decoratorName(func);
decoratedFunc();