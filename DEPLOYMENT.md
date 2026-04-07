# HongJun Website 部署配置

## 域名配置

### 主域名
- **主域名**: hongjunshuke.com
- **二级域名**: www.hongjunshuke.com

### DNS 配置

在你的域名DNS服务商（如阿里云、腾讯云、Cloudflare等）添加以下记录：

```
类型    主机记录    记录值                          TTL
A       @           [你的服务器IP地址]            600
A       www         [你的服务器IP地址]            600
```

如果使用Cloudflare或其他CDN：
```
类型    主机记录    记录值                          代理状态
A       @           [你的服务器IP地址]            已代理（橙色云朵）
A       www         [你的服务器IP地址]            已代理（橙色云朵）
```

## 服务器部署

### 1. 上传文件到服务器
将以下文件上传到服务器网站根目录：
- index.html
- config.js
- products.json
- sitemap.xml
- robots.txt
- _headers (用于Netlify，或其他服务器配置)
- images/ (整个文件夹)

### 2. Nginx 配置示例

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name www.hongjunshuke.com hongjunshuke.com;

    # 重定向到 www
    if ($host = 'hongjunshuke.com') {
        return 301 https://www.hongjunshuke.com$request_uri;
    }

    # HTTPS 重定向
    return 301 https://www.hongjunshuke.com$request_uri;
}

server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name www.hongjunshuke.com;

    # SSL 证书配置
    ssl_certificate /path/to/ssl/cert.pem;
    ssl_certificate_key /path/to/ssl/key.pem;

    # SSL 优化配置
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    # 网站根目录
    root /var/www/hongjunshuke.com;
    index index.html;

    # 静态文件缓存
    location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # Gzip 压缩
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml;

    # 安全头
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;

    # 主域名重定向
    location = / {
        try_files $uri $uri/ /index.html;
    }
}
```

### 3. Apache 配置示例

```apache
<VirtualHost *:80>
    ServerName hongjunshuke.com
    Redirect permanent / https://www.hongjunshuke.com/
</VirtualHost>

<VirtualHost *:443>
    ServerName www.hongjunshuke.com
    DocumentRoot /var/www/hongjunshuke.com
    
    # SSL 配置
    SSLEngine on
    SSLCertificateFile /path/to/ssl/cert.pem
    SSLCertificateKeyFile /path/to/ssl/key.pem

    # 启用 Gzip
    <IfModule mod_deflate.c>
        AddOutputFilterByType DEFLATE text/html text/plain text/xml text/css text/javascript application/javascript
    </IfModule>

    # 静态文件缓存
    <IfModule mod_expires.c>
        ExpiresActive On
        ExpiresByType image/jpg "access plus 1 year"
        ExpiresByType image/jpeg "access plus 1 year"
        ExpiresByType image/gif "access plus 1 year"
        ExpiresByType image/png "access plus 1 year"
        ExpiresByType text/css "access plus 1 year"
        ExpiresByType application/javascript "access plus 1 year"
    </IfModule>

    <Directory /var/www/hongjunshuke.com>
        Options -Indexes +FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
```

### 4. 静态托管平台部署

#### Netlify
1. 连接 GitHub 仓库或拖拽文件夹上传
2. 构建设置：
   - 构建命令: (留空)
   - 发布目录: (留空，使用根目录)
3. 添加域名: `www.hongjunshuke.com`
4. Netlify 自动配置 HTTPS 和重定向

#### Vercel
1. 安装 Vercel CLI: `npm i -g vercel`
2. 在项目目录运行: `vercel`
3. 在 Vercel 控制台添加自定义域名: `www.hongjunshuke.com`

#### Cloudflare Pages
1. 连接 GitHub 仓库或直接上传
2. 构建设置:
   - 构建命令: (留空)
   - 输出目录: (留空)
3. 添加自定义域名并配置 DNS

## SSL 证书配置

### 使用 Let's Encrypt (免费)

```bash
# 安装 Certbot
sudo apt-get install certbot python3-certbot-nginx

