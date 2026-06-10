//js objects
var myObj={
    gift:"pony",
    pet:"kitten",
    bed:"sleigh"
};
function checkObj(checkProp){
    if (myObj.hasOwnProperty(checkProp)){
        return myObj[checkProp];

    }
    else{
        return "NOt found";
    }
}

console.log(myObj.car);



//manipulation of complex objects objects inside an array
var myMusic=[{
    "artist":"Alan walker",
    "title":"AlonePT",
    "release":1973,
    "formats":["CD","BT","LP"],
    "gold":true
},
{
    "artist":"Samuel james",
    "title":"Sue",
    "release":1970,
    "formats":["YTB VDO"],
}];
//for(var i=0,myMusic.length,i=i+1){
console.log(myMusic[1].artist);

//}




//nested arrays
var myPlants=[
    {
        type:"flowers",
        list:["rose","tulip","lilly"]
    },
    {
        type:"animals",
        list:["dog","cat","tiger"]
    }
];
console.log(myPlants[0].list[2]);




//record collection
/*
record collection is object containing multiple objects inside it
where each object represents as a record*/
var myCollections={
    1:{
        type:"casual",
        shoes:"leather casuals",
        watch:"Titan"
    },
    2:{
        type:"Formal",
        shoes:"leather casuals",
        watch:"Sonata"
    },
    3:{
        type:"occasional",
        shoes:"HRX boots",
        watch:"Titan",
        access:["chain","ring","perfume"]
    },
    4:
    {

    }
};
console.log(myCollections[3].access[2]);
//manual updation of record 
console.log(myCollections[3].access[3]="bracelet");


//updating a record
console.log(myCollections);
console.log(" ");
console.log(myCollections[2].type="Semi-Formal");
console.log(myCollections);



// //function to create a record dynamically

// function createRecord(id,type,shoes,watch){
//     myCollections[id]={
//         type:type,
//         shoes:shoes,
//         watch:watch
//     };
// }

// createRecord(5,"kids","kids wear","baby watch");
// console.log(myCollections);


// console.log("     ");

// //function to update the records
// function updatecollections(id,prop,value){
//     if (value ===""){
//         delete myCollections[id][prop];
//     }
//     else if (prop=="access")
//     {
    
//         if (!myCollections[id].hasOwnProperty("access")) {
//             myCollections[id].access = [];
//         }

//         myCollections[id].access.push(value);
//     }
//     else {
//         myCollections[id][prop] = value;
//     }

//     return myCollections;
// }

//create and save record dynamically

function saveRecord(id,prop,value) {

    // Create record if it doesn't exist
    if (!myCollections[id]) {
        myCollections[id] = {};
    }
    // If prop is an object, update entire record
    if (typeof prop === "object") {

        myCollections[id] = {
            ...myCollections[id],
            ...prop
        };

        return myCollections;
    }
    // Delete property
    if (value === "") {
        delete myCollections[id][prop];
    }

    // Handle accessories array
    else if (prop === "access") {

        if (!myCollections[id].access) {
            myCollections[id].access = [];
        }

        myCollections[id].access.push(value);
    }

    // Create/Update normal property
    else {
        myCollections[id][prop] = value;
    }

    return myCollections;
}
// updatecollections(4,"type","holiday");
// console.log(myCollections);


// updatecollections(4,"shoes"," ");
// console.log(myCollections);

console.log(saveRecord(6,{type:"winterwear",shoes:"boots",watch:"sonata",access:["baby cloths","baby milk bottle"]}));
console.log(saveRecord(5,{type:"monsoon",shoes:"rainboots",watch:"fastrack=water-proof",access:["umbrella","raincover"]}));

