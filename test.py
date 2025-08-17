import os
def print_environment_variables():
    # 获取所有环境变量
    env_vars = os.environ

    # 打印每个环境变量
    print("环境变量列表:")
    print("=" * 40)
    for key, value in env_vars.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    print_environment_variables()