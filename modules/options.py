import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--port", type=int, default="6006")
parser.add_argument("--model-path", type=str, default="/root/autodl-tmp/base-model/ZhipuAI/ChatGLM-6B")
parser.add_argument("--pre_seq_len", type=int, default=128)
parser.add_argument("--prefix_projection", type=bool, default=False)
parser.add_argument("--ptuning_checkpoint", type=str, default=None)
parser.add_argument("--precision", type=str, help="evaluate at this precision",
                    choices=["fp32", "fp16", "int4", "int8"], default="fp16")
parser.add_argument("--listen", action='store_true',
                    help="launch gradio with 0.0.0.0 as server name, allowing to respond to network requests")
parser.add_argument("--cpu", action='store_true', help="use cpu", default=False)
parser.add_argument("--share", action='store_true', help="use gradio share", default=False)
parser.add_argument("--device-id", type=str, help="select the default CUDA device to use", default=None)
parser.add_argument("--ui-dev", action='store_true', help="ui develop mode", default=None)
parser.add_argument("--path-prefix", type=str, help="url root path, e.g. /app", default="")

cmd_opts = parser.parse_args()
need_restart = False
