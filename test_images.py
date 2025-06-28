#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试图片URL可访问性
"""

import requests
import time
from config import CHARACTERS

def test_image_url(url):
    """测试单个图片URL是否可访问"""
    try:
        response = requests.head(url, timeout=10)
        if response.status_code == 200:
            return True, "✅ 可访问"
        else:
            return False, f"❌ HTTP {response.status_code}"
    except requests.exceptions.RequestException as e:
        return False, f"❌ 连接失败: {str(e)}"

def main():
    """主函数"""
    print("🖼️ 测试蔚蓝档案角色图片URL可访问性\n")
    
    total_urls = 0
    accessible_urls = 0
    
    for rarity, data in CHARACTERS.items():
        print(f"\n{rarity}角色:")
        print("-" * 30)
        
        for character in data["角色"]:
            name = character["名称"]
            url = character["图片"]
            total_urls += 1
            
            print(f"测试 {name}: {url}")
            is_accessible, message = test_image_url(url)
            print(f"  {message}")
            
            if is_accessible:
                accessible_urls += 1
            
            # 避免请求过于频繁
            time.sleep(0.5)
    
    print(f"\n📊 测试结果:")
    print(f"总URL数: {total_urls}")
    print(f"可访问: {accessible_urls}")
    print(f"不可访问: {total_urls - accessible_urls}")
    print(f"成功率: {(accessible_urls/total_urls)*100:.1f}%")

if __name__ == "__main__":
    main() 