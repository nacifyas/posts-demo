from setuptools import setup

setup(
    name="posts-ms",
    version="0.0.1",
    description="MS for posts",
    py_modules=["main"],
    package_dir={'':'src'},
    install_requires=[
        "redis-om >= 0.0.27",
        "fastapi >= 0.78.0",
        "uvicorn >= 0.18.2"
    ],
)