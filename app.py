from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime
import csv

app = Flask(__name__)
CORS(app)

# 数据存储目录
DATA_DIR = 'data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# 用户数据文件
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
POSTS_FILE = os.path.join(DATA_DIR, 'posts.json')

# 初始化数据文件
def init_data_files():
    """初始化JSON数据文件"""
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False)
    
    if not os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False)

# 读取用户数据
def load_users():
    """加载所有用户"""
    try:
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

# 保存用户数据
def save_users(users):
    """保存用户数据"""
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

# 读取帖子数据
def load_posts():
    """加载所有帖子"""
    try:
        with open(POSTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

# 保存帖子数据
def save_posts(posts):
    """保存帖子数据"""
    with open(POSTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

# ==================== 路由 ====================

@app.route('/')
def index():
    """主页"""
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def send_page(filename):
    """提供HTML页面和静态文件"""
    try:
        if filename.endswith('.html'):
            return send_from_directory('.', filename)
        elif filename in ['common.css', 'image.png']:
            return send_from_directory('.', filename)
        else:
            return send_from_directory('.', filename)
    except:
        return '404 - 文件不存在', 404

@app.route('/api/login', methods=['POST'])
def login():
    """用户登陆/注册"""
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'success': False, 'message': '用户名或密码不能为空'})
    
    users = load_users()
    
    if username in users:
        if users[username]['password'] == password:
            return jsonify({
                'success': True,
                'message': '登陆成功',
                'user_id': username
            })
        else:
            return jsonify({'success': False, 'message': '密码错误'})
    else:
        # 自动注册
        users[username] = {
            'password': password,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'collected_items': []
        }
        save_users(users)
        return jsonify({
            'success': True,
            'message': '注册成功',
            'user_id': username
        })

@app.route('/api/user/<user_id>', methods=['GET'])
def get_user(user_id):
    """获取用户信息"""
    users = load_users()
    
    if user_id in users:
        user = users[user_id]
        return jsonify({
            'success': True,
            'user_id': user_id,
            'created_at': user.get('created_at'),
            'collected_items': user.get('collected_items', [])
        })
    else:
        return jsonify({'success': False, 'message': '用户不存在'}), 404

@app.route('/api/posts', methods=['GET'])
def get_posts():
    """获取所有帖子"""
    posts = load_posts()
    return jsonify({
        'success': True,
        'posts': posts,
        'count': len(posts)
    })

@app.route('/api/posts', methods=['POST'])
def create_post():
    """创建新帖子"""
    data = request.json
    username = data.get('username')
    content = data.get('content')
    
    if not username or not content:
        return jsonify({'success': False, 'message': '用户名或内容不能为空'})
    
    posts = load_posts()
    new_post = {
        'id': len(posts) + 1,
        'username': username,
        'content': content,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'likes': 0
    }
    
    posts.append(new_post)
    save_posts(posts)
    
    return jsonify({
        'success': True,
        'message': '发布成功',
        'post': new_post
    })

@app.route('/api/posts/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
    """点赞帖子"""
    posts = load_posts()
    
    for post in posts:
        if post.get('id') == post_id:
            post['likes'] = post.get('likes', 0) + 1
            save_posts(posts)
            return jsonify({
                'success': True,
                'message': '点赞成功',
                'likes': post['likes']
            })
    
    return jsonify({'success': False, 'message': '帖子不存在'}), 404

@app.route('/api/user/<user_id>/collected', methods=['GET'])
def get_collected_items(user_id):
    """获取用户收集的物品"""
    users = load_users()
    
    if user_id in users:
        items = users[user_id].get('collected_items', [])
        return jsonify({
            'success': True,
            'user_id': user_id,
            'items': items,
            'count': len(items)
        })
    else:
        return jsonify({'success': False, 'message': '用户不存在'}), 404

@app.route('/api/user/<user_id>/collected', methods=['POST'])
def add_collected_item(user_id):
    """添加收集物品"""
    users = load_users()
    data = request.json
    item_name = data.get('item_name')
    
    if user_id not in users:
        return jsonify({'success': False, 'message': '用户不存在'}), 404
    
    if item_name not in users[user_id]['collected_items']:
        users[user_id]['collected_items'].append(item_name)
        save_users(users)
        return jsonify({
            'success': True,
            'message': '收集成功',
            'collected_items': users[user_id]['collected_items']
        })
    else:
        return jsonify({'success': False, 'message': '已收集过此物品'})

@app.route('/api/locations', methods=['GET'])
def get_locations():
    """获取所有地点"""
    locations = [
        {
            'id': 1,
            'name': '陶然亭公园',
            'address': '西城区太平街19号',
            'lat': 39.8806,
            'lng': 116.3885
        },
        {
            'id': 2,
            'name': '陕西巷',
            'address': '西城区陕西巷',
            'lat': 39.9013,
            'lng': 116.4033
        },
        {
            'id': 3,
            'name': '前门大街',
            'address': '东城区小江胡同1号',
            'lat': 39.9004,
            'lng': 116.4067
        },
        {
            'id': 4,
            'name': '北平高等师范学校旧址',
            'address': '西城区大栅栏街道南新华街18号',
            'lat': 39.9245,
            'lng': 116.3892
        },
        {
            'id': 5,
            'name': '女师大旧址',
            'address': '西城区新文化街45号',
            'lat': 39.9238,
            'lng': 116.3899
        }
    ]
    
    return jsonify({
        'success': True,
        'locations': locations,
        'count': len(locations)
    })

@app.route('/api/location/<location_name>', methods=['GET'])
def get_location(location_name):
    """获取单个地点详情"""
    locations = [
        {
            'id': 1,
            'name': '陶然亭公园',
            'address': '西城区太平街19号',
            'lat': 39.8806,
            'lng': 116.3885,
            'story': '陶然亭公园是一个文化底蕴深厚的地方...'
        },
        {
            'id': 2,
            'name': '陕西巷',
            'address': '西城区陕西巷',
            'lat': 39.9013,
            'lng': 116.4033,
            'story': '陕西巷是北京八大胡同之一...'
        }
    ]
    
    for location in locations:
        if location['name'] == location_name:
            return jsonify({
                'success': True,
                'location': location
            })
    
    return jsonify({'success': False, 'message': '地点不存在'}), 404

# ==================== 错误处理 ====================

@app.errorhandler(404)
def not_found(error):
    return jsonify({'success': False, 'message': '资源不存在'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'success': False, 'message': '服务器错误'}), 500

# ==================== 启动应用 ====================

if __name__ == '__main__':
    init_data_files()
    print("应用启动成功！")
    print("访问地址：http://127.0.0.1:5000")
    app.run(debug=True, host='127.0.0.1', port=5000)
