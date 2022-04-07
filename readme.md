# IntelliLabel
![app.png](./app.png)

IntelliLabel is built by using pretrained [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) model and fine-tuning it on the
[github ticket tagger dataset](https://tickettagger.blob.core.windows.net/datasets/dataset-labels-top3-30k-real.txt) under PyTorch and HuggingFace framework. It can classify issue into 3 common categories: Bug, Enhancement, Questions.

## Clone Project
Run the commands belows to download project along with the model bin from [HuggingFace Hub](https://huggingface.co/ivanlau/distil-bert-uncased-finetuned-github-issues):
```cmd
git clone https://github.com/IvanLauLinTiong/IntelliLabel.git
cd IntelliLabel
git submodule update --init --recursive
```
Or simply:
```cmd
git clone --recurse-submodules https://github.com/IvanLauLinTiong/IntelliLabel.git
```

## Demo

Try it out:
[Streamlit Cloud](https://share.streamlit.io/ivanlaulintiong/intellilabel/main/app.py) OR
[HuggingFace Spaces](https://huggingface.co/spaces/ivanlau/IntelliLabel)
