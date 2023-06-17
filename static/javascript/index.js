// Get all the navigation links
const navLinks = document.querySelectorAll('.nav-link');

// Function to handle click event
function handleNavLinkClick(event) {
  // Remove active class from all navigation links
  navLinks.forEach(link => {
    link.classList.remove('active');
  });

  // Add active class to the clicked navigation link
  event.target.classList.add('active');
}

// Add click event listener to each navigation link
navLinks.forEach(link => {
  link.addEventListener('click', handleNavLinkClick);
});
