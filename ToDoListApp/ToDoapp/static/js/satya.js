let p = document.querySelectorAll('.a')
let form = document.querySelectorAll('.c')
let tasks = document.querySelectorAll('.t')

console.log(p)

p.forEach((val,index)=>{
if (val.innerText=='Completed'){
    form[index].remove()
    tasks[index].classList.add('text-decoration-line-through')
}
})