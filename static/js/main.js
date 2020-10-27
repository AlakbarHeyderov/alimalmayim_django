var a = false;
function menu(){
    if(a == false){
        document.getElementById("hidden-menu").classList.remove("hide");
        document.getElementById("hidden-menu").classList.add("show");
        a = true;
    }else if(a == true){
        document.getElementById("hidden-menu").classList.remove("show");
        document.getElementById("hidden-menu").classList.add("hide");
        a = false;
    }
    
}


window.onscroll = function() {scroll()};
function scroll(){
if(document.body.scrollTop > 50 || document.documentElement.scrollTop > 50){
        document.getElementById("navbar").style.height = "40px";
    }else if(document.body.scrollTop < 50 || document.documentElement.scrollTop < 50){
        document.getElementById("navbar").style.height = "55px";
    }else{
        alert('Navbar Onscroll Problem');
    }
}



