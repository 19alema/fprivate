// const user_name = document.getElementById('username').value
// const password= document.getElementById('password').value
// const confirm_password = document.getElementById('confirm-password').value

// console.log(user_name, password)


// const form = document.getElementById('signup-form')

// form.onsubmit((e) => {
//     e.preventDefault()
    
//     fetch('/signup', {
//         method: "POST",
//         body: JSON.stringify({
//         'username': user_name,
//         'password': password,
//         'confirm_password' : confirm_password
//         }),
//         headers: {
//             'Content-Type': 'application/json'
//         }
//     })
// }).then(function(response) {
//     if (!response.ok)
//         throw Error('Some Error has occured')
//     else {
//         return response.json()
//     }
// })
//     .then(data => console.log(data))
//     .catch((error) => {
//         console.log(error)
// })