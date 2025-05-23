import json

def calculate_expression(expression: str, variables: dict) -> float:
    """
    安全计算表达式，仅允许访问传入的变量字典
    """
    try:
        # 限制 eval 的作用域为传入的变量字典
        return eval(expression, {"__builtins__": None}, variables)
    except (SyntaxError, NameError, TypeError) as e:
        raise ValueError(f"表达式计算失败：{expression}\n错误信息：{e}")

def load_core_parameters(json_path: str) -> dict:
    """
    加载 JSON 文件并动态计算表达式参数（如 Aw）
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        core_data = json.load(f)
    
    for core_type, params in core_data.items():
        # 提取所有数值型参数（排除字符串表达式）
        variables = {k: v for k, v in params.items() if isinstance(v, (int, float))}
        
        # 检查并计算 Aw 表达式
        if "Aw" in params and isinstance(params["Aw"], str):
            expression = params["Aw"]
            try:
                aw_value = calculate_expression(expression, variables)
                params["Aw"] = aw_value  # 更新 Aw 为计算结果
            except ValueError as e:
                print(f"磁芯型号 {core_type} 的 Aw 计算失败：{e}")
                params["Aw"] = None  # 标记为无效值
        
        # 计算 AP（依赖 Aw）
        if params.get("Aw") is not None:
            params["AP"] = params["Ae"] * 1e-2 * params["Aw"] * 1e-2  # cm⁴
        else:
            params["AP"] = None
    
    return core_data