# 自动获取并配置证书
sudo certbot --nginx -d www.hongjunshuke.com -d hongjunshuke.com

# 自动续期
sudo certbot renew --dry-run
```

### 使用 Cloudflare SSL
1. 在 Cloudflare 控制台的 SSL/TLS 设置中，选择"Full"模式
2. Cloudflare 会自动提供免费 SSL 证书

## 性能优化

### 1. 图片优化
- 使用 WebP 格式（已有jpg，可考虑添加webp版本）
- 图片已添加 `loading="lazy"` 属性
- 考虑使用 CDN 加速图片加载

### 2. 资源压缩
- 已配置 Gzip 压缩
- CSS 和 JS 已内联（无外部依赖）

### 3. CDN 配置
建议使用 CDN 加速静态资源：
- Cloudflare（免费）
- 阿里云 CDN
- 腾讯云 CDN

## 安全配置

### 1. HTTPS 强制跳转
已配置主域名 `hongjunshuke.com` 重定向到 `www.hongjunshuke.com`

### 2. 安全头
```nginx
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
```

### 3. 文件权限
```bash
# 设置正确的文件权限
chmod 644 index.html config.js products.json sitemap.xml robots.txt
chmod 755 images/
chmod 644 images/*.jpg images/*.mp4
```

## SEO 配置

### 1. 提交站点地图
- Google Search Console: `https://www.hongjunshuke.com/sitemap.xml`
- Bing Webmaster Tools: `https://www.hongjunshuke.com/sitemap.xml`

### 2. 百度站长平台
- 添加网站并验证
- 提交 Sitemap
- 设置自动推送

### 3. 搜索引擎收录
- Google: https://search.google.com/search-console
- Bing: https://www.bing.com/webmasters
- 百度: https://ziyuan.baidu.com/

## 监控与分析

### 1. 添加统计代码（可选）
在 `</head>` 前添加：
```html
<!-- 百度统计 -->
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?YOUR_TRACKING_ID";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>

<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### 2. 性能监控
- Google PageSpeed Insights
- GTmetrix
- Lighthouse

## 联系信息更新

如需更新联系方式，请修改 `config.js` 文件：

```javascript
contact: {
  email: 'your-email@domain.com',
  phone: '+86 XXXX XXXX XXXX',
  whatsapp: '+86 XXXX XXXX XXXX',
  wechat: 'your-wechat-id',
  telegram: 'your-telegram'
}
```

## EmailJS 配置

表单提交使用 EmailJS 服务，如需更改，请修改 `config.js`：

```javascript
emailjs: {
  serviceId: 'your-service-id',
  templateId: 'your-template-id',
  publicKey: 'your-public-key'
}
```

参考文档: `EMAILJS-SETUP.md`

## 备份与维护

### 定期备份
```bash
# 创建备份脚本
#!/bin/bash
DATE=$(date +%Y%m%d)
tar -czf backup-$DATE.tar.gz /var/www/hongjunshuke.com
```

### 日志监控
```bash
# Nginx 访问日志
tail -f /var/log/nginx/access.log

# Nginx 错误日志
tail -f /var/log/nginx/error.log
```

## 故障排查

### 常见问题

1. **图片无法加载**
   - 检查图片路径是否正确
   - 检查文件夹权限
   - 查看 Nginx/Apache 错误日志

2. **表单无法提交**
   - 检查 EmailJS 配置
   - 查看浏览器控制台错误
   - 参考 `EMAILJS-SETUP.md`

3. **SEO 不生效**
   - 确认 sitemap.xml 可访问
   - 提交到搜索引擎站长平台
   - 等待搜索引擎收录（通常1-2周）

4. **HTTPS 证书过期**
   - 运行 `sudo certbot renew`
   - 检查自动续期配置

## 联系支持

如有问题，请联系：
- 开发团队: [开发人员联系方式]
- 文档更新: 2026-04-07
