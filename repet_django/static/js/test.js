const slides = document.querySelectorAll('.question-slide');
let currentSlide = 0;

function showSlide(index) {
  slides.forEach((slide, i) => {
    slide.classList.remove('active');
    if (i === index) {
      slide.classList.add('active');
    }
  });
  document.querySelector('.prev').style.display = index === 0 ? 'none' : 'inline-block';
  document.querySelector('.next').style.display = index === slides.length - 1 ? 'none' : 'inline-block';
  document.querySelector('form button[type="submit"]').style.display = index === slides.length - 1 ? 'block' : 'none';
}

function nextSlide() {
  if (currentSlide < slides.length - 1) {
    currentSlide++;
    showSlide(currentSlide);
  }
}

function prevSlide() {
  if (currentSlide > 0) {
    currentSlide--;
    showSlide(currentSlide);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  showSlide(currentSlide);
});