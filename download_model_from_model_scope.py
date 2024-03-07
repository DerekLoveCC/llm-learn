from modelscope import snapshot_download
mod_dir = snapshot_download('shakechen/Llama-2-7b-hf')
print(mod_dir)