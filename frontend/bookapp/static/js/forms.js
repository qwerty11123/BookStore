function FormContain(what) {
    var divContainer = document.getElementById('form-contain');
    var html = ''
    if (what ==='Login'){
        html = `<div>
                    <h3>Login Your Account</h3>
                     <p id="err" style="color:red;"></p>
                    <form onsubmit="return LoginUser(event)" >
                    <input type="text" id="username" placeholder="Username" required class="form-control"
                    style="max-width: 500px">
                    <br><br>
                    <input type="password" id="pwd" placeholder="Password" required class="form-control"
                    style="max-width: 500px">
                    <br><br>
                    <input type="submit" id="loginBtn" value="Login"  class="btn btn-primary">
                    <br><br>
                    
                     </form></div>
                     `}

    else if(what==='Signup'){
         html = `<div>
                    <h3>Create New Your Account</h3>
                   
                    <form onsubmit="return SignupUser(event)">
                     <p id="errUser" style="color:red;"></p>
                    <input type="text" id="username" placeholder="Username" required class="form-control"
                    style="max-width: 500px">
                    <br><br>
                     <p id="errPwd" style="color:red;"></p>
                    <input type="password" id="pwd" placeholder="Password" required class="form-control"
                    style="max-width: 500px">
                    <br><br>
                     <p style="color: red" id="error"></p> 
                     <input type="password" id="cpwd" placeholder="Confirm Password" required class="form-control"
                    style="max-width: 500px">
                    <br><br>
                     <p id="errEmail" style="color:red;"></p>
                     <input type="email" id="email" placeholder="Email" required class="form-control"
                    style="max-width: 500px">
                    <br><br>
                    <input type="text" id="fname" placeholder="First Name" required class="form-control"
                    style="max-width: 500px">
                    <br><br>
                     <input type="text" id="lname" placeholder="Last Name" required class="form-control"
                    style="max-width: 500px">
                    <br><br>
                    <input type="submit" id="signupBtn" value="SignUp"  class="btn btn-primary">
                    <br><br>
                    
                     </form></div>
                     `
    }
    divContainer.innerHTML = html;

}


function LoginUser(e) {
    e.preventDefault();
    var username = document.getElementById('username').value;
    var pwd = document.getElementById('pwd').value;
    var formData = new FormData();
    formData.set("username",username);
    formData.set('password',pwd);
    fetch('http://127.0.0.1:8000/login/',{
        'method':"POST",
        'body':formData,
        })
        .then(res=>res.json())
        .then(jRes=>{
           if(jRes.token){
               localStorage.setItem('userToken',jRes.token)
               window.location = '/home'
           }
           else{
               document.getElementById('err').innerText='Either Username or Password is Incorrect'
               return false
           }
        })
        .catch(err=>console.log("error.."))

}

function SignupUser(e) {
    e.preventDefault()
    var username = document.getElementById('username').value;
    var pwd = document.getElementById('pwd').value;
    var fname = document.getElementById('fname').value;
    var lname = document.getElementById('lname').value;
    var email = document.getElementById('email').value;
    var cpwd = document.getElementById('cpwd').value;

    if (pwd !== cpwd){
        document.getElementById('error').innerText='Please Re-enter the Password'
        return false
    }
    else{
         document.getElementById('error').innerText=''

         var formData = new FormData();
         formData.set('username',username)
         formData.set('password',pwd)
         formData.set('first_name',fname)
         formData.set('last_name',lname)
         formData.set('email',email)
        fetch('http://127.0.0.1:8000/create_user/',{
        'method':"POST",
        'body':formData
    }).then(res=>res.json())
      .then(jRes=>{
       if(jRes.error){
           if(jRes.error.email){
                document.getElementById('errEmail').innerText = jRes.error.email
            }
             if(jRes.error.password){
                document.getElementById('errPwd').innerText = 'Password Is too Week'
            }
             if(jRes.error.username){
                document.getElementById('errUser').innerText = jRes.error.username
            }
       }
       else{
           FormContain('Login')
       }

      })
      .catch(err=>console.log(err))

    }



}












