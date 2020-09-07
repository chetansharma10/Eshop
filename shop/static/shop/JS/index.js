//For Slider

var one=document.querySelector('.one');
var child1=document.querySelector('.child1');
var child2=document.querySelector('.child2');
var child3=document.querySelector('.child3');
var two=document.querySelector('.two');
var three=document.querySelector('.three');

one.addEventListener('click',()=>{
  
 child1.style.transform="translateX(0px)";
 child2.style.transform="translateX(2020px)";
 child3.style.transform="translateX(2000px)";
 child1.style.transition="1s ease";
 child2.style.transition="1s ease";
 child3.style.transition="1s ease";




});

two.addEventListener('click',()=>{
  
  child1.style.transform="translateX(2020px)";
  child2.style.transform="translateX(0px)";
  child3.style.transform="translateX(2020px)";
  child1.style.transition="1s ease";
  child2.style.transition="1s ease";
  child3.style.transition="1s ease";
   


});

three.addEventListener('click',()=>{
  child1.style.transform="translateX(2020px)";
  child2.style.transform="translateX(2020px)";
  child3.style.transform="translateX(0px)";
  child1.style.transition="1s ease";
  child2.style.transition="1s ease";
  child3.style.transition="1s ease";
   


});



//For Products
var next=document.querySelector('.btn1');
var prev=document.querySelector('.btn2');

var box=document.querySelector('.box');
var max_length=window.box.scrollWidth/2;
var min_length=0;

window.next.addEventListener('click',()=>{
  if(min_length<=max_length){
    min_length=min_length+100;
    window.box.scrollLeft=min_length;


  }


});
prev.addEventListener('click',()=>{
  window.box.style.transition="1s ease";
  

  window.box.scrollLeft=0;
  min_length=0;
  


});

