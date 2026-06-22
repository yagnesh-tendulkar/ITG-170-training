// var result=

function add()
{
    var sum=0;
    let a= Number(document.getElementById("a").value)
    let b= Number(document.getElementById("b").value)

    sum = a+b

    document.getElementById("result").innerText=sum
}

// let result = add(10,-5,-2,-1);
// console.log(result);

function substract()
{
    var sub=0;
    let a= Number(document.getElementById("a").value)
    let b= Number(document.getElementById("b").value)

    sub = a-b

    document.getElementById("result").innerText=sub
}

function multiply()
{
    var mul=1;
    let a= Number(document.getElementById("a").value)
    let b= Number(document.getElementById("b").value)

    mul = a*b

    document.getElementById("result").innerText=mul
}

function divide()
{
    var div=0;
    let a= Number(document.getElementById("a").value)
    let b= Number(document.getElementById("b").value)

    mul = a/b

    document.getElementById("result").innerText=mul
}
