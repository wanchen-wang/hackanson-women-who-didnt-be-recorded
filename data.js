// 数据存储
const data = {
    locations: [
        {
            id: 1,
            name: "陶然亭公园",
            address: "西城区太平街19号",
            order: 1,
            story: "在陶然亭公园，许多伟大的女性曾在此思考人生...",
            people: "待补充",
            gameType: "待补充",
            collectItems: []
        },
        {
            id: 2,
            name: "陕西巷（八大胡同之一）",
            address: "西城区陕西巷",
            order: 2,
            distance: "2公里",
            story: "陕西巷见证了北京古城的风云变幻...",
            people: "待补充",
            gameType: "待补充",
            collectItems: []
        },
        {
            id: 3,
            name: "前门大街",
            address: "东城区小江胡同1号",
            order: 3,
            distance: "1.3公里",
            story: "前门大街是老北京的象征...",
            people: "待补充",
            gameType: "待补充",
            collectItems: []
        },
        {
            id: 4,
            name: "北平高等师范学校旧址",
            address: "西城区大栅栏街道南新华街18号",
            order: 4,
            distance: "1.3公里",
            story: "这里培养了一代代的教育者...",
            people: "待补充",
            gameType: "待补充",
            collectItems: []
        },
        {
            id: 5,
            name: "女师大旧址（京师女子师范学堂）",
            address: "西城区新文化街45号",
            order: 5,
            distance: "1.8公里",
            story: "京师女子师范学堂是中国第一所女性教育机构...",
            people: "待补充",
            gameType: "待补充",
            collectItems: []
        }
    ],
    routes: [
        {
            from: "陶然亭公园",
            to: "陕西巷（八大胡同之一）",
            distance: "2公里",
            method: "步行/地铁",
            time: "约30分钟"
        },
        {
            from: "陕西巷（八大胡同之一）",
            to: "前门大街",
            distance: "1.3公里",
            method: "步行/地铁",
            time: "约15分钟"
        },
        {
            from: "前门大街",
            to: "北平高等师范学校旧址",
            distance: "1.3公里",
            method: "步行/地铁",
            time: "约15分钟"
        },
        {
            from: "北平高等师范学校旧址",
            to: "女师大旧址",
            distance: "1.8公里",
            method: "步行/地铁",
            time: "约25分钟"
        }
    ],
    collectItems: [
        {
            id: 1,
            name: "书籍",
            icon: "📚",
            people: "待补充"
        },
        {
            id: 2,
            name: "笔",
            icon: "✒️",
            people: "待补充"
        },
        {
            id: 3,
            name: "照片",
            icon: "📷",
            people: "待补充"
        }
    ],
    posts: [
        {
            user: "用户名",
            content: "这个故事让我印象深刻..."
        }
    ],
    categories: {
        "凤骨丹心": {
            story: "凤骨丹心的故事...",
            locations: [],
            collectItems: []
        },
        "错位芳华": {
            story: "错位芳华的故事...",
            locations: data.locations,
            collectItems: []
        },
        "舞台之上": {
            story: "舞台之上的故事...",
            locations: [],
            collectItems: []
        }
    }
};

// 初始化分类数据
data.categories["错位芳华"].locations = data.locations;
data.categories["错位芳华"].collectItems = data.collectItems;

// 用于存储地理编码结果的缓存
const coordinatesCache = {
    "陶然亭公园": { lat: 39.9382, lng: 116.3694 },
    "陕西巷（八大胡同之一）": { lat: 39.9013, lng: 116.4033 },
    "前门大街": { lat: 39.9004, lng: 116.4067 },
    "北平高等师范学校旧址": { lat: 39.9245, lng: 116.3892 },
    "女师大旧址（京师女子师范学堂）": { lat: 39.9238, lng: 116.3899 }
};
