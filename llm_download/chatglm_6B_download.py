from modelscope.hub.snapshot_download import snapshot_download

model_dir = snapshot_download('ZhipuAI/ChatGLM-6B', cache_dir='/root/autodl-tmp/base-model/', revision='v1.0.1')
