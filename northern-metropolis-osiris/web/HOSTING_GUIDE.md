# Northern Metropolis OSIRIS - Web Hosting Guide

Complete instructions for hosting the interactive globe visualization on atmospheres.hk

## Quick Links

- **Live Demo:** https://atmospheres.hk/northern-metropolis/
- **GitHub Repository:** https://github.com/JonRodgers/Northern-Metropolis
- **API Documentation:** See main README.md

## Option 1: Static File Hosting (Simplest)

### Requirements
- Web server (Nginx, Apache, or similar)
- HTTPS certificate (recommended)
- FTP/SFTP access

### Steps

1. **Prepare Files**
   ```bash
   # Copy these files to your web server:
   - index.html
   - globe.js
   ```

2. **Upload to Server**
   ```bash
   # Using SCP
   scp index.html user@atmospheres.hk:/var/www/northern-metropolis/
   scp globe.js user@atmospheres.hk:/var/www/northern-metropolis/
   ```

3. **Configure Web Server (Nginx)**
   ```nginx
   server {
       listen 443 ssl http2;
       server_name atmospheres.hk;
       
       ssl_certificate /etc/ssl/certs/atmospheres.hk.crt;
       ssl_certificate_key /etc/ssl/private/atmospheres.hk.key;
       
       location /northern-metropolis/ {
           root /var/www;
           index index.html;
           
           # Enable CORS
           add_header 'Access-Control-Allow-Origin' '*';
           add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
           
           # Cache control
           expires 1h;
           add_header Cache-Control "public, max-age=3600";
           
           # Gzip compression
           gzip on;
           gzip_types text/html text/css application/javascript;
       }
   }
   ```

4. **Access**
   ```
   https://atmospheres.hk/northern-metropolis/
   ```

## Option 2: Node.js Server (Recommended)

### Requirements
- Node.js 14+ installed
- npm or yarn
- Port 3000 available (or configure different port)

### Steps

1. **Install Dependencies**
   ```bash
   cd web/
   npm install
   ```

2. **Start Server**
   ```bash
   npm start
   # Server runs on http://localhost:3000
   ```

3. **Production Deployment with PM2**
   ```bash
   # Install PM2 globally
   npm install -g pm2
   
   # Start with PM2
   pm2 start server.js --name "nm-osiris-web"
   
   # Save PM2 configuration
   pm2 save
   
   # Enable startup on reboot
   pm2 startup
   ```

4. **Configure Reverse Proxy (Nginx)**
   ```nginx
   server {
       listen 443 ssl http2;
       server_name atmospheres.hk;
       
       ssl_certificate /etc/ssl/certs/atmospheres.hk.crt;
       ssl_certificate_key /etc/ssl/private/atmospheres.hk.key;
       
       location /northern-metropolis/ {
           proxy_pass http://localhost:3000/;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection 'upgrade';
           proxy_set_header Host $host;
           proxy_cache_bypass $http_upgrade;
           
           # CORS headers
           add_header 'Access-Control-Allow-Origin' '*';
           add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
       }
   }
   ```

5. **Access**
   ```
   https://atmospheres.hk/northern-metropolis/
   ```

## Option 3: Docker Container

### Requirements
- Docker installed
- Docker Compose (optional)

### Steps

1. **Create Dockerfile**
   ```dockerfile
   FROM node:16-alpine
   
   WORKDIR /app
   
   COPY package*.json ./
   RUN npm install --production
   
   COPY . .
   
   EXPOSE 3000
   
   CMD ["npm", "start"]
   ```

2. **Build Image**
   ```bash
   docker build -t nm-osiris-web:latest .
   ```

3. **Run Container**
   ```bash
   docker run -d \
     --name nm-osiris-web \
     -p 3000:3000 \
     -e NODE_ENV=production \
     nm-osiris-web:latest
   ```

4. **Docker Compose (Optional)**
   ```yaml
   version: '3.8'
   
   services:
     web:
       build: .
       ports:
         - "3000:3000"
       environment:
         - NODE_ENV=production
       restart: unless-stopped
   ```

   ```bash
   docker-compose up -d
   ```

## Option 4: Cloud Hosting

### Vercel (Recommended for Static)

1. **Push to GitHub**
   ```bash
   git push origin main
   ```

2. **Connect to Vercel**
   - Visit https://vercel.com
   - Import repository
   - Deploy

3. **Custom Domain**
   - Add CNAME record: `northern-metropolis.atmospheres.hk`
   - Configure in Vercel dashboard

### Netlify

1. **Deploy**
   ```bash
   npm install -g netlify-cli
   netlify deploy --prod
   ```

2. **Configure Domain**
   - Add DNS records
   - Enable HTTPS

### AWS S3 + CloudFront

1. **Upload to S3**
   ```bash
   aws s3 sync . s3://northern-metropolis-osiris/
   ```

2. **Create CloudFront Distribution**
   - Origin: S3 bucket
   - Domain: northern-metropolis.atmospheres.hk
   - Enable HTTPS

## Configuration

### Environment Variables

Create `.env` file:
```env
NODE_ENV=production
PORT=3000
HOST=0.0.0.0
API_URL=https://api.northern-metropolis.local
CORS_ORIGIN=https://atmospheres.hk
```

### API Integration

