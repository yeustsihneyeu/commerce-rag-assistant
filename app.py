import gradio as gr
import traceback

from routing import domain_router
from pipelines.faq_pipeline import FaqPipeline
from pipelines.base_pipeline import BasePipeline
from pipelines.chat_pipeline import ChatPipeline

pipeline = ChatPipeline(domain_router, FaqPipeline(), BasePipeline())


def format_history(history) -> str:
    if not history:
        return ""

    lines = []
    for item in history:
        if isinstance(item, dict):
            role = item.get("role", "user")
            content = item.get("content", "")
        else:
            role = getattr(item, "role", "user")
            content = getattr(item, "content", "")

        if isinstance(content, str) and content.strip():
            lines.append(f"{role}: {content.strip()}")
    return "\n".join(lines)


def chat(message: str, history):
    result = (
        pipeline.run(
            message,
            chat_history=format_history(history),
        )
        or {}
    )
    log_text = "\n\n".join(
        [
            "ROUTE:",
            result.get("route") or "No route found.",
            "====================",
            "HISTORY:",
            result.get("chat_history") or "No previous messages.",
            "====================",
            "REWRITTEN QUERY:",
            result.get("rewritten_query") or message,
            "====================",
            "RETRIEVAL QUERY:",
            result.get("retrieval_query") or message,
            "====================",
            "CONTEXT:",
            result.get("context") or "No context found.",
            "====================",
            "PROMPT:",
            result.get("prompt") or "No prompt available.",
        ]
    )
    return result.get("answer") or "No answer returned.", log_text


with gr.Blocks() as demo:
    gr.Markdown("# FAQ Assistant")
    gr.Markdown("Local FAQ chat powered by the FAQ pipeline.")

    with gr.Row():
        chatbot = gr.Chatbot(label="Chat", height=500, scale=3)
        log_box = gr.Textbox(label="Logs", lines=20, scale=2)

    state = gr.State([])
    msg = gr.Textbox(label="Message", placeholder="Type your question here...")
    send = gr.Button("Send")
    clear = gr.Button("Clear")

    def add_user_message(message: str, history):
        history = history or []
        if not message or not message.strip():
            return history, history, "", "Empty message."

        history = history + [{"role": "user", "content": message.strip()}]
        return history, history, "", ""

    def respond(history):
        history = history or []
        if not history:
            return history, history, "Empty message."

        message = history[-1]["content"]
        previous_history = history[:-1]

        try:
            answer, log_text = chat(message, previous_history)
        except Exception as error:
            answer = f"Error: {error}"
            log_text = traceback.format_exc()

        history = history + [{"role": "assistant", "content": answer}]
        return history, history, log_text

    msg.submit(
        add_user_message,
        inputs=[msg, state],
        outputs=[chatbot, state, msg, log_box],
        queue=False,
    ).then(
        respond,
        inputs=[state],
        outputs=[chatbot, state, log_box],
    )
    send.click(
        add_user_message,
        inputs=[msg, state],
        outputs=[chatbot, state, msg, log_box],
        queue=False,
    ).then(
        respond,
        inputs=[state],
        outputs=[chatbot, state, log_box],
    )
    clear.click(
        lambda: ([], [], "", ""),
        outputs=[chatbot, state, msg, log_box],
        queue=False,
    )


if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        share=True,
        show_error=True,
        debug=True,
    )
