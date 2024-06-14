import gradio as gr
import os

tgi_endpoint = os.environ['tgi_endpoint']
description = os.getenv('description', 'This is a demo for text generation with LLM')
title = os.getenv('title', 'HuggingFace TGI on OCI OKE  🚀 🚀 🚀')
example1 = os.getenv('example1','Which came first - the chicken or the egg?')
example2 = os.getenv('example2', 'Write a sample python script to list all the bucket in an OCI tenancy')
max_token = int(os.getenv('max_token', 300))

from huggingface_hub import InferenceClient
client = InferenceClient(model=tgi_endpoint)

def inference(message, history):
    partial_message = ""
    for token in client.text_generation(message, max_new_tokens=max_token, stream=True):
        partial_message += token
        yield partial_message

gr.ChatInterface(
    inference,
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder="Chat with me!", container=False, scale=7),
    description=description,
    title=title,
    examples=[example1, example2],
    retry_btn="Retry",
    undo_btn="Undo",
    clear_btn="Clear",
).queue().launch(server_name="0.0.0.0", share=True)
