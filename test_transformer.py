from transformers import AutoTokenizer, AutoConfig, AutoModelForSequenceClassification, DataCollatorWithPadding
# If below breaks use !pip install --upgrade transformers
tokenizer = AutoTokenizer.from_pretrained("roberta-base")
id2label = {0: "negative", 1: "positive"}
label2id = {"negative": 0, "positive": 1}
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# fix loading model weight
model = AutoModelForSequenceClassification.from_pretrained(
    "thaile/roberta-base-tweets_hate_speech_detection-saved", num_labels=2, id2label=id2label, label2id=label2id
)
print(model)