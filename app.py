from transformers import AutoTokenizer, AutoModelForSequenceClassification
import neattext.functions as nfx
import re
import torch
import streamlit as st

# labels
labels = [
    'bug', 
    'enhancement', 
    'question'
]

# Model path
# LOCAL
# MODEL_DIR = "./model/distil-bert-uncased-finetuned-github-issues/"

# REMOTE
MODEL_DIR = "ivanlau/distil-bert-uncased-finetuned-github-issues"


@st.cache(allow_output_mutation=True, show_spinner=False)
def load_model():
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    return model, tokenizer

# Helpers
reg_obj = re.compile(r'[^\u0000-\u007F]+', re.UNICODE)
def is_english_text(text):
    return (False if reg_obj.match(text) else True)

# remove the stopwords, emojis from the text and convert it into lower case
def neatify_text(text):
    text = str(text).lower()
    text = nfx.remove_stopwords(text)
    text = nfx.remove_emojis(text)
    return text



def main():
    # st UI setting
    st.set_page_config(
        page_title="IntelliLabel",
        page_icon="🏷",
        layout="centered",
        initial_sidebar_state="auto",
    )
    st.title("IntelliLabel")
    st.write("IntelliLabel is a github issue classification app. It classifies issue into 3 categories (Bug, Enhancement, Question).")

    # load model
    with st.spinner("Downloading model (takes ~1 min)"):
        model, tokenizer = load_model()



    default_text = "Unable to run Speech2Text example in documentation"

    text = st.text_area('Enter text here:', value=default_text)
    submit = st.button('Predict 🏷')


    if submit:
        text = text.strip(" \n\t")
        if is_english_text(text):
            text = neatify_text(text)
            tokenized_sentence = tokenizer(text, return_tensors='pt')
            output = model(**tokenized_sentence)
            predictions = torch.nn.functional.softmax(output.logits, dim=-1)
            _, preds = torch.max(predictions, dim=-1)
            predicted = labels[preds.item()]

            predictions = predictions.tolist()[0]
            c1, c2, c3 = st.columns(3)
            c1.metric(label="Bug", value=round(predictions[0],3))
            c2.metric(label="Enhancement", value=round(predictions[1],3))
            c3.metric(label="Question", value=round(predictions[2],3))
            
            st.info("Prediction")
            st.write(predicted.capitalize())

        else:
            st.error(str("Please input english text."))


if __name__ == '__main__':
	main()