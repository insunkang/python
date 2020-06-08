# python



## python install

git clone https://github.com/pyenv/pyenv.git ~/.pyenv 

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc 

echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc 

echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc 

echo 'eval "$(pyenv init -)"' >> ~/.bashrc

 source ~/.bashrc

 pyenv install --list 

pyenv install 3.7.2 

pyenv global 3.7.2 

pyenv rehash 

pyenv versions

