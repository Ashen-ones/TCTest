import os
import util

IS_TEST = False

UNREAL_EDITOR_PATH = rf"D:\ue\5.5.1\Engine\Binaries\Win64\UnrealEditor.exe"


class ProjectBuildInformation:
    def __init__(self):
        print("Init ")
        self.PackagePath = ""

    def init_work_space(self):
        print("InitWorkSpace")

        util.delete_path(self.get_depoly_path())
        util.delete_path(self.get_package_path())

    def set_build_information(self):
        all_def_params = {
            "PROJECT_ROOT_PATH": rf"E:\UnrealProject\local_trunk\LyraStarterGame",
            "ENGINE_ROOT_PATH": r"E:\UE-Release\UE_5.5",
            "ORIGINAL_WORKSPACE": "",
            "BRANCH_NAME": "trunk",
            "CONFIGURATION": "Development",
            "BUILD_PLATFORM": "Win64",
            "BUILD_TARGET": "LyraGame",  # 不需要外部输入，通过上面的自动确认
            "GAME_NAME": "LyraStarterGame",
            "SKIP_COOK": "",
            "SKIP_PAK": "",
            "ITERATE_COOK": "true",
            "CHANGELIST": "-1",  # 不需要外部输入，本地构建默认-1
            "UBT_ARGS": "",
            "PROJECT_CLEAN": "false",  # 是否清理项目
            "BUILD_ID": "-1",  # 本地构建默认-1
            "SKIP_BUILD": "",
        }

        if IS_TEST:
            all_def_params['ENGINE_ROOT_PATH'] = r"D:\S1WS\trunk\UE5EA"
            all_def_params['PROJECT_ROOT_PATH'] = r"D:\UE5P\PT"
            all_def_params['ORIGINAL_WORKSPACE'] = r"D:\S1WS"
            all_def_params['BUILD_TYPE'] = r"0"
            all_def_params['BRANCH_NAME'] = r"trunk"
            all_def_params['CONFIGURATION'] = r"Development"
            all_def_params['BUILD_PLATFORM'] = "Win64"
            all_def_params['GAME_NAME'] = r"PT"
            # all_def_params['BUILD_PLATFORM'] = r"Android"
            all_def_params['BUILD_TYPE'] = r"Package"
            all_def_params['P4CLIENT'] = r"huijin"
            all_def_params['SKIP_COOK'] = r"false"
            all_def_params['SKIP_BUILD'] = r"false"
            all_def_params['ITERATE_COOK'] = r"false"

        for AllDefParamsKey, AllDefParamsValue in all_def_params.items():
            all_def_params_key_str = str(AllDefParamsKey)
            # 没有输入就给默认值
            setattr(self, all_def_params_key_str, AllDefParamsValue)
            print(all_def_params_key_str, AllDefParamsValue)
        env_vars = os.environ

        for env_var_key, env_var_value in env_vars.items():
            for AllDefParamsKey, AllDefParamsValue in all_def_params.items():
                all_def_params_key_str = str(AllDefParamsKey)
                if env_var_key == all_def_params_key_str:
                    setattr(self, all_def_params_key_str, env_var_value)
                    print(all_def_params_key_str, env_var_value)

    def get_depoly_path(self):
        pass

    def get_package_path(self):
        pass

    def get_uproject_path(self):
        project_path = os.path.join(self.PROJECT_ROOT_PATH, f"{self.GAME_NAME}.uproject")
        return os.path.abspath(project_path)

    def get_uat_path(self):
        uat_path = os.path.join(self.ENGINE_ROOT_PATH, "Engine", "Build", "BatchFiles", "RunUAT.bat")
        return os.path.abspath(uat_path)


def print_environment_variables():
    env_vars = os.environ
    print("show env var:")
    print("=" * 40)
    for key, value in env_vars.items():
        print(f"env var: {key}: {value}")


def build_cook_run():
    print("starr build cook run")
    command = f'"{UNREAL_EDITOR_PATH}" "D:/ue/5.5.1/Engine/Plugins/Marketplace/TCTest/TCTest.uproject" -run=Cook -TargetPlatform=Win64 -build -cook -map=/Game/Maps/ExampleMap -unversioned -stdout -CrashForUAT -unattended'
    util.execute_command(command)


def load_env_var():
    print("load env par")


def build_cook_run():
    command = f'{build_information.get_uat_path()} ' \
              f'BuildCookRun ' \
              f'-project={build_information.get_uproject_path()} ' \
              f'-noP4 ' \
              f'-platform={build_information.BUILD_PLATFORM} ' \
              f'-target={build_information.BUILD_TARGET} ' \
              f'-cookflavor=ASTC ' \
              f'-clientconfig={build_information.CONFIGURATION} ' \
              f'-serverconfig={build_information.CONFIGURATION} ' \
              f'-package ' \
              f'-archive ' \
              f'-archivedirectory={build_information.get_depoly_path()} '

    if build_information.SKIP_PAK == 'true':
        command += '-SkipPak '
    else:
        command += '-pak '

    if build_information.SKIP_COOK == 'true':
        command += '-SkipCook '
    else:
        command += '-Cook '

    if build_information.SKIP_BUILD == "true":
        print("跳过Build这个阶段")
    else:
        command += '-build '

    command += '-stage -compressed -prereqs -multiprocess -v -applocaldirectory="$(EngineDir)/Binaries/ThirdParty/AppLocalDependencies" '

    UBT_ARGS = ""

    if build_information.UBT_ARGS != "":
        UBT_ARGS = build_information.UBT_ARGS

    if build_information.PROJECT_CLEAN == "true":
        command += " -Clean "

    if build_information.ITERATE_COOK == "true":
        command += " -iterate"

    if build_information == "Development":  # Dev下开启CrashReportClient
        command += " -CrashReporter"

    if UBT_ARGS != "":
        command += f' -UbtArgs="{UBT_ARGS}"'
    # 如果这个参数不为空,那么就会强行覆盖掉BuildCookRun的参数
    # if BuildInformation.force_bkr_cmd != "":
    #     command = arguments.force_bkr_cmd

    print("构建命令查看\n", command, "\n")
    util.execute_command(command)


if __name__ == "__main__":
    print_environment_variables()

    build_information = ProjectBuildInformation()
    build_information.set_build_information()
    load_env_var()
    build_cook_run()
