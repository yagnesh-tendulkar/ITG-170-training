//callback function order(callback)
function PlaceOrder(name,callback){
    console.log("Order Placed By User"+name)
    setTimeout(() =>{
     console.log("Order Ready");
     callback();},7000);}
function Order(){
    console.log("Order Delivered");
}
PlaceOrder('geethu',Order)
//callbavck example iwill create another babu
function vennala(song,callback){
    console.log("she liked telugu songs very well:"+song)
    setTimeout(() => {
        console.log("aagu songs on the way bujji vennala amma");
        callback();},8000);}
function vennalasonglist(){
    console.log("oyy oyy");
    console.log("chirru chiru");
    console.log("love songs");
}       
vennala('telugusongs',vennalasonglist)
