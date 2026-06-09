function test(val1, val2) {
    if (val1 === val2) {
        return "Strictly equal (same value and same datatype)";
    } 
    else if (val1 == val2) {
        return "Equal (same value but datatype may differ)";
    } 
    else {
        return "Not equal";
    }
}

console.log(test("12", "12"));

