import os
from pathlib import Path
import subprocess
import ray


@ray.remote(num_cpus=1)
def compress(input_filepath, output_filepath, target_size_mb):
    cmd = ['bash', 'compress.sh', str(input_filepath), str(output_filepath), str(target_size_mb)]
    print('running ', ' '.join(cmd))
    p = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    p.communicate()
    return p.returncode


def compress(input_filepath, output_filepath, target_size_mb):
    cmd = ['bash', 'compress.sh', str(input_filepath), str(output_filepath), str(target_size_mb)]
    print('running ', ' '.join(cmd))
    p = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    p.communicate()
    return p.returncode


if __name__ == '__main__':
    input_path = Path('G:/storage/research/corl2022/videos/real/raw/new')
    output_path = Path('videos_output')
    output_size = 200

    # ray.init()
    # ray_ids = []
    for name in os.listdir(input_path):
        input_name = input_path / name
        name_no_ext = name.split('.')[0]
        output_name = output_path / (name_no_ext + '_sm.mp4')

        # ray_ids.append(compress.remote(input_name, output_name, output_size))

        compress(input_name, output_name, output_size)

    # return_codes = ray.get(ray_ids)
        