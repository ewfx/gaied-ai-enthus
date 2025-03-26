import csv
import pandas as pd
from datasets import load_dataset, ClassLabel
import torch
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
from transformers import TrainingArguments, Trainer

import global_variables as gv

if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")



def tokenize_function(x, tokenizer, max_length=512):
    tokenized = tokenizer(
        x["text"],
        padding=True,
        truncation=True,
        max_length=max_length,
        return_tensors="pt"
    )
    
    return tokenized

def train_on_classification(model_name, data_file):
    #print("data_file: ",data_file)
   
    dataset = load_dataset("csv", data_files=data_file)
    unique_labels = list(set(dataset["train"]["label"]))
    num_labels = len(unique_labels)

    if not isinstance(dataset["train"].features["label"], ClassLabel):
        class_label = ClassLabel(num_classes=len(unique_labels), names=[str(label) for label in unique_labels])
        dataset = dataset.cast_column("label", class_label)
    split_dataset = dataset["train"].train_test_split(test_size=0.2, stratify_by_column="label")
    #split_dataset = split_dataset.rename_columns({"train": "train", "test": "validation"})
    
    tokenizer = DistilBertTokenizerFast.from_pretrained(model_name)
    tokenized_datasets = split_dataset.map(lambda x: tokenize_function(x, tokenizer), batched=True)
    
    tokenized_datasets = tokenized_datasets.remove_columns("text")
    tokenized_datasets.set_format("torch", columns=['input_ids', 'attention_mask', 'label'])

    model = DistilBertForSequenceClassification.from_pretrained(
        model_name,
        num_labels=num_labels,
    )
    model.to(device)

    training_args = TrainingArguments(
        output_dir=str(gv.PROJECT_ROOT/"code/src/saved_model"),
        eval_strategy="epoch",
        save_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=32,
        per_device_eval_batch_size=32,
        num_train_epochs=20,
        weight_decay=0.01,
        push_to_hub=False,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["test"]
    )

    trainer.train()
    model.save_pretrained(str(gv.PROJECT_ROOT/"code/src/saved_model"))
    tokenizer.save_pretrained(str(gv.PROJECT_ROOT/"code/src/saved_model"))
    

train_on_classification("distilbert-base-uncased", str(gv.PROJECT_ROOT/"data/training/trainingdata.csv"))
