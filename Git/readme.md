## 사용자 이름, 이메일 확인

- git config user.name

- git config user.email

## 유저 변경

- git config --global user.name Dohee

- git config --global user.email dohee0203x@naver.com

## Private Repo clone

- git clone https://사용자의NAME:비밀번호@github.com/저장소를판유저이름/저장소이름

- (working example) git clone https://Dohee-Jung@github.com/NuviLabs/web_admin_total_front.git

## 그 외

- git rm => 원격 저장소와 로컬 저장소에 있는 파일을 삭제한다.

- git rm --cached => 원격 저장소에 있는 파일을 삭제한다. 로컬 저장소에 있는 파일은 삭제하지 않는다.

## Git - remote: Repository not found 해결방법

verify git configuration:

```
git config --list
```

should be like:

```
...
remote.origin.url=https://github.com/ORG/repo-name.git
...
```

update remote.origin.url with ssh to be used:

```
git remote set-url origin git@github.com:ORG/repo-name.git
```
