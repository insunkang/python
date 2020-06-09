# Vscode



## settings

command settings

prefernces:open settings (JSON)

```json
{
    "[python]": {
        "editor.insertSpaces": true,
        "editor.tabSize": 4
    },
    "[html]": {
        "editor.insertSpaces": true,
        "editor.tabSize": 2
    },
    "terminal.integrated.shell.osx": "/bin/bash",
    "window.zoomLevel": 1,
    "python.defaultInterpreterPath": "/Library/Frameworks/Python.framework/Versions/3.8/bin/python3"
}

```

```
VS Code 단축기

여러줄 동시 입력 :  option + command  + up or down

전체 페이지 format : shift + option + f

선택 부분 :  format : command + k => command + f

라인 전체 이동 : option + up or down 

라인 복사 : shift + option + up or down 

라인 삭제 : shift + command + k

라인 주석 추가 : command + k => command + c

라인 주석 해제 : command + k => command + u

선택 부분 주석/해제 : command + /

```

# Django



```bash
# 가상환경 실행
$ source venv/bin/activate
(venv) $ 
```

```bash
WARNING: You are using pip version 19.2.3, however version 20.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(venv) ip-70-12-224-148:django kang-inseon$ vi .gitignore
(venv) ip-70-12-224-148:django kang-inseon$ ls
venv
(venv) ip-70-12-224-148:django kang-inseon$ django-admin startproject intro
c(venv) ip-70-12-224-148:django kang-inseon$ cd intro
(venv) ip-70-12-224-148:intro kang-inseon$ ls
intro           manage.py
(venv) ip-70-12-224-148:intro kang-inseon$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have 15 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

June 09, 2020 - 06:36:05
Django version 2.1.15, using settings 'intro.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

## Django intro

### Start Django

1. 장고 설치

   ```bash
   pip install django==2.1.15
   pip3 install django==2.1.15
   pip list
   ```

   

2. 프로젝트 생성

   ```bash
   django-admin startproject <프로젝트 명>
   ```

   ```bash
   python manage.py runserver
   ```

3. 프로젝트 생성시 제공하는 파일

   - manage.py
     - 전체 django와 관련된 모든 명령어를 manage.py를 통해 실행합니다.
   - \__init__.py
     - 전체 \__init__.py 파일이 존재하는 폴더를 하나의 프로젝트, 혹은 패키지로 인식하게 해주는 파일.
   - setting.py
     - 현재 프로젝트의 전체적인 설정 및 관리를 위해 존재하는 파일.
   - urls.py
     - 내 프로젝트에 접근 할 수 있는 경로를 설정하기 위한 파일.

4. app 생성

   ```bash
    python manage.py startapp pages
   ```

   setting.py에서 추가

   ```python
   INSTALLED_APPS=[
     'pages'
   ]
   ```

   

   

