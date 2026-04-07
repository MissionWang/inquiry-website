# Logo 部署指南

## 操作步骤

### 1. 准备 Logo 文件

将你的 Logo 图片命名为 **`logo.jpg`**，并确保：
- 文件大小建议：10-50 KB
- 推荐尺寸：200x40 像素（保持 5:1 宽高比）
- 格式：JPG（透明背景请使用 PNG 并重命名为 logo.png）
- 背景：白色或透明背景

### 2. 放置 Logo 文件

将 `logo.jpg` 放到以下目录：

```
D:/workspace/inquiry-website/images/logo.jpg
```

目录结构应该是：
```
images/
├── logo.jpg          # ← 放在这里
├── products/
│   ├── product-01.jpg
│   ├── product-02.jpg
│   └── ...
└── videos/
    ├── video-1.mp4
    └── video-2.mp4
```

### 3. 代码已自动适配

网站代码已经配置好，会自动：
- ✅ 显示 Logo 图片
- ✅ 如果 Logo 加载失败，显示备用图标 "H"
- ✅ 导航栏和页脚都会显示 Logo
- ✅ SEO 结构化数据包含 Logo URL

### 4. 测试验证

部署后检查：
1. 导航栏是否显示 Logo
2. 页脚是否显示 Logo
3. 点击 Logo 是否跳转首页
4. Alt 文本是否为 "HongJun Logo"

### 5. 备用方案

如果不想用图片 Logo，当前代码已支持：
- 图片加载失败时自动降级显示文字图标
- 永远不会显示空白

---

**当前品牌配置**：
- 品牌名称: HongJun
- 域名: https://autodispenserpro.com
- 全称: HongJun Vacuum Encapsulation Technology
