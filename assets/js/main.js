let navButtonEl = document.querySelector('.hamburger');
let bodyEl = document.querySelector('body');

if (navButtonEl && bodyEl) {
  navButtonEl.addEventListener('click', () => {
    bodyEl.classList.toggle('nav-active');
  });
}
