from setuptools import setup, find_packages

setup(
    name="pmyutils",
    version="0.0.4",
    packages=find_packages(where="."),
    # packages=['o3dpackage', 'utilpackage'],
    # Make sure package data is included
    include_package_data=True,
    install_requires=[
        'numpy',
        'open3d',
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
    python_requires='>=3.6',
    # 添加项目页面和bug跟踪链接
    project_urls={
        'Bug Reports': 'https://github.com/mingyangpeng/pmyutils/issues',
        'Source': 'https://github.com/mingyangpeng/pmyutils',
    },
    # Explicitly include package data
   
    # Ensure all subpackages are found
)
# Note: To publish this package to PyPI, run:
# python setup.py sdist bdist_wheel
# twine upload dist/*
    
# When updating code, follow these steps:
# 1. Update version number above (e.g., from '0.0.1' to '0.0.2')
# 2. Clean previous builds: rm -rf dist/ build/ *.egg-info/
# 3. Build package: python setup.py sdist bdist_wheel
# 4. Upload to PyPI: twine upload dist/*
