from setuptools import setup, find_packages

setup(
    name='mcqgenrators',
    version = '0.0.1',
    author = 'peng ni',
    author_email = 'ayx81@qq.com',
    install_requires = ["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)