Update `globe.js` to connect to backend:

```javascript
const API_BASE = 'https://api.northern-metropolis.local';

async function fetchKPIData() {
    try {
        const response = await fetch(`${API_BASE}/api/v1/analytics/health`);
        const data = await response.json();
        
        // Update KPI displays
        document.getElementById('kpi-renewable').textContent = 
            Math.round(data.energy.renewable_percentage);
        document.getElementById('kpi-green').textContent = 
            Math.round(data.environmental.green_space_percentage);
        document.getElementById('kpi-aqi').textContent = 
            Math.round(data.air_quality.average_aqi);
        document.getElementById('kpi-sustainability').textContent = 
            Math.round(data.sustainability_score);
    } catch (error) {
        console.error('Failed to fetch KPI data:', error);
    }
}

// Update every 5 seconds
setInterval(fetchKPIData, 5000);
```

## SSL/HTTPS Setup

### Let's Encrypt (Free)

```bash
# Install Certbot
sudo apt-get install certbot python3-certbot-nginx

# Generate certificate
sudo certbot certonly --nginx -d atmospheres.hk

# Auto-renewal
sudo systemctl enable certbot.timer
sudo systemctl start certbot.timer
```

### Manual Certificate

```bash
# Copy certificate files
sudo cp /path/to/cert.pem /etc/ssl/certs/atmospheres.hk.crt
sudo cp /path/to/key.pem /etc/ssl/private/atmospheres.hk.key

# Set permissions
sudo chmod 644 /etc/ssl/certs/atmospheres.hk.crt
sudo chmod 600 /etc/ssl/private/atmospheres.hk.key
```

## Performance Optimization

### Enable Gzip Compression

```nginx
gzip on;
gzip_vary on;
gzip_min_length 1000;
gzip_types text/plain text/css text/xml text/javascript 
           application/x-javascript application/xml+rss 
           application/javascript application/json;
```

### Browser Caching

```nginx
location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}

location ~* \.(html)$ {
    expires 1h;
    add_header Cache-Control "public, must-revalidate";
}
```

### CDN Integration

```nginx
# Use CloudFlare or similar CDN
# Add CNAME: northern-metropolis.atmospheres.hk -> cdn.example.com
```

## Monitoring & Logging

### Access Logs

```nginx
access_log /var/log/nginx/northern-metropolis-access.log;
error_log /var/log/nginx/northern-metropolis-error.log;
```

### Application Monitoring

```bash
# Monitor Node.js process
pm2 monit

# View logs
pm2 logs nm-osiris-web

# Health check
curl https://atmospheres.hk/northern-metropolis/health
```

## Troubleshooting

### 404 Errors

```bash
# Check file permissions
ls -la /var/www/northern-metropolis/

# Verify Nginx configuration
sudo nginx -t

# Reload Nginx
sudo systemctl reload nginx
```

### CORS Issues

```nginx
# Add CORS headers
add_header 'Access-Control-Allow-Origin' '*' always;
add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS' always;
add_header 'Access-Control-Allow-Headers' 'Content-Type' always;

if ($request_method = 'OPTIONS') {
    return 204;
}
```

### Performance Issues

```bash
# Check server resources
top
free -h
df -h

# Monitor Nginx
sudo systemctl status nginx
```

## Backup & Recovery

### Backup Files

```bash
# Backup web files
tar -czf nm-osiris-web-backup.tar.gz /var/www/northern-metropolis/

# Upload to S3
aws s3 cp nm-osiris-web-backup.tar.gz s3://backups/
```

### Restore Files

```bash
# Download from S3
aws s3 cp s3://backups/nm-osiris-web-backup.tar.gz .

# Extract
tar -xzf nm-osiris-web-backup.tar.gz -C /var/www/
```

## Security Checklist

- [ ] HTTPS enabled with valid certificate
- [ ] CORS properly configured
- [ ] Input validation implemented
- [ ] Rate limiting enabled
- [ ] Security headers set
- [ ] Regular backups scheduled
- [ ] Monitoring and alerts configured
- [ ] Access logs reviewed regularly
- [ ] Dependencies kept up to date
- [ ] Firewall rules configured

## Maintenance

### Regular Updates

```bash
# Update Node.js packages
npm update

# Check for vulnerabilities
npm audit

# Fix vulnerabilities
npm audit fix
```

### Log Rotation

```bash
# Configure logrotate
sudo nano /etc/logrotate.d/northern-metropolis

# Content:
/var/log/nginx/northern-metropolis-*.log {
    daily
    rotate 14
    compress
    delaycompress
    notifempty
    create 0640 www-data adm
    sharedscripts
    postrotate
        systemctl reload nginx > /dev/null 2>&1 || true
    endscript
}
```

## Support

For issues or questions:
1. Check logs: `pm2 logs nm-osiris-web`
2. Test connectivity: `curl https://atmospheres.hk/northern-metropolis/`
3. Review browser console for errors
4. Contact development team

## Additional Resources

- [Three.js Documentation](https://threejs.org/docs/)
- [Express.js Guide](https://expressjs.com/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Node.js Best Practices](https://nodejs.org/en/docs/guides/)

---

**Version:** 1.0.0  
**Last Updated:** 2026-05-27  
**Status:** Production Ready ✅
