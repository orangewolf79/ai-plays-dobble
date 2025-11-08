import torch
import torchvision


"""
Objective: a machine learning model that can play dobble against a human WITHOUT memorizing all the card combinations - it must play like a human
Strategy:
Segmentation net to divide into 2 cards, 8 symbols each.
Run quick mapping to see if any symbol is in both cards (eg. if shape > 85% accurate)
Pretrained areas for 50 different symbols
TTS to say the actual symbol (random.randn time delay) - simulates an actual game

Resources:
https://wandb.ai/ishandutta/semantic_segmentation_unet/reports/Semantic-Segmentation-with-UNets-in-PyTorch--VmlldzoyMzA3MTk1
"""