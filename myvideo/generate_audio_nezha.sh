#!/bin/bash

# Copyright (c) 2025 SparkAudio
#               2025 Xinsheng Wang (w.xinshawn@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Get the absolute path of the script's directory
script_dir=$(dirname "$(realpath "$0")")

# Get the root directory
root_dir=$(dirname "$script_dir")

# Set default parameters
device=0
save_dir='myvideo/results'
model_dir="pretrained_models/Spark-TTS-0.5B"
text="自己选择的路，再荒谬也要走完！"
# text="身临其境，换新体验。塑造开源语音合成新范式，让智能语音更自然。"
prompt_text="他们说我注定不配拥有什么。注定要背负那些沉重的枷锁。活在他们的期望里。每天都的做那些他们安排好的事。像个没有自由的傀儡，根本没法活成自己。这个世界，这些人，真的一点也不值得我去在乎。"
prompt_speech_path="myvideo/prompt_audio/wav/nezha.wav"

# Change directory to the root directory
cd "$root_dir" || exit

source sparktts/utils/parse_options.sh

# Run inference
python -m cli.inference \
    --text "${text}" \
    --device "${device}" \
    --save_dir "${save_dir}" \
    --model_dir "${model_dir}" \
    --prompt_text "${prompt_text}" \
    --prompt_speech_path "${prompt_speech_path}"
    
    