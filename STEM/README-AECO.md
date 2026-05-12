# NEW TERRITORIES AECO TRAINING FOR INDUSTRY

## Professional Digital Production & AI Workflows Training Platform

A sophisticated, dark-themed professional training website for architecture, engineering, and construction (AECO) industry professionals, students, colleges, universities, and practice directors.

---

## 📋 Project Overview

This project consists of a complete professional training platform website designed with a dark theme inspired by The Gnomon Workshop's premium aesthetic. The platform showcases comprehensive training programs in digital production, BIM, computational design, and AI workflows.

### Target Audience
- **Industry Professionals**: Architects, engineers, and construction specialists
- **Students**: Aspiring professionals in AEC fields
- **Educational Institutions**: Colleges and universities
- **Practice Directors**: Leadership and organizational development
- **Digital Production Specialists**: Advanced computational design practitioners

---

## 📁 File Structure

```
STEM/
├── index2.html          # Main HTML file with embedded CSS
├── styles2.css          # External stylesheet (optional)
├── script2.js           # Interactive functionality and enhancements
└── README-AECO.md       # This documentation file
```

### File Descriptions

#### `index2.html` (1,365 lines)
Complete HTML5 document with:
- Embedded CSS styling (dark theme)
- Semantic HTML structure
- Responsive design
- All content sections
- Professional navigation and footer

**Key Sections:**
1. Header & Navigation
2. Hero Section
3. Features Section (6 feature cards)
4. Programs Section (6 training programs)
5. Industry Partnerships
6. Professional Credentials
7. Testimonials
8. Call-to-Action Section
9. Footer with contact information

#### `styles2.css` (Optional External Stylesheet)
Extracted CSS for better maintainability:
- CSS variables for theming
- Responsive breakpoints
- Animation definitions
- Component styles
- Utility classes

**Usage:** Replace embedded `<style>` tag with:
```html
<link rel="stylesheet" href="styles2.css">
```

#### `script2.js` (Interactive Enhancements)
JavaScript functionality including:
- Smooth scroll navigation
- Active navigation state tracking
- Button click handlers with ripple effects
- Scroll animations with Intersection Observer
- Form validation utilities
- Mobile menu toggle
- Lazy loading image support
- Analytics event tracking
- Scroll-to-top button
- Performance monitoring
- Keyboard navigation support

**Usage:** Add before closing `</body>` tag:
```html
<script src="script2.js"></script>
```

---

## 🎨 Design System

### Color Palette

| Variable | Color | Usage |
|----------|-------|-------|
| `--bg-primary` | #0a0e27 | Main background |
| `--bg-secondary` | #1a1f3a | Secondary background |
| `--bg-tertiary` | #252d4a | Tertiary background |
| `--accent-primary` | #00d4ff | Primary accent (Cyan) |
| `--accent-secondary` | #ff6b35 | Secondary accent (Orange) |
| `--accent-tertiary` | #4ecdc4 | Tertiary accent (Teal) |
| `--text-primary` | #ffffff | Primary text |
| `--text-secondary` | #b0b8d4 | Secondary text |
| `--text-tertiary` | #7a8299 | Tertiary text |

### Typography

- **Primary Font**: Segoe UI, Helvetica Neue, Arial (sans-serif)
- **Secondary Font**: Georgia, Times New Roman (serif)
- **Monospace Font**: Courier New

### Spacing Scale

- `--spacing-xs`: 0.5rem
- `--spacing-sm`: 1rem
- `--spacing-md`: 1.5rem
- `--spacing-lg`: 2rem
- `--spacing-xl`: 3rem
- `--spacing-xxl`: 4rem
- `--spacing-xxxl`: 6rem

### Border Radius

- `--radius-sm`: 4px
- `--radius-md`: 8px
- `--radius-lg`: 12px
- `--radius-xl`: 16px

---

## 📚 Training Programs

### 1. Digital Production Fundamentals
- **Level**: Beginner to Intermediate
- **Duration**: 8 weeks | 40 hours
- **Topics**: Revit, Rhino, Grasshopper, Visualization, Documentation

### 2. Advanced BIM & Coordination
- **Level**: Intermediate to Advanced
- **Duration**: 10 weeks | 50 hours
- **Topics**: BIM Execution, Clash Detection, Coordination, ISO 19650

### 3. Computational Design & Automation
- **Level**: Advanced
- **Duration**: 12 weeks | 60 hours
- **Topics**: Grasshopper, Generative Design, Python, Optimization

### 4. AI Workflows & Digital Innovation
- **Level**: Advanced
- **Duration**: 10 weeks | 50 hours
- **Topics**: AI Design, Machine Learning, Predictive Analytics, Digital Twins

### 5. Leadership & Practice Direction
- **Level**: Executive
- **Duration**: 6 weeks | 30 hours
- **Topics**: Digital Strategy, Team Development, Technology Implementation

### 6. Specialized Workshops
- **Level**: Flexible
- **Duration**: 2-4 weeks | 10-20 hours
- **Topics**: Dynamo, Unreal Engine, Point Clouds, Photogrammetry

---

## 🔧 Customization Guide

### Changing Colors

Edit CSS variables in the `:root` selector:

```css
:root {
    --accent-primary: #00d4ff;  /* Change this */
    --accent-secondary: #ff6b35;
    /* ... other variables ... */
}
```

### Modifying Content

All content is clearly marked with HTML comments:

