@echo off
echo ================================
echo 未被书写的她 - 应用启动
echo ================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python，请先安装Python 3.7+
    pause
    exit /b 1
)

echo [1/3] 安装Python依赖...
pip install -r requirements.txt -q

if errorlevel 1 (
    echo 错误: 安装依赖失败
    pause
    exit /b 1
)

echo [2/3] 依赖安装完成！
echo.
echo [3/3] 启动应用...
echo.
echo 应用已启动，请在浏览器中打开:
echo.
echo   http://localhost:5000
echo.
echo 按 Ctrl+C 停止应用
echo.

python app.py

pause
