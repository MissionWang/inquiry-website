# EmailJS 配置指南

## 问题: "The recipients address is empty"

这个错误是因为 EmailJS 模板中缺少接收邮箱配置。

---

## 🚀 快速解决方案 (2分钟搞定)

### 步骤 1: 登录 EmailJS
访问: https://dashboard.emailjs.com/

### 步骤 2: 编辑邮件模板
1. 点击左侧 **Email Templates**
2. 找到模板: `template_fdj773n`
3. 点击 **Edit** (编辑按钮)

### 步骤 3: 配置接收邮箱 (三选一)

#### 方法 A: 动态邮箱 (推荐)
在模板的 **To** 字段输入:
```
{{to_email}}
```
这样会自动发送到 `config.js` 中配置的邮箱。

#### 方法 B: 固定邮箱 (最简单)
直接在模板的 **To** 字段输入:
```
info@mail.hongjunshuke.com
```

#### 方法 C: 多邮箱
在模板的 **To** 字段输入多个邮箱:
```
info@mail.hongjunshuke.com, sales@mail.hongjunshuke.com
```

### 步骤 4: 保存模板
点击 **Save** 保存即可。

---

## ✅ 验证配置

完成配置后:

1. **刷新浏览器** (Ctrl+F5)
2. **填写测试表单**
3. **点击提交**
4. **检查邮箱** `info@mail.hongjunshuke.com`

---

## 📋 当前配置

### config.js
```javascript
emailjs: {
  serviceId: 'service_cyr2jg8',
  templateId: 'template_fdj773n',
  publicKey: 'loeH7DBCwJm48R2kt'
},
contact: {
  email: 'info@mail.hongjunshuke.com'
}
```

### index.html (已更新)
```javascript
var templateParams = {
  to_name: 'HongJun Sales Team',
  to_email: SITE_CONFIG.contact.email,  // ← 动态接收邮箱
  from_name: body.name,
  from_email: body.email,
  phone: body.phone || 'N/A',
  company: body.company || 'N/A',
  product_interest: body.product || 'General Inquiry',
  message: body.message,
  sent_date: new Date().toLocaleString('en-US', { timeZone: 'Asia/Shanghai' }),
  website: 'HongJun Website'
};
```

---

## 🔍 调试方法

如果还是报错:

1. 打开浏览器控制台 (F12)
2. 提交表单
3. 查看 Console 中的错误信息

已添加错误提示:
```
邮件配置错误: 需要在 EmailJS 后台设置接收邮箱
```

---

## 📧 备用方案

### 方案 A: Formspree (超简单)

```html
<form action="https://formspree.io/f/your-form-id" method="POST">
  <!-- 表单字段 -->
</form>
```

### 方案 B: EmailJS 新模板

如果现有模板有问题,可以创建新模板:

1. 在 EmailJS 点击 **Create New Template**
2. 输入模板名称: `contact_form`
3. 配置 To 字段为 `{{to_email}}`
4. 复制新模板 ID 到 `config.js`

---

## 💡 提示

- **免费账户**: 每月 200 封邮件
- **推荐邮箱**: Gmail 配置最稳定
- **响应时间**: 通常 2-5 秒

---

## ❓ 常见问题

| 错误信息 | 解决方法 |
|---------|---------|
| "The recipients address is empty" | 在 EmailJS 后台设置 To 字段 |
| "Invalid service ID" | 检查 service_cyr2jg8 是否正确 |
| "Invalid template ID" | 检查 template_fdj773n 是否正确 |
| "Public key not found" | 检查 publicKey 是否正确 |

---

## 📞 紧急联系

如果邮件功能暂时无法使用,可以在网站添加直接联系方式:

- **WhatsApp**: +86 15346172906
- **WeChat**: 13265409026
- **Email**: info@mail.hongjunshuke.com

