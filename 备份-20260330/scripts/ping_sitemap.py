import requests
import sys

# 配置您的站点地图地址
SITEMAP_URL = "https://www.aichatx.com.cn/sitemap.xml"

def ping_bing():
    """向 Bing 发送 Sitemap 更新通知"""
    url = f"https://www.bing.com/ping?sitemap={SITEMAP_URL}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("✅ Bing 通知成功！")
        else:
            print(f"❌ Bing 通知失败，状态码: {response.status_code}")
    except Exception as e:
        print(f"❌ Bing 连接错误: {e}")

def main():
    print(f"正在通知搜索引擎更新: {SITEMAP_URL}")
    print("-" * 30)
    
    # 1. Ping Bing
    ping_bing()
    
    # 2. Google 说明
    print("-" * 30)
    print("ℹ️  Google 说明: Google 已于 2023 年停止支持 Sitemap Ping 接口。")
    print("   请确保您的 Sitemap 已提交至 Google Search Console，Google 会定期自动抓取。")
    
    # 3. Baidu 说明
    print("-" * 30)
    print("ℹ️  百度 说明: 百度需要使用 API 主动推送或在站长平台手动提交。")
    print("   建议登录 https://ziyuan.baidu.com/ 获取推送 API 密钥。")

if __name__ == "__main__":
    main()
