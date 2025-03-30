# util 说明
## 依赖安装

```python
pip install pydub
```

## convert_audio.py
- 功能：将视频中的音频提取出来，保存为 wav 格式。可以处理单个webm文件的转换，也可以批量处理整个目录中的所有webm文件。它会将webm文件转换为wav格式，并且可以指定输出的采样率。
- 用法：python convert_audio.py -i input_video_path -o output_audio_path -r sample_rate
- 示例1 - 转换单个webm文件：
```python
python convert_audio.py ../prompt_audio/nezha.webm -o ../prompt_audio/nezha.wav
```
- 示例2 - 批量转换目录中的所有webm文件：
```python
python convert_audio.py ../prompt_audio/webm -o ../prompt_audio/wav 
```

- 示例3 - 转换webm文件并指定采样率（默认为16000Hz）：
```python
python convert_audio.py ../prompt_audio/webm/nezha.webm -o ../prompt_audio/wav/nezha-44100.wav -r 44100
```
