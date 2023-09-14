..\python_embeded\python.exe .\update.py ..\QuasarUI\
..\python_embeded\python.exe -s -m pip install --upgrade --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cu121 -r ../QuasarUI/requirements.txt pygit2
pause
