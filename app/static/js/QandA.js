function Post_Answer_Check(){
    var posted_ans_box = document.getElementById('user-ans');
    var posted_ans = document.getElementById('user-ans').value;
    var posted_ans_tooltip = document.getElementById('post-ans-msg');
    if(posted_ans==""|| posted_ans==null){
        posted_ans_tooltip.innerHTML = "Answer cannot be empty!";
        posted_ans_tooltip.style.color = "red";
        posted_ans_box.style.border =  "1px solid red";
        return false;
    }
    else
        return true;
}

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

function Accept_Answer(){
    var accept_but = document.getElementById('accept-ans');
    var accpeted = document.getElementById('accept-but-text');
    var tick_span = document.getElementById('answer-accepted');
    tick_span.style.display = "block";
    accpeted.style.display = "none";
    accept_but.disabled = "true";
    accept_but.style.border = "none";
    accept_but.style.boxShadow = "none";
}

