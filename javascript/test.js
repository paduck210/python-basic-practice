
// var means empty box
// equal > ===

//var weather = 'sunny'

//if (weather === 'sunny') {
//  console.log(weather)
//} else if (weather === 'sunny') {
//  console.log('lowercase')
//}


// logical AND
// var result = a && b ;

// logical OR
// var result = a || b ;

// logical NOT
// var result = !a ;


//var sunny = false
//if (!sunny) {
//  console.log('returned')
//}


//var comp = 'computer'
//console.log (comp[0] + comp[1])

//var comp = 'cafe bene'
//console.log (comp[5])

var name1 = 'tom'
var name2 = 'sam'
if (name1[0] === 't') {
  console.log(name1)
} else if (name === 's') {
  console.log(name2)
} else {
  console.log('No Match')
}


//Array
var students = [ "john", "Paul", "Ringo" ]
console.log(students)

//Array.length
console.log(students.length)

//Array.element
console.log(students[0])

//Array. add element
var fruits = ["Banana", "Orange", "Apple", "Mango"];
console.log(fruits)
fruits.push("Kiwi");
console.log(fruits)


//Array + match with exsited var
var name1 = "tom"
var name2 = "sam"

var arr = [name1, name2,"paul","Paduck"]
arr.forEach(function(name) {
  console.log(name)
})


//define

function fullName(x,y) {
  var full = x + ' ' + y
  return full
}

var name1 = "Harry"
var name2 = "Poter"

var result = fullName(name1,name2)
console.log(result)
