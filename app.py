import gradio as gr
import traceback

from pipelines.faq_pipeline import FaqPipeline


faq_pipeline = FaqPipeline()


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
    result = faq_pipeline.run(
        message,
        chat_history=format_history(history),
    )
    log_text = "\n\n".join(
        [
            "HISTORY:",
            result["chat_history"] or "No previous messages.",
            "REWRITTEN QUERY:",
            result["rewritten_query"],
            "RETRIEVAL QUERY:",
            result["retrieval_query"],
            "CONTEXT:",
            result["context"] or "No context found.",
            "PROMPT:",
            result["prompt"],
        ]
    )
    return result["answer"], log_text


with gr.Blocks() as demo:
    gr.Markdown("# FAQ Assistant")
    gr.Markdown("Local FAQ chat powered by the FAQ pipeline.")

    with gr.Row():
        chatbot = gr.Chatbot(label="Chat", height=700, scale=3)
        log_box = gr.Textbox(label="Logs", lines=30, scale=2)

    state = gr.State([])
    msg = gr.Textbox(label="Message", placeholder="Type your question here...")
    send = gr.Button("Send")
    clear = gr.Button("Clear")

    def respond(message: str, history):
        history = history or []
        if not message or not message.strip():
            return history, history, "", "Empty message."

        try:
            answer, log_text = chat(message, history)
        except Exception as error:
            answer = f"Error: {error}"
            log_text = traceback.format_exc()

        history = history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": answer},
        ]
        return history, history, "", log_text

    msg.submit(
        respond,
        inputs=[msg, state],
        outputs=[chatbot, state, msg, log_box],
        queue=False,
    )
    send.click(
        respond,
        inputs=[msg, state],
        outputs=[chatbot, state, msg, log_box],
        queue=False,
    )
    clear.click(
        lambda: ([], [], "", ""),
        outputs=[chatbot, state, msg, log_box],
        queue=False,
    )


if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        share=False,
        show_error=True,
        debug=True,
    )
