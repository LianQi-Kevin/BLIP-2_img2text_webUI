import argparse
import logging
import os
import time
import json
import shutil
from uuid import uuid4

import gradio as gr
from PIL import Image
from clip_interrogator import Config, Interrogator

from utils.prompt_note import title, end_message
from utils.utils import log_set, clear_port


def gr_infer(image_path: str):
    global ci, args, global_index

    if image_path is None:
        return "Please upload image"
    else:
        # print
        logging.info(image_path)

        # create output_path
        project_uuid = "{}_{}_{}".format(global_index, time.strftime("%y-%m-%d_%H-%M-%S"), uuid4())
        global_index += 1
        logging.info(project_uuid)
        output_dir = os.path.join(args.output_path, project_uuid)
        os.makedirs(output_dir, exist_ok=True)
        shutil.copy(image_path, os.path.join(output_dir, os.path.basename(image_path)))

        # load image
        image = Image.open(image_path).convert('RGB')

        # interrogate
        export_str = ci.interrogate(image)
        logging.info("export str: {}, save path: {}".format(export_str, output_dir))

        with open(os.path.join(output_dir, "config.json"), "w") as json_f:
            json.dump({"export_str": export_str}, fp=json_f, ensure_ascii=False,
                      sort_keys=True, indent=4, separators=(",", ": "))
        return export_str


def gr_page():
    global args
    with gr.Blocks(title="109美术高中AI与美术融合课", css="utils/style.css") as demo:
        with gr.Column():
            gr.Markdown(title)
            with gr.Row():
                with gr.Column():
                    with gr.Group():
                        # gr.Markdown("#### 上传图片")
                        input_img = gr.Image(image_mode="RGB",
                                             source="upload", type="filepath", label="Init image",
                                             show_label=True, interactive=True, visible=True, elem_id="init_image")
                        generate_button = gr.Button("Go", elem_id="go_button")
                with gr.Column():
                    export_str = gr.Textbox(lines=3, label="export text",
                                            show_label=True, interactive=False, visible=True)

            gr.Markdown(value=end_message)

        # action
        generate_button.click(gr_infer, inputs=[input_img], outputs=[export_str])

        # style
        generate_button.style(margin=False, rounded=(False, False, True, True), full_width="True")

    demo.queue(concurrency_count=args.concurrency_count, max_size=15, api_open=False)
    demo.launch(server_port=args.server_port, share=False, quiet=False, show_error=False, enable_queue=True)


if __name__ == '__main__':
    # args
    parse = argparse.ArgumentParser("Clip Img2text")
    parse.add_argument("--model_id", "-id", choices=["ViT-L-14/openai", "ViT-H-14/laion2b_s32b_b79k"], type=str,
                       help="Which img2text model will be used", default="ViT-L-14/openai")
    parse.add_argument("--output_path", "-o", type=str, help="image export path", default="outputs")
    parse.add_argument("--model_path", "-m", type=str, help="model path", default="models")
    parse.add_argument("--server_port", type=int, help="webpage server port", default=6006)
    parse.add_argument("--concurrency_count", type=int, help="Number of worker threads", default=1)
    args = parse.parse_args()

    # create path
    os.makedirs(args.output_path, exist_ok=True)
    os.makedirs(args.model_path, exist_ok=True)

    # logging set
    log_set(logging.INFO, logging.INFO)

    # kill port 6006
    clear_port(6006)
    gr.close_all()

    # global save index
    global_index = 0

    # load model
    ci = Interrogator(Config(clip_model_name=args.model_id, download_cache=True, cache_path=args.model_path))
    logging.info("Successful load {}".format(args.model_id))

    # run
    gr_page()
