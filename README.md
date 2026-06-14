# 南光AI图像宽高互换（ComfyUI插件）

## 特性
- 交换宽度与高度值
- 提供**输入端口**（可连接上游节点）和**面板控件**（未连线时使用）
- 独立开关控制是否禁止互换
- 全中文界面

## 安装
1. 将整个文件夹 `ComfyUI_Nanguang_WH_Swap` 放入 `ComfyUI/custom_nodes/`
2. 重启 ComfyUI

## 节点使用
- **宽度 / 高度**：可连线接收值，也可直接在节点上修改
- **禁止互换**：勾选后直接输出原值；不勾选则输出互换后的宽高

## 常见问题
**Q：为什么之前没有输入端口？**  
A：旧版代码缺少 `"forceInput": True` 声明，现已修复。请替换 `node_wh_swap.py` 后重启。

**Q：禁用开关显示为文字而非复选框？**  
A：新版已强制使用 `BOOLEAN` 的标准样式，现在会显示为勾选框。


### 南光AIGC绘画

南光AIGC-AIGC全能方案设计解决专家 VX:nankodesign2001

RH新人注册网址---
粉丝福利：https://pre.runninghub.cn/?inviteCode=t7ztfeiw-填入邀请码，领1000RH币，每天登录还有100币 邀请码：t7ztfeiw

仙宫云新人注册网址---
https://www.xiangongyun.com/register/MJAT43 新人注册仙宫云送5元代金券， 填写邀请码（输入我们的邀请码：MJAT43 ）还额外送3元代金券 完成后可以得到仙宫云8元账户余额，可以免费带你玩转5小时发高配4090 D显卡AIGC绘画。


PS软件（AI）插件
https://istarry.com.cn/?sfrom=jbEHmC
提供多种强大的AI功能，轻松提升设计效率，邀您免费体验


### 三大自媒体平台

小红书
https://www.xiaohongshu.com/user/profile/5fe63b41000000000100811d?m_source=itab

抖音
https://www.douyin.com/user/self?showTab=post

bilibili（B站）
https://space.bilibili.com/404783526


### 如果您受益于本项目，不妨请作者喝杯咖啡，您的支持是我最大的动力

<div style="display: flex; justify-content: left; gap: 20px;">
    <img src="https://github.com/balu112121/ComfyUI_NanKo_AI_Recognize/blob/main/Alipay.jpg" width="300" alt="支付宝收款码">
    <img src="https://github.com/balu112121/ComfyUI_NanKo_AI_Recognize/blob/main/WeChat.jpg" width="300" alt="微信收款码">
</div>

# 商务合作
如果您有定制工作流/节点的需求，或者想要学习插件制作的相关课程，请联系我
wechat:nankodesign2001

## 作者
南光AI

## 许可
MIT License