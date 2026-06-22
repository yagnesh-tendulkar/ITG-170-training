function f1()
{
    console.log("f1 function is called")
}

// f1();


function f2(callback)
{
    console.log("f2 function is called<br>")
    callback();
}

// f2(f1);


// async function getMessage()
// {
//     console.log("getMessage() started<br>")
//     let num=1
//     for(let i=0;i<10;i++)
//     {
      
//         getCount(i);

//     }
//     console.log("getMessage() ended")

// }

// async function getCount(num)
// {
//     setTimeout(()=>console.log(`${num}<br>`),1000)

// }

// getMessage()


async function getMessage() {
    console.log("getMessage() started");

    const promises = [];

    for (let i = 0; i < 10; i++) {
        promises.push(getCount(i));
    }

    await Promise.all(promises);

    console.log("getMessage() ended");
}

async function getCount(num) {
    const delay = Math.floor(Math.random() * 5000); // 0-5 seconds

    return new Promise((resolve) => {
        setTimeout(() => {
            console.log(num);
            resolve();
        }, delay);
    });
}

// getMessage();

let i=0;
function greet()
{
    let messages=['Thank You','Oo! You clicked again','You still there','Stop it please','This is last warning']
    document.getElementById("message").innerText=messages[i];
    i++;
}