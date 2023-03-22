# Install requirements
install:
    @pip install -e .

# Remove temp / unnecessary files
clean:
    @rm -f */version.txt
    @rm -f .coverage
    @rm -f */.ipynb_checkpoints
    @rm -Rf build
    @rm -Rf */__pycache__
    @rm -Rf */*.pyc
