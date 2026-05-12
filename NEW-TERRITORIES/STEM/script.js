/* ============================================
   New Territories STEM - Main JavaScript
   Interactive functionality and user experience
   ============================================ */

document.addEventListener('DOMContentLoaded', function() {
    
    /* ============================================
       1. MOBILE MENU TOGGLE
       ============================================ */
    
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (menuToggle) {
        // Toggle menu when hamburger button is clicked
        menuToggle.addEventListener('click', function() {
            this.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
        
        // Close menu when a navigation link is clicked
        const navLinks = document.querySelectorAll('.nav-menu a');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                menuToggle.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });
        
        // Close menu when Escape key is pressed
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape') {
                menuToggle.classList.remove('active');
                navMenu.classList.remove('active');
            }
        });
    }
    
    /* ============================================
       2. SMOOTH SCROLLING FOR ANCHOR LINKS
       ============================================ */
    
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // Only prevent default if the target exists
            if (href !== '#' && document.querySelector(href)) {
                e.preventDefault();
                
                const targetElement = document.querySelector(href);
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    /* ============================================
       3. ACTIVE NAVIGATION HIGHLIGHTING
       ============================================ */
    
    function updateActiveNavigation() {
        const sections = document.querySelectorAll('section');
        const navLinks = document.querySelectorAll('.nav-menu a');
        
        let currentSection = '';
        
        // Find which section is currently in view
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            
            if (window.pageYOffset >= sectionTop - 100) {
                currentSection = section.getAttribute('id');
            }
        });
        
        // Update active state on navigation links
        navLinks.forEach(link => {
            link.classList.remove('active');
            
            if (link.getAttribute('href') === '#' + currentSection) {
                link.classList.add('active');
            }
        });
    }
    
    // Update active nav on scroll
    window.addEventListener('scroll', updateActiveNavigation);
    
    // Initial call to set active nav on page load
    updateActiveNavigation();
    
    /* ============================================
       4. CTA BUTTON - SCROLL TO BOOKING
       ============================================ */
    
    const ctaButtons = document.querySelectorAll('.cta-button');
    ctaButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Only handle internal scroll, not external links
            const href = this.getAttribute('href');
            if (href && href.startsWith('#')) {
                e.preventDefault();
                const targetElement = document.querySelector(href);
                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
    
    /* ============================================
       5. FORM VALIDATION (if contact form exists)
       ============================================ */
    
    const contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form inputs
            const nameInput = document.getElementById('name');
            const emailInput = document.getElementById('email');
            const messageInput = document.getElementById('message');
            
            // Get values and trim whitespace
            const name = nameInput ? nameInput.value.trim() : '';
            const email = emailInput ? emailInput.value.trim() : '';
            const message = messageInput ? messageInput.value.trim() : '';
            
            // Validate name
            if (!name) {
                alert('Please enter your name');
                if (nameInput) nameInput.focus();
                return;
            }
            
            // Validate email
            if (!email) {
                alert('Please enter your email');
                if (emailInput) emailInput.focus();
                return;
            }
            
            // Validate email format
            if (!isValidEmail(email)) {
                alert('Please enter a valid email address');
                if (emailInput) emailInput.focus();
                return;
            }
            
            // Validate message
            if (!message) {
                alert('Please enter a message');
                if (messageInput) messageInput.focus();
                return;
            }
            
            // If all validation passes, show success message
            alert('Thank you for your message! We will get back to you soon.');
            contactForm.reset();
        });
    }
    
    /* ============================================
       6. EMAIL VALIDATION HELPER
       ============================================ */
    
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
    
    /* ============================================
       7. HOVER EFFECTS ON CARDS
       ============================================ */
    
    const cards = document.querySelectorAll('.card, .tutor-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.cursor = 'pointer';
        });
    });
    
    /* ============================================
       8. CONSOLE LOG - CONFIRMATION
       ============================================ */
    
    console.log('✓ New Territories STEM - Website loaded successfully!');
    console.log('✓ All interactive features are active');
    
});

/* ============================================
   9. UTILITY FUNCTIONS (Outside DOMContentLoaded)
   ============================================ */

/**
 * Smooth scroll to element
 * @param {string} elementId - The ID of the element to scroll to
 */
function scrollToElement(elementId) {
    const element = document.querySelector('#' + elementId);
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

/**
 * Toggle class on element
 * @param {string} elementSelector - CSS selector for the element
 * @param {string} className - Class name to toggle
 */
function toggleClass(elementSelector, className) {
    const element = document.querySelector(elementSelector);
    if (element) {
        element.classList.toggle(className);
    }
}

/**
 * Add class to element
 * @param {string} elementSelector - CSS selector for the element
 * @param {string} className - Class name to add
 */
function addClass(elementSelector, className) {
    const element = document.querySelector(elementSelector);
    if (element) {
        element.classList.add(className);
    }
}

/**
 * Remove class from element
 * @param {string} elementSelector - CSS selector for the element
 * @param {string} className - Class name to remove
 */
function removeClass(elementSelector, className) {
    const element = document.querySelector(elementSelector);
    if (element) {
        element.classList.remove(className);
    }
}
