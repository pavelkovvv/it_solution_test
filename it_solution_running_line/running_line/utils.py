import imageio
from PIL import Image, ImageDraw, ImageFont
import numpy as np


def create_video_with_text(text, duration, width, height, size_text):
    # Задаем параметры видео
    width, height = int(width), int(height)
    fps = 30

    # Создаем список для хранения кадров видео
    frames = []

    # Создаем изображение с черным фоном
    image = Image.new('RGB', (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Задаем шрифт и размер текста
    font = ImageFont.truetype('arial.ttf', size_text)

    # Вычисляем скорость движения бегущей строки
    text_width, text_height = draw.textsize(text, font=font)
    speed = (text_width + width) / (fps * duration)

    # Создаем кадры видео
    for t in range(fps * duration):
        # Очищаем изображение
        draw.rectangle((0, 0, width, height), fill=(0, 0, 0))

        # Рассчитываем текущую позицию бегущей строки
        x = int(width - t * speed)

        # Рисуем текст на изображении
        draw.text((x, (height - text_height) // 2), text, font=font, fill=(255, 255, 255))

        # Конвертируем изображение в массив numpy
        frame = np.array(image)

        # Добавляем кадр в список
        frames.append(frame)

    # Сохраняем список кадров в видеофайл
    output_file = 'output.mp4'
    imageio.mimsave(output_file, frames, fps=fps)

    return output_file
