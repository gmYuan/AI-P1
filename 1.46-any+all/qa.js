

//-------------------------------------------------------------------------------

const list = [0,2,4]

//js中的some对应python中的any
function mySome(array,predicate){
    for(let i=0;i<array.length;i++){
        if(predicate?predicate(array[i],i,array):array[i]){
            return true;
        }
    }
    return false
}
console.log(mySome(list,x=>x%2==0))

//js 中的every对应python中的all
function myEvery(array,predicate){
    for(let i=0;i<array.length;i++){
        if(!(predicate?predicate(array[i],i,array):array[i])){
            return false;
        }
    }
    return true
}

console.log(myEvery(list,x=>x%2==0))
console.log(list.every(x=>x%2==0))
console.log(list.some(x=>x%2==0))


