import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="demucs", # Replace with your own username
    version="0.0.1",
    author="facebookresearch",
    author_email="jeffreyca16@gmail.com",
    description="Demucs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JeffreyCA/demucs/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'lameenc==1.2.2',
        'musdb==0.3.1',
        'museval==0.3.0',
        'requests>=2.22',
        'scipy>=1.3.1',
        'setuptools>=41.0.0',
        'torch==1.4.0',
        'tqdm==4.36.1',
        'treetable==0.2.3',
    ],
    python_requires='>=3.6',
)
