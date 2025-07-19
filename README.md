# Mount Kenya University South Sudanese Students' Association

![QR Code](mkusssa_qr_cropped.png)

A modern, responsive landing page with QR code functionality designed to connect South Sudanese students at Mount Kenya University. This project helps students easily access the association's social media channels and community resources.

## 🌟 Features

- **Responsive Design**: Mobile-first approach with seamless experience across all devices
- **Social Media Integration**: Direct links to WhatsApp, Instagram, Facebook, and TikTok
- **High-Quality QR Code**: Generated with error correction for reliable scanning
- **Modern UI/UX**: Clean, professional design with smooth animations and transitions
- **Accessibility**: ARIA labels and semantic HTML for better accessibility
- **Fast Loading**: Optimized assets and efficient CSS

## 📋 Project Components

- **Landing Page** ([index.html](index.html)): Mobile-friendly HTML/CSS site with association information and contact links
- **QR Code Generator** ([generate_qr.py](generate_qr.py)): Python script to create a scannable QR code for the landing page
- **Dependencies** ([requirements.txt](requirements.txt)): Python packages required for QR code generation

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### QR Code Generation

1. Install required packages:

```bash
pip install -r requirements.txt
```

2. Generate the QR code:

```bash
python generate_qr.py
```

This will create `mkusssa_qr_cropped.png` with a QR code pointing to the deployed landing page.

### Local Development

Simply open [index.html](index.html) in your web browser to view the landing page locally.

## 🌐 Deployment

The landing page is live at: **[https://mkusssa.netlify.app/](https://mkusssa.netlify.app/)**

### Deploy Your Own

1. Fork this repository
2. Connect to Netlify, Vercel, or GitHub Pages
3. Deploy the repository (no build process needed)

## 🎨 Customization

### Updating Social Media Links

Edit the links in [index.html](index.html) around line 183-194:

```html
<div class="icons-grp">
  <a class="link-btn whatsapp-btn" href="YOUR_WHATSAPP_LINK">
  <a class="link-btn instagram-btn" href="YOUR_INSTAGRAM_LINK">
  <a class="link-btn facebook-btn" href="YOUR_FACEBOOK_LINK">
  <a class="link-btn tiktok-btn" href="YOUR_TIKTOK_LINK">
</div>
```

### Updating QR Code URL

Modify the URL in [generate_qr.py](generate_qr.py) line 11:

```python
qr.add_data("https://your-new-url.com/")
```

## 🛠️ Technical Details

- **Frontend**: HTML5, CSS3 with CSS Custom Properties
- **Icons**: Font Awesome 6.7.2
- **QR Code**: Python with qrcode and Pillow libraries
- **Error Correction**: High-level error correction for better scanning reliability

## 📱 Social Media Channels

- **WhatsApp**: Direct messaging for quick inquiries
- **Instagram**: [@mkusssa](https://www.instagram.com/mkusssa)
- **Facebook**: [MKU South Sudanese Students Association](https://www.facebook.com/people/MKU-South-Sudanese-Students-Association-Nairobi-Campus/61560526555617/)
- **TikTok**: [@mkusssa](https://www.tiktok.com/@mkusssa)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Contact

Connect with us through any of the social media channels linked on the landing page, or reach out via WhatsApp for immediate assistance.

---

**Made with ❤️ for the South Sudanese student community at Mount Kenya University**
