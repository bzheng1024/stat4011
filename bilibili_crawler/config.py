import execjs
import os
os.environ["EXECJS_RUNTIME"]="Node"
print(execjs.get().name)