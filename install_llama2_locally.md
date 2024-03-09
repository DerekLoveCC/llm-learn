1. Windows 10下安装visual studio 2022 community edition
2. 安装anaconda并设置国内的源
3. 下载llama.cpp并编译 https://github.com/ggerganov/llama.cpp
   1.1 git clone  https://github.com/ggerganov/llama.cpp.git
   1.2 打开visual studio的命令行并进入1.1中下载的repo目录下，执行cmake
   1.3 执行成功后会生成bin/debug目录，里面包含可执行文件如：main.exe和quantize.exe
4. 下载llama2模型 Llama-2-7b-hf
   2.1 从魔搭下载
5. 准备python环境
   5.1 conda create --name llama2 python=3.10.13
   5.2 conda activate llama2
   5.3 进入llama.cpp的目录并执行pip install -r requirements.txt或者conda install --yes --file requirements.txt
6. 转换模型为GGML FP16格式：python convert.py <folder path of model>
7. 做4bit的量化(quantize)模型：quantize <path of file generated at step4> <new model file path> q4_0
8.  测试:
   main -m <new model file path> -n 80 --prompt "it is a good day"
   main -m <new model file path> -n 80 --prompt "床前明月光"