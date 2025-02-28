from groq import Groq # type: ignore
import gradio as gr   # type: ignore

client = Groq(api_key='Your_api_key_here')

def chatbot(input_text, device_details):
    chat_completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": "You are an expert assistant that assists users with tech troubleshooting."
            },
            {
                "role": "user",
                "content": input_text + " My device is " + device_details,
            }
        ]
    )
    return chat_completion.choices[0].message.content

demo = gr.Interface(
    fn=chatbot, 
    inputs=["text", "text"], 
    outputs="text", 
    title="Customer Service Assistant", 
    description="This is a customer service assistant that assists users with tech troubleshooting. Enter your issue and device details to get help.")

demo.launch(share = True)