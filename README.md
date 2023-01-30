# LinkedIn_Profile_Search
링크드인 프로필 검색하기 
## 1. 셀레니움(Selenium) 설치 (OS환경 : Amazon Linux2)
### 1) python & pip3 설치
---

```
sudo yum isntall python3 pip3 
```

### 2) 크롬 설치를 위한 yum 레파짓토리 추가
---
#### - yum 레파짓토리 파일 생성
```
sudo vi /etc/yum.repos.d/google-chrome.repo
```
#### - 생성한 yum 레파짓토리 파일에 아래의 내용 추가
---
```
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/<br>stable/$basearch
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/<br>linux_signing_key.pub
```
### 3) 크롬 드라이버 설치
---
#### - 크롬 설치 및 버전 확인
```bash
sudo yum install google-chrome-stable # 크롬 설치
google-chrome --version # 설치한 크롬의 버전 확인
```
#### - 크롬 드라이버 다운로드 및 압축 풀기
```bash
wget -N http://chromedriver.storage.googleapis.com/[크롬 버전 입력]/chromedriver_linux64.zip # 크롬 드라이버 다운로드
unzip chromedriver_linux64.zip # 압축 풀기 
```

