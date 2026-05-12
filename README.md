# New Territories STEM

A modern, mobile-first educational website for Science, Technology, Engineering, and Mathematics (STEM) programs offered by New Territories ESF.

## 🎯 Features

- **Mobile-First Design**: Optimized for mobile devices, tablets, and desktop screens
- **Responsive Layout**: Breakpoints at 768px (tablet) and 1024px (desktop)
- **Cross-Browser Compatible**: Works on all modern browsers and mobile platforms
- **Accessibility**: Semantic HTML, keyboard navigation support, respects `prefers-reduced-motion`
- **No Dependencies**: Pure HTML, CSS, and JavaScript—no frameworks required
- **Fast Loading**: Minified assets and system fonts for optimal performance
- **Interactive Elements**: Mobile menu toggle, smooth scrolling, form validation
- **JotForm Integration**: Booking system powered by JotForm (https://www.atmospheres.hk/booking-1)

## 📱 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile Safari (iOS 12+)
- Chrome Mobile (Android 8+)
- Samsung Internet (12+)

## 🏗️ Responsive Breakpoints

| Breakpoint | Device | Width |
|-----------|--------|-------|
| Mobile | Phone | 320px - 767px |
| Tablet | iPad, etc. | 768px - 1023px |
| Desktop | Monitor | 1024px+ |

## 📂 File Structure

```
STEM/
├── index.html              # Main website (production)
├── styles.css              # Minified responsive CSS
├── script.js               # Minified interactive JavaScript
├── README.md               # This file
├── NT-STEM.md              # Project documentation
├── atmospheres.md          # Atmospheres project notes
└── NEW-TERRITORIES-ESF-Arc.md  # Architecture notes
```

## 🚀 Getting Started

### Local Development

1. Clone this repository or download the files
2. Open `index.html` in your web browser
3. No build process or installation required!

### Customization

#### Change Colors
Edit the CSS variables in `styles.css`:
```css
:root {
    --primary-color: #0066cc;
    --secondary-color: #ff6b35;
    --accent-color: #00d9ff;
    /* ... more colors ... */
}
```

#### Add New Sections
Add new `<section>` elements to `index.html` and corresponding CSS in `styles.css`.

#### Update Content
- Edit course information in the pathways section
- Update team member information
- Modify program details in the programs table
- Update social links in the footer

## 📋 Booking System

The booking system is powered by **JotForm** for simplicity and reliability:
- **Booking Form**: https://www.atmospheres.hk/booking-1
- No backend server required
- Automatic email notifications
- Form responses stored securely in JotForm

## 🌐 Deployment

### GitHub Pages
This repository is configured for GitHub Pages deployment.

### Other Hosting Platforms

**Netlify**
1. Connect your GitHub repository to Netlify
2. Set build command: (leave empty)
3. Set publish directory: `/` (root)
4. Deploy!

**Vercel**
1. Import your repository into Vercel
2. No configuration needed
3. Deploy!

**Traditional Web Hosting**
1. Upload all files to your web server
2. Ensure `index.html`, `styles.css`, and `script.js` are in the root directory
3. Access via your domain

## ♿ Accessibility

- Semantic HTML5 elements
- Keyboard navigation support
- Focus states on interactive elements
- Color contrast ratios meet WCAG AA standards
- Respects `prefers-reduced-motion` system setting

## 📊 Performance

- No external dependencies
- Minified CSS and JavaScript
- System fonts (no web font loading required)
- Optimized for Core Web Vitals
- Fast First Contentful Paint (FCP)

## 🛠️ Technologies Used

- **HTML5**: Semantic markup
- **CSS3**: Flexbox, Grid, Media Queries, CSS Variables
- **JavaScript (ES6)**: Vanilla JavaScript, no frameworks
- **JotForm**: Booking form management

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📧 Contact

For questions or support, please open an issue on GitHub or contact New Territories ESF directly.

---

**Created with ❤️ for STEM educators and learners**
