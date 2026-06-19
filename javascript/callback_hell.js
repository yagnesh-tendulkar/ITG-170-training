function OrderPlacing(name,callback){
    console.log('bujji nuvu order pettav memmu order tesukunam bujji wait for sometime'+name);
    setTimeout(() => {
        console.log("bujjama wait mare");
    callback();}, 2000);
}
function payment(callback) {
    setTimeout(() => {
        console.log("Payment Done");

        callback();
    }, 2000);
}
function packing(callback) {
    setTimeout(() => {
        console.log("Packing Done");

        callback();
    }, 2000);
}
function delivery() {
    console.log("Order Delivered");
}
OrderPlacing("geethu", function () {
    payment(function () {
        packing(function () {
            delivery();
        });
    });
});