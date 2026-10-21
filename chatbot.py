from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
conversation_history = []
print("Chatbot ready! (type 'exit' to quit)\n")
