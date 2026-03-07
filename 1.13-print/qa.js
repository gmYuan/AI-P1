

/**
// ---------------------------------------------------------------------------
1.13-1.1 todo


**/




class Student{
    toString(){
        return "stu"
    }
}
const s = new Student()
console.log(s)
console.log(s+"$");
console.log(String(s));
console.log(s.toString());

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



const str = "a,b,c"
const arr = str.split(',')
console.log(arr)
const str2 = arr.join(',')
console.log(str2)



const arr = [1,2,3]
console.log("a,b,c".split(',').join(','))