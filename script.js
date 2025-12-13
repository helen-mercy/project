const lowbtn=document.getElementById("low");
const r=document.getElementById("reset");
const upbtn=document.getElementById("up");

let count=0;

upbtn.onclick=function(){
    count++;
    countl.textContent=count;
}
lowbtn.onclick=function(){
    count--;
    countl.textContent=count;
}
r.onclick=function(){
    count= 0;
    countl.textContent=count;
}