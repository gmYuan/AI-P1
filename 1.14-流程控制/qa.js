

/**
// ---------------------------------------------------------------------------
//1.14-1.1 toSting定义后，会在使用String()时 被调用

const book = {
    name:'red',
    toString(){
        return "bookred"
    }
}

console.log(book);
console.log(book+"$");
console.log(String(book));
console.log(book.toString());

**/