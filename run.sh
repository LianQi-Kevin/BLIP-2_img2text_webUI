# set var
#model_id="ViT-H-14/laion2b_s32b_b79k"
model_id="ViT-L-14/openai"
model_path="/root/autodl-tmp/models"
output_path="/root/autodl-tmp/outputs"
server_port=6006
concurrency_count=2

# create cache path
mkdir -p $model_path
mkdir -p $output_path
mkdir -p /root/autodl-tmp/huggingface

# run
python /root/BLIP-2/img2text_page.py --model_id $model_id --output_path $output_path \
--model_path $model_path --server_port $server_port --concurrency_count $concurrency_count
