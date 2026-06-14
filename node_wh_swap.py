"""
南光AI图像宽高互换节点（修正版）
强制显示输入端口，禁用开关为复选框
"""

class Comfyui_Width_Height_Interchange:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT", {
                    "default": 512,
                    "min": 1,
                    "max": 8192,
                    "step": 1,
                    "display": "number",
                    "label": "宽度",
                    "forceInput": True,      # 强制显示为输入端口
                }),
                "height": ("INT", {
                    "default": 512,
                    "min": 1,
                    "max": 8192,
                    "step": 1,
                    "display": "number",
                    "label": "高度",
                    "forceInput": True,      # 强制显示为输入端口
                }),
                "disable_swap": ("BOOLEAN", {
                    "default": False,
                    "label": "禁止互换（停用宽高互换）",
                    "label_off": "允许互换",
                    "label_on": "禁止互换",
                }),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("宽度", "高度")
    FUNCTION = "swap"
    CATEGORY = "南光AI/切换"
    OUTPUT_NODE = False
    DESCRIPTION = "将宽度与高度值互换，可通过开关禁用。输入端口可连线，不连线时使用面板数值。"

    def swap(self, width, height, disable_swap):
        if disable_swap:
            return (width, height)
        else:
            return (height, width)


NODE_CLASS_MAPPINGS = {
    "Comfyui_Width_Height_Interchange": Comfyui_Width_Height_Interchange
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Comfyui_Width_Height_Interchange": "南光AI图像宽高互换"
}