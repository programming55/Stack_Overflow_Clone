
function panel1(){
    pid1 = document.getElementById("panel-but1");
    pid1.classList.toggle("active");
    var panel = pid1.nextElementSibling;
    if (panel.style.maxHeight){
    panel.style.maxHeight = null;
    } else {
    panel.style.maxHeight = panel.scrollHeight + "px";
    } 
}
function panel2(){
    pid2 = document.getElementById("panel-but2");
    pid2.classList.toggle("active");
    var panel = pid2.nextElementSibling;
    if (panel.style.maxHeight){
    panel.style.maxHeight = null;
    } else {
    panel.style.maxHeight = panel.scrollHeight + "px";
    } 
}
function panel3(){
    pid3 = document.getElementById("panel-but3");
    pid3.classList.toggle("active");
    var panel = pid3.nextElementSibling;
    if (panel.style.maxHeight){
        panel.style.maxHeight = null;
    } 
    else {
        panel.style.maxHeight = panel.scrollHeight + "px";
    } 
}

function User_Check(){
        return $.ajax({
            url: "/checklogin",
            type: "post",
            async: false,
            // dataType: 'json',
        });
    }
    function CheckLogin(result){
            if(result=='true'){
                console.log(result);
                return true;
            }
            else{
                // alert("You must Log In before posting any answers!");
                return false;
            }
    }



function Validate_Username(){
    var username_box = document.getElementById('username');
    var username = document.getElementById('username').value;
    var username_tooltip = document.getElementById('user_name-tooltip');
    $.ajax({
        url: "/checklogin",
        type: "post",
        data: {'user':username} ,
        success: function(result){
            console.log(result, result.constructor);
            if(result==="false"){
                username_box.style.border = "1px solid red";
                username_tooltip.innerHTML = "Username alredy exists!";
                return false;
            }
            else{
                username_tooltip.innerHTML = "";        
                username_box.style.border = "2px solid #04d812";
                return true;
            }
        }
    });
}

function Check_Username(){
    var username_box = document.getElementById('user');
    var username = document.getElementById('user').value;
    var username_tooltip = document.getElementById('usr-tooltip');
    $.ajax({
        url: "/checklogin",
        type: "post",
        data: {'user':username} ,
        success: function(result){
            console.log(result, result.constructor);
            if(result==="true"){
                username_box.style.border = "1px solid red";
                username_tooltip.innerHTML = "Username not found!";
                return false;
            }
            else{
                username_tooltip.innerHTML = "";        
                username_box.style.border = "2px solid #04d812";
                return true;
            }
        }
    });

}


function Validate_Email(){
    var email_box = document.getElementById('email');
    var email = document.getElementById('email').value;
    var email_pattern1 = new RegExp("[a-z0-9]*@students.iiit.ac.in$","i");
    var email_pattern2 = new RegExp("[a-z0-9]*@research.iiit.ac.in$","i");
    var email_res1 = email_pattern1.test(email);
    var email_res2 = email_pattern2.test(email);
    var email_tooltip = document.getElementById('email-tooltip');
    if(email_res1 || email_res2){
        email_box.style.border = "2px solid #04d812";
        email_tooltip.innerHTML = "";
        return true;
    }
    else{
            email_box.style.border =  "1px solid red";
            email_tooltip.innerHTML = "Incorrect Email Format";
            email_tooltip.style.color = "orange";
            email_tooltip.style.textDecoration = "underline";
            email_tooltip.style.textDecorationColor="red";
            email_tooltip.style.fontWeight = "bold";
            email_tooltip.style.fontSize = "large";
            return false;
    }
}


function Validate_Recovery_Email(){
    var email_box = document.getElementById('email-forgot-body');
    var email = document.getElementById('email-forgot-body').value;
    var email_pattern1 = new RegExp("[a-z0-9]*@students.iiit.ac.in$","i");
    var email_pattern2 = new RegExp("[a-z0-9]*@research.iiit.ac.in$","i");
    var email_res1 = email_pattern1.test(email);
    var email_res2 = email_pattern2.test(email);
    var email_tooltip = document.getElementById('forgot-email-tooltip');
    if(email_res1 || email_res2){
        email_box.style.border = "2px solid #04d812";
        email_tooltip.innerHTML = "Password Reset Link Sent to registered email successfully. Click Close to exit this dialog box";
        email_tooltip.style.color = "green";
        return true;
    }
    else{
            email_box.style.border =  "1px solid red";
            email_tooltip.innerHTML = "Incorrect Email Format! Please enter your registered email only";
            email_tooltip.style.color = "red";
            // email_tooltip.style.textDecoration = "underline";
            // email_tooltip.style.textDecorationColor="red";
            // email_tooltip.style.fontWeight = "bold";
            // email_tooltip.style.fontSize = "large";
            return false;
    }
}


function Validate_Password1(){
    var password_box = document.getElementById("newpass");
    var password = document.getElementById("newpass").value;
    var password_tooltip = document.getElementById('password-tooltip');
    if(password.length<8){
        password_box.style.border =  "1px solid red";
        password_tooltip.innerHTML = "Password must be atleast 8 characters";
        password_tooltip.style.color = "orange";
        password_tooltip.style.textDecoration = "underline";
        password_tooltip.style.textDecorationColor="red";
        password_tooltip.style.fontWeight = "bold";
        password_tooltip.style.fontSize = "large";
        
        return false;
    }
    else{
        password_box.style.border =  "2px solid #04d812";
        password_tooltip.innerHTML = "";
        return true;
    }
    
}
function Validate_Password2(){
    var password_box = document.getElementById("newpassr");
    var password = document.getElementById("newpassr").value;
    var password_tooltip = document.getElementById('password-repeat-tooltip');
    var pass_initial = document.getElementById("newpass").value;
    if(password!=pass_initial){
        password_box.style.border =  "1px solid red";
        password_tooltip.innerHTML = "Passwords don't match!";
        password_tooltip.style.color = "orange";
        password_tooltip.style.textDecoration = "underline";
        password_tooltip.style.textDecorationColor="red";
        password_tooltip.style.fontWeight = "bold";
        password_tooltip.style.fontSize = "large";

        
        return false;
    }
    else{
        password_box.style.border =  "2px solid #04d812";
        password_tooltip.innerHTML = "";
        return true;
        
    }
    
}

function Validate_SignUp(){
    var username_tooltip = document.getElementById('user_name-tooltip').innerHTML;
    if(username_tooltip!=""){
        return false;
    }
    var check_email =Validate_Email();
    var check_pass =Validate_Password1();
    var check_passr =Validate_Password2();
    if(check_email && check_pass && check_passr){
        return true
    }
    else{
        return false;
    }
}