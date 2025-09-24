from pathlib import Path
import pygame


def import_folder(path: str):
    path = Path(path)
    # Get all image files and sort them by name to ensure correct order
    image_files = [img_file for img_file in path.glob("*") if img_file.is_file()]
    image_files.sort(key=lambda x: x.name)
    
    return [
        pygame.image.load(img_file).convert_alpha()
        for img_file in image_files
    ]


def import_folder_dict(path: str):
    path = Path(path)
    return {
        img_file.stem: pygame.image.load(img_file).convert_alpha()
        for img_file in path.glob("*")
        if img_file.is_file()
    }