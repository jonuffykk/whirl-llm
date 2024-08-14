from PIL import Image
import numpy as np
import torch
from torchvision import transforms
from torchvision.models import resnet50
from core.config import settings

class ImageAnalyzer:
    def __init__(self):
        self.model = resnet50(pretrained=True)
        self.model.eval()
        self.preprocess = transforms.Compose([
            transforms.Resize(settings.IMAGE_SIZE),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def analyze_image(self, image_path: str) -> dict:
        image = Image.open(image_path).convert('RGB')
        input_tensor = self.preprocess(image)
        input_batch = input_tensor.unsqueeze(0)

        with torch.no_grad():
            output = self.model(input_batch)

        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        top_prob, top_catid = torch.topk(probabilities, 5)

        return {
            "top_classes": [self.get_imagenet_class(idx.item()) for idx in top_catid],
            "probabilities": top_prob.tolist()
        }

    @staticmethod
    def get_imagenet_class(idx):
        return f"Class_{idx}"