const currentYearEl = document.querySelector('#current');
const ratingEl = document.querySelectorAll('.rating');
const ratingEl1 = document.querySelectorAll('.show__rating');
const headerEl = document.getElementById('header')
const heroEl = document.querySelector('.hero')

//! Adding date on copyright text
const currentYear = new Date()
currentYearEl.textContent = currentYear.getFullYear();


//! Adding stars in testimonials cards
const html = `<ion-icon class="icon" name="star"></ion-icon>`

ratingEl.forEach(el => {
    const parent = el.closest('.ratings');
    for(let i = 1; i <= el.innerText; i++){
        parent.insertAdjacentHTML('beforeEnd', html)
    }
})

//! making navigation sticky

const navigationFun = (el) => {
    if(!el[0].isIntersecting){
        headerEl.classList.add('b-bt')
    }else{
        headerEl.classList.remove('b-bt')
    }
};

const options = {
root: null,
threshold: .1,
};
const observer = new IntersectionObserver(navigationFun, options);
observer.observe(heroEl)