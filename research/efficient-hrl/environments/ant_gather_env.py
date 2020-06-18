from .ant import AntEnv
from .gather_env import GatherEnv


class AntGatherEnv(GatherEnv):
    MODEL_CLASS = AntEnv
