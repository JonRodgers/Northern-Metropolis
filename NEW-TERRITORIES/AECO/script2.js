/* ============================================
   NEW TERRITORIES AECO TRAINING - Script2.js
   Interactive Functionality & Enhancements
   ============================================ */

// ============================================
// 1. SMOOTH SCROLL BEHAVIOR
// ============================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ============================================
// 2. NAVIGATION ACTIVE STATE
// ============================================

function updateActiveNavigation() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('nav a[href^="#"]');

    window.addEventListener('scroll', () => {
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (pageYOffset >= sectionTop - 200) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').slice(1) === current) {
                link.classList.add('active');
            }
        });
    });
}

// Initialize navigation tracking
updateActiveNavigation();

// ============================================
// 3. BUTTON CLICK HANDLERS
// ============================================

document.querySelectorAll('.btn-primary, .btn-secondary, .cta-button').forEach(button => {
    button.addEventListener('click', function(e) {
        // Add ripple effect
        const ripple = document.createElement('span');
        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;

        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        ripple.classList.add('ripple');

        this.appendChild(ripple);

        // Remove ripple after animation
        setTimeout(() => ripple.remove(), 600);

        // Log enrollment action
        console.log('Enrollment button clicked');
    });
});

// ============================================
// 4. SCROLL ANIMATIONS
// ============================================

const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe all cards and feature elements
document.querySelectorAll('.feature-card, .program-card, .credential-item, .testimonial-card, .partner-logo').forEach(el => {
    observer.observe(el);
});

// ============================================
// 5. FORM VALIDATION (for future form integration)
// ============================================

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validateForm(formData) {
    const errors = [];
    
    if (!formData.name || formData.name.trim() === '') {
        errors.push('Name is required');
    }
    
    if (!formData.email || !validateEmail(formData.email)) {
        errors.push('Valid email is required');
    }
    
    if (!formData.program || formData.program === '') {
        errors.push('Please select a program');
    }
    
    return {
        isValid: errors.length === 0,
        errors: errors
    };
}

// ============================================
// 6. MOBILE MENU TOGGLE (if needed)
// ============================================

function initMobileMenu() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('nav ul');
    
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            this.classList.toggle('active');
        });
    }
}

initMobileMenu();

// ============================================
// 7. LAZY LOADING IMAGES (for future optimization)
// ============================================

if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.add('loaded');
                observer.unobserve(img);
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// ============================================
// 8. ANALYTICS TRACKING
// ============================================

function trackEvent(eventName, eventData = {}) {
    console.log(`Event: ${eventName}`, eventData);
    
    // Integration point for Google Analytics, Mixpanel, etc.
    if (typeof gtag !== 'undefined') {
        gtag('event', eventName, eventData);
    }
}

// Track page view
trackEvent('page_view', {
    page_title: document.title,
    page_location: window.location.href
});

// Track button clicks
document.querySelectorAll('.btn-primary, .btn-secondary').forEach(button => {
    button.addEventListener('click', function() {
        trackEvent('button_click', {
            button_text: this.textContent,
            button_class: this.className
        });
    });
});

// ============================================
// 9. SCROLL TO TOP BUTTON
// ============================================

function initScrollToTop() {
    const scrollButton = document.createElement('button');
    scrollButton.id = 'scroll-to-top';
    scrollButton.innerHTML = '↑';
    scrollButton.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 50px;
        height: 50px;
        background: linear-gradient(135deg, #00d4ff 0%, #4ecdc4 100%);
        color: #0a0e27;
        border: none;
        border-radius: 50%;
        cursor: pointer;
        font-size: 24px;
        font-weight: bold;
        display: none;
        z-index: 999;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3);
        transition: all 0.3s ease;
    `;

    document.body.appendChild(scrollButton);

    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            scrollButton.style.display = 'block';
        } else {
            scrollButton.style.display = 'none';
        }
    });

    scrollButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    scrollButton.addEventListener('mouseover', () => {
        scrollButton.style.transform = 'scale(1.1)';
    });

    scrollButton.addEventListener('mouseout', () => {
        scrollButton.style.transform = 'scale(1)';
    });
}

initScrollToTop();

// ============================================
// 10. PERFORMANCE MONITORING
// ============================================

function logPerformanceMetrics() {
    if (window.performance && window.performance.timing) {
        const timing = window.performance.timing;
        const metrics = {
            pageLoadTime: timing.loadEventEnd - timing.navigationStart,
            domContentLoadedTime: timing.domContentLoadedEventEnd - timing.navigationStart,
            resourceLoadTime: timing.responseEnd - timing.fetchStart,
            domInteractiveTime: timing.domInteractive - timing.navigationStart
        };
        
        console.log('Performance Metrics:', metrics);
    }
}

window.addEventListener('load', logPerformanceMetrics);

// ============================================
// 11. KEYBOARD NAVIGATION
// ============================================

document.addEventListener('keydown', (e) => {
    // Escape key to close any modals (future implementation)
    if (e.key === 'Escape') {
        console.log('Escape key pressed');
    }
    
    // Tab key for accessibility
    if (e.key === 'Tab') {
        document.body.classList.add('keyboard-nav');
    }
});

document.addEventListener('mousedown', () => {
    document.body.classList.remove('keyboard-nav');
});

// ============================================
// 12. INITIALIZATION
// ============================================

document.addEventListener('DOMContentLoaded', () => {
    console.log('NEW TERRITORIES AECO TRAINING - Script loaded successfully');
    
    // Initialize all interactive features
    initMobileMenu();
    updateActiveNavigation();
    
    // Log initialization
    trackEvent('script_initialized', {
        timestamp: new Date().toISOString()
    });
});

// ============================================
// 13. UTILITY FUNCTIONS
// ============================================

// Debounce function for performance optimization
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Throttle function for scroll events
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Get URL parameters
function getUrlParameter(name) {
    name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
    const regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
    const results = regex.exec(location.search);
    return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
}

// ============================================
// 14. EXPORT FUNCTIONS FOR EXTERNAL USE
// ============================================

window.NTAECOTraining = {
    validateForm: validateForm,
    validateEmail: validateEmail,
    trackEvent: trackEvent,
    getUrlParameter: getUrlParameter,
    debounce: debounce,
    throttle: throttle
};