```html
<!-- ============================================
     SECTION NAME
     ============================================ -->
```

Simply locate the section and edit the content within.

### Adding New Programs

Copy the program card structure:

```html
<div class="program-card">
    <div class="program-header">
        <h3>Program Name</h3>
        <div class="program-level">Level</div>
    </div>
    <div class="program-body">
        <!-- Content here -->
    </div>
</div>
```

### Responsive Breakpoints

- **Desktop**: 1400px max-width
- **Tablet**: 768px breakpoint
- **Mobile**: 480px breakpoint

---

## 🚀 Deployment

### Quick Start

1. **Copy files to your web server:**
   ```
   index2.html
   styles2.css (optional)
   script2.js (optional)
   ```

2. **Update links if using external files:**
   - Replace `<style>` tag with `<link rel="stylesheet" href="styles2.css">`
   - Add `<script src="script2.js"></script>` before `</body>`

3. **Update contact information:**
   - Email: `info@ntaeco.com`
   - Phone: `+852 1234 5678`
   - Social media links

### SEO Optimization

The file includes:
- Proper meta tags
- Semantic HTML structure
- Descriptive headings
- Alt text ready for images
- Mobile viewport configuration

### Performance Tips

1. **Minify CSS and JavaScript** for production
2. **Optimize images** before deployment
3. **Enable gzip compression** on server
4. **Use CDN** for faster delivery
5. **Implement lazy loading** for images

---

## 📱 Responsive Design

### Mobile-First Approach

The design is optimized for:
- **Mobile phones** (320px - 480px)
- **Tablets** (481px - 768px)
- **Desktops** (769px+)

### Key Responsive Features

- Flexible grid layouts
- Scalable typography
- Touch-friendly buttons
- Optimized spacing
- Readable line lengths

---

## ♿ Accessibility

The site includes:
- Semantic HTML structure
- Proper heading hierarchy
- Color contrast compliance
- Keyboard navigation support
- Focus indicators
- ARIA-ready structure

---

## 🔐 Security Considerations

Before deploying:

1. **Update contact information** with real details
2. **Implement form validation** on backend
3. **Use HTTPS** for all connections
4. **Sanitize user inputs** if adding forms
5. **Implement CSRF protection** for forms
6. **Add privacy policy** and terms of service

---

## 📊 Analytics Integration

The script includes hooks for:
- Google Analytics
- Mixpanel
- Custom event tracking
- Performance monitoring

### Example Integration

```javascript
// Google Analytics
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_ID');
</script>
```

---

## 🛠️ Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

---

## 📝 Content Management

### Updating Program Information

1. Locate the program card in the HTML
2. Update the program name, level, and duration
3. Modify the topics list
4. Update the enrollment button

### Adding Testimonials

Add new testimonial cards in the testimonials section:

```html
<div class="testimonial-card">
    <div class="testimonial-quote">"</div>
    <p class="testimonial-text">Quote text here</p>
    <div class="testimonial-author">Author Name</div>
    <div class="testimonial-role">Job Title, Company</div>
</div>
```

### Managing Partners

Update partner logos in the partnerships section:

```html
<div class="partner-logo">
    <div class="partner-name">Partner Name</div>
</div>
```

---

## 🎯 Features Checklist

- ✅ Dark theme design (Gnomon Workshop inspired)
- ✅ Responsive mobile design
- ✅ Professional navigation
- ✅ Hero section with CTAs
- ✅ Feature cards (6 items)
- ✅ Training programs (6 programs)
- ✅ Industry partnerships
- ✅ Professional credentials
- ✅ Testimonials section
- ✅ Call-to-action section
- ✅ Professional footer
- ✅ Smooth scroll animations
- ✅ Hover effects and transitions
- ✅ Keyboard navigation
- ✅ Performance optimized
- ✅ SEO ready
- ✅ Accessibility compliant

---

## 📞 Support & Contact

For questions or customization needs:

- **Email**: info@ntaeco.com
- **Phone**: +852 1234 5678
- **Website**: [Your domain]

---

## 📄 License

This project is proprietary to NEW TERRITORIES AECO TRAINING FOR INDUSTRY.

---

## 🔄 Version History

### Version 1.0 (2026-05-12)
- Initial release
- Complete HTML structure
- Dark theme design
- 6 training programs
- Responsive design
- Interactive features

---

## 🚀 Future Enhancements

Potential additions:
- [ ] Student enrollment form with backend integration
- [ ] Payment gateway integration
- [ ] Student dashboard
- [ ] Course progress tracking
- [ ] Certificate generation
- [ ] Discussion forums
- [ ] Video course integration
- [ ] Live chat support
- [ ] Mobile app
- [ ] API for third-party integrations

---

## 📚 Resources

### Design Inspiration
- The Gnomon Workshop (gnomon.edu)
- Modern dark theme best practices
- Professional SaaS design patterns

### Technologies Used
- HTML5
- CSS3 (with CSS Variables)
- Vanilla JavaScript (ES6+)
- Responsive Design
- Intersection Observer API

### Learning Resources
- [MDN Web Docs](https://developer.mozilla.org/)
- [CSS-Tricks](https://css-tricks.com/)
- [Web.dev](https://web.dev/)

---

**Last Updated**: 2026-05-12
**Created by**: NEW TERRITORIES AECO TRAINING FOR INDUSTRY
**Status**: Production Ready
