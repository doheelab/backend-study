# git reset과 git revert 쉽게 이해하기

* 이 글은 `git add`, `git commit`, `git push` 등 `git`의 기본 개념에 대한 이해를 전제로 합니다.


## git reset, revert를 사용하는 이유

`git reset`과 `git revert`는 `commit` 또는 `push`했던 내용을 이전 상태로 되돌리는 경우에 사용하는 명령어입니다.

로컬의 commit 내용을 변경하고자 할 때는 reset을 주로 사용하지만, 원격 저장소에 push한 결과를 되돌리고 싶을 때는 revert를 사용해야합니다.

---
<br/>

## git의 4가지 영역

![gitfourarea](https://miro.medium.com/max/1000/1*Eced1qZ6rVz0npKAvJKJgw.png)

git은 `Working Directory`, `Repository`, `Index`, `Stash` 의 4개의 영역으로 구성되어 있습니다. 

### 1. Working Directory(작업영역)

프로젝트 디렉토리이며, 개발자가 직접 코드를 수정하는 공간을 의미합니다.

`.git`을 제외한 모든 영역에 해당합니다.

### 2. Repository(저장소)

파일이나 폴더를 변경 이력별로 저장해두는 곳입니다.

`.git` 디렉토리 내에 존재합니다.

Local, Remote Repository로 구분

### 3. Index (Staging Area)

Working Directory 에서 Repository로 정보가 저장되기 전 준비 영역입니다.

`.git/index` 파일로 관리됩니다.

### 4. Stash

임시적으로 작업사항을 저장해두고, 나중에 꺼내올 수 있는 영역입니다.

영역 | 역할 | 위치
:---:|:---:|:---:
`Working Directory` | 프로젝트 디렉토리이며, 개발자가 직접 코드를 수정하는 공간을 의미합니다. | `.`
`Repository` | 파일이나 폴더를 변경 이력별로 저장해두는 곳입니다. | `.git`
`Index (Staging Area)` | Working Directory 에서 Repository로 정보가 저장되기 전 준비 영역입니다. | `.git/index`
`Stash` | 임시적으로 작업사항을 저장해두고, 나중에 꺼내올 수 있는 영역입니다. |  `.git/refs/stash`

---
<br/>


## git reset

```
$ git reset 커밋ID
```


과거 커밋 지점으로 이동하고, 이동된 이후의 커밋은 삭제하는 명령어 입니다. `git reset`에는 3가지 종류가 있습니다.


### 2.1 git reset --hard

해당 커밋ID의 상태로 Working Directory와 Index영역 모두 초기화합니다.

### 2.2 git reset --mixed

해당 커밋ID의 상태로 Index영역은 초기화되고 Working Directory는 변경되지 않습니다.

### 2.3 git reset --soft

해당 커밋ID의 상태로 Index영역과 Working Directory 모두 변경되지 않고, commit된 파일들을 staging area로 돌려놓습니다.


명령어 | 역할 
:---:|:---:
`git reset --hard` | 해당 커밋ID의 상태로 Working Directory와 Index영역 모두 초기화합니다. 
`git reset --mixed` | 해당 커밋ID의 상태로 Index영역은 초기화되고 Working Directory는 변경되지 않습니다. 
`git reset --soft` | 해당 커밋ID의 상태로 Index영역과 Working Directory 모두 변경되지 않습니다. 

---
<br/>

## 유의사항

원격 저장소에 push한 경우에는 `git reset`을 사용할 때 주의가 필요합니다.

예를 들어, 커밋 A, B, C, D을 push한 후 `git reset`을 사용한다고 가정해봅시다.

![](https://media.vlpt.us/images/sonypark/post/1a2445b7-8ade-429a-a8eb-480004aa575a/image.png)

이 때 B 커밋으로 `reset --hard`를 하게 되면 C, D 커밋은 사라지게 되지만, 원격 저장소에는 C, D가 남아있습니다.  

![](https://media.vlpt.us/images/sonypark/post/b9231368-309f-4cad-bcff-5fe93fe5f10a/image.png)

나 혼자 사용하는 브랜치라면 `push --force` 명령어로 원격 저장소에 올릴 수 있지만, 다른 팀원이 있는 경우 충돌이 발생합니다. 

이럴 때 사용할 수 있는 것이 `git revert`입니다.

---
<br/>

# git revert

```
$ git revert 커밋ID
```


`git revert 커밋ID`를 사용하면 이전 커밋 내역을 그대로 남겨둔 채 새로운 커밋을 생성합니다. 

앞선 상황에서, git revert를 사용한 결과는 다음과 같습니다.

![](https://media.vlpt.us/images/sonypark/post/34a1717b-93aa-4eac-96b1-5ccd0dddc900/image.png)

되돌릴 커밋이 여러개라면 범위를 주어서 여러개를 선택할 수도 있습니다.

```
git revert 2664ce8..15413dc
```

<!-- 
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
``` -->

# Reference

[Git 좀 잘 써보자] https://wikidocs.net/17165

[GIT] 비공개 repository와 터미널로 clone하기 https://mparchive.tistory.com/153

[Demystifying Git: Stash, Basic workflow in the four areas] https://medium.com/technoider/demystifying-git-stash-basic-workflow-in-the-four-areas-f2192b5e509c

[git reset vs git revert 차이] https://velog.io/@sonypark/git-reset-vs-git-revert-%EC%B0%A8%EC%9D%B4