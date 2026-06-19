
function OrderPlacing(name){
    return new Promise((resolve, reject) => {
         console.log(`Order placed by: ${name}`);
        setTimeout(() =>  {
            console.log("order taken");
            resolve();
        },1000);
    });
}
function Payment(){
    return new Promise((resolve,reject)=> {
        console.log("upi payment");
        setTimeout(() => {
            console.log("order payment done");
            resolve();},3000);
        });
}
function Packing(){
    console.log("order packed");
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("order will be delivered in 5 mins");
            resolve();},7000);
        })
    }

function Delivered(){
    console.log("payment done");
    return new Promise((resolve, reject) => {
    setTimeout(() => {
    console.log("order delivered");
    resolve();},10000);
        
    });
}
async function processOrder() {
    try {
        await OrderPlacing("geethu");
        await Payment();
        await Packing();
        await Delivered();
    }
    catch (error) {
        console.log("Something went wrong:", error);
    }
}

processOrder();