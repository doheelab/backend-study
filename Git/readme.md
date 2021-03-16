## git reset과 git revert 쉽게 이해하기

이 글은 git add, git commit, git push 등의 개념에 대한 이해를 전제로 합니다.


![gitfourarea](https://miro.medium.com/max/1000/1*Eced1qZ6rVz0npKAvJKJgw.png)


# 01. Git의 4개의 영역

Git은 일반적으로 `Working Directory`, `Repository`, `Index`, `Stash` 의 4개의 영역으로 구성되어 있습니다. 




## 1. Working Directory(작업영역)

프로젝트 디렉토리이며, 개발자가 직접 코드를 수정하는 공간을 의미합니다.

`.git`을 제외한 모든 영역에 해당합니다.

## 2. Repository(저장소)

파일이나 폴더를 변경 이력별로 저장해두는 곳입니다.

`.git` 디렉토리 내에 존재합니다.

Local, Remote Repository로 구분

## 3. Index (Staging Area)

Working Directory 에서 Repository로 정보가 저장되기 전 준비 영역입니다.

`.git/index` 파일로 관리됩니다.

## 4. Stash

임시적으로 작업사항을 저장해두고, 나중에 꺼내올 수 있는 영역입니다.

영역 | 역할 | 위치
:---:|:---:|:---:
`Working Directory` | 프로젝트 디렉토리이며, 개발자가 직접 코드를 수정하는 공간을 의미합니다. | `.`
`Repository` | 파일이나 폴더를 변경 이력별로 저장해두는 곳입니다. | `.git`
`Index (Staging Area)` | Working Directory 에서 Repository로 정보가 저장되기 전 준비 영역입니다. | `.git/index`
`Stash` | 임시적으로 작업사항을 저장해두고, 나중에 꺼내올 수 있는 영역입니다. |  `.git/refs/stash`


<br/>
<br/>

# 03. 기본적인 작업 흐름

## 1. 정방향 흐름(코드를 수정하고 repository에 반영하는 과정)

1. Working Directory 에서 파일 수정

    * index, repository영역에는 반영되지 않은 상태

    * git diff 명령어로 변경점 확인 가능

2. `git add [파일명 또는 경로 복수지정가능]` 명령어 실행

    * Working Directory와 Index영역이 동기화 됨, repository영역에는 반영되지 않은 상태
  
    * `git diff` 명령어로는 변경점이 확인 되지 않음

    * `git diff --cached` 명령어로 Index영역과 repository영역을 비교할 수 있음

3. `git commit` 명령어 실행

    * Index와 repository영역이 정보가 동기화 되면서 3가지 영역의 데이터가 모두 동기화됨

    * `git diff`명령어와 `git diff --cached` 명령어로는 변경점이 없음


## 2. 역방향 흐름(repository의 다른 Branch의 수정 정보를 가져와 작업 영역에 반영하는 과정)

1. `git branch` 현재 프로젝트가 가지고 있는 브랜치의 정보를 확인하는 명령어

2. `git diff 비교대상브랜치명1 비교대상브랜치명2` 다른 Branch와의 코드 비교

3. `git checkout 대상브랜치` 다른 브랜치로의 변경 후 동작

## 3. Index에서 파일 삭제

`git rm --cached 파일명` : `git add` 명령어로 Index영역에서 파일을 추가한 후에 되돌려서 Index영역에서만 삭제하여 git add명령어 실행 전으로 되돌릴 때


# 04. git log와 git reset

## 1. git log

`git log` 커밋 기록을 확인하는 명령어; 커밋 해시ID를 확인할 수 있음;

## 2. git reset

### 2.1 git reset 기본적인 내용

- 특정 지점의 과거 커밋으로 이동, 이동 된 이후의 커밋은 삭제됨

- **사용 상 주의 요망** : 과거 커밋으로 이동하면서 그 이후 커밋은 삭제되어 되돌릴수 없으므로 주의가 필요

- 특히 Push 후에는 다른사람의 코드에 문제 일으킬 소지 있으므로 금지

- 기본 사용법

    - 주로 사용하는 옵션은 3가지 : `--mixed`, `--hard`, `--soft`, 기본값은 `--mixed`

    - 커밋ID는 앞자리 일부만 사용가능

```
$ git reset 커밋ID
```


### 2.2 git reset --hard

해당 커밋ID의 상태로 Working Directory와 Index영역 모두 초기화된다.

### 2.3 git reset --mixed

해당 커밋ID의 상태로 Index영역은 초기화되고 Working Directory는 변경되지 않는다.

### 2.4 git reset --soft

해당 커밋ID의 상태로 Index영역과 Working Directory 모두 변경되지 않는다.


## 05. git stash

### 1. git stash

`stash` (안전한 곳에) 숨겨두다.

작업 도중 커밋을 할 수는 없는 상태지만, 브랜치 전환을 하거나 커밋 변경을 해야할때 임시적으로 저장할 수 있는 명령어

`commit`되기 이전 작업 중 파일과 `git add`로 추가된 파일 까지 모두 `stash` 영역으로 저장되며 수정분량은 제거 된다.

단 `git add` 명령어로 한번이라도 `index` 영역에 트래킹 된 파일만 `stash`영역으로 저장됨

새롭게 생성한 파일은 `git add` 후 `git stash` 명령어를 사용하거나 `git stash -u` 옵션을 같이 사용할 것

### 2. git stash 기본적인 사용법

- git stash

- git stash save 명칭

- git stash list

- git stash apply

- git stash apply stash아이디

- git stash drop

- git stash pop

## 사용자 이름, 이메일 확인

```
git config user.name
git config user.email
```

## 유저 변경

```
git config --global user.name Dohee
git config --global user.email dohee0203x@naver.com
```

## Private Repo clone

```
git clone https://사용자의NAME:비밀번호@github.com/저장소를판유저이름/저장소이름 
```

## Push 에러 시 

```
git remote set-url origin https://doheelab@github.com/doheelab/optimization.git
```

# Reference

[Git 좀 잘 써보자] https://wikidocs.net/17165

[GIT] 비공개 repository와 터미널로 clone하기 https://mparchive.tistory.com/153

[Demystifying Git: Stash, Basic workflow in the four areas] https://medium.com/technoider/demystifying-git-stash-basic-workflow-in-the-four-areas-f2192b5e509c