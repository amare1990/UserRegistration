const navLinks = document.querySelectorAll('.nav-link');

function handleNavLinkClick(event) {
  navLinks.forEach(link => {
    link.classList.remove('active');
  });

  event.target.classList.add('active');
}

navLinks.forEach(link => {
  link.addEventListener('click', handleNavLinkClick);
});
