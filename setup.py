from setuptools import find_packages,setup

setup(
    name='mcq-genrator',
    version='0.0.1',
    author='Muhammad Adil Ali',
    author_email='muhamad.adil.ale@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)

# You can also install the local packages in the virtual env by running this command: python setup.py install
# Otherwise you can write "e ." in the requrements.txt it automatically search for packages and execute step.py install