import json
import random
import datetime
from typing import Dict, List, Tuple

class CampusAIPromotion:
    """校园AI产品推广模拟器"""
    
    def __init__(self, product_name: str):
        self.product_name = product_name
        self.core_users = []
        self.feedbacks = []
        self.activity_log = []
        
    def generate_content_with_ai(self, topic: str) -> str:
        """使用AI生成内容脚本（模拟）"""
        ai_templates = [
            f"大家好！今天为大家介绍{self.product_name}，这是一款强大的AI工具，能够帮助您快速完成创意工作。",
            f"校园AI工具推荐：{self.product_name}，通过简单的操作即可生成专业级内容，提升学习工作效率。",
            f"【AI工具教程】如何使用{self.product_name}进行创作？本期视频将带您快速上手这款神器。"
        ]
        script = random.choice(ai_templates)
        self.log_activity(f"AI生成内容脚本 - 主题：{topic}")
        return script
    
    def publish_content(self, platform: str, content: str) -> bool:
        """发布内容到指定平台"""
        platforms = {
            "公众号": "文章发布成功",
            "视频号": "视频发布成功",
            "社群": "社群消息发送成功"
        }
        
        if platform in platforms:
            self.log_activity(f"在{platform}发布内容")
            print(f"[{platform}] {content[:50]}...")
            return True
        return False
    
    def promote_in_group(self, member_count: int) -> Tuple[int, List[str]]:
        """在社群中进行推广，返回转化用户和核心用户列表"""
        print(f"\n开始在{member_count}人的社群中进行推广...")
        
        # 模拟社群互动
        base_conversion = int(member_count * 0.1)  # 10%基础转化率
        random_factor = random.randint(-5, 15)     # 随机因素
        converted = max(5, base_conversion + random_factor)
        
        # 生成核心用户
        self.core_users = [f"user_{i:03d}" for i in range(converted)]
        
        self.log_activity(f"社群推广完成，转化{converted}名核心用户")
        print(f"✅ 成功转化 {converted} 名核心用户体验{self.product_name}")
        
        return converted, self.core_users
    
    def collect_feedback(self, user_count: int) -> List[Dict]:
        """收集用户反馈"""
        print(f"\n开始收集用户反馈...")
        
        feedback_types = [
            {"type": "功能建议", "content": "希望增加更多模板"},
            {"type": "体验优化", "content": "界面可以更简洁一些"},
            {"type": "性能反馈", "content": "生成速度很快，效果不错"},
            {"type": "bug报告", "content": "偶尔会出现保存失败的情况"}
        ]
        
        self.feedbacks = []
        for i in range(user_count):
            feedback = random.choice(feedback_types).copy()
            feedback["user"] = f"user_{i:03d}"
            feedback["timestamp"] = datetime.datetime.now().isoformat()
            self.feedbacks.append(feedback)
            
        self.log_activity(f"收集到{len(self.feedbacks)}份用户反馈")
        print(f"📝 收集到 {len(self.feedbacks)} 份产品反馈")
        
        return self.feedbacks
    
    def analyze_results(self) -> Dict:
        """分析推广结果"""
        print(f"\n=== 推广效果分析 ===")
        
        # 计算社群活跃度提升（模拟）
        activity_improvement = 20 + random.randint(0, 10)
        
        results = {
            "product_name": self.product_name,
            "core_users": len(self.core_users),
            "feedbacks": len(self.feedbacks),
            "activity_improvement": f"{activity_improvement}%",
            "promotion_date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "feedback_types": {}
        }
        
        # 统计反馈类型
        for fb in self.feedbacks:
            fb_type = fb["type"]
            results["feedback_types"][fb_type] = results["feedback_types"].get(fb_type, 0) + 1
        
        # 打印结果
        print(f"产品名称: {results['product_name']}")
        print(f"核心用户数: {results['core_users']}人")
        print(f"收集反馈: {results['feedbacks']}份")
        print(f"社群活跃度提升: {results['activity_improvement']}")
        print(f"反馈类型分布: {json.dumps(results['feedback_types'], ensure_ascii=False)}")
        
        return results
    
    def log_activity(self, activity: str):
        """记录活动日志"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.activity_log.append(f"[{timestamp}] {activity}")
    
    def save_report(self, filename: str = "promotion_report.json"):
        """保存推广报告"""
        report = {
            "summary": self.analyze_results(),
            "feedbacks": self.feedbacks,
            "activity_log": self.activity_log[-10:],  # 最近10条日志
            "generated_at": datetime.datetime.now().isoformat()
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print(f"\n📊 推广报告已保存至 {filename}")

def main():
    """主函数 - 模拟校园AI产品推广流程"""
    print("=" * 50)
    print("校园AI产品推广模拟器")
    print("=" * 50)
    
    # 初始化推广项目
    promotion = CampusAIPromotion("AI绘图工具")
    
    # 第一阶段：内容创作与发布
    print("\n🎬 第一阶段：内容创作与发布")
    script = promotion.generate_content_with_ai("AI工具介绍")
    promotion.publish_content("公众号", script)
    promotion.publish_content("视频号", script)
    
    # 第二阶段：社群推广
    print("\n👥 第二阶段：社群推广")
    converted_users, core_users = promotion.promote_in_group(800)
    
    # 第三阶段：反馈收集
    print("\n💬 第三阶段：反馈收集")
    feedback_count = min(40, converted_users // 5)  # 从转化用户中收集反馈
    feedbacks = promotion.collect_feedback(feedback_count)
    
    # 第四阶段：结果分析与报告
    print("\n📈 第四阶段：结果分析")
    results = promotion.analyze_results()
    
    # 保存详细报告
    promotion.save_report()
    
    print("\n" + "=" * 50)
    print("✅ 校园AI产品推广模拟完成！")
    print("=" * 50)

if __name__ == "__main__":
    main()