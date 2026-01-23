# Event Ticketing Landing Page

A beautiful, modern landing page for your online event ticketing system.

## 🎨 Design Features

### Color Palette
- **Primary Blue**: #318CE7 - Energetic, trustworthy
- **Accent Orange**: #FF8200 - Dynamic, optimistic
- **Accent Pink**: #FF0080 - Special highlights

### Typography
- **Headers**: Urbanist (Modern, bold, clean)
- **Body**: Lato (Friendly, professional)

## 📋 Page Sections

1. **Hero Section**
   - Eye-catching headline with gradient highlight
   - Dual CTA buttons (Browse Events & Learn More)
   - Trust badges (Secure, Instant, Mobile)
   - Floating metric cards showing 2M+ customers and 50K+ events
   - Dynamic concert image with 3D perspective effect

2. **Features Section**
   - 4 key features with gradient icons
   - Easy Discovery, Instant Booking, Secure Payment, Mobile Tickets
   - Hover animations for engagement

3. **How It Works**
   - 3-step process with numbered cards
   - Browse → Book → Attend
   - Clear, simple journey visualization

4. **Featured Events**
   - 3 event cards with images
   - Date, location, and pricing information
   - "Book Now" CTAs with smooth hover effects

5. **Testimonials**
   - 3 customer reviews with star ratings
   - Dark background for contrast
   - Glassmorphism card design

6. **Final CTA**
   - Bold call-to-action section
   - Gradient background with decorative elements
   - Large "Start Exploring Events" button

7. **Footer**
   - Company info and social links
   - Multi-column navigation (Company, Support, Explore, Legal)
   - Professional dark theme

## 🚀 Access the Page

The landing page is accessible at: `/events/`

### Local Development
```bash
# The CSS is already compiled, but if you need to recompile:
npx sass static/sass/landing.scss static/css/landing.css --no-source-map

# Or use the watch mode for development:
npx sass static/sass/landing.scss static/css/landing.css --watch
```

## 🎯 Key Features

- **Fully Responsive**: Works beautifully on all devices
- **Modern Design**: 2025-ready with gradient effects, glassmorphism, and smooth animations
- **Bootstrap 5**: Built with the latest Bootstrap framework
- **Performance**: Optimized images from Pexels with proper attribution
- **Accessibility**: Semantic HTML and ARIA attributes
- **SEO Optimized**: Proper meta tags and descriptions
- **Smooth Scrolling**: Navigation with smooth scroll behavior
- **Interactive Elements**: Hover effects, transitions, and micro-interactions

## 📁 File Structure

```
static/
├── sass/
│   └── landing.scss          # Landing page styles (source)
└── css/
    └── landing.css           # Compiled CSS

templates/pages/
└── events-to-delete.html     # Landing page template

apps/dashboard/
├── views.py                  # Landing view added
└── urls.py                   # Route configured
```

## 🎨 Customization

### Colors
Edit the variables in `static/sass/landing.scss`:
```scss
$primary-blue: #318CE7;
$accent-orange: #FF8200;
$accent-pink: #FF0080;
```

### Typography
Change fonts in the SCSS file:
```scss
$heading-font: 'Urbanist', sans-serif;
$body-font: 'Lato', sans-serif;
```

### Content
Edit the HTML in `templates/pages/events-to-delete.html` to update:
- Event listings
- Testimonials
- Footer links
- Company information

## 📸 Image Credits

All stock images are from Pexels with proper attribution:
- Rahul Pandit
- Mae Gregorio
- Noland Live
- Wendy Wei

## 🔧 Tech Stack

- **Frontend**: HTML5, CSS3 (SASS), JavaScript
- **Framework**: Bootstrap 5.3
- **Icons**: Bootstrap Icons
- **Fonts**: Google Fonts (Urbanist, Lato)
- **Backend**: Django
- **Build Tool**: Webpack + Sass compiler

## 🌟 Best Practices

- Semantic HTML structure
- Mobile-first responsive design
- Optimized for performance
- Cross-browser compatible
- Accessible for all users
- SEO-friendly markup

---

**Note**: This is a standalone landing page with its own CSS. It loads Bootstrap from CDN for simplicity. If you want to integrate it with your webpack build system, add a new entry point in `webpack/common.config.js`.
