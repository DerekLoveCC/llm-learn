1. 下载llama.cpp并编译 https://github.com/ggerganov/llama.cpp
2. 下载llama2模型 Llama-2-7b-hf
3. 准备python环境
   1) 进入llama.cpp的目录
   2) 创建Python虚拟环境并激活python env:
   3) 安装python包：pip install -r requirements.txt
4. 转换模型为GGML FP16格式：python convert.py <folder path of model>
5. 做4bit的量化(quantize)模型：quantize <path of file generated at step4> <new model file path> q4_0
6. 测试：main -m <new model file path> --prompt "it is a good day"