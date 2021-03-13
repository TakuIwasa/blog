import environ

# settings.pyの位置を起点として３つ上の親ディレクトリを参照。
BASE_DIR = environ.Path(__file__) - 3

env = environ.Env()

# 環境変数でDJANGO_READ_ENV_FILEをTrueにしておくと.envを読んでくれる。
READ_ENV_FILE = env.bool('DJANGO_READ_ENV_FILE', default=False)
if READ_ENV_FILE:
    env_file = str(BASE_DIR.path('.env'))
    env.read_env(env_file)

DATABASES = {
    'default': env.db() # デフォルトでDATABASE_URLの環境変数を分解してくれる
}