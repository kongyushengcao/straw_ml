## 蒸汽爆破可视化页面

基于机器学习的生物质预处理预测系统，支持 6 个目标的预测。

### 预测目标
- 纤维素回收率 (Cellulose Recovery) — RF 模型
- 半纤维素脱除率 (Hemicellulose Removal) — XGBoost 模型
- 葡萄糖固相酶解 (Glucose Solid Enzymatic Hydrolysis) — XGBoost 模型
- 糠醛 (Furfural) — XGBoost 模型
- 羟甲基糠醛 (HMF) — XGBoost 模型
- 乙酸 (Acetic Acid) — XGBoost 模型

### 后端
使用 conda 环境 `straw_ml` 运行：

```bash
cd backend
conda activate straw_ml
python main.py
```

服务默认运行在 `http://localhost:8000`。

### 前端
需要提前安装 Node.js，然后在 front 文件夹下：

```bash
cd front
npm install
npm run dev
```

按住 Ctrl 点击终端输出的网址即可在浏览器中打开页面。
