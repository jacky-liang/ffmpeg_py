import os
from pathlib import Path
import subprocess
import ray


@ray.remote(num_cpus=1)
def remove_audio(input_filepath, output_filepath):
    p = subprocess.Popen(
        ['ffmpeg', '-i', str(input_filepath), '-c', 'copy', '-an', str(output_filepath)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    p.communicate()
    return p.returncode


if __name__ == '__main__':
    input_path = Path('videos_input')
    output_path = Path('videos_output')

    ray.init()
    ray_ids = []
    for name in os.listdir(input_path):
        input_name = input_path / name
        name_no_ext = name.split('.')[0]
        output_name = output_path / (name_no_ext + '_no_audio.mp4')

        ray_ids.append(remove_audio.remote(input_name, output_name))

    return_codes = ray.get(ray_ids)
        