# Northern Metropolis OSIRIS - Troubleshooting Guide

## Globe Not Loading

### Step 1: Check Browser Console
1. Open Developer Tools (F12 or Right-click → Inspect)
2. Go to Console tab
3. Look for error messages

### Step 2: Common Issues & Solutions

#### Issue: "THREE is not defined"
**Solution:** Three.js library failed to load
```html
<!-- Ensure this is in your HTML head -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
```

#### Issue: "OrbitControls is not defined"
**Solution:** OrbitControls library failed to load
```html
<!-- Ensure this is in your HTML head -->
<script src="https://cdn.jsdelivr.net/npm/three@r128/examples/js/controls/OrbitControls.js"></script>
```

#### Issue: "Canvas element not found"
**Solution:** Canvas element missing or wrong ID
```html
<!-- Ensure this exists in your HTML body -->
<canvas id="globe-canvas"></canvas>
```

#### Issue: WebGL not supported
**Solution:** Browser doesn't support WebGL
- Try a different browser (Chrome, Firefox, Safari)
- Update your graphics drivers
- Check if WebGL is enabled in browser settings

### Step 3: Test WebGL Support

Add this to your HTML to test WebGL:
```html
<script>
function testWebGL() {
    try {
        const canvas = document.createElement('canvas');
        const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
        if (gl) {
            console.log('WebGL is supported');
            return true;
        }
    } catch(e) {
        console.error('WebGL not supported:', e);
        return false;
    }
}
testWebGL();
</script>
```

### Step 4: Check Network Requests

1. Open Developer Tools → Network tab
2. Reload page
3. Check if these files load successfully:
   - `three.min.js` (should be ~600KB)
   - `OrbitControls.js` (should be ~20KB)
   - `globe.js` (should be ~30KB)

If any show red (404 error), the CDN link is broken.

### Step 5: Check Console Logs

Look for these success messages:
```
Initializing Northern Metropolis Globe...
Globe created successfully
Northern Metropolis boundary created
Zone markers added
Globe initialized successfully
```

If you see errors instead, note the exact error message.

## Performance Issues

### Globe is Slow/Laggy

**Solution 1: Reduce Star Count**
In `globe.js`, find `createStarfield()`:
```javascript
const starCount = 500;  // Reduce from 1000
```

**Solution 2: Reduce Sphere Complexity**
In `globe.js`, find `createGlobe()`:
```javascript
const geometry = new THREE.SphereGeometry(1, 32, 32);  // Reduce from 64, 64
```

**Solution 3: Disable Auto-Rotate**
In `globe.js`, find `setupControls()`:
```javascript
this.controls.autoRotate = false;  // Keep disabled
```

**Solution 4: Lower Renderer Quality**
In `globe.js`, find `setupScene()`:
```javascript
this.renderer.setPixelRatio(1);  // Reduce from window.devicePixelRatio
```

## UI Not Showing

### Panels are Hidden

**Solution:** Check CSS z-index
```css
.ui-panel {
    z-index: 100;  /* Should be higher than canvas */
}
```

### Buttons Not Working

**Solution:** Check if elements exist
```javascript
const btn = document.getElementById('btn-globe');
if (btn) {
    btn.addEventListener('click', () => console.log('Clicked'));
}
```

## KPI Metrics Not Updating

**Solution:** Check if elements exist
```javascript
const el = document.getElementById('kpi-renewable');
if (el) {
    el.textContent = '45';
}
```

## API Connection Issues

### Cannot Connect to Backend

**Solution 1: Check API URL**
In `globe.js`, verify:
```javascript
const API_BASE = 'http://localhost:3000';  // or your API URL
```

**Solution 2: Enable CORS**
In `server.js`, ensure CORS is enabled:
```javascript
app.use(cors());
```

**Solution 3: Check Network Tab**
- Open Developer Tools → Network
- Look for API requests
- Check response status (should be 200)

## Mobile Issues

### Touch Controls Not Working

**Solution:** Ensure OrbitControls supports touch
```javascript
this.controls.enableZoom = true;
this.controls.enablePan = true;
```

### UI Too Small on Mobile

**Solution:** Add viewport meta tag
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

## Hosting Issues

### 404 Error When Accessing

**Solution 1: Check File Paths**
```
✓ index.html
✓ globe.js
✓ server.js (if using Node.js)
```

**Solution 2: Check Web Server Configuration**
```nginx
location /northern-metropolis/ {
    root /var/www;
    index index.html;
}
```

### CORS Errors

**Solution:** Add CORS headers
```nginx
add_header 'Access-Control-Allow-Origin' '*';
add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
```

## Browser-Specific Issues

### Chrome/Edge
- Usually works best
- Check if hardware acceleration is enabled
- Settings → Advanced → System

### Firefox
- May need to enable WebGL
- about:config → webgl.disabled = false

### Safari
- May need `-webkit-` prefixes
- Check if WebGL is enabled
- Preferences → Advanced → Show Develop menu

## Getting Help

### Collect Debug Information

1. **Browser & Version**
   ```javascript
   console.log(navigator.userAgent);
   ```

2. **WebGL Info**
   ```javascript
   const canvas = document.createElement('canvas');
   const gl = canvas.getContext('webgl');
   console.log(gl.getParameter(gl.VERSION));
   ```

3. **Console Errors**
   - Screenshot of console errors
   - Full error message and stack trace

4. **Network Requests**
   - Screenshot of Network tab
   - Which files failed to load

### Report Issues

Include:
- Browser and version
- Operating system
- Console error messages
- Network tab screenshot
- Steps to reproduce

## Quick Fixes Checklist

- [ ] Three.js library loaded (check Network tab)
- [ ] OrbitControls library loaded
- [ ] Canvas element exists with id="globe-canvas"
- [ ] WebGL is supported (test with code above)
- [ ] No console errors
- [ ] globe.js file loaded successfully
- [ ] Browser is up to date
- [ ] Hardware acceleration enabled
- [ ] JavaScript is enabled

## Still Having Issues?

1. **Clear Cache**
   - Ctrl+Shift+Delete (or Cmd+Shift+Delete on Mac)
   - Clear all cache
   - Reload page

2. **Try Different Browser**
   - Chrome, Firefox, Safari, Edge
   - See if issue persists

3. **Check Console Logs**
   - Look for specific error messages
   - Search for error message online
   - Check Three.js documentation

4. **Test Locally**
   ```bash
   cd web/
   npm install
   npm start
   # Open http://localhost:3000
   ```

5. **Contact Support**
   - Provide all debug information
   - Include screenshots
   - Describe steps to reproduce

---

**Last Updated:** 2026-05-27
**Version:** 1.0.0
