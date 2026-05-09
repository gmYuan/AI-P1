

//-------------------------------------------------------------------------------

function add_item(item, target_list=[]){
    target_list.push(item)
    return target_list
}

list1 = add_item("apple")
console.log(list1)
list2 = add_item("banana")
console.log(list2)



//-----------------------------------------------

function calculate_sum(...args){

}




//--------------------------------------------------------------------------
function decorator(){

}
//@decorator()
class Person{}

function wrapper() {}


function register() {
    console.log("register")
}

wrapper.register = register
wrapper.register()



// py 实现单例是不是 也有静态属性