#!/usr/bin/env python
"""
測試正確的 Google Maps URL 格式
"""

def test_google_maps_urls():
    """測試各種 Google Maps URL 格式"""
    print("=== Google Maps URL 格式測試 ===")
    
    # 正確的 Google Maps URL 格式示例
    examples = [
        {
            "name": "Tokyo Skytree",
            "address": "1-1-2 Oshiage, Sumida City, Tokyo 131-0045, Japan",
            "correct_url": "https://www.google.com/maps/search/?api=1&query=Tokyo+Skytree+1-1-2+Oshiage+Sumida+City+Tokyo+131-0045+Japan"
        },
        {
            "name": "Senso-ji Temple",
            "address": "2-3-1 Asakusa, Taito City, Tokyo 111-0032, Japan",
            "correct_url": "https://www.google.com/maps/search/?api=1&query=Senso-ji+Temple+2-3-1+Asakusa+Taito+City+Tokyo+111-0032+Japan"
        },
        {
            "name": "Meiji Shrine",
            "address": "1-1 Kamizono-cho, Shibuya City, Tokyo 150-0001, Japan",
            "correct_url": "https://www.google.com/maps/search/?api=1&query=Meiji+Shrine+1-1+Kamizono-cho+Shibuya+City+Tokyo+150-0001+Japan"
        },
        {
            "name": "Tsukiji Outer Market",
            "address": "4 Chome Tsukiji, Chuo City, Tokyo 104-0045, Japan",
            "correct_url": "https://www.google.com/maps/search/?api=1&query=Tsukiji+Outer+Market+4+Chome+Tsukiji+Chuo+City+Tokyo+104-0045+Japan"
        }
    ]
    
    print("✅ 正確的 Google Maps URL 格式:")
    print("基本格式: https://www.google.com/maps/search/?api=1&query=[Location+Name]+[Full+Address]")
    print()
    
    for i, example in enumerate(examples, 1):
        print(f"{i}. {example['name']}")
        print(f"   地址: {example['address']}")
        print(f"   正確URL: {example['correct_url']}")
        print()
    
    print("🔧 URL 格式規則:")
    print("1. 使用 https://www.google.com/maps/search/?api=1&query=")
    print("2. 所有空格用 + 替換")
    print("3. 包含完整的地點名稱和地址")
    print("4. 避免使用特殊字符")
    print()
    
    print("❌ 錯誤格式示例:")
    print("- https://maps.google.com/maps?q=Tokyo+Skytree (舊格式)")
    print("- https://goo.gl/maps/... (短網址)")
    print("- 缺少 api=1 參數的網址")
    print()
    
    print("✅ 建議的 AI 指令格式:")
    print('為每個地點提供 Google Maps URL，格式為:')
    print('Google Maps: https://www.google.com/maps/search/?api=1&query=[地點名稱]+[完整地址]')
    print('所有空格用+替換，包含完整地址信息')

def generate_url(name, address):
    """生成正確的 Google Maps URL"""
    # 清理並格式化名稱和地址
    clean_name = name.replace(' ', '+').replace(',', '').replace('(', '').replace(')', '')
    clean_address = address.replace(' ', '+').replace(',', '+').replace('(', '').replace(')', '')
    
    url = f"https://www.google.com/maps/search/?api=1&query={clean_name}+{clean_address}"
    return url

if __name__ == "__main__":
    test_google_maps_urls()
    
    print("\n=== URL 生成測試 ===")
    test_locations = [
        ("Tokyo Station", "1-9-1 Marunouchi, Chiyoda City, Tokyo 100-0005, Japan"),
        ("Shibuya Crossing", "Shibuya City, Tokyo, Japan")
    ]
    
    for name, address in test_locations:
        url = generate_url(name, address)
        print(f"{name}: {url}")