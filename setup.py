from setuptools import setup, find_packages

setup(
    name='pmyutils',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        # 列出你的依赖项，例如 'requests', 'numpy' 等
    ],
    author='PMY',
    author_email='863102089@qq.com',
    description='personal utils',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mingyangpeng/pmyutils.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
