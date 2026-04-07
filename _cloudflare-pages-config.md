# Cloudflare Pages 配置指南

## 快速部署到 Cloudflare Pages

### 方法 1: 通过 Git 集成自动部署

1. **登录 Cloudflare Dashboard**
   - 访问: https://dash.cloudflare.com/
   - 进入 Workers & Pages > Pages

2. **连接到 GitHub**
   - 点击 "Create a project"
   - 选择 "Connect to Git"
   - 授权 GitHub 账户
   - 选择 `MissionWang/inquiry-website` 仓库

3. **配置构建设置**
   ```
   Build command: (留空，静态网站无需构建)
   Build output directory: /
   Root directory: (留空)
   ```

4. **环境变量（可选）**
   ```
   EMAILJS_PUBLIC_KEY: your_emailjs_public_key
   EMAILJS_SERVICE_ID: your_emailjs_service_id
   EMAILJS_TEMPLATE_ID: your_emailjs_template_id
   ```

5. **部署**
   - 点击 "Save and Deploy"
   - Cloudflare 会自动部署到全球 CDN
   - 获得 `*.pages.dev` 域名

---

## 方法 2: 直接上传部署

### 使用 Wrangler CLI

1. **安装 Wrangler**
   ```bash
   npm install -g wrangler
   ```

2. **登录**
   ```bash
   wrangler login
   ```

3. **部署项目**
   ```bash
   cd d:/workspace/inquiry-website
   wrangler pages deploy . --project-name=hongjun-website
   ```

---

## Cloudflare 优化配置

### 1. Speed 优化（极速加载）

#### Auto Minify
在 Cloudflare Dashboard > Speed > Optimization:
- [x] Auto Minify HTML
- [x] Auto Minify CSS
- [x] Auto Minify JavaScript

#### Brotli 压缩
在 Cloudflare Dashboard > Speed > Optimization:
- [x] Enable Brotli（比 Gzip 效率高 15-20%）

#### Rocket Loader
在 Cloudflare Dashboard > Speed > Optimization:
- [x] Enable Rocket Loader（提升 JS 页面加载速度）

---

### 2. Image Optimization（图片优化）

#### Polish（图片压缩）
在 Cloudflare Dashboard > Speed > Optimization:
- [x] Enable Polish
- [x] Mode: Lossy
- [x] WebP: Enable（自动转换为 WebP 格式）

#### Resizing（响应式图片）
在 Cloudflare Dashboard > Speed > Optimization:
- [x] Enable Image Resizing
- 配置响应式图片规则

---

### 3. Performance（性能优化）

#### Cache Rules（缓存规则）
在 Cloudflare Dashboard > Rules > Cache Rules:
```
规则 1: 静态资源缓存
- 字段: URL Path
- 值: *.(jpg|jpeg|png|gif|webp|svg|css|js|woff2)
- 操作: Cache Level: Cache Everything
- 操作: Browser Cache TTL: 1 year
- 操作: Edge Cache TTL: 1 month

规则 2: HTML 页面
- 字段: URL Path
- 值: *.html
- 操作: Cache Level: Standard
- 操作: Browser Cache TTL: 4 hours
- 操作: Edge Cache TTL: 2 hours
```

---

### 4. Security（安全配置）

#### Firewall Rules（防火墙规则）
在 Cloudflare Dashboard > Security > WAF > Custom Rules:
```
规则 1: 阻止恶意爬虫
- 字段: User Agent
- 值: *bot* AND NOT *Googlebot* AND NOT *Bingbot*
- 操作: Block

规则 2: 限制频繁请求
- 字段: Request Count
- 值: > 100 per minute
- 操作: Challenge
```

---

### 5. Page Rules（页面规则）

#### 域名重定向（hongjunshuke.com → www.hongjunshuke.com）
在 Cloudflare Dashboard > Rules > Page Rules:
```
规则 1: 主域名到二级域名重定向
- URL pattern: hongjunshuke.com/*
- 设置: Forwarding URL (301)
- 目标: https://www.hongjunshuke.com/$1
```

#### HTTPS 强制
```
规则 2: 强制 HTTPS
- URL pattern: *hongjunshuke.com/*
- 设置: Always Use HTTPS: On
```

