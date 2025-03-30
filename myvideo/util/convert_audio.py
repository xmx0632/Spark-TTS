# 使用 python3 把webm文件转换为wav文件

import os
import argparse
from pydub import AudioSegment

def convert_webm_to_wav(input_file, output_file=None, sample_rate=16000):
    """
    将webm文件转换为wav文件
    
    参数:
        input_file (str): 输入的webm文件路径
        output_file (str, optional): 输出的wav文件路径，如果不指定则使用相同文件名但扩展名为.wav
        sample_rate (int, optional): 输出wav文件的采样率，默认为16000Hz
    
    返回:
        str: 输出文件的路径
    """
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"输入文件不存在: {input_file}")
    
    # 如果未指定输出文件，则使用相同的文件名但扩展名为.wav
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + ".wav"
    
    # 加载webm文件
    audio = AudioSegment.from_file(input_file, format="webm")
    
    # 设置采样率
    audio = audio.set_frame_rate(sample_rate)
    
    # 导出为wav文件
    audio.export(output_file, format="wav")
    
    print(f"转换完成: {input_file} -> {output_file}")
    return output_file

def batch_convert(input_dir, output_dir=None, sample_rate=16000):
    """
    批量转换目录中的所有webm文件为wav文件
    
    参数:
        input_dir (str): 输入目录路径
        output_dir (str, optional): 输出目录路径，如果不指定则使用输入目录
        sample_rate (int, optional): 输出wav文件的采样率，默认为16000Hz
    """
    # 如果未指定输出目录，则使用输入目录
    if output_dir is None:
        output_dir = input_dir
    
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 获取所有webm文件
    webm_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.webm')]
    
    if not webm_files:
        print(f"在目录 {input_dir} 中未找到webm文件")
        return
    
    # 转换每个文件
    for webm_file in webm_files:
        input_path = os.path.join(input_dir, webm_file)
        output_path = os.path.join(output_dir, os.path.splitext(webm_file)[0] + ".wav")
        convert_webm_to_wav(input_path, output_path, sample_rate)
    
    print(f"批量转换完成，共转换了 {len(webm_files)} 个文件")

def main():
    parser = argparse.ArgumentParser(description="将webm文件转换为wav文件")
    parser.add_argument("input", help="输入的webm文件或包含webm文件的目录")
    parser.add_argument("-o", "--output", help="输出的wav文件或目录")
    parser.add_argument("-r", "--rate", type=int, default=16000, help="输出wav文件的采样率，默认为16000Hz")
    
    args = parser.parse_args()
    
    # 检查输入是文件还是目录
    if os.path.isfile(args.input):
        # 单个文件转换
        convert_webm_to_wav(args.input, args.output, args.rate)
    elif os.path.isdir(args.input):
        # 批量转换目录
        batch_convert(args.input, args.output, args.rate)
    else:
        print(f"错误: 输入路径不存在 {args.input}")

if __name__ == "__main__":
    main()