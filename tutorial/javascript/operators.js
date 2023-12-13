console.log(typeof "hello");
console.log(typeof 1.23);
console.log(typeof false);

// in javascipt NaN is not equal to itself
console.log(NaN == NaN) // false
console.log("hello" == "hello")

// ternary operator
console.log(1 < 2? "yes": "no");


// auto type conversion
console.log(8 * null) // 0

console.log("5"-1);  // think of this as "5" - "1" (nope), so 5 -1 -> 4

console.log("5" +  1); // think as "5" + "1" -> 51 so valid return (co-ersion left to right)

console.log("five" * 2)

console.log("4" == 4) // no strict type check

console.log("4" === 4) // strict type check