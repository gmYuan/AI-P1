

// ------------------------------------------------------------------------

let my_list_original = [1, 2, 3, 4, 2, 5]


const index = my_list_original.indexOf(2)
//my_list_original.splice(index,1)
//console.log(my_list_original)


//my_list_original.splice(2,1)
//del my_list_del[2]


//del my_list_del[2:4]
my_list_original.splice(2,2)
console.log(my_list_original)



var my_list_original2 = [1, 2, 3, 4, 2, 5]
delete my_list_original2;
console.log(my_list_original2)


let my_list_original3 = [1, 2, 3, 4, 2, 5]
const index = my_list_original3.findIndex(item=>item==2)
console.log(index)