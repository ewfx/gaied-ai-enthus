import csv
import pandas as pd
from datasets import load_dataset
import torch
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
from transformers import TrainingArguments, Trainer

import emailhandler
import preprocessing
import global_variables as gv
from requesttypesconfig import RequestTypesConfig

def tokenize_function(x, tokenizer, max_length=512):
    tokenized = tokenizer(
        x["text"],
        padding=True,
        truncation=True,
        max_length=max_length,
        return_tensors="pt"
    )
    
    return tokenized
    

def evaluate_by_pretrained(model_path, eval_text):
    #print(model_path)
    model = DistilBertForSequenceClassification.from_pretrained(model_path)
    tokenizer = DistilBertTokenizerFast.from_pretrained(model_path)
    model.eval()
    
    inputs = tokenizer(eval_text, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
    
    probabilities = torch.nn.functional.softmax(logits, dim=-1)
    predictions = torch.argmax(probabilities, dim=1)
    print(predictions)
    return RequestTypesConfig().request_types[predictions.item()]

o_requesttype, o_requestsubtype = evaluate_by_pretrained(str(gv.PROJECT_ROOT/"code/src/saved_model"),emailhandler.extract_email_content(str(gv.PROJECT_ROOT/"data/test_emails/closingnotice_reallocationfee_7.eml")))
print(o_requesttype, o_requestsubtype)
