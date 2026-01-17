# 未被书写的她 - 手机应用

一个北京古建筑风格的手机应用，展示伟大女性的故事和游览路线。

## 项目结构

```
MAGA/
├── index.html              # 主HTML文件（所有页面）
├── styles.css              # 样式表（北京古建筑配色）
├── app.js                  # 前端逻辑
├── data.js                 # 前端数据
├── app.py                  # Python后端（Flask）
├── image.png               # 背景图片
├── 路线1地址 - Sheet1.csv  # 地点数据
├── requirements.txt        # Python依赖
└── data/                   # 数据存储目录
    ├── users.json          # 用户数据
    └── posts.json          # 帖子数据
```

## 功能说明

### 前端页面

1. **首页（Page 1）**
   - 竖立标语："未被书写的她，由你续写"
   - 背景为伟大女性照片
   - 点击任意位置进入登陆界面

2. **登陆界面（Page 2）**
   - 用户名和密码输入
   - 支持自动注册

3. **分类菜单（Page 3）**
   - APP名称："未被书写的她"
   - 三个分类按钮：
     - 凤骨丹心
     - 错位芳华
     - 舞台之上

4. **分类详情页（Page 4）**
   - 返回按钮
   - 主线故事概要
   - "游览路线"和"待收集品"按钮
   - 收集品图标预览

5. **游览路线（Page 5）**
   - 百度地图展示
   - 地点标记（可点击查看详情）
   - 路线连接线和箭头（可点击查看路线信息）
   - 弹框显示地点/路线详细信息

6. **待收集品（Page 6）**
   - 收集品图标（可点击查看详情）
   - 用户发言帖子列表

### 后端API

#### 用户管理
- `POST /api/login` - 用户登陆/注册
- `GET /api/user/<user_id>` - 获取用户信息

#### 地点管理
- `GET /api/locations` - 获取所有地点
- `GET /api/location/<location_name>` - 获取单个地点

#### 帖子管理
- `GET /api/posts` - 获取所有帖子
- `POST /api/posts` - 发布新帖子
- `POST /api/posts/<post_id>/like` - 点赞帖子

#### 收集品管理
- `GET /api/user/<user_id>/collected` - 获取用户已收集物品
- `POST /api/user/<user_id>/collected` - 添加收集品

#### 地理编码
- `POST /api/geocode` - 获取地点坐标

## 安装运行

### 前置要求
- Python 3.7+
- 现代浏览器（支持ES6）
- 百度地图API密钥（已配置）

### 安装依赖
```bash
pip install -r requirements.txt
```

### 启动应用
```bash
python app.py
```

然后在浏览器中打开：
```
http://localhost:5000
```

## 配置说明

### 百度地图API
- 密钥已配置在 `index.html` 中
- 不做域名限制

### 数据源
- 地点数据从 `路线1地址 - Sheet1.csv` 读取
- 用户数据保存在 `data/users.json`
- 帖子数据保存在 `data/posts.json`

## 颜色配置

所有颜色遵循北京古建筑风格：

```
--primary-red: #C60C30      /* 宫廷红 */
--gold-color: #DAA520       /* 金色 */
--dark-brown: #8B6F47       /* 深棕色 */
--light-beige: #F5DEB3      /* 浅米色 */
--dark-bg: #2C2C2C          /* 深灰背景 */
```

## 后续功能扩展

1. **完善故事内容**
   - 补充每个地点的故事梗概、历史人物、游戏类型

2. **添加收集品**
   - 为每个地点添加可收集物品
   - 上传收集品图标

3. **增加数据库**
   - 从JSON迁移到SQL数据库（MySQL/PostgreSQL）

4. **用户认证**
   - 集成JWT令牌认证
   - 密码加密存储

5. **移动优化**
   - 适配各种屏幕尺寸
   - 离线模式支持

## 文件说明

### index.html
- 定义了所有6个页面的HTML结构
- 引入了百度地图API
- 引入了前端脚本和样式

### styles.css
- 响应式设计
- 北京古建筑配色主题
- 按钮、弹框、地图等组件样式

### app.js
- 页面导航逻辑
- 弹框显示/隐藏
- 地图初始化和交互
- 事件监听

### data.js
- 前端数据存储
- 地点信息、路线、收集品等
- 百度地图坐标缓存

### app.py
- Flask应用主文件
- 所有API端点定义
- JSON文件读写操作
- CSV数据导入

## 常见问题

**Q: 如何添加新的故事分类？**
A: 在 `data.js` 中修改 `data.categories` 对象，添加新分类及其对应数据。

**Q: 地图不显示？**
A: 检查百度地图API密钥是否正确，以及网络连接。

**Q: 如何修改配色？**
A: 在 `styles.css` 中修改 `:root` 中定义的CSS变量。

**Q: 如何添加更多地点？**
A: 编辑 `路线1地址 - Sheet1.csv` 文件，添加新行数据。

## 联系方式

如有问题，请联系开发者。

---

**祝您使用愉快！**
