const loginBtn = document.querySelector("#login-btn")
const username = document.querySelector("#username")
const password = document.querySelector("#password")
const user1 = {
    username: "admin",
    password: "admin"
}

loginBtn.addEventListener("click", (event) => {
    if (username.value === user1.username && password.value === user1.password){
        console.log("Your in")
            window.location.href = "../index.html";
    }
    else{
        console.log(`${username.value}`)
        console.log(`${password.value}`)

    }
})