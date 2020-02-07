import os
from onnpdf import create_pdf


def main():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    assets_dir = f'{current_dir}{os.sep}assets'
    template_file_path = f'{current_dir}{os.sep}templates{os.sep}demo.html'
    output_file_path = os.sep.join([current_dir, 'outputs', 'demo.pdf'])

    kv_pairs = {
        'title': 'OzNetNerd.com Demo PDF',
        'author': 'Will Robinson',
        'job_title': 'DevOps Specialist',
        'company': 'OzNetNerd.com',
        'email': 'will@oznetnerd.com',
        'phone': '+61 00 000 000',
        'website': 'https://oznetnerd.com'
    }

    create_pdf(template_file_path, assets_dir, output_file_path, kv_pairs)


if __name__ == '__main__':
    main()
