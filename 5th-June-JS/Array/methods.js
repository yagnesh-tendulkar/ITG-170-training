let arr = [9,5,3,2,8,6,1,4,7]

document.write(arr);

document.write("<br><br><br>")

for(let i=0;i<arr.length;i++)
{
    document.write(arr[i]+"<br>")
}

document.write("<br><br><br>")

arr.forEach(element=>document.write(element+"<br>"))

document.write("<br><br><br>")

arr.filter(element=>element>=5).forEach(element=>document.write(element+"<br>"))

arr.sort()

document.write("<br><br><br>")

arr.forEach(e=>document.write(e+"<br>"))

document.write("<br><br><br>")

arr.sort((a,b)=>b-a).forEach(element=>document.write(element+"<br>"))

document.write("<br><br><br>")

arr.sort() //again sorted in ascending order

arr.map(element=>element*element).forEach(element=>document.write(element+"<br>"))

document.write("<br><br><br>")

document.write("Index of 1 : "+arr.indexOf(1))

document.write("<br><br><br>")

document.write(arr.find(num=>num>=5)) //o/p: 5

document.write("<br><br><br>")

document.write(arr.pop()) //9

document.write("<br><br><br>")

document.write(arr.push(9)) //9

document.write("<br><br><br>")

document.write(arr);

document.write("<br><br><br>")

document.write(arr.shift())

document.write("<br><br><br>")

document.write(arr);

document.write("<br><br><br>")

document.write("array unshifted : "+arr.unshift(100,200,300)) //returns the new length of the array

document.write("<br><br><br>")

document.write(arr);

document.write("<br><br><br>")

document.write("array slice : "+arr.slice(1,5)) //returns the part of the original array

document.write("<br><br><br>")

document.write("array splice adding "+arr.splice(1,0,99)) //returns nothing but does its work

document.write("<br><br><br>")

document.write(arr);

document.write("<br><br><br>")

document.write("array splice deleting "+arr.splice(1,1)) //returns the element and does its work

document.write("<br><br><br>")

document.write(arr);

document.write("<br><br><br>")

document.write("array splice updating "+arr.splice(1,1,99)) //returns the old value and update the new value

document.write("<br><br><br>")

document.write(arr);