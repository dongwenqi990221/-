# -*- coding: utf-8 -*-
import time

print("=" * 40)
print("🌟 年龄验证系统")
print("=" * 40)

# 用户交互
name = input("请输入您的姓名：")
age = int(input("请输入您的年龄："))

if age >= 18:
    print("\n🎉 欢迎您，成年用户！")
    print("正在为您加载专属内容...")
    time.sleep(1)

    # 显示图片功能
    print("🖼️ 正在加载成年用户专属图片...")  # Changed to simulate image loading
    print("图片链接为: https://picsum.photos/600/400?grayscale")  # Print image link instead

    time.sleep(2)  # 等待图片加载
    print("✅ 专属内容加载完成！")

else:
    print("\n👶 未成年人模式启动")
    print("为您提供适合的内容...")

print("\n" + "=" * 40)
print("感谢使用！程序执行完毕。")
print("=" * 40)
time.sleep(3)