---

### 6. Custom Domain（自定义域名）

#### 添加域名
1. 在 Cloudflare Dashboard > Pages > hongjun-website > Custom Domains
2. 点击 "Set up a custom domain"
3. 输入 `www.hongjunshuke.com`
4. 按照提示配置 DNS 记录：
   ```
   类型: CNAME
   名称: www
   目标: hongjun-website.pages.dev
   Proxy: 已启用（橙色云朵）
   ```

#### DNS 配置
在 Cloudflare DNS 中添加：
```
类型: CNAME
名称: www
目标: hongjun-website.pages.dev
代理状态: 已启用（Proxied）

类型: A
名称: @
目标: (留空或指向你的服务器 IP)
代理状态: 已启用
```

---

## 性能优化检查清单

### Core Web Vitals（核心网页指标）

#### Largest Contentful Paint (LCP) < 2.5s
- [x] 启用 Brotli 压缩
- [x] 图片转换为 WebP
- [x] 使用 CDN（Cloudflare 全球网络）
- [x] 启用图片懒加载
- [ ] 添加图片 width/height 属性

#### First Input Delay (FID) < 100ms
- [x] 启用 Rocket Loader
- [x] Minify JavaScript
- [ ] 优化第三方脚本（EmailJS）

#### Cumulative Layout Shift (CLS) < 0.1
- [ ] 添加图片 width/height 属性
- [ ] 优化字体加载
- [ ] 预留广告/图片空间

---

## 监控和分析

### Cloudflare Web Analytics
1. 在 Cloudflare Dashboard > Analytics & Logs > Web Analytics
2. 点击 "Add a site"
3. 输入 `www.hongjunshuke.com`
4. 复制以下代码到 `index.html` 的 `<head>` 中：
```html
<script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "YOUR_TOKEN"}'></script>
```

### Cloudflare Speed Page
访问: https://www.cloudflare.com/speed-test/
测试 `www.hongjunshuke.com` 的全球加载速度

---

## 成本估算

### Cloudflare Free Plan（免费版）
✅ 无限带宽
✅ 无限请求
✅ 全球 CDN
✅ SSL/TLS 证书
✅ DDoS 防护
✅ 基本缓存规则
❌ 图片优化（需 Pro 计划）

### Cloudflare Pro Plan（$20/月）
✅ 所有免费功能
✅ 图片优化（Polish + WebP）
✅ 高级缓存规则
✅ 图像调整大小
✅ 优先支持

### 建议
- 开发阶段：使用 Free Plan
- 生产环境：升级到 Pro Plan 以启用图片优化

---

## 常见问题

### Q: 如何清除缓存？
**A**: 在 Cloudflare Dashboard > Caching > Configuration > Purge Everything

### Q: 图片为什么不转换为 WebP？
**A**: Free Plan 不支持 WebP 转换，需要升级到 Pro Plan

### Q: 如何查看缓存命中率？
**A**: 在 Cloudflare Dashboard > Analytics > Cache

### Q: 如何测试全球加载速度？
**A**: 使用 Cloudflare Speed Page 或 GTmetrix.com

---

## 故障排查

### 问题: 页面无法访问
**检查**:
1. DNS 记录是否正确
2. SSL/TLS 模式是否为 Full
3. Page Rules 是否冲突

### 问题: 图片不显示
**检查**:
1. 图片路径是否正确
2. 文件名大小写是否匹配
3. 浏览器缓存是否清除

### 问题: 表单提交失败
**检查**:
1. EmailJS 配置是否正确
2. Service ID 和 Template ID 是否有效
3. 浏览器控制台是否有错误

---

## 下一步

1. [ ] 部署到 Cloudflare Pages
2. [ ] 配置自定义域名
3. [ ] 启用所有优化功能
4. [ ] 配置 Google Search Console
5. [ ] 配置 Google Analytics 4
6. [ ] 提交 sitemap.xml 到搜索引擎

---

**文档版本**: 1.0
**创建日期**: 2026-04-07
**Cloudflare 文档**: https://developers.cloudflare.com/pages/
