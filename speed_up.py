import os
import subprocess
from pathlib import Path


def speed_up(input_filepath, output_filepath, speed_up_factor):
    cmd = [
        'bash', 
        'speed_up.sh',
        str(input_filepath).replace('\\', '/'),
        str(output_filepath).replace('\\', '/'),
        f'{1/speed_up_factor:.3f}',
    ]
    print('Running: ', ' '.join(cmd))
    p = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    p.communicate()
    return p.returncode


if __name__ == '__main__':
    input_path = Path('C:/Users/liang/ws/ffmpeg_py/videos_input')
    output_path = Path('C:/Users/liang/Desktop/outputs')
    speed_up_factor = 10

    for name in os.listdir(input_path):
        input_name = input_path / name
        name_no_ext = name.split('.')[0]
        output_name = output_path / (name_no_ext + f'_{speed_up_factor}x.mp4')

        speed_up(input_name, output_name, speed_up_factor)
