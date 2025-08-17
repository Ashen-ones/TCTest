import os

UNREAL_EDITOR_PATH = rf"D:\ue\5.5.1\Engine\Binaries\Win64\UnrealEditor.exe"

def print_environment_variables():
    env_vars = os.environ
    print("show env var:")
    print("=" * 40)
    for key, value in env_vars.items():
        print(f"env var: {key}: {value}")
def build_cook_run():
    print("starr build cook run")

def load_env_var():
    print("load env par")

if __name__ == "__main__":
    print_environment_variables()
    load_env_var()
    build_cook_run()
