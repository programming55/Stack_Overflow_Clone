
// function Login_Check(){
//     return $.ajax({
//         url: "/checklogin",
//         type: "post",
//         async: false,
//         // dataType: 'json',
//     });
// }
// function CheckLogin(result){
//         if(result=='true'){
//             console.log(result);
//             return true;
//         }
//         else{
//             alert("You must Log In before posting any answers!");
//             return false;
//         }
// }

// function Post_Answer_Check(){
//     var logged_in = Login_Check().done(CheckLogin);
//     if (logged_in.responseText== "false")
//         return false;
//     else 
//         return true;
// }


// function Post_Comment_Check(){
//     var logged_in = CheckLogin();
//     console.log(logged_in);
//     if(logged_in==false || logged_in == undefined){
//         alert("You must Log In before posting any comments!");
//         return false;
//     }
//     else
//         return true;
// }

// function Validate_Comments(){
//     var comment_box = document.getElementById('comment-body');
//     var comment = document.getElementById('comment-body').value;
//     var comment_tooltip = document.getElementById('user-comm-check');
//     if(comment==""|| comment==null){
//         comment_tooltip.innerHTML = "Comment cannot be empty!";
//         comment_tooltip.style.color = "red";
//         comment_box.style.border =  "1px solid red";
//         return false;
//     }
//     else
//         return true;
// }

function Accept_Answer(ans_id){
    var accept_but = document.getElementById('accept-ans');
    // var accpeted = document.getElementById('accept-but-text');
    var tick_span = document.getElementById('answer-accepted');
    // accepted.style.display = "none";
    accept_but.disabled = "true";
    accept_but.style.border = "none";
    accept_but.style.boxShadow = "none";
    accept_but.style.display = "none";
    var image = document.getElementById('accepted-image');
    tick_span.style.display = "block";
    image.style.display = "block";
    var answerid = Number(ans_id)
    console.log(answerid)
    $.ajax({
        url: "/acceptans",
        type: "post",
        data: {'ans_id':answerid} ,
        success: function(result){
            if(result=='true'){
                console.log(result, result.constructor);
                
                // return true;
            }
        }
    });
}

function Check_Accepted(){
    accepted = true;
    var tick_span = document.getElementById('answer-accepted');
    tick_span.style.display = "block";
    var answerid = document.getElementById('ans-bdy').innerHTML;
  
    $.ajax({
        url: "/ansaccepted",
        type: "post",
        data: {'ans_id':answerid} ,
        success: function(result){
            console.log(result, result.constructor);
            if(result==="true"){
                var image = document.getElementById('accepted-image');
                image.style.display = "block"
                // return false;
            }
            // else{
            //     username_tooltip.innerHTML = "";        
            //     username_box.style.border = "2px solid #04d812";
            //     return true;
            // }
        }
    });
}

